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
2. **Validar Autor del Último Commit:** Si el último commit fue del compañero (ej. Claude hizo `85abf7e`), **LEER EL DIFF** antes de modificar para conservar todos sus fixes (ej. bugs resueltos, mejoras de accesibilidad o estilos).
3. **Fusión, no sustitución:** Si ambos modificaron la misma área (ej. el Showcase del Robot o HUD), se integran ambas capas técnicas.
4. **Handoff & QA Cruzado:** Al finalizar un cambio, actualizar el bloque de estado en este documento y marcar la tarea como `pendiente_qa (Claude)` o `pendiente_qa (Viernes)` según corresponda.

---

## 🌟 ESTADO AGREGADO DEL SISTEMA (FUSIÓN TÉCNICA Y MEJORA NEURONAL VERIFICADA)
En la iteración actual (2026-08-01 13:14), se ejecutaron y verificaron los siguientes avances en estricto cumplimiento del diseño JARVIS PC:

### 1. Robot en el Mismo Plano que AgentDeck 3D & Mirada Invertida ✅
- **Orientación Corregida:** Aplicado `transform: scaleX(-1)` para que el robot mire de izquierda a derecha en dirección hacia el centro y los títulos principales.
- **Desvanecimiento Total del Contorno (Fusión Holográfica):** Combinado `mix-blend-mode: screen;` con una **máscara radial multi-parada suave** (`radial-gradient(circle at 48% 50%, #000 30%, rgba(0,0,0,0.7) 55%, rgba(0,0,0,0.2) 76%, transparent 88%)`). Todos los píxeles oscuros y bordes desaparecen por completo; el androide emerge iluminado y fundido al 100% en el lienzo AgentDeck.
- **Píldora HUD Flotante:** La placa de estado reposa flotando en el perímetro inferior como un elemento HUD sin cortar la imagen ni bloquear la constelación.

### 2. Nodos con la Exacta Misma Forma que el Nodo Central (Icosaedro Wireframe) ✅
- Todos los 46 nodos de los agentes en el motor Three.js pasaron de ser esferas simples a **Icosaedros Wireframe rotativos** (`IcosahedronGeometry(0.58, 2)` con `wireframe: true`), exactamente la misma forma geométrica futurista del Núcleo Oráculo Maestro.
- Cada nodo incorpora además un pequeño núcleo radiante en su centro (`IcosahedronGeometry(0.22, 1)`) que late con telemetría cian o ámbar al ritmo del reloj universal.

### 3. Animación Viva de Red Neuronal Estilo JARVIS PC ✅
- **Oscilación Biológica / Neuronal Individual:** Cada agente tiene su propia velocidad, fase y trayectoria senoidal 3D en lugar de rotar rígidamente en círculo.
- **Pulsos Sinápticos:** Las líneas que conectan al núcleo adaptan sus vértices dinámicamente al movimiento del nodo y parpadean con ondas sinápticas de energía (`opacity` pulsante).
- **Enjambre de Datos Holográfico & Parallax:** Añadidas 280 partículas sinápticas en adición al movimiento de cámara sensible al cursor (Parallax HUD).
- **Preservación de Fixes de Claude:** Conservado 100% el fix de 404 en el portafolio de Odontología (`assets/hero_odontologia.png`), las scanlines globales `body::after` y la accesibilidad `@media (prefers-reduced-motion: reduce)`.

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 | **Claude Opus 5** | Commit `85abf7e`: Máscara radial, HUD global, fix 404 odontología | Completado en rama |
| 2026-08-01 | **Viernes (Gemini)** | Commit `7233c7e`: Fusión total + protocolo de colaboración | Completado y verificado |
| 2026-08-01 (13:14) | **Viernes (Gemini)** | Contorno 100% desvanecido con mix-blend-mode screen y nodos Icosaedro Wireframe idénticos al central | `pendiente_qa (Claude)` |

> **Nota de Viernes para Claude:** *Colega, he llevado la integración visual a nivel cine: el contorno del robot fue desvanecido por completo con mix-blend-mode screen y máscara de difuminado radical para fundirlo sin rastros en el AgentDeck 3D. Además, reemplacé la geometría esférica de los 46 nodos por Icosaedros Wireframe rotativos (idéntica forma que el Oráculo Maestro central), manteniendo la red neuronal en vibrante movimiento. Queda en `pendiente_qa (Claude)` para tu inspección de calidad.*
