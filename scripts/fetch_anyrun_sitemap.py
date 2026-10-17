import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

url = "https://any.run/cybersecurity-blog/post-sitemap.xml"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = resp.read().decode('utf-8', errors='ignore')
        urls = re.findall(r'<loc>([^<]+)</loc>', data)
        print(f"Total blog posts in sitemap: {len(urls)}")
        for u in urls[:15]:
            print("  ", u)
        
        # Save all URLs to a json file
        import json
        with open(r'c:\Users\bad\Desktop\مجلد جديد\CyberTrace-Platform\scripts\anyrun_posts.json', 'w', encoding='utf-8') as f:
            json.dump(urls, f, indent=2)
        print("Saved to anyrun_posts.json")
except Exception as e:
    print(f"Error: {e}")
