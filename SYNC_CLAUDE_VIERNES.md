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
En la iteración actual (2026-08-01 13:35), se ejecutaron y verificaron los siguientes avances en estricto cumplimiento del diseño JARVIS PC:

### 1. Robot Humanoide Anclado en el Extremo Derecho ✅
- **Posición Inamovible a Petición del Usuario:** La silueta pura sin fondo (`robot_ai_humanoid_transparent.png`) se mantiene firmemente anclada al ras de la pantalla en `position: absolute; right: -10px; top: 52%;`. Su espalda comienza en la orilla derecha de la pantalla y mira hacia la red neuronal central.

### 2. AgentDeck 3D Centrado en el Lienzo ✅
- **Centrado Cartesiano en Three.js:** Se regresó la posición de `constellationGroup` al centro exacto (`X=0, Y=1.5, Z=-0.5`).
- **Equilibrio Visual del Ecosistema:** Ahora la composición presenta los tres pilares de Colombia Tech Systems en una sinergia perfecta:
  - **Izquierda (0% - 54%):** Títulos principales, descripción, métricas y botones CTAs con legibilidad garantizada.
  - **Centro (X=0):** Núcleo Oráculo Maestro y órbitas wireframe de los 46 agentes girando en el espacio 3D.
  - **Derecha (Al Ras Exterior):** Robot Android IA extendiendo su mano e impulsos cerebrales desde la orilla derecha hacia la constelación central en el mismo plano de flotación 3D.

### 3. Preservación y Respeto Absoluto a Claude ✅
- **Parches y Mejoras Mantenidos:** Conservados inalterados los aportes de Claude (scanlines globales, accesibilidad `prefers-reduced-motion` y la corrección de 404 del portafolio en `hero_odontologia.png`).

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 | **Claude Opus 5** | Commit `85abf7e`: Máscara radial, HUD global, fix 404 odontología | Completado en rama |
| 2026-08-01 | **Viernes (Gemini)** | Commit `2bf98ef`: Contorno desvanecido (mix-blend-mode) y Nodos Icosaedro Wireframe | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `4d2beab`: Alineate Robot y AgentDeck 3D a la derecha | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `9bcfb10`: Robot en borde derecho exacto + silueta PNG transparente | Completado y verificado |
| 2026-08-01 (13:35) | **Viernes (Gemini)** | Robot inamovible en borde derecho y AgentDeck 3D centrado en el lienzo | `pendiente_qa (Claude)` |

> **Nota de Viernes para Claude:** *Colega, el usuario ordenó mantener la silueta del robot exactamente donde quedó (con la espalda cortando en la orilla derecha externa) y recentrar el clúster AgentDeck 3D de Three.js en el centro exacto de la pantalla (`X=0`). He aplicado esta distribución armónica tripartita en `index.html`. Queda en `pendiente_qa (Claude)` para tu supervisión y relevo.*
