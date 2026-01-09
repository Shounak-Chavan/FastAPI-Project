<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql" />
  <img src="https://img.shields.io/badge/Redis-Cache-red?logo=redis" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
</p>

# 🚗 Car Price Prediction – Full-Stack AI Application
### *(ML Model • FastAPI • JWT Auth • Redis Cache • PostgreSQL)*

A production-style full-stack AI application that predicts car prices using a trained ML model, with authentication, caching, persistence, monitoring, and modern frontend integration.

This project demonstrates **real backend engineering practices**, not just model inference.

---

## 🔥 Features

- 🔐 **JWT Authentication** (Login → Protected APIs)
- 🤖 **ML-powered car price prediction**
- 🧠 **Redis caching** for faster repeated predictions
- 🗄️ **PostgreSQL** for persistent prediction history
- 📊 **Prediction history dashboard**
- 🌐 **Frontend–backend integration** (Modern HTML/CSS/JS)
- 📈 **Prometheus metrics** endpoint
- 🧩 **Clean, modular FastAPI architecture**

---

## 🏗️ Architecture Overview

```
Frontend (HTML + JS)
        |
        |  HTTP (JSON + JWT)
        v
FastAPI Backend
 ├── Auth (JWT)
 ├── Prediction API
 ├── Redis Cache
 ├── PostgreSQL DB
 └── Prometheus Metrics
```

---

## 🧰 Tech Stack

### **Backend**
- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis
- JWT Authentication
- Prometheus FastAPI Instrumentator

### **Machine Learning**
- Scikit-learn / XGBoost
- Pretrained regression model
- Feature preprocessing pipeline

### **Frontend**
- Modern HTML5
- CSS3 with Glassmorphism
- Vanilla JavaScript
- Fetch API

---

## 🔐 Authentication Flow

1. User logs in with credentials
2. Backend issues a JWT token
3. Token is stored in browser (`localStorage`)
4. Token is sent in headers for protected routes
5. Backend verifies JWT before processing requests

```
Login → JWT → Protected APIs → Response
```

---

## 📊 Prediction Flow

1. User enters car details (12+ parameters)
2. Frontend sends request to `/predict`
3. Backend:
   - Checks Redis cache
   - Runs ML model if cache miss
   - Saves result to PostgreSQL
4. Predicted price is returned to UI

---

## 🗄️ Database Schema

**PostgreSQL** stores prediction history with:
- Input features (company, year, fuel type, etc.)
- Predicted price
- Timestamp
- User information

Example Query:
```sql
SELECT * FROM predictions ORDER BY created_at DESC;
```

---

## 🚀 Running Locally

### **1️⃣ Clone the Repository**
```bash
git clone <repo-url>
cd <repo>
```

### **2️⃣ Create `.env` File**
```env
DATABASE_URL=postgresql://user:password@localhost:5432/db_name
REDIS_URL=redis://localhost:6379/0
JWT_SECRET_KEY=your_secret_key_here
API_KEY=your_api_key_here
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Start Required Services**
- Start PostgreSQL
- Start Redis

### **5️⃣ Run the Application**
```bash
uvicorn app.main:app --reload
```

### **6️⃣ Access the App**
- Frontend: `http://localhost:8000/login.html`
- API Docs: `http://localhost:8000/docs`
- Metrics: `http://localhost:8000/metrics`

---

## 📈 Monitoring & Observability

**Prometheus metrics** exposed at `/metrics`

Metrics include:
- Request count per endpoint
- Response latency
- Error rates
- Cache hit/miss ratio
- Database query performance

---

## 🎨 Frontend Features

- **Modern Glassmorphic UI** with gradient backgrounds
- **Floating label animations** on all input fields
- **Smooth transitions** and micro-interactions
- **Loading states** with animations
- **Error handling** with shake effects
- **Fully responsive** design (mobile + desktop)
- **Interactive cards** with hover effects

---

## 🧠 Machine Learning Pipeline

### **Input Features (12)**
- Company
- Year
- Owner Type
- Fuel Type
- Seller Type
- Transmission
- KM Driven
- Mileage (MPG)
- Engine (CC)
- Max Power (BHP)
- Torque (NM)
- Seats

### **Model Architecture**
- Trained regression model
- Feature scaling & preprocessing
- Optimized for accuracy and speed
- Cached predictions for identical inputs

---

## 🔑 API Endpoints

### **Authentication**
```
POST /login
Body: { "username": "user", "password": "pass" }
Response: { "access_token": "jwt_token" }
```

### **Prediction**
```
POST /predict
Headers: { "token": "jwt_token", "api-key": "key" }
Body: { car details... }
Response: { "predicted_price": "₹X,XX,XXX" }
```

### **History**
```
GET /predictions
Headers: { "token": "jwt_token", "api-key": "key" }
Response: [ { "id": 1, "predicted_price": "..." }, ... ]
```

---

## 🧩 Key Learnings

- ✅ Designing **production-ready APIs**
- ✅ **JWT-based authentication** implementation
- ✅ **Caching strategies** using Redis
- ✅ **Database persistence** with SQLAlchemy
- ✅ **Frontend–backend communication**
- ✅ **Observability** with Prometheus
- ✅ **Clean project structuring** with modular architecture
- ✅ **Modern UI/UX** with CSS animations

---

## 🔮 Future Improvements

- 🐳 **Dockerization** & container orchestration
- 🔄 **Alembic migrations** for database versioning
- 👥 **Role-based access control** (RBAC)
- 📄 **Pagination** for prediction history
- ⚛️ **React frontend** upgrade
- ☁️ **Cloud deployment** (AWS / Render / Railway)
- 📊 **Analytics dashboard** with charts
- 🔔 **Real-time notifications**
- 🧪 **Unit & integration tests**
- 📝 **API rate limiting**

---

## ⚠️ Disclaimer

This project is **for educational and demonstration purposes only** and should not be used for real commercial car price predictions without proper validation.

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, please ⭐ the repository!
