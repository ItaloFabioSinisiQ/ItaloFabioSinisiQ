<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Italo Fabio Sinisi Quintana. Full Stack Developer and Data Analyst. Logistics platforms, Business Intelligence and data engineering. Python, FastAPI, PostgreSQL, TypeScript, React, React Native, Docker, CI/CD, Rust. 5+ years of experience, based in Lima, Peru, open to remote work.">
</picture>

<p align="center">
  <a href="https://italofabiosinisiq.github.io/-dev-holaMundo-true-/"><b>Portfolio</b></a>
  &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/italo-fabio-sinisi-quintana/"><b>LinkedIn</b></a>
  &nbsp;·&nbsp;
  <a href="mailto:sinisiquintanaitalo@gmail.com"><b>Email</b></a>
  &nbsp;·&nbsp;
  <a href="https://wa.me/51977170609"><b>WhatsApp</b></a>
</p>

## Profile

I am a Full Stack Developer and Data Analyst with more than five years of experience delivering software that companies run every day. I lead software development for the Business Intelligence area at **Auren**, a mass-consumer goods distributor in Peru. There I design, build and operate the platforms behind last-mile logistics, field sales and executive reporting.

My background is in data analysis, so I start each system from the business metric it must move, and I make sure the result can be measured once it is in production. I work across the full stack: Python and FastAPI services on PostgreSQL, React and React Native clients, ERP integrations, and Docker and GitHub Actions pipelines that keep releases safe.

**Core competencies:** full stack web and mobile development · REST API design · relational data modeling · ERP and GPS integrations · offline-first mobile architecture · CI/CD and automated testing · business intelligence and analytics · AI-assisted development.

**Currently:** studying Systems & Computer Engineering at Universidad Privada del Norte (UPN). Open to remote positions with international teams, freelance engagements and challenging roles in Peru.

## Selected results

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/impact-dark.svg">
  <img src="assets/impact-light.svg" width="100%" alt="Selected results: order rejection rate reduced from 7% to 1% with RutaLiquidador at Auren; sales conversion increased 15% at UBYCALL; credit default losses reduced 18% at Alfin Banco; 80% of manual reporting automated at UBYCALL.">
</picture>

## Featured project — RutaLiquidador

**Last-mile delivery, fleet tracking and route settlement platform.** Designed, built and operated as lead developer at Auren. *Private repository, in daily production use.*

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/case-metrics-dark.svg">
  <img src="assets/case-metrics-light.svg" width="100%" alt="RutaLiquidador at a glance: 207 REST API endpoints; more than 7,700 automated tests; 47 PostgreSQL tables and 60 migrations; driver app rolled out to 43 devices.">
</picture>

#### Context

Every morning the company dispatches trucks across Lima. Each truck carries a crew of three to four people (driver, settlement clerk and helpers) and dozens of stops. Measured over real routes, mobile signal is available only about 64% of the shift. The office needed to know in real time what was delivered, what was rejected and why, where each truck was, and exactly how much money each crew member had to hand in at the end of the day.

#### Problems solved

| Problem | Solution |
|---|---|
| **Settlement disputes.** With partial deliveries, nobody could say exactly how much money a driver owed. | Line-by-line settlement against the ERP order in exact decimal arithmetic, using the real weight of weighed products, with the amount owed by **each crew member**. |
| **Lost deliveries in multi-person crews.** The original design assumed one person per truck, so a second crew member's confirmation could be silently lost. | An append-only, multi-user delivery log. Each submission carries a signature so network retries never count twice, and conflicts are detected and resolved on the server with a full audit trail. |
| **Over-delivered free goods.** The ERP exports free-goods lines without the promotion that generated them, so partial rejections led to giving away too much product. | A promotion identification engine covering **14 promotion types**. It recalculated **2,000 of 2,000** validation cases correctly, where the previous approach failed in about 4%. The driver app can lock the correct free quantity, even offline. |
| **Rejections with no follow-up.** Rejected orders that were later recovered disappeared from the statistics. | Rejection management that rebuilds history from the audit log and measures recovered sales, plus an instant **WhatsApp alert when an uncollected amount exceeds S/ 1,000**. |
| **Commercial fraud and losses.** Inflated orders, fictitious customers and weight losses were hard to detect. | Automatic signals: orders inflated to pass the minimum ticket, customers flagged by drivers for review, weight loss above the expected rate for frozen products, rejections recorded more than 100 m from the customer, and deliveries logged at an impossible pace. |
| **No visibility of the fleet.** The office could not see where trucks were or which routes were stuck. | A live fleet map through a secure proxy to the GPS tracker, with each route classified as in progress, stalled, closed or not started. |
| **Unreliable connectivity.** Without signal, unsent deliveries piled up until the evidence on the phone became unreadable. | An offline-first driver app with an encrypted local queue, bounded storage and a one-day retention policy, which syncs automatically when coverage returns. |
| **Manual reporting.** Supervisors and management assembled reports by hand. | Scheduled start, midday and closing reports by email and WhatsApp, protected against duplicate sends, and a management drill-down from period to driver, customer and product. |

#### Architecture

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-dark.svg">
  <img src="assets/architecture-light.svg" width="100%" alt="RutaLiquidador architecture. Data sources: ERP on SQL Server (read-only sync of dispatch, invoices and promotions), fleet GPS tracker, OSRM routing and self-hosted map tiles. Platform core: FastAPI backend with the promotion identification engine, route settlement and delivery log, offline conflict resolution and audit trail, a scheduler with 12 background jobs, and PostgreSQL 16 with 47 tables. Clients: offline-first driver app, React control tower and WhatsApp gateway. Delivery: Docker Compose, Nginx, GitHub Actions and scripted deploy with rollback.">
</picture>

#### Engineering

- **Testing:** more than 7,700 automated tests across backend (pytest), mobile (Jest) and web (Vitest and Playwright end-to-end), plus mutation testing on each pull request to prove the tests catch real defects.
- **Continuous delivery:** six GitHub Actions workflows gate every release. The deployment kit runs pre-flight checks, a database backup, a smoke test and an automatic rollback path, with about 15 seconds of downtime per release.
- **Performance:** a database audit replaced a non-indexable query pattern used in 16 places, cutting response time from 4.9 s to 7 ms (about 700× faster). Background jobs were moved out of the web process to remove a concurrency bottleneck.
- **Reliability and security:** exact decimal arithmetic for money, row locking and version tokens for offline conflicts, server-side permission checks, JWT sessions with refresh, rate limiting, and security, performance and financial audits reviewed by independent passes.
- **Data-driven decisions:** features are measured before they are built or kept. A collision counter ran in production before the conflict-resolution screen was built, and the closing alert hour was set from the 90th percentile of the last stop of the day. An analytics job that wrote 278,000 rows a day to a screen nobody opened was retired.

#### Results

- **Order rejection rate reduced from 7% to 1%.**
- Real-time GPS visibility of the whole truck fleet and of served versus pending stops, which improved delivery effectiveness and route times.
- Exact, auditable settlement per crew member, including promotional free goods.
- Early detection of commercial fraud signals and of high-value uncollected deliveries.

**Stack:** Python · FastAPI · SQLAlchemy (async) · Alembic · PostgreSQL 16 · SQL Server · APScheduler · TypeScript · React 18 · Vite · Tailwind · Leaflet · React Native · Expo · MapLibre · OSRM · Docker · Nginx · GitHub Actions

## Other projects

| Project | Description | Technologies |
|---|---|---|
| **Ventory Multicanal** | **Problem:** companies with field sales teams could not verify attendance, location or the sales their sellers reported. **Solution:** an offline-first platform with a mobile app and an administration panel: selfie and GPS attendance, fake-location and rooted-device detection, a server-side check for impossible travel speeds, device binding, encrypted on-device storage, and idempotent sync that never duplicates a sale. A variant for home fiber internet sales adds on-device coverage-map validation and partner APIs for sales export and targets. | FastAPI, PostgreSQL, React Native, React, Docker |
| **Portal de Concursos** | **Problem:** monthly sales contests were configured and tracked by hand. **Solution:** managers define each contest's rules (products, groups, quotas, tiers and caps) and an engine turns them into read-only ERP queries that compute each seller's progress and prize. It recalculates 14 contests every business day and was validated with **zero discrepancies across 281,788 rows**. | Next.js, FastAPI, SQL Server, SQLite, Docker |
| **Capturas de Preventa** | **Problem:** supervisors needed pre-sales tables on WhatsApp for 225 supervisor and category combinations, too many to capture by hand. **Solution:** a scheduled service that rebuilds each table from the reporting API, renders it as an image and delivers it to WhatsApp groups. It uses rate limiting to protect the sending number, guarantees no duplicate sends and has about 350 tests, including a golden test that keeps the figures identical to the dashboard. In production. | Python, FastAPI, Playwright, Node.js, Docker |
| **AurenPulse** | **Problem:** leadership did not know who actually used the company's internal systems. **Solution:** a usage analytics panel showing who is online, time spent per system and person, systems nobody uses, hour-by-day heatmaps and people who stopped logging in, with Excel export. It is read-only at two levels (a SELECT-only database role and read-only transactions) and uses signed sessions with brute-force lockout. | FastAPI, PostgreSQL, Docker |
| **AUSPEX** | **Problem:** sales supervisors had no live view of their teams. **Solution:** a supervisor dashboard on Google Apps Script with role-based access, inactivity alerts, rankings, multi-brand theming and an audit log of access and exports. A migration to a Node.js, TypeScript and PostgreSQL backend with a React Native app is in progress. | Google Apps Script, Node.js, TypeScript, Prisma, React Native |
| **TomaPedidos** | **Problem:** field sellers decide what to offer each customer from memory. **Solution (in design):** a suggested-order engine combining repurchase cycles, market-basket affinity and a gradient-boosted ranker, to be validated by replaying nine years of sales history, with suggestions precomputed nightly so the app works offline. | Python, PostgreSQL, LightGBM |

These systems are built for the companies I work with, so their repositories are private. Architecture and code walkthroughs are available on request.

## Technical skills

| Area | Technologies |
|---|---|
| Backend | Python, FastAPI, SQLAlchemy, Alembic, Pydantic, APScheduler, Node.js, Express, Prisma, REST APIs, JWT |
| Frontend | TypeScript, React, Next.js, Vite, Tailwind CSS, Leaflet, MapLibre, Recharts, ECharts |
| Mobile | React Native, Expo, offline-first synchronization, encrypted local storage, background GPS |
| Data and BI | PostgreSQL, SQL Server, SQLite, ETL pipelines, ERP integration, Pandas, Power BI |
| DevOps and quality | Docker, Docker Compose, Nginx, Linux, GitHub Actions, pytest, Jest, Vitest, Playwright, mutation testing |
| Languages | Python, TypeScript, JavaScript, SQL, Rust |

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/languages-dark.svg">
  <img src="assets/languages-light.svg" width="100%" alt="Code across 15 production repositories, about 484K non-blank lines: TypeScript 44.8%, Python 40.7%, HTML and CSS 5.5%, JavaScript 5.3%, Shell 2.9%, SQL 0.7%.">
</picture>

## Professional experience

**Full Stack Developer, Business Intelligence** — Auren · Lima, Peru · *December 2025 – Present*
- Lead developer of the Business Intelligence area, responsible for the design, development, deployment and operation of the company's internal platforms.
- Built RutaLiquidador, reducing the order rejection rate from 7% to 1% and adding real-time GPS control of the truck fleet.
- Built the promotion identification engine, field sales applications, a sales incentive platform and analytics dashboards on top of the company ERP.
- Introduced containerized deployments, CI/CD pipelines and automated testing across projects.

**Call Center Data Analyst** — UBYCALL (Pizza Hut) · *February 2023 – November 2024*
- Increased sales conversion by 15% through predictive analysis of customer behavior.
- Automated 80% of manual reporting with Python and SQL and built executive dashboards in Power BI.

**Financial Analyst** — Alfin Banco · *March 2022 – December 2022*
- Developed machine learning credit-scoring models that reduced default losses by 18%.
- Built an automated ETL pipeline processing more than 100,000 transactions per day.

## Education and certifications

- **B.S. Systems & Computer Engineering** — Universidad Privada del Norte (UPN) · *In progress*
- **AWS Certified Solutions Architect – Associate** · *In preparation*
- **Microsoft Certified: Power BI Data Analyst Associate**
- **Certified ScrumMaster (CSM)** — Scrum Alliance
- **Genesys Cloud Certified**
- **EDTEAM** — Python and Data Analysis · SQL Databases · REST API Development
