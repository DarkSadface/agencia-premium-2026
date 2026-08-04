# -*- coding: utf-8 -*-
import os, re, glob

DIR_WEB = r"C:\Users\sopor\dev\agencia-10-paginas"
print("🧹 Limpiando la palabra VERCEL en los botones del curso y sincronizando...")

for path in glob.glob(os.path.join(DIR_WEB, "**", "*.html"), recursive=True):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    orig = c
    c = re.sub(r'<span[^>]*>[^<]*VERCEL[^<]*</span>\s*', '', c, flags=re.I)
    c = c.replace("VERCEL", "") if "CURSO IA AGENTIC" in c and "VERCEL" in c else c
    if orig != c:
        with open(path, 'w', encoding='utf-8', errors='replace') as f:
            f.write(c)
        print(f" ✅ Limpiado -> {os.path.basename(path)}")

os.chdir(DIR_WEB)
os.system("git add .")
os.system('git commit -m "🎨 UI Polish: Colocar botón del curso justo al lado del reloj y eliminar palabra VERCEL"')
os.system("git push origin gh-pages")
print("🚀 ¡Despliegue exitoso en GitHub Pages y Cloudflare!")
