"""Gera PGRScore.html: um unico arquivo auto-suficiente (HTML+CSS+JS+dados
embutidos) que abre com duplo-clique, sem servidor e sem CORS."""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(BASE, "index.html"), encoding="utf-8").read()
appjs = open(os.path.join(BASE, "app.js"), encoding="utf-8").read()
datajs = open(os.path.join(BASE, "data.js"), encoding="utf-8").read()

# remove as tags <script src="data.js"...> e <script src="app.js">
html = re.sub(r'<script src="data\.js"[^>]*></script>\s*', '', html)
html = re.sub(r'<script src="app\.js"></script>\s*', '', html)

# injeta data.js + app.js inline antes de </body>
inline = "<script>\n" + datajs + "\n</script>\n<script>\n" + appjs + "\n</script>\n"
html = html.replace("</body>", inline + "</body>")

out = os.path.join(BASE, "PGRScore.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(html)

print("OK -> %s (%.1f KB)" % (out, os.path.getsize(out) / 1024))
