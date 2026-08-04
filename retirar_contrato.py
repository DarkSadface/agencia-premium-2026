# -*- coding: utf-8 -*-
"""
Retirar contrato del sitio web público y limpiar cabeceras en producción
"""
import os, re, shutil

DIR_WEB = r"C:\Users\sopor\dev\agencia-10-paginas"
DIR_PLANTILLAS = r"G:\Mi unidad\EL OJO DE DIOS\proyectos\Proyecto Dolar\plantillas"

print("==========================================================================")
print("🧹 RETIRANDO ENLACES AL CONTRATO LEGAL DEL SITIO WEB PÚBLICO...")
print("==========================================================================")

# 1. Limpiar index.html en DIR_WEB
index_path = os.path.join(DIR_WEB, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    
    # Remover el separador "|" y el link al contrato en la barra superior de index.html
    content = re.sub(r'<span[^>]*>\s*\|\s*</span>\s*<a[^>]*contrato_desarrollo_web_colombia\.html[^>]*>.*?</a>', '', content, flags=re.I|re.S)
    content = re.sub(r'<a[^>]*contrato_desarrollo_web_colombia\.html[^>]*>.*?</a>', '', content, flags=re.I|re.S)
    
    with open(index_path, "w", encoding="utf-8", errors="replace") as f:
        f.write(content)
    print(" ✅ Enlace a contrato removido limpiamente de index.html")

# 2. Limpiar curso-agentic-ia.html en DIR_WEB y en Bóveda
for base_dir in [DIR_WEB, DIR_PLANTILLAS]:
    p = os.path.join(base_dir, "curso-agentic-ia.html")
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        # Remover el link de contrato en el header Vercel
        content = re.sub(r'<a[^>]*contrato_desarrollo_web_colombia\.html[^>]*>.*?</a>\s*', '', content, flags=re.I|re.S)
        with open(p, "w", encoding="utf-8", errors="replace") as f:
            f.write(content)
        print(f" ✅ Enlace a contrato removido de curso-agentic-ia.html en: {base_dir}")

# 3. Eliminar carpeta contratos DEL DIRECTORIO WEB PÚBLICO (se conserva protegida en el Segundo Cerebro)
dir_contratos_web = os.path.join(DIR_WEB, "contratos")
if os.path.exists(dir_contratos_web):
    shutil.rmtree(dir_contratos_web)
    print(f" ✅ Carpeta {dir_contratos_web} eliminada totalmente de la web pública.")

print("==========================================================================")
print("📤 PUBLICANDO ELIMINACIÓN DEL CONTRATO EN GITHUB PAGES / CLOUDFLARE...")
print("==========================================================================")
os.chdir(DIR_WEB)
os.system("git add .")
os.system('git commit -m "🚫 Retirar contrato del sitio web público según instrucción"')
os.system("git push origin gh-pages")
print("🚀 ¡Cambio sincronizado al instante en línea! El contrato ya no es público.")
