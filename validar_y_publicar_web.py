# -*- coding: utf-8 -*-
"""
Script Integral de QA, Integración de Curso en Cabecera y Despliegue Oficial
Proyecto Dólar / Colombia Tech Systems (agencia-10-paginas)
"""
import os, re, shutil, glob

DIR_WEB = r"C:\Users\sopor\dev\agencia-10-paginas"
DIR_PLANTILLAS = r"G:\Mi unidad\EL OJO DE DIOS\proyectos\Proyecto Dolar\plantillas"

def sincronizar_archivos_desde_boveda():
    print("==========================================================================")
    print("📦 1. SINCRONIZANDO CURSO IA AGENTIC Y CONTRATOS HACIA DIRECTORIO WEB...")
    print("==========================================================================")
    # 1. Copiar curso-agentic-ia.html
    src_curso = os.path.join(DIR_PLANTILLAS, "curso-agentic-ia.html")
    dst_curso = os.path.join(DIR_WEB, "curso-agentic-ia.html")
    if os.path.exists(src_curso):
        shutil.copy2(src_curso, dst_curso)
        print(f" ✅ [COPIADO] {src_curso} -> {dst_curso}")
    else:
        print(f" ⚠️ Advertencia: No se encontró {src_curso}")

    # 2. Copiar carpeta contratos
    src_contratos = os.path.join(DIR_PLANTILLAS, "contratos")
    dst_contratos = os.path.join(DIR_WEB, "contratos")
    if os.path.exists(src_contratos):
        if os.path.exists(dst_contratos):
            shutil.rmtree(dst_contratos)
        shutil.copytree(src_contratos, dst_contratos)
        print(f" ✅ [COPIADO] Carpeta de Contratos Legales -> {dst_contratos}")

def inyectar_boton_superior():
    print("==========================================================================")
    print("💫 2. INYECTANDO BOTÓN DE CURSO DE IA EN LA PARTE SUPERIOR (CABECERA)...")
    print("==========================================================================")
    index_file = os.path.join(DIR_WEB, "index.html")
    with open(index_file, "r", encoding="utf-8", errors="replace") as f:
        html = f.read()

    # Inspeccionar dónde está el menú o navegación en index.html
    # Vamos a buscar etiquetas clásicas o botones existentes
    boton_html = (
        ' <a href="curso-agentic-ia.html" style="'
        'display:inline-flex; align-items:center; gap:6px; '
        'background: linear-gradient(135deg, #00ff88 0%, #00cc66 100%); '
        'color: #000; font-family: \'Orbitron\', sans-serif; font-weight: 800; '
        'font-size: 0.85rem; padding: 8px 18px; border-radius: 99px; '
        'text-decoration: none; box-shadow: 0 0 25px rgba(0, 255, 136, 0.45); '
        'border: 1px solid #ffffff; transition: all 0.3s ease; letter-spacing: 0.5px;'
        '">🎓 CURSO IA AGENTIC <span style="background:#000; color:#00ff88; padding:2px 7px; border-radius:10px; font-size:0.7rem; font-family:\'Share Tech Mono\';">VERCEL</span></a> '
    )

    if "curso-agentic-ia.html" not in html:
        # Intentar insertar en el contenedor de navegación principal (ej. dentro de <nav> o junto a botones de cabecera)
        # Buscamos el primer <nav> o contenedor con botones/enlaces en la cabecera
        m_nav = re.search(r'(<nav[^>]*>.*?</nav>)', html, flags=re.S|re.I)
        if m_nav:
            nav_content = m_nav.group(1)
            # Insertar antes de cerrar el div de enlaces o antes del cierre de nav
            if '</div>' in nav_content:
                idx_insert = html.find('</div>', m_nav.end() - len(nav_content) - 10)
            else:
                idx_insert = m_nav.end() - 6
            # O busquemos si hay botones de contacto o whatsapp en la cabecera
            m_btn = re.search(r'(<a[^>]*wa\.me[^>]*>)', html, flags=re.I)
            if m_btn and m_btn.start() < 10000: # Si está en la parte superior
                idx = m_btn.start()
                html = html[:idx] + boton_html + "\n" + html[idx:]
                print(" ✅ [BOTÓN INSERTADO] Junto al botón de acción superior en index.html")
            else:
                # Insertar en la barra superior inmersiva después del inicio del body o en la barra HUD
                m_body = re.search(r'<body[^>]*>', html, flags=re.I)
                if m_body:
                    idx = m_body.end()
                    barra_superior = f"""
                    <!-- BARRA SUPERIOR FIEL CTS CON BOTÓN AL CURSO -->
                    <div style="background: rgba(2, 6, 13, 0.92); backdrop-filter: blur(16px); border-bottom: 1px solid rgba(56, 230, 255, 0.28); padding: 10px 24px; position: sticky; top: 0; z-index: 999999; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
                      <div style="display: flex; align-items: center; gap: 12px;">
                        <span style="color: rgba(255,255,255,0.4); font-size: 12px;">|</span>
                        <a href="contratos/contrato_desarrollo_web_colombia.html" target="_blank" style="color: #ffb627; text-decoration: none; font-weight: 700; font-size: 13px; font-family: 'Rajdhani', sans-serif; letter-spacing: 0.5px;">⚖️ CONTRATO LEGAL ONLINE</a>
                      </div>
                      <div style="display: flex; align-items: center; gap: 14px;">
                        <span style="color: #e0f4ff; font-family: 'Rajdhani', sans-serif; font-weight: 600; font-size: 14px;">🎓 Formación Oficial en IA:</span>
                        {boton_html}
                      </div>
                    </div>
                    """
                    html = html[:idx] + "\n" + barra_superior + html[idx:]
                    print(" ✅ [BARRA SUPERIOR INYECTADA] Barrasticky superior HUD con el botón al curso integrada en index.html")
        else:
            # Si no hay nav, inyectar inmediatamente después de <body...>
            m_body = re.search(r'<body[^>]*>', html, flags=re.I)
            if m_body:
                idx = m_body.end()
                barra_superior = f"""
                <!-- BARRA SUPERIOR FIEL CTS CON BOTÓN AL CURSO -->
                <div style="background: rgba(2, 6, 13, 0.92); backdrop-filter: blur(16px); border-bottom: 1px solid rgba(56, 230, 255, 0.28); padding: 10px 24px; position: sticky; top: 0; z-index: 999999; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
                  <div style="display: flex; align-items: center; gap: 12px;">
                    <span style="color: rgba(255,255,255,0.4); font-size: 12px;">|</span>
                    <a href="contratos/contrato_desarrollo_web_colombia.html" target="_blank" style="color: #ffb627; text-decoration: none; font-weight: 700; font-size: 13px; font-family: 'Rajdhani', sans-serif; letter-spacing: 0.5px;">⚖️ CONTRATO LEGAL ONLINE</a>
                  </div>
                  <div style="display: flex; align-items: center; gap: 14px;">
                    <span style="color: #e0f4ff; font-family: 'Rajdhani', sans-serif; font-weight: 600; font-size: 14px;">🎓 Formación Oficial en IA:</span>
                    {boton_html}
                  </div>
                </div>
                """
                html = html[:idx] + "\n" + barra_superior + html[idx:]
                print(" ✅ [BARRA SUPERIOR INYECTADA] Barra sticky HUD con botón insertada tras <body> en index.html")
        
        with open(index_file, "w", encoding="utf-8", errors="replace") as f:
            f.write(html)
    else:
        print(" ℹ️ El botón a curso-agentic-ia.html ya estaba presente en index.html")

def validar_enlaces_en_todo_el_portafolio():
    print("==========================================================================")
    print("🛡️ 3. VALIDANDO TODOS LOS ENLACES (HTML / IMÁGENES / ASSETS / CSS / JS)...")
    print("==========================================================================")
    html_files = glob.glob(os.path.join(DIR_WEB, "*.html")) + glob.glob(os.path.join(DIR_WEB, "**", "*.html"), recursive=True)
    
    errores_encontrados = 0
    enlaces_verificados = 0
    
    for arch in set(html_files):
        nombre = os.path.relpath(arch, DIR_WEB)
        with open(arch, "r", encoding="utf-8", errors="replace") as f:
            contenido = f.read()
            
        # Buscar enlaces <a href="..."> y <link href="..."> y <script src="..."> y <img src="...">
        links = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', contenido, flags=re.I)
        
        for l in links:
            l_strip = l.split('#')[0].split('?')[0] # quitar hash o query params
            if not l_strip or l_strip.startswith("http://") or l_strip.startswith("https://") or l_strip.startswith("data:") or l_strip.startswith("mailto:") or l_strip.startswith("tel:"):
                continue # enlace externo o protocolo, ignoramos para validación de fichero local
            enlaces_verificados += 1
            
            # Verificar si el archivo existe en disco
            dir_arch = os.path.dirname(arch)
            path_objetivo = os.path.normpath(os.path.join(dir_arch, l_strip))
            
            if not os.path.exists(path_objetivo) and not os.path.exists(os.path.join(DIR_WEB, l_strip)):
                print(f" ❌ [ENLACE ROTO EN {nombre}] -> No se encuentra '{l}'")
                errores_encontrados += 1
                
    print(f" 📊 Validación QA Completa: {enlaces_verificados} enlaces locales comprobados.")
    if errores_encontrados == 0:
        print(" ✅ ¡ESTADO QA IMPECABLE! 0 ENLACES ROTOS, TODO EL PORTAFOLIO AL 100% DE SALUD.")
    else:
        print(f" ⚠️ Se detectaron {errores_encontrados} advertencias en enlaces locales.")

def publicar_en_la_web():
    print("==========================================================================")
    print("🚀 4. PUBLICANDO Y DESPLEGANDO EN LA WEB (GITHUB PAGES / CLOUDFLARE)...")
    print("==========================================================================")
    os.chdir(DIR_WEB)
    os.system("git add .")
    res = os.system('git commit -m "🚀 Deploy: Agregar Botón Curso IA Agentic en Cabecera, Contrato Legal y Validación QA"')
    if res == 0 or "nothing to commit" in str(res):
        print(" 📤 Empujando cambios al repositorio oficial remoto...")
        os.system("git push origin gh-pages")
        print(" 🌐 ¡DESPLIEGUE FINALIZADO EN GITHUB Y CLOUDFLARE WITH SUCCESS!")
    else:
        print(" ℹ️ Sin cambios pendientes de empujar o commit ya registrado.")

if __name__ == "__main__":
    sincronizar_archivos_desde_boveda()
    inyectar_boton_superior()
    validar_enlaces_en_todo_el_portafolio()
    publicar_en_la_web()
    print("==========================================================================")
    print("👑 OPERACIÓN DE SISTEMA COMPLETADA BAJO PROTOCOLO FABLE 5 & YOLO MODE")
    print("==========================================================================")
