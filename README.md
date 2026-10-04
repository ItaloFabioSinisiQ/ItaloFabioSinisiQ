<div align="center">

# Italo Fabio Sinisi Quintana

**Full Stack Developer · Python · PostgreSQL · Docker · CI/CD · Rust**

Lima, Peru · 5+ years building data-driven software · Open to remote (international) and local roles

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/italo-fabio-sinisi-quintana/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:sinisiquintanaitalo@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-111111?style=flat-square&logo=githubpages&logoColor=white)](https://italofabiosinisiq.github.io/-dev-holaMundo-true-/)

</div>

---

## About me

I'm a **Full Stack Developer** who builds production systems end to end: backend APIs, web dashboards, offline-first mobile apps, databases, and the CI/CD and Docker infrastructure that ships them. I currently lead development for the **Business Intelligence** area at **Auren**, a mass-consumer goods distributor in Peru. My work there covers logistics, last-mile delivery, field sales and executive analytics.

My background is in **data analysis**, so I design software around measurable business outcomes. The clearest example is a delivery platform that cut **order rejections from 7% to 1%**.

- 🛠️ Strongest in **Python, FastAPI, PostgreSQL, Docker and CI/CD (GitHub Actions)**. **Rust** is my favorite language.
- 🤖 I use **AI-assisted development** (LLMs, MCP, agentic coding) every day, which lets me pick up new stacks quickly.
- 🎓 Studying **Systems & Computer Engineering** at **Universidad Privada del Norte (UPN)**.
- 🎯 Interested in **remote roles**, **freelance projects** and hard problems in logistics, data and automation.

---

## Tech stack

<p align="left">
  <img src="https://skillicons.dev/icons?i=python,fastapi,rust,postgres,docker,githubactions,ts,react,nodejs,express,prisma,vite,sqlite,nginx,linux,git&perline=16" alt="Tech stack" />
</p>

| Area | Technologies |
|---|---|
| **Backend** | Python, FastAPI, SQLAlchemy (async), Alembic, Pydantic, APScheduler, Node.js, Express, Prisma, REST APIs, JWT/OAuth |
| **Frontend** | React, TypeScript, Vite, Next.js, Leaflet / MapLibre, Recharts, ECharts |
| **Mobile** | React Native, Expo, offline-first sync, SQLite (encrypted), GPS, camera, biometrics |
| **Data** | PostgreSQL, SQL Server, SQLite, ETL pipelines, ERP integration, Pandas, Power BI |
| **DevOps** | Docker, Docker Compose, GitHub Actions CI/CD, Nginx, Linux servers, Sentry, mutation testing |
| **Geo & integrations** | OSRM routing, GPS telemetry, WhatsApp gateway, Google Sheets API, MCP servers |
| **Languages** | Python, TypeScript, JavaScript, SQL, Rust |

---

## Featured projects

> Most of my work is **in production at the companies I build for**, so those repositories are private (🔒). I'm happy to walk through the architecture and code in an interview.

### 🚚 Mi Ruta — Delivery, GPS Tracking & Route Settlement Platform 🔒

An end-to-end logistics platform for a mass-consumer distributor, with three parts: a **mobile app for truck drivers**, a **web control tower** for operations, and a **central API** connected to the company's ERP.

- 📉 **Reduced order rejections from 7% to 1%** by giving drivers and dispatchers real-time visibility of every order, customer and delivery state.
- 🛰️ **Real-time GPS truck tracking** and automatic identification of customers already served, which made routes faster and deliveries more effective.
- 🧠 **Promotion identification engine.** The ERP exports invoices with the link between free-goods lines and their promotions lost. The engine rebuilds that link across **14 promotion types** (progressive N+M, tiered, combos, discounts) and recalculates bonuses when a customer partially rejects an order. It is built from pure functions, covered by tests and validated against real dispatches.
- 📱 **Offline-first** React Native app with maps, photo evidence, biometric login and deferred sync.
- ⚙️ Hundreds of automated tests (pytest + Jest), **mutation testing**, 6 **GitHub Actions** pipelines, Dockerized deployments and Sentry monitoring.

`Python` `FastAPI` `PostgreSQL` `SQL Server` `SQLAlchemy` `React` `TypeScript` `React Native` `Expo` `MapLibre` `OSRM` `Docker` `GitHub Actions`

### More projects

| Project | What it does | Stack |
|---|---|---|
| **🛒 Ventory Multicanal** 🔒 | Offline-first field sales platform with a mobile app for sellers and supervisors plus an admin dashboard. Includes encrypted local storage (AES-256), GPS tracking, fake-GPS detection, device binding and automatic sync. | FastAPI · PostgreSQL · React Native · React · Docker · CI |
| **📍 GeoCamionRuta** 🔒 | Fleet telemetry ingester. Polls the GPS API for every truck, stores position history and derives stops automatically. | Python · asyncio · httpx · PostgreSQL · Alembic · Docker |
| **🧠 TomaPedidos** 🔒 *(in progress)* | Suggested-order recommendation engine for field sellers, built on repurchase cycles, market-basket analysis and an ML ranker backtested on 9 years of sales history. | Python · PostgreSQL · Machine Learning |
| **📊 AUSPEX** 🔒 | Sales supervisor dashboard with real-time KPIs, rankings and risk alerts. Migrated from Google Apps Script to a modern web and mobile stack. | Node.js · TypeScript · Prisma · PostgreSQL · React Native |
| **📈 AurenPulse** 🔒 | Internal product analytics for leadership: who uses each company system, for how long, usage heatmaps and churn, with Excel export. | FastAPI · PostgreSQL · Docker |
| **💰 Finanzas AI** 🔒 | Personal finance tracker you operate by chatting with an AI assistant. Uses a custom **MCP server** and a FastAPI dashboard. | Python · FastMCP · FastAPI · SQLite · ECharts |

**…and 60+ more repositories** covering ETL bots, WhatsApp automations, BI dashboards, database documentation tools and more.

---

## Experience

**Full Stack Developer · Business Intelligence** — *Auren* · Dec 2025 – Present
- Lead developer for the BI area, responsible for the design, development and deployment of internal platforms for logistics, sales and leadership.
- Built the **Mi Ruta** delivery platform, which **cut order rejections from 7% to 1%** and added real-time GPS control of the truck fleet.
- Developed the promotion identification engine, field sales apps, a recommendation engine and analytics dashboards on top of the company ERP (SQL Server → PostgreSQL).
- Run Docker-based deployments and GitHub Actions CI/CD on the company's own servers.

**Call Center Data Analyst** — *UBYCALL (Pizza Hut)* · Feb 2023 – Nov 2024
- **Increased conversions by 15%** through predictive analysis of customer behavior.
- **Automated 80% of manual reports** with Python and SQL, and built executive dashboards in Power BI.

**Financial Analyst** — *Alfin Banco* · Mar 2022 – Dec 2022
- Built machine learning credit-scoring models that **reduced default losses by 18%**.
- Developed an automated ETL pipeline processing **100K+ daily transactions**.

---

## Education & certifications

- 🎓 **B.S. Systems & Computer Engineering** — Universidad Privada del Norte (UPN) · *In progress*
- **AWS Certified Solutions Architect – Associate** · *Coming soon*
- **Microsoft Certified: Power BI Data Analyst Associate**
- **Certified ScrumMaster (CSM)** — Scrum Alliance
- **Genesys Cloud Certified**
- **EDTEAM:** Python & Data Analysis · SQL Databases · REST API Development

---

<div align="center">

**Have a challenging project in mind? Let's talk.**

[LinkedIn](https://www.linkedin.com/in/italo-fabio-sinisi-quintana/) · [sinisiquintanaitalo@gmail.com](mailto:sinisiquintanaitalo@gmail.com)

</div>
