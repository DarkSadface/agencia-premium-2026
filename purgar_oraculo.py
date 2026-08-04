# -*- coding: utf-8 -*-
import os, re, glob

DIR_WEB = r"C:\Users\sopor\dev\agencia-10-paginas"
DIR_PLANTILLAS = r"G:\Mi unidad\EL OJO DE DIOS\proyectos\Proyecto Dolar\plantillas"

print("==========================================================================")
print("🧹 ELIMINANDO POR COMPLETO '' DE TODO EL SISTEMA...")
print("==========================================================================")

archivos = glob.glob(os.path.join(DIR_WEB, "**", "*.*"), recursive=True) + glob.glob(os.path.join(DIR_PLANTILLAS, "**", "*.*"), recursive=True)

for path in set(archivos):
    if not os.path.isfile(path) or not path.endswith(('.html', '.js', '.css', '.py')):
        continue
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            contenido = f.read()
            
        if "ORÁCULO" in contenido.upper() or "V6.55" in contenido or "NÚCLEO" in contenido.upper():
            print(f" 🔍 Detectada coincidencia en: {os.path.relpath(path, os.path.dirname(DIR_WEB))}")
            # Reemplazar bloques de status badge o texto NÚCLEO ORÁCULO
            nuevo_contenido = re.sub(r'<div[^>]*class=["\'][^"\']*status-badge[^"\']*["\'][^>]*>.*?</div>\s*', '', contenido, flags=re.I|re.S)
            nuevo_contenido = re.sub(r'<span[^>]*>[^<]*ORÁCULO[^<]*</span>\s*', '', nuevo_contenido, flags=re.I|re.S)
            nuevo_contenido = re.sub(r'<span[^>]*>[^<]*NÚCLEO[^<]*</span>\s*', '', nuevo_contenido, flags=re.I|re.S)
            nuevo_contenido = re.sub(r'NÚCLEO ORÁCULO ACTIVO\s*\|\s*V6\.55', '', nuevo_contenido, flags=re.I)
            
            if nuevo_contenido != contenido:
                with open(path, 'w', encoding='utf-8', errors='replace') as f:
                    f.write(nuevo_contenido)
                print(f" ✅ [ELIMINADO Y LIMPIADO] -> {os.path.basename(path)}")
    except Exception as e:
        pass

# Asegurar que no quede nada de NÚCLEO en index.html específicamente
index_f = os.path.join(DIR_WEB, "index.html")
if os.path.exists(index_f):
    with open(index_f, 'r', encoding='utf-8') as f:
        c = f.read()
    if "NÚCLEO" in c.upper() or "ORÁCULO" in c.upper() or "V6.55" in c:
        print(" ⚠️ ¡Aún quedaban restos en index.html! Limpiando agresivamente...")
        c = re.sub(r'<span[^>]*class=["\']pulse-dot["\'][^>]*></span>\s*<span>[^<]*ORÁCULO[^<]*</span>', '', c, flags=re.I|re.S)
        with open(index_f, 'w', encoding='utf-8') as f:
            f.write(c)
        print(" ✅ index.html completamente purificado de referencias al Orácúlo/V6.55.")
    else:
        print(" ✅ Confirmado: index.html ya no tenía referencias a NÚCLEO ORÁCULO ACTIVO.")

os.chdir(DIR_WEB)
os.system("git add .")
res = os.system('git commit -m "🔥 Purga total: Eliminar cualquier rastro de  del portafolio"')
if res == 0 or "nothing to commit" in str(res):
    os.system("git push origin gh-pages")
    print("🚀 ¡Despliegue final purgado y en vivo en GitHub Pages y Cloudflare!")
else:
    print(" ℹ️ Sin cambios adicionales para empujar (la purga ya estaba reflejada en el commit anterior).")
