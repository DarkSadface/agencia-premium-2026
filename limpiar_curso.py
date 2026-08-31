# -*- coding: utf-8 -*-
import re, os

path = r"C:\Users\sopor\dev\agencia-10-paginas\curso-agentic-ia.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

orig = c

# 1. Eliminar el botón de Inscribirme Hoy ($290 USD) y el contenedor si queda vacío
c = re.sub(r'<div style="display: flex; align-items: center; gap: 12px;">\s*<a[^>]*Inscribirme Hoy[^>]*>.*?</a>\s*</div>', '', c, flags=re.IGNORECASE|re.DOTALL)
c = re.sub(r'<a[^>]*Inscribirme Hoy[^>]*>.*?</a>', '', c, flags=re.IGNORECASE|re.DOTALL)

# 2. Eliminar referencias al recuadro amarillo "- basado en el roadmap de datapath.ai"
c = c.replace(" - basado en el roadmap de datapath.ai", "")
c = c.replace("- basado en el roadmap de datapath.ai", "")
c = c.replace("· datapath.ai", "")
c = c.replace("roadmap de <b>datapath.ai</b>:", "roadmap oficial:")
c = c.replace("roadmap de datapath.ai:", "roadmap oficial:")

# 3. Eliminar el recuadro amarillo "Guárdalo en tu bóveda "El Ojo de Dios"..."
c = re.sub(r'<p[^>]*>.*?Guárdalo en tu bóveda.*?</p>', '', c, flags=re.IGNORECASE|re.DOTALL)
c = re.sub(r'<div[^>]*>.*?Guárdalo en tu bóveda.*?</div>', '', c, flags=re.IGNORECASE|re.DOTALL)
c = re.sub(r'Guárdalo en tu bóveda.*?\.', '', c, flags=re.IGNORECASE)

if c != orig:
    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("✅ Archivo curso-agentic-ia.html limpio y actualizado.")
else:
    print("⚠️ No se hicieron cambios automáticos por regex, imprimamos dónde aparecen para ajuste manual:")

# Verificamos si aún queda algo
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if any(k in l.lower() for k in ["inscribirme", "290", "datapath", "ojo de dios", "bóveda"]):
        print(f"Línea restante {i+1}: {l.strip()}")

os.chdir(r"C:\Users\sopor\dev\agencia-10-paginas")
os.system("git add curso-agentic-ia.html")
os.system('git commit -m "🧹 Clean UI & Content: Eliminar botón de inscripción, referencias a datapath y textos de la bóveda en curso IA"')
os.system("git push origin gh-pages")
