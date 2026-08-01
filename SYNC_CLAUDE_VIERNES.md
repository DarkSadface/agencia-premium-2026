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

### 2. Directiva del Usuario para Claude: Rediseño Impecable Vercel ⏳ (`pendiente_ejecucion (Claude)`)
- **Abogados (`abogados.html`):** Corregir el contraste del titular principal (*"Justicia. Precisión. Discreción."*) e inyectar excelencia lumínica Vercel Dark Mode sobre `assets/hero_abogados.png`.
> **Consultar documento dedicado:** [CLAUDE_VERCEL_REDESIGN_TASKS.md](file:///C:/Users/sopor/dev/agencia-10-paginas/CLAUDE_VERCEL_REDESIGN_TASKS.md).

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 (16:15) | **Viernes (Gemini)** | Commit `34c19ce`: Fix imágenes rotas/vacías en `gimnasio.html` y `estetica.html` | Completado en Cloudflare |
| 2026-08-01 (16:35) | **Viernes (Gemini)** | Commit `cbcfbe3`: Rediseño Vercel Dark Luxury de `finanzas.html` con `assets/hero_finanzas.jpg` | Completado en Cloudflare |
| 2026-08-01 (16:45) | **Viernes (Gemini)** | Commit `2b52cd1`: Fix 4 imágenes rotas/vacías ("IMAGEN NO DISPONIBLE") en `autos.html` | Completado en Cloudflare |
| 2026-08-01 (16:55) | **Viernes (Gemini)** | Rediseño Vercel Dark Luxury de `restaurante.html` con `assets/restaurante_plato.jpg` | `pendiente_qa (Claude)` |
| 2026-08-01 | **Claude (Supervisión)** | Rediseño estilo Vercel Dark Mode de `abogados.html` | **`EN COLA (Próximo paso de Claude)`** |
