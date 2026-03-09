# RAWG Videogames Dashboard

**Interfaz visual interactiva** para explorar y consultar datos de la industria de videojuegos,
construida con Streamlit y conectada a una API REST desplegada en AWS EC2.

**Interactive visual interface** to explore and query videogame industry data,
built with Streamlit and connected to a REST API deployed on AWS EC2.

**[Ver app en vivo / Live app](https://rawg-app-dashboard-qbhmmsbmroaakdavbqtbh8.streamlit.app/)**

---

## Demo

[Ver vídeo demo / Watch demo video](https://youtu.be/1VSvDha3Cec)

Clica lal imagen inferior para ver el vídeo demo.
Click the image below to watch the demo video.

[![Vídeo Demo](https://img.youtu.be/1VSvDha3Cec/maxresdefault.jpg)](https://youtu.be/1VSvDha3Cec)

---

## Screenshots

![Inicio](docs/screenshots/inicio.png)
![Predictor de Éxito](docs/screenshots/predictor.png)
![Visualizaciones](docs/screenshots/visualizaciones.png)
![Consultas](docs/screenshots/consultas.png)

---

## ¿Qué es esta aplicación? / What is this app?

Esta aplicación es la **capa de visualización** del proyecto
[GamerFutur — RAWG Analytics](https://github.com/Daniel-GH12/rawg-aws-ml-analytics).

This app is the **visualization layer** of the
[GamerFutur — RAWG Analytics](https://github.com/Daniel-GH12/rawg-aws-ml-analytics) project.

Permite a cualquier usuario — sin conocimientos de SQL ni programación — **interactuar con ~20.000 videojuegos** almacenados en PostgreSQL RDS mediante lenguaje natural, predicción ML y gráficos automáticos.

It allows any user — without SQL or programming knowledge — to **interact with ~20,000 videogames** stored in PostgreSQL RDS through natural language, ML prediction, and automatic charts.

---

## Funcionalidades / Features

| Sección | Descripción | Section | Description |
|---------|-------------|---------|-------------|
| 🏠 **Inicio** | Métricas del proyecto y resumen del sistema | **Home** | Project metrics and system overview |
| 🎯 **Predictor** | Predice el éxito de un videojuego con XGBoost (86% accuracy) | **Predictor** | Predicts videogame success with XGBoost (86% accuracy) |
| 📊 **Visualizaciones** | Gráficos automáticos desde preguntas en lenguaje natural | **Charts** | Automatic charts from natural language questions |
| 💬 **Consultas** | Respuestas textuales desde preguntas en lenguaje natural | **Queries** | Text answers from natural language questions |

---

## Arquitectura / Architecture

```
Usuario / User
     ↓
Streamlit (esta app / this app)
     ↓  HTTP
FastAPI (AWS EC2)
     ↓              ↓               ↓
XGBoost ML    Gemini 2.5 Flash   PostgreSQL RDS
(predicción)  (Text-to-SQL)      (~20.000 juegos)
```

---

## Stack tecnológico / Tech Stack

| Tecnología | Uso / Usage |
|-----------|-------------|
| **Streamlit** | Interfaz web / Web interface |
| **Python** | Lenguaje principal / Main language |
| **Requests** | Llamadas HTTP a la API / HTTP calls to API |
| **Pillow** | Renderizado de imágenes / Image rendering |
| **FastAPI** (EC2) | Backend API REST |
| **XGBoost** (EC2) | Modelo ML de predicción / ML prediction model |
| **Gemini 2.5 Flash** (EC2) | Text-to-SQL con IA / AI Text-to-SQL |
| **PostgreSQL RDS** | Base de datos / Database |

---

## Instalación local / Local Setup

```bash
# 1. Clonar el repositorio / Clone the repository
git clone https://github.com/CrisRguezA/rawg-streamlit-dashboard.git
cd rawg-streamlit-dashboard

# 2. Instalar dependencias / Install dependencies
pip install -r requirements.txt

# 3. Ejecutar la app / Run the app
streamlit run app.py
```

> ⚠️ Requiere que la API de EC2 esté activa. Actualizar `BASE_URL` en `app.py` con la IP pública actual de la instancia.
>
> ⚠️ Requires the EC2 API to be running. Update `BASE_URL` in `app.py` with the current EC2 public IP.

---

## Proyecto completo / Full Project

Esta app es solo la capa visual. El sistema completo incluye ETL pipeline, Lambda functions, FastAPI y modelo XGBoost:

This app is only the visual layer. The full system includes ETL pipeline, Lambda functions, FastAPI, and XGBoost model:

🔗 [GamerFutur — RAWG Analytics](https://github.com/Daniel-GH12/rawg-aws-ml-analytics)

---

## Autora / Author

**Cristina Rodríguez Arroyo**
Data Engineer · AI & Data Science  
[GitHub](https://github.com/CrisRguezA) 

---

## About this project”

Este proyecto fue desarrollado como parte de mi proceso de aprendizaje en ingeniería de datos, con foco en arquitecturas basadas en APIs, despliegue en la nube y dashboards interactivos.

This project was developed as part of my data engineering learning journey, focusing on API-based architectures, cloud deployment and interactive dashboards.