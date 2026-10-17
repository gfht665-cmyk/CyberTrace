import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

url = "https://any.run/cybersecurity-blog/post_tag-sitemap.xml"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = resp.read().decode('utf-8', errors='ignore')
        tags = re.findall(r'<loc>([^<]+)</loc>', data)
        print(f"Total tags in sitemap: {len(tags)}")
        for t in tags[:20]:
            print("  ", t)
        
        # Save tags
        import json
        with open(r'c:\Users\bad\Desktop\مجلد جديد\CyberTrace-Platform\scripts\anyrun_tags.json', 'w', encoding='utf-8') as f:
            json.dump(tags, f, indent=2)
except Exception as e:
    print(f"Error: {e}")
