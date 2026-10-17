import os
import sys
import re
import shutil
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, 'images')
BACKUP_DIR = os.path.join(IMAGES_DIR, '.orig')

os.makedirs(BACKUP_DIR, exist_ok=True)

# Select Windows font
FONT_BOLD_PATH = r"C:\Windows\Fonts\segoeuib.ttf"
if not os.path.exists(FONT_BOLD_PATH):
    FONT_BOLD_PATH = r"C:\Windows\Fonts\arialbd.ttf"

FONT_REG_PATH = r"C:\Windows\Fonts\segoeui.ttf"
if not os.path.exists(FONT_REG_PATH):
    FONT_REG_PATH = r"C:\Windows\Fonts\arial.ttf"

def watermark_raster_image(filepath):
    filename = os.path.basename(filepath)
    backup_path = os.path.join(BACKUP_DIR, filename)
    
    # Store pristine original if not already backed up
    if not os.path.exists(backup_path):
        shutil.copyfile(filepath, backup_path)
    
    # Open from backup to ensure clean, non-duplicated watermarking
    try:
        with Image.open(backup_path) as im:
            # Convert to RGBA for drawing translucent badges
            orig_format = im.format or os.path.splitext(filename)[1].replace('.', '').upper()
            if orig_format == 'JPG':
                orig_format = 'JPEG'
                
            has_alpha = im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info)
            working_im = im.convert('RGBA')
            
            w, h = working_im.size
            
            # Create transparent overlay layer
            overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)
            
            # Scale badge dynamically based on image resolution
            # Standard badge width: 330px, height: 38px
            badge_w = 340
            badge_h = 36
            
            # If image is very small, scale down badge
            scale = 1.0
            if w < 400 or h < 300:
                scale = max(0.65, min(w / 450, h / 350))
                badge_w = int(badge_w * scale)
                badge_h = int(badge_h * scale)
                
            margin_right = max(10, int(15 * scale))
            margin_bottom = max(10, int(15 * scale))
            
            bx1 = w - badge_w - margin_right
            by1 = h - badge_h - margin_bottom
            bx2 = w - margin_right
            by2 = h - margin_bottom
            
            # Ensure coordinates are within image
            if bx1 < 0: bx1 = 0
            if by1 < 0: by1 = 0
            
            # Draw sleek badge background (Dark slate #0f172a, 92% opacity)
            # and vibrant cyan border (#0ea5e9)
            badge_bg = (15, 23, 42, 235)
            badge_border = (14, 165, 233, 255)
            draw.rounded_rectangle([bx1, by1, bx2, by2], radius=int(6 * scale), fill=badge_bg, outline=badge_border, width=max(1, int(1.5 * scale)))
            
            # Draw Telegram emblem circle
            emblem_radius = int(10 * scale)
            emblem_cx = bx1 + int(18 * scale)
            emblem_cy = by1 + badge_h // 2
            draw.ellipse([emblem_cx - emblem_radius, emblem_cy - emblem_radius, emblem_cx + emblem_radius, emblem_cy + emblem_radius], fill=(0, 136, 204, 255))
            
            # Font sizes
            font_size_main = max(10, int(13 * scale))
            font_size_sub = max(9, int(11 * scale))
            font_size_icon = max(8, int(10 * scale))
            
            try:
                font_main = ImageFont.truetype(FONT_BOLD_PATH, font_size_main)
                font_sub = ImageFont.truetype(FONT_REG_PATH, font_size_sub)
                font_icon = ImageFont.truetype(FONT_BOLD_PATH, font_size_icon)
            except Exception:
                font_main = ImageFont.load_default()
                font_sub = ImageFont.load_default()
                font_icon = ImageFont.load_default()
                
            # TG icon text
            draw.text((emblem_cx - int(6 * scale), emblem_cy - int(6 * scale)), "TG", fill=(255, 255, 255, 255), font=font_icon)
            
            # Text 1: Telegram: @wgkgi0x0
            text_x = emblem_cx + emblem_radius + int(8 * scale)
            text_y = by1 + int(10 * scale)
            draw.text((text_x, text_y), "Telegram: ", fill=(226, 232, 240, 255), font=font_sub)
            
            # Measure "Telegram: " width
            t_box = draw.textbbox((text_x, text_y), "Telegram: ", font=font_sub)
            user_x = t_box[2]
            draw.text((user_x, text_y), "@wgkgi0x0", fill=(56, 189, 248, 255), font=font_main)
            
            # Separator & t.me/wgkgi0x0
            u_box = draw.textbbox((user_x, text_y), "@wgkgi0x0", font=font_main)
            sep_x = u_box[2] + int(6 * scale)
            draw.text((sep_x, text_y), "|", fill=(100, 116, 139, 255), font=font_sub)
            link_x = sep_x + int(6 * scale)
            draw.text((link_x, text_y), "t.me/wgkgi0x0", fill=(148, 163, 184, 255), font=font_sub)
            
            # Composite
            final_im = Image.alpha_composite(working_im, overlay)
            
            # Save back in appropriate format
            if orig_format in ('JPEG', 'JPG'):
                final_im.convert('RGB').save(filepath, format='JPEG', quality=95, optimize=True)
            elif orig_format == 'WEBP':
                final_im.save(filepath, format='WEBP', quality=95)
            else: # PNG
                if not has_alpha:
                    final_im.convert('RGB').save(filepath, format='PNG', optimize=True)
                else:
                    final_im.save(filepath, format='PNG', optimize=True)
                    
            print(f"  [Raster] Watermarked: {filename} ({w}x{h})")
            return True
    except Exception as e:
        print(f"  ❌ Error watermarking {filename}: {e}")
        return False

def watermark_svg_image(filepath):
    filename = os.path.basename(filepath)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            svg_text = f.read()
            
        # Check if watermark already injected
        if 'id="tg-watermark-wgkgi0x0"' in svg_text:
            # Already watermarked, remove existing badge to update cleanly
            svg_text = re.sub(r'\s*<!-- Telegram Watermark Badge -->[\s\S]*?</g>', '', svg_text)
            
        # Find viewBox or width/height
        vb_match = re.search(r'viewBox=["\']\s*([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)["\']', svg_text)
        if vb_match:
            vx, vy, vw, vh = [float(x) for x in vb_match.groups()]
        else:
            w_m = re.search(r'width=["\']([0-9.]+)["\']', svg_text)
            h_m = re.search(r'height=["\']([0-9.]+)["\']', svg_text)
            vw = float(w_m.group(1)) if w_m else 1000.0
            vh = float(h_m.group(1)) if h_m else 600.0
            vx, vy = 0.0, 0.0
            
        badge_w = 320.0
        badge_h = 32.0
        margin_r = 18.0
        margin_b = 15.0
        
        bx = (vx + vw) - badge_w - margin_r
        by = (vy + vh) - badge_h - margin_b
        
        watermark_g = f'''
  <!-- Telegram Watermark Badge -->
  <g id="tg-watermark-wgkgi0x0">
    <rect x="{bx:.1f}" y="{by:.1f}" width="{badge_w:.1f}" height="{badge_h:.1f}" rx="5" fill="#0f172a" fill-opacity="0.92" stroke="#0ea5e9" stroke-width="1.5"/>
    <circle cx="{bx + 18:.1f}" cy="{by + 16:.1f}" r="8" fill="#0088cc"/>
    <text x="{bx + 18:.1f}" y="{by + 19.5:.1f}" fill="#ffffff" font-family="'Segoe UI', Arial, sans-serif" font-size="8" font-weight="900" text-anchor="middle">TG</text>
    <text x="{bx + 34:.1f}" y="{by + 20:.1f}" fill="#cbd5e1" font-family="'Segoe UI', -apple-system, sans-serif" font-size="11">Telegram: <tspan fill="#38bdf8" font-weight="700">@wgkgi0x0</tspan></text>
    <text x="{bx + 215:.1f}" y="{by + 20:.1f}" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">|</text>
    <text x="{bx + 225:.1f}" y="{by + 20:.1f}" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="10">t.me/wgkgi0x0</text>
  </g>
</svg>'''
        
        # Replace closing </svg>
        new_svg = re.sub(r'</svg>\s*\Z', watermark_g, svg_text.strip(), flags=re.IGNORECASE)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_svg)
            
        print(f"  [SVG] Watermarked: {filename} (viewBox: {vw}x{vh})")
        return True
    except Exception as e:
        print(f"  ❌ Error watermarking SVG {filename}: {e}")
        return False

print("=== Starting Comprehensive Forensic Watermarking (@wgkgi0x0) ===")
total_processed = 0
raster_count = 0
svg_count = 0

for root, dirs, files in os.walk(IMAGES_DIR):
    if '.orig' in dirs:
        dirs.remove('.orig') # Don't process backup
    for f in sorted(files):
        ext = os.path.splitext(f)[1].lower()
        filepath = os.path.join(root, f)
        if ext in ('.png', '.jpg', '.jpeg', '.webp'):
            if watermark_raster_image(filepath):
                raster_count += 1
                total_processed += 1
        elif ext == '.svg':
            if watermark_svg_image(filepath):
                svg_count += 1
                total_processed += 1

print("\n=== Watermarking Execution Completed ===")
print(f"Total images stamped with 'Telegram: @wgkgi0x0': {total_processed}")
print(f"  - Raster Images (PNG/JPG/WEBP): {raster_count}")
print(f"  - Vector Schematics (SVG): {svg_count}")
