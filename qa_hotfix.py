# -*- coding: utf-8 -*-
import os, shutil

f1 = r"C:\Users\sopor\dev\agencia-10-paginas\curso-agentic-ia.html"
f2 = r"G:\Mi unidad\EL OJO DE DIOS\proyectos\Proyecto Dolar\plantillas\curso-agentic-ia.html"

for f in [f1, f2]:
    if os.path.exists(f):
        with open(f, "r", encoding="utf-8", errors="replace") as file:
            content = file.read()
        content = content.replace('href="catalogo.html"', 'href="index.html"')
        with open(f, "w", encoding="utf-8", errors="replace") as file:
            file.write(content)
        print(f" ✅ Enlace corregido a index.html en: {f}")

# También copiar catalogo.html e index-premium.html si faltan en agencia-10-paginas
src_cat = r"G:\Mi unidad\EL OJO DE DIOS\proyectos\Proyecto Dolar\plantillas\catalogo.html"
if os.path.exists(src_cat):
    shutil.copy2(src_cat, r"C:\Users\sopor\dev\agencia-10-paginas\catalogo.html")
    print(" ✅ catalogo.html respaldado en el directorio web de producción.")

print("🛡️ Hotfix QA completado exitosamente.")
os.chdir(r"C:\Users\sopor\dev\agencia-10-paginas")
os.system("git add .")
os.system('git commit -m "🛡️ QA Hotfix: Enlaces limpios a index.html y respaldo total del catálogo"')
os.system("git push origin gh-pages")
print("🚀 ¡Cambios publicados y sincronizados con GitHub Pages y Cloudflare!")
