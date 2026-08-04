# -*- coding: utf-8 -*-
import os, re, glob

DIR_WEB = r"C:\Users\sopor\dev\agencia-10-paginas"
NUEВО_CORREO = "colombiatechsystems@gmail.com"

print("==========================================================================")
print(f"📧 ACTUALIZANDO CORREO ELECTRÓNICO A: {NUEВО_CORREO}")
print("==========================================================================")

archivos = glob.glob(os.path.join(DIR_WEB, "**", "*.*"), recursive=True)
correos_cambiados = set()

# Regex para detectar correos comunes que no sean el nuevo correo
regex_correo = re.compile(r'\b[A-Za-z0-9._%+-]+@(?!gmail\.com\b)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b|\b[A-Za-z0-9._%+-]+@gmail\.com\b')

for path in archivos:
    if not os.path.isfile(path) or not path.endswith(('.html', '.js', '.md', '.txt')):
        continue
    if "actualizar_correo.py" in path or ".git" in path:
        continue
        
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        orig = c
        
        # Buscar todos los correos actuales
        encontrados = regex_correo.findall(c)
        for e in encontrados:
            if e.lower() != NUEВО_CORREO.lower() and not e.endswith(".png") and not e.endswith(".jpg") and not "user@" in e and not "sopor@" in e:
                c = c.replace(e, NUEВО_CORREO)
                correos_cambiados.add(e)
                
        if "mailto:" in c:
            c = re.sub(r'mailto:[^"\'>\s]+', f'mailto:{NUEВО_CORREO}', c, flags=re.I)
            
        if orig != c:
            with open(path, 'w', encoding='utf-8', errors='replace') as f:
                f.write(c)
            print(f" ✅ Actualizado correo en -> {os.path.relpath(path, DIR_WEB)}")
    except Exception as ex:
        pass

if correos_cambiados:
    print(f" 🔍 Correos antiguos sustituidos: {', '.join(correos_cambiados)}")
else:
    # Si no había correos previos explícitos, verifiquemos si en el pie de página (footer) de index.html falta añadirlo
    print(" ℹ️ No se detectaron correos previos diferentes, verificando presencia en index.html...")

os.chdir(DIR_WEB)
# Asegurar que esté presente de forma explícita en la sección de contacto o footer del index.html si no existía
index_path = os.path.join(DIR_WEB, "index.html")
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        idx_c = f.read()
    if NUEВО_CORREO not in idx_c:
        print(" 📌 Incorporando el correo oficial en la sección de contacto / pie de página en index.html...")
        idx_c = re.sub(r'(<footer.*?>)', r'\1\n    <div style="text-align:center; padding:15px; font-family:\'Share Tech Mono\', monospace; color:#38e6ff; background:#02060d; letter-spacing:1px;">✉️ CORREO OFICIAL: <a href="mailto:' + NUEВО_CORREO + '" style="color:#00ff88; text-decoration:underline;">' + NUEВО_CORREO + '</a></div>', idx_c, flags=re.I|re.S)
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(idx_c)
        print(" ✅ Añadido bloque de correo en el footer de index.html.")

os.system("git add .")
res = os.system(f'git commit -m "✉️ Contact Info: Actualizar correo oficial de contacto a {NUEВО_CORREO}"')
if res == 0 or "nothing to commit" in str(res):
    os.system("git push origin gh-pages")
    print("🚀 ¡Cambios de correo sincronizados y desplegados en vivo!")
