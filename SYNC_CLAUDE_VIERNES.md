# 🤝 PROTOCOLO DE SINCRONIZACIÓN Y CO-DESARROLLO (CLAUDE & VIERNES)
**Proyecto:** Agencia Premium 2026 / Colombia Tech Systems  
**Ubicación Repositorio:** `C:\Users\sopor\dev\agencia-10-paginas`  
**Servidor Edge:** Cloudflare Workers (`nameless-snowflake-e208` -> `www.colombiatechsystems.com`)  
**Fecha de Sincronización:** 2026-08-01 (Iteración 16:45 COT)

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

### 1. Arreglos Visuales Invertidos y Ejecutados en Caliente por Viernes (En Producción) ✅
- **Superdeportivos MOTORHAUS (`autos.html`):** Se eliminó el texto ficticio `"IMAGEN NO DISPONIBLE"` de las tres tarjetas de inventario (*Apex V8*, *Nemesis Híbrido*, *Spectre Track-Only*) y el contenedor vacío con rayas grises en *"FIBRA DE CARBONO GRADO MILITAR"*. Se inyectaron 4 fotografías reales de hiperdeportivos y fibra de carbono en alta definición con efectos zoom y neón rojo.
- **Gestión Patrimonial AETHELGARD (`finanzas.html`):** Transformada de un fondo blanco plano sin imágenes a una obra maestra **Vercel Dark Luxury Mode** (`#04070E` y Oro Ducal `#D4AF37`). Se incorporó `assets/hero_finanzas.jpg` en una torre arquitectónica flotante en el Hero y una segunda fotografía institucional de mercados en la sección de Filosofía de Inversión, con paridad móvil garantizada.
- **Gimnasio EQUINOX (`gimnasio.html`):** Se eliminaron los contenedores grises vacíos (divs con gradiente CSS) y se incrustaron fotografías de entrenamiento de fuerza bruta y jaulas de potencia en alta resolución.
- **Estética Vogue Clínica (`estetica.html`):** Se solucionó el vacío en el lado izquierdo frente a las tarjetas *"Bioestimulación"* y *"Skin Quality"* incrustando una fotografía clínica de bio-colágeno y tecnología láser en un grid responsive de dos columnas.
- **Nodo Oráculo Maestro en `index.html`:** Reducido milimétricamente al tamaño del cerebro cuántico de la androide (radio `1.6`) y posicionado flotando en coronación justo **arriba del cerebro** en PC, Tablet y Móvil (Poco F6 / ADB).

### 2. Directiva del Usuario para Claude: Rediseño Impecable Vercel ⏳ (`pendiente_ejecucion (Claude)`)
El usuario ha asignado formalmente a **Claude** el rediseño de dos páginas críticas con estándar **Vercel Dark Mode Impecable**:
- **Abogados (`abogados.html`):** Corregir la ilegibilidad del titular principal (*"Justicia. Precisión. Discreción."*), el cual se oscurece contra el fondo negro. Colocar fondo arquitectónico inmersivo con `assets/hero_abogados.png`, textos blanco puro / oro ducal y efectos lumínicos Vercel.
- **Restaurante L'Étoile Rouge (`restaurante.html`):** Reemplazar el fondo blanco plano con degradado cian deslucido por una experiencia gastronómica VIP inmersiva en Dark Mode carbón, borgoña y oro, utilizando `assets/hero_restaurante.png` de fondo escénico.
> **Consultar documento dedicado:** [CLAUDE_VERCEL_REDESIGN_TASKS.md](file:///C:/Users/sopor/dev/agencia-10-paginas/CLAUDE_VERCEL_REDESIGN_TASKS.md) para el detalle completo del diagnóstico.

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 | **Claude Opus 5** | Commit `85abf7e`: Máscara radial, HUD global, fix 404 odontología | Completado en rama |
| 2026-08-01 | **Viernes (Gemini)** | Commit `5e71b9d` & `f8e3cd6`: Paridad responsive total + Nodo Oráculo Maestro | Completado y verificado |
| 2026-08-01 (16:15) | **Viernes (Gemini)** | Commit `34c19ce`: Fix imágenes rotas/vacías en `gimnasio.html` y `estetica.html` | Completado en Cloudflare |
| 2026-08-01 (16:35) | **Viernes (Gemini)** | Commit `cbcfbe3`: Rediseño Vercel Dark Luxury de `finanzas.html` con `assets/hero_finanzas.jpg` | Completado en Cloudflare |
| 2026-08-01 (16:45) | **Viernes (Gemini)** | Fix 4 imágenes rotas/vacías ("IMAGEN NO DISPONIBLE" y composite) en `autos.html` | `pendiente_qa (Claude)` |
| 2026-08-01 | **Claude (Supervisión)** | Rediseño estilo Vercel Dark Mode de `abogados.html` y `restaurante.html` | **`EN COLA (Próximo paso de Claude)`** |
