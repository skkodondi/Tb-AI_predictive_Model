# TB-AI Predictive Model

An AI-powered predictive model for Tuberculosis risk assessment using GIS features and geospatial data analysis for Kenya counties.

## 🎯 Project Overview

This project leverages machine learning and geographic information systems (GIS) to predict TB (Tuberculosis) risk levels across different counties in Kenya. The model analyzes various geographical and health-related features to provide risk predictions and county-specific statistics.

**Repository:** [skkodondi/Tb-AI_predictive_Model](https://github.com/skkodondi/Tb-AI_predictive_Model)

## ✨ Features

- **ML Prediction Engine**: Predicts TB risk levels (Low, Medium, High) based on input features
- **GIS Integration**: Uses GeoJSON data for Kenya counties with geospatial analysis
- **Choropleth Visualization**: Interactive maps showing TB risk distribution across counties
- **County Detection**: Automatically identifies county based on latitude/longitude coordinates
- **County Statistics**: Provides pseudo-random but deterministic health statistics per county
- **Web Interface**: Flask-based web application with interactive UI
- **RESTful API**: JSON endpoints for programmatic access

## 🛠️ Technology Stack

- **Backend**: Flask, Python 3.11
- **ML Libraries**: scikit-learn, joblib, numpy, pandas
- **GIS Libraries**: Shapely, folium, django-geojson
- **Visualization**: Leaflet.js, folium
- **Containerization**: Docker, Gunicorn
- **Deployment**: Heroku (via Procfile)

## 📋 Prerequisites

Before you begin, ensure you have installed:
- Python 3.11 or higher
- pip (Python package manager)
- Git

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/skkodondi/Tb-AI_predictive_Model.git
cd Tb-AI_predictive_Model
