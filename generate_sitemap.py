from datetime import datetime, timezone
from pathlib import Path

urls = [u.strip() for u in Path("urls.txt").read_text(encoding="utf-8").splitlines() if u.strip()]
today = datetime.now(timezone.utc).date().isoformat()

xml = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for i, u in enumerate(urls):
    pr = "1.0" if i == 0 else "0.8"
    xml += ["  <url>",
            f"    <loc>{u}</loc>",
            f"    <lastmod>{today}</lastmod>",
            f"    <priority>{pr}</priority>",
            "  </url>"]
xml.append("</urlset>\n")
Path("sitemap.xml").write_text("\n".join(xml), encoding="utf-8")
print("Generated sitemap.xml with", len(urls), "URLs")
