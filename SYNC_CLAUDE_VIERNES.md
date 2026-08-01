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
En la iteración actual (2026-08-01 13:45), se ejecutaron y verificaron los siguientes avances en estricto cumplimiento del diseño JARVIS PC:

### 1. Eliminación de Texto Excesivo en Etiqueta Dorada ✅
- **Optimización del Hero:** Se retiró el texto `"DE BUCLE OJO DE DIOS"` del recuadro dorado superior en la sección izquierda del hero. Ahora lee de manera concisa y escaneable: `"⚡ INGENIERÍA AGENTIC & AUTOMATIZACIÓN"`.

### 2. Nodo Central Oráculo Maestro Flotando Sobre el Cerebro del Robot (Sin Taparlo) ✅
- **Elevación Cartesiana en Three.js:** Se trasladó la coordenada maestra del `constellationGroup` a la posición `X=7.5, Y=3.5, Z=-1.2` (en resoluciones de escritorio mayores a 1200px).
- **Corona Neuronal Sin Oclusión:** Al elevar en Y (`3.5`) y dar una ligera profundidad Z (`-1.2`), el gigantesco nodo central Oráculo Maestro flota **directamente encima de la corteza cerebral brillante del androide**, irradiando luz hacia su cabeza pero **sin cubrir, tapar ni pisar en ningún momento el rostro ni el cráneo de la IA**. Los 46 agentes satélite orbitan como una constelación interactiva sobre el androide.

### 3. Nodos Orbitales Más Pequeños y Cero Recuadros en Nombres (Texto Puro) ✅
- **Estética Limpia:** Geometría reducida (`0.28`) y etiquetas `.node-label` completamente desprovistas de bordes o fondos, flotando como texto de neón en la escena 3D.

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
| 2026-08-01 | **Viernes (Gemini)** | Commit `04230f5`: Nodos orbitales más pequeños, eliminación de cajas en etiquetas (solo texto) | Completado y verificado |
| 2026-08-01 (13:45) | **Viernes (Gemini)** | Eliminado texto sobrante de etiqueta dorada + Nodo central posicionado flotando sobre el cerebro sin taparlo | `pendiente_qa (Claude)` |

> **Nota de Viernes para Claude:** *Colega, el usuario solicitó eliminar "DE BUCLE OJO DE DIOS" del badge dorado del hero (ahora queda solo "INGENIERÍA AGENTIC & AUTOMATIZACIÓN") y reposicionamos el clúster AgentDeck 3D de Three.js hacia el cuadrante superior derecho (`X=7.5, Y=3.5, Z=-1.2`), logrando que el gigantesco nodo central Oráculo Maestro flote como un halo cuántico directamente encima del cerebro brillante del androide, sin taparlo ni entorpecedr su visibilidad en el plano. He aplicado todo esto en `index.html`. Queda en `pendiente_qa (Claude)` para tu supervisión y relevo.*
