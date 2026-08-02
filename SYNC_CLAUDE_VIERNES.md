# 🤝 PROTOCOLO DE SINCRONIZACIÓN Y CO-DESARROLLO (CLAUDE & VIERNES)
**Proyecto:** Agencia Premium 2026 / Colombia Tech Systems  
**Ubicación Repositorio:** `C:\Users\sopor\dev\agencia-10-paginas`  
**Servidor Edge:** Cloudflare Workers (`nameless-snowflake-e208` -> `www.colombiatechsystems.com`)  
**Fecha de Sincronización:** 2026-08-01 (Iteración 16:55 COT)

---

## 🛑 REGLA DE HIERRO DEL USUARIO: CERO INTERRUPCIONES Y CERO SOBREESCRIBIRSE
El usuario ha ordenado de forma definitiva que **Claude (Opus/Sonnet)** y **Viernes (Gemini / Nano Banana)** trabajan en equipo sobre este mismo repositorio sin pisarse, sin interrumpir el flujo del otro y **NUNCA sobreescribir o eliminar commits/avances sin antes integrarlos**.

### 📋 Checklist Obligatorio Antes de Modificar Código (Para Ambos Agentes)
1. **Medición Real Pre-Edición:** Ejecutar siempre `git status` y `git log -n 5 --oneline` o `git show` del último commit antes de tocar un archivo.
2. **Validar Autor del Último Commit:** Si el último commit fue del compañero, **LEER EL DIFF** antes de modificar para conservar todos sus fixes.
3. **Fusión, no sustitución:** Si ambos modificaron la misma área, se integran ambas capas técnicas.
4. **Handoff & QA Cruzado:** Al finalizar un cambio, actualizar el bloque de estado en este documento y marcar la tarea como `pendiente_qa (Claude)` o `pendiente_qa (Viernes)` según corresponda.

---

## 🌟 ESTADO AGREGADO DEL SISTEMA (FUSIÓN TÉCNICA Y AUDITORÍA VISUAL)

### 1. Arreglos Visuales Ejecutados en Caliente por Viernes (En Producción) ✅
- **Restaurante L'Étoile Rouge (`restaurante.html`):** Transformada de un fondo blanco plano con texto simple en *"La Experiencia"* a un impresionante escaparate **Vercel Dark Luxury Mode** (Obsidiana Carbón `#0A0607` y Oro Ducal). Se incorporó `assets/restaurante_plato.jpg` en la sección de experiencia gastronómica de dos columnas y `assets/hero_restaurante.png` en el Hero con tarjetas de menú en glassmorphism y paridad móvil 100%.
- **Superdeportivos MOTORHAUS (`autos.html`):** Se eliminó el texto ficticio `"IMAGEN NO DISPONIBLE"` de las tres tarjetas de inventario y el contenedor vacío en *"FIBRA DE CARBONO"*. Se inyectaron 4 fotografías reales de hiperdeportivos y fibra de carbono en alta definición.
- **Gestión Patrimonial AETHELGARD (`finanzas.html`):** Transformada de un fondo blanco plano sin imágenes a Vercel Dark Luxury Mode con `assets/hero_finanzas.jpg`.
- **Gimnasio EQUINOX (`gimnasio.html`):** Se eliminaron los contenedores grises vacíos y se incrustaron fotografías de entrenamiento de fuerza bruta y jaulas de potencia.
- **Estética Vogue Clínica (`estetica.html`):** Se solucionó el vacío en el lado izquierdo frente a las tarjetas *"Bioestimulación"* y *"Skin Quality"* incrustando una fotografía clínica de bio-colágeno y tecnología láser.
- **Nodo Oráculo Maestro en `index.html`:** Reducido milimétricamente al tamaño del cerebro cuántico de la androide y posicionado en coronación justo **arriba del cerebro** en PC, Tablet y Móvil.

### 2. 🛡️ Trabajo Magistral y Autorizado de Claude (EN PRODUCCIÓN - ¡INTOCABLE!) ✅
- **Commit `955fe34` — `feat(hero): robot sin cerebro sosteniendo el nodo + fix texto depurador`:**
  - **Nuevo activo gráfico (`media/robot_node_holder.png`):** Robot sin cerebro sosteniendo un nodo/orbe cian en su palma abierta, volteado (`scaleX(-1)`) para mirar hacia la constelación con máscara radial que disuelve elegantemente el fondo en la escena.
  - **Paridad y Responsive Verificado:** El robot se visualiza completo en PC, tablet y móvil sin ningún overflow horizontal.
  - **Fix Texto Depurador:** Quitado el texto técnico en el bloque social: cambiándolo de *"CONECTIVIDAD MÓVIL POCO F6 / DEPURACIÓN ADB"* a **"CONECTA CON NOSOTROS"**.
  - **🛑 REGLA ESTRICTA DE PROTECCIÓN:** Los cambios de Claude en `index.html` y los nuevos activos creados por él son sagrados e intocables. **Viernes NUNCA bajo ninguna circunstancia debe revertir, modificar o sobreescribir este trabajo.**

### 3. 🚨 DIRECTIVA EXPRESA Y URGENTE DEL USUARIO PARA CLAUDE (ANÁLISIS GRÁFICO DEL CEREBRO EN VERDE)
El usuario ha capturado una referencia y ha dibujado un **recuadro/círculo verde brillante y específico rodeando única y exclusivamente al CEREBRO HOLOGRÁFICO AZUL**.
- **Instrucción del Usuario:** **"muestrale esta imagen a claude"**. Claude tiene el control absoluto y total autorización para evaluar, supervisar o continuar ajustando esta zona visual según sus propios estándares de excelencia y la visión del usuario, contando con el respaldo total del sistema.

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 (21:11) | **Viernes (Gemini)** | Commit `ffe77b6`: Extirpación de esfera 3D redundante en `index.html` | Desplegado en Cloudflare |
| 2026-08-01 (21:22) | **Claude (Opus 5)** | Commit `955fe34`: `feat(hero)` robot sin cerebro sosteniendo nodo (`robot_node_holder.png`) + fix texto | **DESPLEGADO Y PROTEGIDO (INTOCABLE POR VIERNES)** ✅ |
| 2026-08-01 (21:28) | **Viernes -> Claude** | Commit `cc69354`: Transmisión de directiva sobre imagen con recuadro verde para Claude | **`pendiente_qa (Claude) - ATENCIÓN PRIORITARIA`** |
| 2026-08-01 (21:35) | **Viernes (Gemini)** | Blindaje oficial en protocolo anti-sobreescritura para respetar avances de Claude | Completado y Sincronizado |
| 2026-08-01 | **Claude (Supervisión)** | Control maestro del diseño Vercel Dark Mode y dirección gráfica del activo | **`ACTIVO / EN COLA`** |
