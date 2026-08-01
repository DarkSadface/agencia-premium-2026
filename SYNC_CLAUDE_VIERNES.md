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
En la iteración actual (2026-08-01 13:28), se ejecutaron y verificaron los siguientes avances en estricto cumplimiento del diseño JARVIS PC:

### 1. Silueta Pura Sin Fondo (PNG Transparente + Fusión Cuántica) ✅
- **Procesamiento de Imagen en Python:** Se generó `media/robot_ai_humanoid_transparent.png` mediante un algoritmo que convirtió el fondo oscuro a 100% transparente (Alpha 0) preservando el brillo y los fotones del androide y su cerebro neuronal.
- **Cero Recuadros ni Marcos:** La imagen ya no necesita recuadro, degradados difusos de corte ni fondo rectangular; es una silueta pura flotando libre en el lienzo de Three.js.

### 2. Espalda Anclada al Borde Derecho Exacto del Pantalla ✅
- **Posicionamiento Absoluto al Ras de Pantalla:** Se colocó `.robot-showcase-hologram` en `position: absolute; right: -10px; top: 52%;`. Esto garantiza que **la espalda del robot comienza justo en la orilla derecha de la pantalla del usuario**, mirando con autoridad hacia el lado izquierdo donde resplandece el título de la marca.
- **Despeje de Textos:** El lado izquierdo ocupa el 54% del ancho en exclusiva, sin empujar al robot y sin sufrir ruido visual de fondo.

### 3. Integración en el Exacto Mismo Plano del AgentDeck 3D ✅
- **Coordenadas Unificadas en Three.js:** Se situó el `constellationGroup` de Three.js en `X=+7.8, Y=1.2, Z=-0.5`, concentrando el Núcleo Oráculo Maestro y las órbitas icosaédricas wireframe de los 46 agentes alrededor de la mano y el cerebro iluminado del robot.
- **Profundidad de Capas y Etiquetas:** Al mantener `mix-blend-mode: screen` en el robot, los rayos del lienzo resplandecen a través de la silueta y las etiquetas `.node-label` de los agentes operan en `z-index: 8` flotando alrededor del rostro y dedos de la IA en auténtico parallax 3D.

### 4. Preservación y Respeto Absoluto a Claude ✅
- **Parches y Mejoras Mantenidos:** Conservados inalterados los aportes de Claude (scanlines globales, accesibilidad `prefers-reduced-motion` y la corrección de 404 del portafolio en `hero_odontologia.png`).

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 | **Claude Opus 5** | Commit `85abf7e`: Máscara radial, HUD global, fix 404 odontología | Completado en rama |
| 2026-08-01 | **Viernes (Gemini)** | Commit `2bf98ef`: Contorno desvanecido (mix-blend-mode) y Nodos Icosaedro Wireframe | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `4d2beab`: Alineate Robot y AgentDeck 3D a la derecha | Completado y verificado |
| 2026-08-01 (13:28) | **Viernes (Gemini)** | Robot anclado con espalda en el borde derecho de pantalla + Silueta PNG en plano 3D | `pendiente_qa (Claude)` |

> **Nota de Viernes para Claude:** *Colega, el usuario ordenó recortar el fondo del robot para tener únicamente la silueta y su cerebro luminoso, posicionando la espalda al ras del borde derecho de la pantalla e integrando sus coordenadas con el plano 3D del AgentDeck. Generé el asset `robot_ai_humanoid_transparent.png`, alineé el elemento absoluto al límite `right: -10px` del viewport y sincronicé las coordenadas en Three.js (`X=+7.8`). Queda rotulado como `pendiente_qa (Claude)` para nuestra verificación de equipo.*
