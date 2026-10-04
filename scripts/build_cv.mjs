// Build the CV as PDF in English and Spanish:
//   cv/Italo-Sinisi-CV-EN.pdf and cv/Italo-Sinisi-CV-ES.pdf
//
// Requires Node and Playwright (npm i playwright). Run from the repo root:
//   node scripts/build_cv.mjs
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const b64 = (p) => readFileSync(join(root, p)).toString('base64');
const FONT_SANS = b64('cv/fonts/Inter.woff2');
const FONT_SERIF = b64('cv/fonts/SourceSerif4.woff2');
const PHOTO = b64('assets/profile-photo.jpg');

const CONTACT = {
  phone: '+51 977 170 609',
  email: 'sinisiquintanaitalo@gmail.com',
  linkedin: 'linkedin.com/in/italo-fabio-sinisi-quintana',
  github: 'github.com/ItaloFabioSinisiQ',
};

const CV = {
  en: {
    file: 'Italo-Sinisi-CV-EN.pdf',
    lang: 'en',
    title: 'Full Stack Developer & Data Analyst',
    location: 'Lima, Peru · GMT-5 · Open to remote',
    summaryTitle: 'Profile',
    summary:
      'Full Stack Developer and Data Analyst with 5+ years of experience in software and data. I design, build and run production platforms for last-mile logistics, field sales and business intelligence, from Python and PostgreSQL backends to React and React Native clients, ERP integrations and CI/CD. I start every system from the business metric it has to move and measure it in production.',
    resultsTitle: 'Selected results',
    results: [
      ['7% → 1%', 'order rejection rate'],
      ['+15%', 'sales conversion'],
      ['−18%', 'credit default losses'],
      ['80%', 'reporting automated'],
    ],
    experienceTitle: 'Experience',
    experience: [
      {
        role: 'Full Stack Developer, Business Intelligence',
        org: 'Auren · FMCG distribution',
        dates: 'Dec 2025 – Present',
        bullets: [
          'Design, build, deploy and operate the BI area\'s internal platforms on Python, FastAPI, PostgreSQL, React and React Native.',
          '<b>RutaLiquidador</b>, a last-mile delivery and route settlement platform: reduced the order rejection rate <b>from 7% to 1%</b> and added real-time GPS control of the truck fleet. 207 API endpoints, 7,700+ automated tests, 43 devices in production.',
          'Promotion identification engine covering 14 promotion types, <b>correct in 2,000 of 2,000</b> validation cases (previous method: about 4% errors). Settlement per crew member in exact decimals, offline-first driver app, fraud signals and WhatsApp alerts.',
          'Sales contest engine that recalculates 14 contests every business day, validated with <b>zero discrepancies across 281,788 rows</b>; automated WhatsApp reporting for 225 supervisor and category combinations.',
          'Introduced Docker deployments, GitHub Actions CI/CD, mutation testing and scripted releases with backup and rollback (about 15 s of downtime). Cut a critical query from 4.9 s to 7 ms.',
        ],
      },
      {
        role: 'Call Center Data Analyst',
        org: 'UBYCALL · Pizza Hut Peru account',
        dates: 'Feb 2023 – Nov 2024',
        bullets: [
          'Increased telesales conversion by <b>15%</b> through KPI and customer behavior analysis.',
          'Automated <b>80%</b> of manual reporting with Python and SQL; built Power BI dashboards for management.',
          'Supervised a team of agents and improved telesales processes based on performance data.',
        ],
      },
      {
        role: 'Financial Analyst',
        org: 'Alfin Banco',
        dates: 'Mar 2022 – Dec 2022',
        bullets: [
          'Built credit-risk scoring models that reduced default losses by <b>18%</b>.',
          'Developed an automated ETL pipeline processing more than <b>100,000 transactions a day</b>, and client dashboards in Power BI.',
        ],
      },
      {
        role: 'Administrative Assistant (internship)',
        org: 'Gestión Inmobiliaria Pacífico',
        dates: 'May 2021 – Mar 2022',
        bullets: [
          'Restructured internal databases with SQL and built Power BI reports that reduced time spent on administrative tasks.',
        ],
      },
    ],
    projectsTitle: 'Selected projects',
    projects: [
      ['RutaLiquidador', 'Delivery, fleet tracking and route settlement platform', 'FastAPI · PostgreSQL · React · React Native · OSRM · Docker'],
      ['Ventory Multicanal', 'Field sales platform with GPS audit and offline sync', 'FastAPI · PostgreSQL · React Native · React'],
      ['Portal de Concursos', 'Sales contest engine on read-only ERP queries', 'Next.js · FastAPI · SQL Server'],
      ['Capturas de Preventa', 'Scheduled WhatsApp report bot, about 350 tests', 'Python · FastAPI · Playwright · Node.js'],
    ],
    skillsTitle: 'Skills',
    skills: [
      ['Backend', 'Python, FastAPI, SQLAlchemy, Alembic, Pydantic, Node.js, Express, Prisma, REST APIs, JWT'],
      ['Frontend', 'TypeScript, React, Next.js, Vite, Tailwind CSS, Leaflet, MapLibre, Recharts'],
      ['Mobile', 'React Native, Expo, offline-first sync, encrypted storage, background GPS'],
      ['Data and BI', 'PostgreSQL, SQL Server, ETL pipelines, ERP integration, Pandas, scikit-learn, Power BI'],
      ['DevOps', 'Docker, Nginx, Linux, GitHub Actions, pytest, Jest, Vitest, Playwright'],
    ],
    educationTitle: 'Education and certifications',
    education: [
      ['Bachelor\'s in Systems & Computer Engineering', 'Universidad Privada del Norte (UPN) · in progress'],
      ['Technical degree in Construction Management', 'SENCICO'],
      ['Microsoft Certified: Power BI Data Analyst Associate (PL-300)', 'Microsoft'],
      ['Certified ScrumMaster (CSM)', 'Scrum Alliance'],
      ['Genesys Cloud certification', 'Genesys'],
      ['Python, Data Analysis, SQL and REST APIs', 'EDTEAM'],
    ],
    languagesTitle: 'Languages',
    languages: 'Spanish (native)',
  },
  es: {
    file: 'Italo-Sinisi-CV-ES.pdf',
    lang: 'es',
    title: 'Desarrollador Full Stack y Analista de Datos',
    location: 'Lima, Perú · GMT-5 · Disponible para remoto',
    summaryTitle: 'Perfil',
    summary:
      'Desarrollador Full Stack y Analista de Datos con más de 5 años de experiencia en software y datos. Diseño, construyo y opero plataformas en producción para logística de última milla, fuerza de ventas e inteligencia de negocios, desde backends en Python y PostgreSQL hasta clientes en React y React Native, integraciones con ERP y CI/CD. Diseño cada sistema a partir de la métrica de negocio que debe mejorar y la mido en producción.',
    resultsTitle: 'Resultados destacados',
    results: [
      ['7% → 1%', 'rechazo de pedidos'],
      ['+15%', 'conversión de ventas'],
      ['−18%', 'pérdidas por impago'],
      ['80%', 'reportes automatizados'],
    ],
    experienceTitle: 'Experiencia',
    experience: [
      {
        role: 'Full Stack Developer, Inteligencia de Negocios',
        org: 'Auren · distribución de consumo masivo',
        dates: 'Dic 2025 – Actualidad',
        bullets: [
          'Diseño, construyo, despliego y opero las plataformas internas del área de BI con Python, FastAPI, PostgreSQL, React y React Native.',
          '<b>RutaLiquidador</b>, plataforma de reparto de última milla y liquidación de rutas: redujo la tasa de rechazo de pedidos <b>de 7% a 1%</b> y dio control GPS de la flota en tiempo real. 207 endpoints de API, más de 7,700 tests automatizados y 43 dispositivos en producción.',
          'Motor de identificación de promociones con 14 tipos, <b>correcto en 2,000 de 2,000</b> casos de validación (método anterior: alrededor de 4% de error). Liquidación por tripulante con decimales exactos, app offline-first para choferes, señales de fraude y alertas por WhatsApp.',
          'Motor de concursos comerciales que recalcula 14 concursos cada día hábil, validado con <b>cero diferencias en 281,788 filas</b>; reportes automáticos por WhatsApp para 225 combinaciones de supervisor y categoría.',
          'Introduje despliegues con Docker, CI/CD con GitHub Actions, mutation testing y despliegues automatizados con backup y rollback (unos 15 s de interrupción). Reduje una consulta crítica de 4.9 s a 7 ms.',
        ],
      },
      {
        role: 'Analista de Datos de Call Center',
        org: 'UBYCALL · cuenta de Pizza Hut Perú',
        dates: 'Feb 2023 – Nov 2024',
        bullets: [
          'Aumenté la conversión de televentas en <b>15%</b> con análisis de KPIs y del comportamiento de los clientes.',
          'Automaticé el <b>80%</b> de los reportes manuales con Python y SQL; construí dashboards gerenciales en Power BI.',
          'Supervisé un equipo de agentes y mejoré los procesos de televenta a partir de datos de desempeño.',
        ],
      },
      {
        role: 'Analista Financiero',
        org: 'Alfin Banco',
        dates: 'Mar 2022 – Dic 2022',
        bullets: [
          'Desarrollé modelos de scoring de riesgo crediticio que redujeron las pérdidas por impago en <b>18%</b>.',
          'Construí un pipeline ETL automatizado que procesa más de <b>100,000 transacciones al día</b>, y dashboards de clientes en Power BI.',
        ],
      },
      {
        role: 'Asistente Administrativo (prácticas)',
        org: 'Gestión Inmobiliaria Pacífico',
        dates: 'May 2021 – Mar 2022',
        bullets: [
          'Reestructuré bases de datos internas con SQL y construí reportes en Power BI que redujeron el tiempo dedicado a tareas administrativas.',
        ],
      },
    ],
    projectsTitle: 'Proyectos destacados',
    projects: [
      ['RutaLiquidador', 'Reparto, rastreo de flota y liquidación de rutas', 'FastAPI · PostgreSQL · React · React Native · OSRM · Docker'],
      ['Ventory Multicanal', 'Fuerza de ventas con auditoría GPS y sincronización offline', 'FastAPI · PostgreSQL · React Native · React'],
      ['Portal de Concursos', 'Motor de concursos sobre consultas de solo lectura al ERP', 'Next.js · FastAPI · SQL Server'],
      ['Capturas de Preventa', 'Bot de reportes programados por WhatsApp, unos 350 tests', 'Python · FastAPI · Playwright · Node.js'],
    ],
    skillsTitle: 'Habilidades',
    skills: [
      ['Backend', 'Python, FastAPI, SQLAlchemy, Alembic, Pydantic, Node.js, Express, Prisma, APIs REST, JWT'],
      ['Frontend', 'TypeScript, React, Next.js, Vite, Tailwind CSS, Leaflet, MapLibre, Recharts'],
      ['Móvil', 'React Native, Expo, sincronización offline-first, almacenamiento cifrado, GPS en segundo plano'],
      ['Datos y BI', 'PostgreSQL, SQL Server, pipelines ETL, integración con ERP, Pandas, scikit-learn, Power BI'],
      ['DevOps', 'Docker, Nginx, Linux, GitHub Actions, pytest, Jest, Vitest, Playwright'],
    ],
    educationTitle: 'Educación y certificaciones',
    education: [
      ['Ingeniería de Sistemas Computacionales', 'Universidad Privada del Norte (UPN) · en curso'],
      ['Técnico en Administración de Obras de Construcción Civil', 'SENCICO'],
      ['Microsoft Certified: Power BI Data Analyst Associate (PL-300)', 'Microsoft'],
      ['Certified ScrumMaster (CSM)', 'Scrum Alliance'],
      ['Certificación Genesys Cloud', 'Genesys'],
      ['Python, Análisis de Datos, SQL y APIs REST', 'EDTEAM'],
    ],
    languagesTitle: 'Idiomas',
    languages: 'Español (nativo)',
  },
};

const css = `
@font-face { font-family: 'Inter'; src: url(data:font/woff2;base64,${FONT_SANS}) format('woff2'); font-weight: 100 900; }
@font-face { font-family: 'Source Serif'; src: url(data:font/woff2;base64,${FONT_SERIF}) format('woff2'); font-weight: 200 900; }
@page { size: A4; margin: 14mm 15mm 14mm 15mm; }
:root { --ink: #1f2328; --ink2: #59636e; --line: #d0d7de; --accent: #0969da; --panel: #f6f8fa; }
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; font-size: 9.2pt; line-height: 1.45; color: var(--ink); }
a { color: inherit; text-decoration: none; }
header { display: flex; align-items: center; gap: 7mm; padding-bottom: 5mm; border-bottom: 1.2pt solid var(--accent); }
header img { width: 27mm; height: 27mm; border-radius: 50%; object-fit: cover; outline: 0.9pt solid var(--accent); outline-offset: 1.6pt; }
h1 { font-family: 'Source Serif', serif; font-weight: 500; font-size: 25pt; line-height: 1.05; margin: 0 0 1.6mm; letter-spacing: -0.2pt; }
.title { font-weight: 600; font-size: 11.5pt; margin: 0 0 2mm; }
.contact { color: var(--ink2); font-size: 8.4pt; display: flex; flex-wrap: wrap; column-gap: 3.2mm; margin-top: 0.6mm; }
.contact span + span::before { content: '·'; margin-right: 3.2mm; color: var(--line); }
section { margin-top: 5mm; }
h2 { break-after: avoid; font-size: 7.8pt; font-weight: 700; letter-spacing: 1.1pt; text-transform: uppercase; color: var(--accent); margin: 0 0 2.2mm; }
.summary { margin: 0; color: var(--ink); }
.results { display: grid; grid-template-columns: repeat(4, 1fr); border: 0.8pt solid var(--line); border-radius: 2mm; background: var(--panel); }
.results div { padding: 2.6mm 3.6mm; }
.results div + div { border-left: 0.8pt solid var(--line); }
.results b { display: block; font-size: 15pt; font-weight: 700; line-height: 1.1; }
.results span { color: var(--ink2); font-size: 8pt; }
.job { margin-bottom: 3.2mm; break-inside: avoid; }
.job-head { display: flex; justify-content: space-between; align-items: baseline; gap: 4mm; }
.job-head .role { font-weight: 600; font-size: 10pt; }
.job-head .dates { color: var(--ink2); font-size: 8.4pt; white-space: nowrap; }
.org { color: var(--ink2); font-size: 8.6pt; margin-bottom: 1mm; }
ul { margin: 0; padding-left: 4mm; }
li { margin: 0 0 0.9mm; }
li::marker { color: var(--accent); }
li b, .summary b { font-weight: 600; }
.projects, .skills, .education { break-inside: avoid; }
.grid { display: grid; grid-template-columns: 37mm 1fr; column-gap: 4mm; row-gap: 1.3mm; }
.grid .k { font-weight: 600; }
.grid .v { color: var(--ink); }
.projects .v .tech { color: var(--ink2); }
.edu { display: grid; grid-template-columns: 1fr auto; column-gap: 4mm; row-gap: 1.1mm; }
.edu .k { font-weight: 500; }
.edu .v { color: var(--ink2); text-align: right; }
`;

const esc = (s) => s.replace(/&(?!amp;)/g, '&amp;');

function render(c) {
  const line = (items) => `<div class="contact">${items.map((x) => `<span>${x}</span>`).join('')}</div>`;
  const contact = line([
    c.location,
    CONTACT.phone,
    `<a href="mailto:${CONTACT.email}">${CONTACT.email}</a>`,
  ]) + line([
    `<a href="https://www.${CONTACT.linkedin}/">${CONTACT.linkedin}</a>`,
    `<a href="https://${CONTACT.github}">${CONTACT.github}</a>`,
  ]);
  const jobs = c.experience.map((j) => `
    <div class="job">
      <div class="job-head"><span class="role">${esc(j.role)}</span><span class="dates">${j.dates}</span></div>
      <div class="org">${esc(j.org)}</div>
      <ul>${j.bullets.map((b) => `<li>${b}</li>`).join('')}</ul>
    </div>`).join('');
  return `<!doctype html><html lang="${c.lang}"><head><meta charset="utf-8"><title>Italo Fabio Sinisi Quintana — CV</title><style>${css}</style></head><body>
  <header>
    <img src="data:image/jpeg;base64,${PHOTO}" alt="">
    <div>
      <h1>Italo Fabio Sinisi Quintana</h1>
      <p class="title">${esc(c.title)}</p>
      ${contact}
    </div>
  </header>
  <section><h2>${c.summaryTitle}</h2><p class="summary">${c.summary}</p></section>
  <section><h2>${c.resultsTitle}</h2><div class="results">${c.results.map(([v, l]) => `<div><b>${v}</b><span>${l}</span></div>`).join('')}</div></section>
  <section><h2>${c.experienceTitle}</h2>${jobs}</section>
  <section class="projects"><h2>${c.projectsTitle}</h2><div class="grid">${c.projects.map(([n, d, t]) => `<div class="k">${n}</div><div class="v">${d} · <span class="tech">${t}</span></div>`).join('')}</div></section>
  <section class="skills"><h2>${c.skillsTitle}</h2><div class="grid">${c.skills.map(([k, v]) => `<div class="k">${k}</div><div class="v">${v}</div>`).join('')}</div></section>
  <section class="education"><h2>${c.educationTitle}</h2><div class="edu">${c.education.map(([k, v]) => `<div class="k">${k}</div><div class="v">${v}</div>`).join('')}</div></section>
  <section><h2>${c.languagesTitle}</h2><div>${c.languages}</div></section>
</body></html>`;
}

const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const page = await browser.newPage();
for (const c of Object.values(CV)) {
  await page.setContent(render(c), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: join(root, 'cv', c.file), format: 'A4', printBackground: true, preferCSSPageSize: true });
  console.log('wrote cv/' + c.file);
}
await browser.close();
