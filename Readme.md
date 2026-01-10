<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql" />
  <img src="https://img.shields.io/badge/Redis-Cache-DC382D?logo=redis" />
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker" />
</p>

# 🚗 AutoValuator AI – Full-Stack AI Application
### *(Scikit-Learn • FastAPI • JWT Auth • Redis Cache • PostgreSQL • Docker • Render • Prometheus)*

A production-style full-stack AI application that predicts car prices using a trained ML model, with authentication, caching, persistence, monitoring, and modern frontend integration.

This project demonstrates **real backend engineering practices**, not just model inference.

---

## 🔥 Features

- 🔐 **Authentication**: JWT-based token auth and API key validation
- 🤖 **ML Model Prediction**: Trained model predicts used car prices
- ⚡ **Redis Caching**: Avoid redundant model computation
- 🗄️ **PostgreSQL**: Persistent prediction history storage
- 📊 **Prediction History Dashboard**: View and analyze past predictions
- 🌐 **Frontend–Backend Integration**: Modern HTML/CSS/JS
- 📈 **Monitoring Ready**: Prometheus metrics + Grafana dashboards
- 🐳 **Dockerized Setup**: Simplified deployment with Docker Compose
- ☁️ **Cloud Deployment**: Easily deploy to [Render](https://render.com)
- 🧩 **Clean, Modular Architecture**: Production-grade FastAPI structure

---

## 🧠 Model Input Variables

The prediction model expects the following input features:

| Feature           | Description                          | Example         |
|------------------|--------------------------------------|-----------------|
| `company`         | Brand of the car                     | `"Maruti"`      |
| `year`            | Year of manufacturing                | `2015`          |
| `owner`           | Number of previous owners            | `"Second"`      |
| `fuel`            | Fuel type                            | `"Petrol"`      |
| `seller_type`     | Individual or Dealer                 | `"Individual"`  |
| `transmission`    | Transmission type                    | `"Manual"`      |
| `km_driven`       | Kilometers driven                    | `45000`         |
| `mileage_mpg`     | Mileage in miles per gallon          | `19.5`          |
| `engine_cc`       | Engine capacity in cc                | `1197`          |
| `max_power_bhp`   | Maximum power in BHP                 | `88.5`          |
| `torque_nm`       | Torque in Newton meters              | `113`           |
| `seats`           | Number of seats                      | `5`             |

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

1. User enters car details (12 parameters)
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

## 🚀 Getting Started (Local)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Autovaluator-Ai.git
cd AutoValuator-Ai
```

### 2️⃣ Set Environment Variables

```env
DATABASE_URL=postgresql://user:password@localhost:5432/autovaluator
REDIS_URL=redis://localhost:6379/0
JWT_SECRET_KEY=your-secret-key-here
API_KEY=your-api-key-here
```

### 3️⃣ Build and Run via Docker

```bash
docker-compose up --build
```

### 4️⃣ Access Interfaces

- 🌐 **Frontend**: http://localhost:8000/login.html
- 📚 **API Docs**: http://localhost:8000/docs
- 📊 **Metrics**: http://localhost:8000/metrics
- 🔍 **Prometheus**: http://localhost:9090
- 📈 **Grafana**: http://localhost:3000

---

## ☁️ Deployment on Render

1. Push code to GitHub
2. Add `render.yaml` to the project root
3. Create a new Web Service on Render
4. Add environment variables
5. Deploy

---

## 🎨 Frontend Features

- ✨ **Modern Glassmorphic UI** with gradient backgrounds
- 🎭 **Floating label animations** on all input fields
- 🔄 **Smooth transitions** and micro-interactions
- ⏳ **Loading states** with animations
- ⚠️ **Error handling** with shake effects
- 📱 **Fully responsive** design (mobile + desktop)
- 🎯 **Interactive cards** with hover effects

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

- 🔄 **Alembic migrations** for database versioning
- 👥 **Role-based access control** (RBAC)
- 📄 **Pagination** for prediction history
- ⚛️ **React frontend** upgrade
- 📊 **Analytics dashboard** with charts
- 🔔 **Real-time notifications**
- 🧪 **Unit & integration tests**
- 📝 **API rate limiting**

---

## ⚠️ Disclaimer

This project is **for educational and demonstration purposes only** and should not be used for real commercial car price predictions without proper validation.

---

## 👨‍💻 Author

Made with ❤️ by **Shounak**

---

## ⭐ If you found this project useful, please ⭐ the repository!