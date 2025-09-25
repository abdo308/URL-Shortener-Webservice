# URL Shortener Webservice

## 📌 Team Members
- **Abdalrhman Magdy**  
- **Mohamed Ezzat**  
- **Safiya Mahmoud**  
- **Mahmoud Hanafy**  
- **Ahmed Tarek**

---

## 🚀 Project Overview
The **URL Shortener Webservice** is a lightweight web application designed to convert long, complex URLs into short and easy-to-share links. It provides users with a simple interface to generate shortened URLs, track usage, and manage their links.  

### ✨ Key Features:
- Shorten long URLs into compact links  
- Redirect to the original URL when the short link is accessed  
- Track the number of times each short link is used  
- REST API support for programmatic URL shortening  
- Optional user accounts for managing personal collections of links  

---

## 📖 Explanation
Long URLs are often difficult to share, remember, or include in text messages, emails, and social media posts. A **URL Shortener** solves this problem by generating a unique identifier (short code) that maps to the original URL.  

When a user enters a long URL:
1. The system generates a short, unique key (e.g., `abc123`).  
2. The key is stored in the database with its corresponding long URL.  
3. A shortened link is created (e.g., `https://short.ly/abc123`).  
4. When users visit the shortened link, the service looks up the key and redirects them to the original URL.  

---

## 📅 Project Timeline

### **Week 1: Build & Containerize the URL Shortener**
**Tasks**  
- Develop the webservice with two endpoints:  
  - `POST /shorten` → Accepts a long URL, returns a short code.  
  - `GET /<short_code>` → Redirects to the original URL.  
- Add **SQLite database** to store URL mappings.  
- Write a **Dockerfile** for containerization.  
- Create an initial **docker-compose.yml** for running the service.  

**Deliverables**  
- Functional URL shortener webservice with source code.  
- Dockerfile that builds a runnable image.  
- docker-compose.yml that runs the service.  
- Service running locally, successfully shortening & redirecting URLs.  

---

### **Week 2: Instrumenting with Custom Prometheus Metrics**
**Tasks**  
- Add Prometheus metrics with client library:  
  - Counter → URLs shortened.  
  - Counter → Successful redirects.  
  - Counter → Failed lookups (404).  
  - Histogram/Summary → Request latency.  
- Create **prometheus.yml** to scrape `/metrics`.  
- Update **docker-compose.yml** to include Prometheus.  

**Deliverables**  
- Webservice exposing `/metrics` endpoint.  
- prometheus.yml scraping the service.  
- Updated docker-compose.yml with Prometheus.  
- Metrics visible in Prometheus UI.  

---

### **Week 3: Advanced Visualization with Grafana**
**Tasks**  
- Add Grafana service to **docker-compose.yml**.  
- Connect Grafana to Prometheus as data source.  
- Build dashboard with:  
  - Rate of URL creations & redirects.  
  - Total count of shortened links.  
  - 95th percentile request latency.  
  - 404 error rate.  

**Deliverables**  
- docker-compose.yml with webservice + Prometheus + Grafana.  
- Custom Grafana dashboard with clear insights.  
- Running stack where short URLs update metrics in real-time.  

---

### **Week 4: Alerting, Persistence, and Documentation**
**Tasks**  
- Configure Grafana alerts for:  
  - High 404 error rate.  
  - High request latency.  
- Enable persistence with **Docker volumes**:  
  - SQLite data  
  - Prometheus data  
  - Grafana dashboards  
- Final testing (restart stack & check persistence).  
- Write documentation (API endpoints + setup).  

**Deliverables**  
- docker-compose.yml with persistent volumes.  
- Configured Grafana alerts.  
- Fully tested, stable & persistent monitoring stack.  
- Comprehensive project documentation.  