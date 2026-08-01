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
En la iteración actual (2026-08-01 13:40), se ejecutaron y verificaron los siguientes avances en estricto cumplimiento del diseño JARVIS PC:

### 1. Nodos Orbitales Más Pequeños y Precisos ✅
- **Reducción Cartesiana en Three.js:** El radio del `IcosahedronGeometry` de los 46 agentes satélite fue reducido de `0.58` a `0.28` y su núcleo interno de `0.22` a `0.12`. Esto les otorga una apariencia mucho más refinada y menos invasiva en el espacio 3D.

### 2. Cero Recuadros de Contorno en Nombres de Agentes (Texto Puro) ✅
- **Estética Limpia Sin Cajas:** Se eliminaron por completo las propiedades `border`, `background` y `box-shadow` en el selector CSS `.node-label`. Ahora los nombres de los agentes flotan sin ningún marco rectangular alrededor, luciendo exclusivamente como texto luminoso con sombra de neón en la profundidad 3D.

### 3. Nodo Central Oráculo Maestro Conserva su Tamaño Majestuoso ✅
- **Dimensión Inamovible:** El núcleo `coreGeo = new THREE.IcosahedronGeometry(2.6, 2);` conserva su tamaño y jerarquía original, reinando de forma dominante en el centro exacto de la constelación (`X=0, Y=1.5, Z=-0.5`).

### 4. Preservación y Respeto Absoluto a Claude ✅
- **Parches y Mejoras Mantenidos:** Conservados inalterados los aportes de Claude (scanlines globales, accesibilidad `prefers-reduced-motion` y la corrección de 404 del portafolio en `hero_odontologia.png`).

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 | **Claude Opus 5** | Commit `85abf7e`: Máscara radial, HUD global, fix 404 odontología | Completado en rama |
| 2026-08-01 | **Viernes (Gemini)** | Commit `2bf98ef`: Contorno desvanecido (mix-blend-mode) y Nodos Icosaedro Wireframe | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `4d2beab`: Alineate Robot y AgentDeck 3D a la derecha | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `9bcfb10`: Robot en borde derecho exacto + silueta PNG transparente | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `8d4433a`: Robot inamovible en borde derecho y AgentDeck 3D centrado en el lienzo | Completado y verificado |
| 2026-08-01 (13:40) | **Viernes (Gemini)** | Nodos orbitales más pequeños, eliminación de cajas en etiquetas (solo texto), nodo central tamaño intacto | `pendiente_qa (Claude)` |

> **Nota de Viernes para Claude:** *Colega, el usuario solicitó reducir el tamaño de los nodos orbitales del AgentDeck 3D (pasamos de geometría `0.58` a `0.28`), eliminar los recuadros de contorno de las etiquetas de texto de cada nodo para dejar solo el nombre flotante sin caja, y mantener el nodo central Oráculo Maestro en su tamaño original (`2.6`). He aplicado todo esto en `index.html`. Queda en `pendiente_qa (Claude)` para tu supervisión y relevo.*
