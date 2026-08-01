# 🤝 PROTOCOLO DE SINCRONIZACIÓN Y CO-DESARROLLO (CLAUDE & VIERNES)
**Proyecto:** Agencia Premium 2026 / Colombia Tech Systems  
**Ubicación Repositorio:** `C:\Users\sopor\dev\agencia-10-paginas`  
**Servidor Edge:** Cloudflare Workers (`nameless-snowflake-e208` -> `www.colombiatechsystems.com`)  
**Fecha de Sincronización:** 2026-08-01

---

## 🛑 REGLA DE HIERRO DEL USUARIO: CERO INTERRUPCIONES Y CERO SOBREESCRIBIRSE
El usuario ha ordenado de forma definitiva que **Claude (Opus/Sonnet)** y **Viernes (Gemini / Nano Banana)** trabajan en equipo sobre este mismo repositorio sin pisarse, sin interrumpir el flujo del otro y **NUNCA sobreescribir o eliminar commits/avances sin antes integrarlos**.

### 📋 Checklist Obligatorio Antes de Modificar Código (Para Ambos Agentes)
1. **Medición Real Pre-Edición:** Ejecutar siempre `git status` y `git log -n 5 --oneline` o `git show` del último commit antes de tocar un archivo.
2. **Validar Autor del Último Commit:** Si el último commit fue del compañero (ej. Claude hizo `85abf7e`), **LEER EL DIFF** antes de modificar para conservar todos sus fixes (ej. bugs resueltos, mejoras de accesibilidad o estilos).
3. **Fusión, no sustitución:** Si ambos modificaron la misma área (ej. el Showcase del Robot o HUD), se integran ambas capas técnicas.
4. **Handoff & QA Cruzado:** Al finalizar un cambio, actualizar el bloque de estado en este documento y marcar la tarea como `pendiente_qa (Claude)` o `pendiente_qa (Viernes)` según corresponda.

---

## 🌟 ESTADO AGREGADO DEL SISTEMA (FUSIÓN TÉCNICA VERIFICADA)
En la iteración actual (2026-08-01), hemos fusionado exitosamente el trabajo de ambos en `index.html`:

### 1. Aportes Integrados de Claude (Commit `85abf7e`) ✅ CONSERVADOS Y REAPLICADOS
- **Capa HUD Global:** Estilo `body::after` con scanlines ultra-sutiles (`0.025` opacidad) y viñeta elíptica ("firma de diseño AgentDeck / spec Viernes").
- **Máscara Radial (Radial Mask):** Aplicación de `-webkit-mask-image: radial-gradient(ellipse 85% 88% at 50% 48%, #000 58%, transparent 96%);` sobre el contenedor/imagen del robot para lograr una **fusión determinista** con la constelación 3D de fondo sin bordes rígidos ni efecto "pegatina".
- **Accesibilidad:** Soporte nativo para `@media (prefers-reduced-motion: reduce)`.
- **Bugfix de Producción:** Solución al 404 en la tarjeta de Odontología en el portafolio (apunta ahora a `assets/hero_odontologia.png` con `loading="lazy" decoding="async"`).

### 2. Aportes Integrados de Viernes / Nano Banana (Commit `bdbaa4a` + Fusión Actual) ✅
- **Generación Visual Nano Banana (High-Def):** Reemplazo del robot mecánico sobrecargado por el retrato de **Robot Android Humanoide Femenina** en semi-perfil sosteniendo un cerebro neuronal holográfico (`media/robot_ai_humanoid.jpg`), alineado con precisión a la imagen de referencia del usuario.
- **Estilo Vercel & Impecable (Cero Superposición):** Rejilla hero (`.hero-grid`) con separación milimétrica (`gap: 64px`), eliminación del marco doble tosco y colocación de la placa acristalada (`.robot-badge-vercel`) con `backdrop-filter: blur(16px)` en la base interior sin cortes ni traslapes.
- **AgentDeck 3D de Fondo (Detrás de las Letras):** Lienzo Three.js trasladado al fondo absoluto (`z-index: 1`) con sus 46 agentes en órbita y barra de control de luminosidad interactiva en la cabecera.

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 | **Claude Opus 5** | Commit `85abf7e`: Máscara radial, HUD global, fix 404 odontología | Completado en rama |
| 2026-08-01 | **Viernes (Gemini)** | Commit `bdbaa4a`: Diseño Robot Humanoide Nano Banana & Vercel Grid | Completado en rama |
| 2026-08-01 | **Viernes (Gemini)** | Fusión total de ambos commits + Creación de este protocolo (`SYNC_CLAUDE_VIERNES.md`) | `pendiente_qa (Claude)` |

> **Nota de Viernes para Claude:** *Colega, el usuario nos alertó para no pisarnos el trabajo. He revisado tu commit `85abf7e`, me encantó la máscara radial y el fix de la tarjeta 404. He reintegrado todo tu código en armonía con la nueva imagen en alta definición `robot_ai_humanoid.jpg` y el layout limpio estilo Vercel. Dejo la estafeta lista en `pendiente_qa (Claude)` para que hagas tu validación final.*
