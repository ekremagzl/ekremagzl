<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img alt="Ekrem Ağzıgüzel: full-stack ve yapay zekâ geliştirici" src="assets/header-light.svg" width="100%">
</picture>

KTO Karatay Üniversitesi'nde Bilgisayar Mühendisliği okuyorum; full-stack geliştirme ile yapay zekânın kesiştiği yerde ürün geliştiriyorum. **FastAPI ve Next.js** ile çok kiracılı SaaS platformları kuruyor, **PostgreSQL** tarafında satır seviyesinde güvenlikle (RLS) verileri izole ediyor; **LLM ve RAG** ile kodu okuyan, yorumlayan ve karar veren sistemler tasarlıyorum. Restoranlar için QR menü platformundan doğrulanmış öğrencilere özel kampüs topluluğuna, NASA uydu verisiyle iklim trendi analizinden pull request inceleyen bir GitHub App'e kadar uçtan uca projeler geliştiriyorum.

### ÖNE ÇIKAN PROJE

<img src="assets/featured.svg" width="100%" alt="PR Review Assistant: RAG tabanlı yapay zekâ kod inceleme asistanı">

**PR Review Assistant**, bitirme projem: GitHub'da açılan pull request'leri yapay zekâ ile otomatik inceleyen bir GitHub App. *Yapay Zeka Destekli Kod İnceleme Asistanı: GitHub Pull Request Analizi için RAG Tabanlı Bir Yaklaşım.*

- **Akış:** PR açılınca webhook imzası doğrulanır, istek hemen `200` ile yanıtlanır ve inceleme arka planda başlar; GitHub App olarak token alınıp diff satır numaralarıyla çekilir.
- **LLM katmanı:** Sağlayıcıdan bağımsız LLM arayüzü, Gemini ile JSON şemalı yapılandırılmış çıktı, yoğunlukta sırayla denenen yedek modeller ve zaman aşımı yönetimi.
- **İnceleme motoru:** Bulgular **hata riski, güvenlik, performans ve okunabilirlik** kategorilerinde sınıflanır, önem sırasıyla PR'a yorum olarak yazılır.
- **Sırada:** tree-sitter ile kod parçalama, satıra bağlı yorumlar, pgvector üzerinde RAG ve doğrulama katmanı; ardından Ollama ile yerel model, web paneli, AWS kurulumu ve karşılaştırmalı deneyler.

### PROJELER

<p>
<img src="assets/cards/menum.svg" width="49%" alt="Menüm: dijital menü SaaS">
<img src="assets/cards/kampusum.svg" width="49%" alt="Kampüsüm: doğrulanmış öğrenci topluluğu">
<img src="assets/cards/earth-trend.svg" width="49%" alt="Earth Trend Detective">
<img src="assets/cards/not-defteri.svg" width="49%" alt="Not Defteri: full-stack not uygulaması">
<a href="https://github.com/ekremagzl/BookStore"><img src="assets/cards/bookstore.svg" width="49%" alt="BookStore"></a>
<a href="https://github.com/ekremagzl/currency-converter"><img src="assets/cards/canli-doviz.svg" width="49%" alt="Canlı Döviz"></a>
</p>

<sub>küçük projeler: <a href="https://github.com/ekremagzl/weather-app">weather-app</a> · <a href="https://github.com/ekremagzl/personel-yonetim">personel-yonetim</a> · <a href="https://github.com/ekremagzl/to-do-list">to-do-list</a> · <a href="https://github.com/ekremagzl/qr-generator">qr-generator</a></sub>

### ŞU AN

Bitirme projemin ikinci iş paketindeyim: tree-sitter ile kodu anlamlı parçalara bölüyor, pgvector üzerinde RAG kurup bulguları satır satır doğrulayan bir katman ekliyorum. Bir yandan da Kampüsüm'ü KTO Karatay'da kapalı betaya hazırlıyor, Menüm'ün çok kiracılı altyapısını ve yayın tarafını (Docker, Caddy) olgunlaştırıyorum.

### BİLDİKLERİM

<b>dil</b><br>
<img src="https://img.shields.io/badge/Python-1f2328?style=flat-square&logo=python&logoColor=2dd4bf" alt="Python"> <img src="https://img.shields.io/badge/TypeScript-1f2328?style=flat-square&logo=typescript&logoColor=2dd4bf" alt="TypeScript"> <img src="https://img.shields.io/badge/JavaScript-1f2328?style=flat-square&logo=javascript&logoColor=2dd4bf" alt="JavaScript"> <img src="https://img.shields.io/badge/SQL-1f2328?style=flat-square" alt="SQL"><br><br>
<b>backend</b><br>
<img src="https://img.shields.io/badge/FastAPI-1f2328?style=flat-square&logo=fastapi&logoColor=2dd4bf" alt="FastAPI"> <img src="https://img.shields.io/badge/SQLAlchemy-1f2328?style=flat-square&logo=sqlalchemy&logoColor=2dd4bf" alt="SQLAlchemy"> <img src="https://img.shields.io/badge/Alembic-1f2328?style=flat-square" alt="Alembic"> <img src="https://img.shields.io/badge/Pydantic-1f2328?style=flat-square&logo=pydantic&logoColor=2dd4bf" alt="Pydantic"> <img src="https://img.shields.io/badge/Node.js-1f2328?style=flat-square&logo=nodedotjs&logoColor=2dd4bf" alt="Node.js"> <img src="https://img.shields.io/badge/Express-1f2328?style=flat-square&logo=express&logoColor=2dd4bf" alt="Express"> <img src="https://img.shields.io/badge/REST%20API-1f2328?style=flat-square" alt="REST API"> <img src="https://img.shields.io/badge/JWT-1f2328?style=flat-square&logo=jsonwebtokens&logoColor=2dd4bf" alt="JWT"> <img src="https://img.shields.io/badge/GitHub%20Apps-1f2328?style=flat-square&logo=github&logoColor=2dd4bf" alt="GitHub Apps"><br><br>
<b>frontend</b><br>
<img src="https://img.shields.io/badge/Next.js-1f2328?style=flat-square&logo=nextdotjs&logoColor=2dd4bf" alt="Next.js"> <img src="https://img.shields.io/badge/React-1f2328?style=flat-square&logo=react&logoColor=2dd4bf" alt="React"> <img src="https://img.shields.io/badge/Tailwind%20CSS-1f2328?style=flat-square&logo=tailwindcss&logoColor=2dd4bf" alt="Tailwind CSS"> <img src="https://img.shields.io/badge/shadcn%2Fui-1f2328?style=flat-square&logo=shadcnui&logoColor=2dd4bf" alt="shadcn/ui"> <img src="https://img.shields.io/badge/TanStack%20Query-1f2328?style=flat-square&logo=reactquery&logoColor=2dd4bf" alt="TanStack Query"> <img src="https://img.shields.io/badge/Vite-1f2328?style=flat-square&logo=vite&logoColor=2dd4bf" alt="Vite"> <img src="https://img.shields.io/badge/Zod-1f2328?style=flat-square&logo=zod&logoColor=2dd4bf" alt="Zod"><br><br>
<b>veri tabanı</b><br>
<img src="https://img.shields.io/badge/PostgreSQL-1f2328?style=flat-square&logo=postgresql&logoColor=2dd4bf" alt="PostgreSQL"> <img src="https://img.shields.io/badge/Supabase-1f2328?style=flat-square&logo=supabase&logoColor=2dd4bf" alt="Supabase"> <img src="https://img.shields.io/badge/Row%20Level%20Security-1f2328?style=flat-square" alt="Row Level Security"> <img src="https://img.shields.io/badge/pgvector-1f2328?style=flat-square" alt="pgvector"> <img src="https://img.shields.io/badge/MySQL-1f2328?style=flat-square&logo=mysql&logoColor=2dd4bf" alt="MySQL"> <img src="https://img.shields.io/badge/Sequelize-1f2328?style=flat-square&logo=sequelize&logoColor=2dd4bf" alt="Sequelize"><br><br>
<b>ai · veri</b><br>
<img src="https://img.shields.io/badge/LLM-1f2328?style=flat-square" alt="LLM"> <img src="https://img.shields.io/badge/RAG-1f2328?style=flat-square" alt="RAG"> <img src="https://img.shields.io/badge/Gemini-1f2328?style=flat-square&logo=googlegemini&logoColor=2dd4bf" alt="Gemini"> <img src="https://img.shields.io/badge/Prompt%20Engineering-1f2328?style=flat-square" alt="Prompt Engineering"> <img src="https://img.shields.io/badge/Pandas-1f2328?style=flat-square&logo=pandas&logoColor=2dd4bf" alt="Pandas"> <img src="https://img.shields.io/badge/Streamlit-1f2328?style=flat-square&logo=streamlit&logoColor=2dd4bf" alt="Streamlit"> <img src="https://img.shields.io/badge/NASA%20Earthdata-1f2328?style=flat-square&logo=nasa&logoColor=2dd4bf" alt="NASA Earthdata"><br><br>
<b>test · devops</b><br>
<img src="https://img.shields.io/badge/pytest-1f2328?style=flat-square&logo=pytest&logoColor=2dd4bf" alt="pytest"> <img src="https://img.shields.io/badge/Vitest-1f2328?style=flat-square&logo=vitest&logoColor=2dd4bf" alt="Vitest"> <img src="https://img.shields.io/badge/Playwright-1f2328?style=flat-square" alt="Playwright"> <img src="https://img.shields.io/badge/Jest-1f2328?style=flat-square&logo=jest&logoColor=2dd4bf" alt="Jest"> <img src="https://img.shields.io/badge/Docker-1f2328?style=flat-square&logo=docker&logoColor=2dd4bf" alt="Docker"> <img src="https://img.shields.io/badge/Caddy-1f2328?style=flat-square&logo=caddy&logoColor=2dd4bf" alt="Caddy"> <img src="https://img.shields.io/badge/Git-1f2328?style=flat-square&logo=git&logoColor=2dd4bf" alt="Git"><br><br>

### AKTİVİTE

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="profile-3d-contrib/ekremagzl-dark.svg">
  <img alt="3D katkı grafiği" src="profile-3d-contrib/ekremagzl-light.svg" width="100%">
</picture>

<img src="assets/languages.svg" width="100%" alt="En çok kullandığım diller">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ekremagzl/ekremagzl/output/snake-dark.svg">
  <img alt="Katkı grafiği animasyonu" src="https://raw.githubusercontent.com/ekremagzl/ekremagzl/output/snake-light.svg" width="100%">
</picture>

### İLETİŞİM

<a href="https://github.com/ekremagzl"><img src="https://img.shields.io/badge/GitHub-1f2328?style=flat-square&logo=github&logoColor=2dd4bf" alt="GitHub"></a>
<!-- LinkedIn ve e-posta: aşağıdaki satırları kendi bilgilerinle doldurup yorumdan çıkar.
<a href="https://www.linkedin.com/in/KULLANICI-ADIN/"><img src="https://img.shields.io/badge/LinkedIn-1f2328?style=flat-square&logo=linkedin&logoColor=2dd4bf" alt="LinkedIn"></a>
<a href="mailto:ADRESIN@ornek.com"><img src="https://img.shields.io/badge/E--posta-1f2328?style=flat-square&logo=gmail&logoColor=2dd4bf" alt="E-posta"></a>
-->
