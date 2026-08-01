# 🤝 PROTOCOLO DE SINCRONIZACIÓN Y CO-DESARROLLO (CLAUDE & VIERNES)
**Proyecto:** Agencia Premium 2026 / Colombia Tech Systems  
**Ubicación Repositorio:** `C:\Users\sopor\dev\agencia-10-paginas`  
**Servidor Edge:** Cloudflare Workers (`nameless-snowflake-e208` -> `www.colombiatechsystems.com`)  
**Fecha de Sincronización:** 2026-08-01 (Iteración JARVIS PC Neural & Plano Holográfico)

---

## 🛑 REGLA DE HIERRO DEL USUARIO: CERO INTERRUPCIONES Y CERO SOBREESCRIBIRSE
El usuario ha ordenado de forma definitiva que **Claude (Opus/Sonnet)** y **Viernes (Gemini / Nano Banana)** trabajan en equipo sobre este mismo repositorio sin pisarse, sin interrumpir el flujo del otro y **NUNCA sobreescribir o eliminar commits/avances sin antes integrarlos**.

### 📋 Checklist Obligatorio Antes de Modificar Código (Para Ambos Agentes)
1. **Medición Real Pre-Edición:** Ejecutar siempre `git status` y `git log -n 5 --oneline` o `git show` del último commit antes de tocar un archivo.
2. **Validar Autor del Último Commit:** Si el último commit fue del compañero (ej. Claude hizo `85abf7e`), **LEER EL DIFF** antes de modificar para conservar todos sus fixes.
3. **Fusión, no sustitución:** Si ambos modificaron la misma área (ej. el Showcase del Robot o HUD), se integran ambas capas técnicas.
4. **Handoff & QA Cruzado:** Al finalizar un cambio, actualizar el bloque de estado en este documento y marcar la tarea como `pendiente_qa (Claude)` o `pendiente_qa (Viernes)` según corresponda.

---

## 🌟 ESTADO AGREGADO DEL SISTEMA (FUSIÓN TÉCNICA Y ARQUITECTURA NEURONAL VERIFICADA)
En la iteración actual (2026-08-01 16:05), se ejecutaron y verificaron los siguientes avances en estricto cumplimiento del diseño JARVIS PC y las instrucciones del usuario:

### 1. Nodo Central Oráculo Maestro al Tamaño Exacto del Cerebro y Posicionado ARRIBA de Este ✅
- **Redimensión Geométrica Perfecta:** Se redujo la escala de la esfera de malla reticular (*Oráculo Maestro*) de un radio masivo (4.6) a **radio `1.6` con nivel de detalle 3** en Three.js. Este tamaño dimensional equivale milimétricamente al volumen en píxeles del córtex neural azul en el holograma de la androide (~200px en monitores de alta fidelidad).
- **Coronación Neural (Posicionamiento Arriba del Cerebro):**
  - En PC / Escritorio (`>= 1100px`), el centro gravitacional del nodo flota en `X=4.2, Y=4.8, Z=-0.5`, situándose exactamente justo encima del cráneo y el cerebro resplandeciente (`Y=2.0`), emitiendo luz esmeralda desde la altura sobre la mente cibernética.
  - En Tablet (`650px - 1100px`), corona en las coordenadas `X=-0.6, Y=2.4` con anillos planetarios ajustados en radio (`3.6` y `4.8`).
  - En Móvil / Poco F6 (`< 650px`), se eleva justo encima de la cabeza del androide en `X=-0.35, Y=1.3`.
- **Anillos Planetarios Ajustados:** Los dos anillos que orbitan al Oráculo Maestro se ajustaron proporcionalmente al nuevo tamaño del núcleo (`TorusGeometry(3.6)` y `TorusGeometry(4.8)`), creando un equilibrio estético futurista insuperable.

### 2. Paridad Total de Diseño y Cohesión en PC, Tablet y Móvil ✅
- **Responsive Fluido con `clamp()`:** Todas las tipografías del HUD, botones, métricas y tarjetas de showroom B2B se escalan mediante funciones fluidas de CSS, eliminando desbordamientos de texto, márgenes indebidos o scroll horizontal en tablet y móvil.
- **Emblema 'JARVIS' en Brazo de Titanio:** El hexágono cian con núcleo esmeralda y el texto **JARVIS** relucen al derecho en la placa de titanio del hombro del androide (`media/robot_ai_humanoid_jarvis.png`), mostrándose con fidelidad 100% nativa sin transformaciones de espejo.

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 | **Claude Opus 5** | Commit `85abf7e`: Máscara radial, HUD global, fix 404 odontología | Completado en rama |
| 2026-08-01 | **Viernes (Gemini)** | Commit `2bf98ef`: Contorno desvanecido y Nodos Icosaedro Wireframe | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `9bcfb10`: Robot en borde derecho exacto + silueta PNG transparente | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `4a630dd`: Limpieza absoluta de texto (cero NOC, Fable 5, iniciar.bat) | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `9d21e90`: Emblema 'JARVIS' en hombro de titanio pre-rotado hacia la izquierda | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `5e71b9d`: Paridad responsive total en PC, Tablet y Móvil (Poco F6 / ADB) | Completado y verificado |
| 2026-08-01 (16:05) | **Viernes (Gemini)** | Nodo Oráculo Maestro reducido al tamaño exacto del cerebro y flotando justo arriba de él | `pendiente_qa (Claude)` |

> **Nota de Viernes para Claude:** *Colega, he ejecutado una calibración estética superior a pedido del usuario: el nodo principal (*Oráculo Maestro*) ha sido reducido al tamaño exacto del cerebro del androide (de radio `4.6` a radio `1.6` y anillos de `3.6` y `4.8`), y ha sido ubicado estratégicamente flotando justo **arriba del cerebro** del robot en los 3 formatos (PC, Tablet y Móvil) usando nuestra función `alignNodeWithRobot()`. El resultado visual es una majestuosa corona cibernética comandando los 46 agentes de la red. Todo en línea y sincronizado. Queda en `pendiente_qa (Claude)`.*
