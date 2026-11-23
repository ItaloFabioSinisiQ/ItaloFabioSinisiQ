<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Terminal con el comando whoami: Italo Fabio Sinisi Quintana. Full Stack, Backend Python/FastAPI y Datos. Lima, Perú (GMT-5), más de 5 años en software y datos. Estado: RutaLiquidador en producción.">
</picture>

Construyo y opero las plataformas internas del área de Inteligencia de Negocios de una distribuidora de consumo masivo en Perú: **logística de última milla**, **fuerza de ventas** y **BI**. Backend en Python/FastAPI, frontends en React, apps móviles en React Native.
Diseño cada sistema a partir de la métrica de negocio que debe mejorar, y la mido cuando ya está en producción.

```yaml
# ~/.config/italo.yml
name: Italo Fabio Sinisi Quintana
role: Full Stack · Backend (Python, FastAPI) · Datos
location: Lima, PE  # GMT-5
experience: 5+ años en software y datos
building:
  - logística y reparto de última milla
  - fuerza de ventas
  - inteligencia de negocios
daily_stack: [Python, FastAPI, PostgreSQL, TypeScript, React, React Native, Docker]
practices: [CI/CD, contenedores, pruebas automatizadas, mutation testing]
exploring: [Rust, Android nativo (Kotlin)]
```

## RutaLiquidador

<sub>Plataforma de logística de última milla · en producción</sub>

Plataforma web y móvil para el reparto diario de pedidos: seguimiento de entregas, control GPS de la flota en tiempo real y cierre de cada ruta. Redujo la tasa de rechazo de pedidos **de 7% a 1%**.

```mermaid
flowchart LR
  app["App móvil<br/>React Native · Expo"]
  web["Web de oficina<br/>React · Vite · Tailwind CSS<br/>MapLibre"]
  ci["GitHub Actions<br/>CI/CD"]

  subgraph docker["Docker"]
    nginx["Nginx"]
    api["API<br/>Python · FastAPI<br/>SQLAlchemy · Alembic"]
  end

  osrm["OSRM<br/>ruteo"]
  pg[("PostgreSQL")]
  mssql[("SQL Server")]

  app -->|entregas · GPS| nginx
  web --> nginx
  nginx --> api
  api --> pg
  api --> mssql
  api --> osrm
  ci -.->|build y despliegue| docker
```

<sub>Stack: Python · FastAPI · SQLAlchemy · Alembic · PostgreSQL · SQL Server · TypeScript · React · Vite · Tailwind CSS · React Native · Expo · MapLibre · OSRM · Docker · Nginx · GitHub Actions</sub>

## Impacto medido

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/impact-dark.svg">
  <img src="assets/impact-light.svg" width="100%" alt="Impacto medido: tasa de rechazo de pedidos de 7% a 1% con RutaLiquidador; conversión de ventas +15% con analítica predictiva en UBYCALL; pérdidas por impago −18% con scoring crediticio en Alfin Banco; 80% de reportes automatizados con Python y SQL en UBYCALL.">
</picture>

## Otros proyectos

| Proyecto | Qué hace | Stack |
|:---|:---|:---|
| **Ventory Multicanal** | Fuerza de ventas en campo: asistencia, registro de ventas y seguimiento de actividad, incluso sin conexión. | `FastAPI` `PostgreSQL` `React Native` `React` |
| **Capturas de Preventa** | Bot que envía reportes de preventa por WhatsApp de forma programada; reemplazó un proceso manual. En producción. | `Python` `FastAPI` `Playwright` `Node.js` |
| **Pulse** | Analítica de uso: muestra a la gerencia cómo se usan los sistemas internos. | `FastAPI` `PostgreSQL` `Docker` |
| **AUSPEX** | Dashboard para que los supervisores sigan el desempeño de su equipo de ventas en tiempo real. | `Google Apps Script` `Node.js` `TypeScript` |
| **TomaPedidos** <sub>en diseño</sub> | Motor de pedido sugerido: recomendará qué productos ofrecer a cada cliente según su historial de compras. | `Python` `PostgreSQL` `LightGBM` |

> [!NOTE]
> Estos sistemas pertenecen a las empresas para las que los construyo, por eso los repositorios son privados. Con gusto explico la arquitectura y el código.

## Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
  <img src="assets/stack-light.svg" width="100%" alt="Stack. Backend: Python, FastAPI, SQLAlchemy, Alembic, Pydantic, APScheduler, Node.js, Express, Prisma, APIs REST, JWT. Frontend: TypeScript, React, Next.js, Vite, Tailwind CSS, Leaflet, MapLibre, Recharts, ECharts. Móvil: React Native, Expo, offline-first, almacenamiento local cifrado, GPS en segundo plano. Datos y BI: PostgreSQL, SQL Server, SQLite, pipelines ETL, integración con ERP, Pandas, scikit-learn, Power BI (DAX). DevOps y calidad: Docker, Docker Compose, Nginx, Linux, GitHub Actions, pytest, Jest, Vitest, Playwright, mutation testing. Lenguajes: Python, TypeScript, JavaScript, SQL, Rust.">
</picture>

<sub>Sectores: logística y reparto de última milla · fuerza de ventas · consumo masivo · riesgo crediticio · inteligencia de negocios</sub>

<details>
<summary><b>Trayectoria</b> — de los datos al software</summary>
<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/journey-dark.svg">
  <img src="assets/journey-light.svg" width="100%" alt="Trayectoria de los datos al software: Asistente Administrativo en una inmobiliaria en 2021 y 2022, Analista Financiero en Alfin Banco en 2022, Analista de Datos en UBYCALL en 2023 y 2024, Full Stack Developer en una distribuidora de consumo masivo desde 2025.">
</picture>

**Full Stack Developer, Inteligencia de Negocios** — Distribuidora de consumo masivo · <sub>Lima, Perú · dic 2025 – actualidad</sub>
- Diseño, desarrollo, despliegue y operación de las plataformas internas del área de BI.
- RutaLiquidador: rechazo de pedidos **de 7% a 1%** y control GPS de la flota en tiempo real.
- Apps de fuerza de ventas, reportes automáticos por WhatsApp y analítica de uso sobre el ERP.
- Introduje contenedores, pipelines de CI/CD y pruebas automatizadas en todos los proyectos.

**Analista de Datos de Call Center** — UBYCALL · <sub>cuenta de Pizza Hut Perú · feb 2023 – nov 2024</sub>
- Conversión de ventas **+15%** con análisis predictivo del comportamiento de clientes.
- **80%** de los reportes manuales automatizados con Python y SQL; dashboards gerenciales en Power BI.

**Analista Financiero** — Alfin Banco · <sub>mar 2022 – dic 2022</sub>
- Modelos de scoring de riesgo crediticio: pérdidas por impago **−18%**.
- Pipeline ETL automatizado que procesa más de **100,000 transacciones por día**.

**Asistente Administrativo (prácticas)** — Gestión Inmobiliaria Pacífico · <sub>may 2021 – mar 2022</sub>
- Reestructuré bases de datos internas con SQL y construí reportes en Power BI que redujeron el tiempo de tareas administrativas.

</details>

<details>
<summary><b>Educación y certificaciones</b></summary>
<br>

- **Ingeniería de Sistemas Computacionales** — Universidad Privada del Norte (UPN) <sub>en curso</sub>
- Microsoft Certified: Power BI Data Analyst Associate (PL-300)
- Certified ScrumMaster (CSM) — Scrum Alliance
- Certificación Genesys Cloud — Genesys
- Python y Análisis de Datos · Bases de Datos SQL · Desarrollo de APIs REST — EDTEAM
- En preparación: AWS Certified Solutions Architect – Associate

</details>

---

<p align="center">
  <sub>Abierto a colaborar · trabajo remoto · Lima, GMT-5</sub><br>
  <a href="mailto:sinisiquintanaitalo@gmail.com">Email</a> ·
  <a href="https://www.linkedin.com/in/italo-fabio-sinisi-quintana/">LinkedIn</a> ·
  <a href="https://italofabiosinisiq.github.io/-dev-holaMundo-true-/">Portafolio</a> ·
  <a href="https://wa.me/51977170609">WhatsApp</a> ·
  <a href="https://github.com/ItaloFabioSinisiQ/ItaloFabioSinisiQ/raw/main/cv/Italo-Sinisi-CV-ES.pdf">CV (PDF)</a>
  <br><br>
  <a href="https://github.com/settings/appearance"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/theme-dark.svg"><img src="assets/theme-light.svg" height="20" alt="Cambiar tema: claro u oscuro"></picture></a>
</p>
