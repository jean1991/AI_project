# Digital Agriculture Platform - Open Source

## Modules
- **Data Ingestion:** Load sensor and satellite data from CSV/API.
- **Data Storage:** SQLite DB for easy prototyping (extendable to cloud).
- **Processing:** Cleaning, feature engineering for model input.
- **ML Models:** Crop yield prediction, disease detection (RandomForest, extendable).
- **Serving:** FastAPI REST endpoints for predictions.
- **Monitoring:** Prometheus metrics on predictions.
- **Visualization:** Yield and NDVI plots.

## Quick Start

1. Add your `.csv` files in `/data` (sensor_data.csv, satellite_data.csv, yield_data.csv, disease_data.csv).
2. Install dependencies:
   ```bash
   pip install pandas scikit-learn fastapi uvicorn joblib prometheus_client matplotlib requests
   ```
3. Setup DB:
   ```bash
   python data_storage/agriculture_db.py
   ```
4. Train models:
   ```bash
   python ml_models/crop_yield_prediction.py
   python ml_models/crop_disease_detection.py
   ```
5. Start API:
   ```bash
   uvicorn deployment.agriculture_api:app --reload
   ```
6. Start Prometheus metrics:
   ```bash
   python monitoring/agriculture_monitor.py
   ```
7. Visualize:
   ```bash
   python visualization/agriculture_visualization.py
   ```

## Extending
- Add new data sources, models, or cloud integrations.
- Containerize for production (Docker/Kubernetes).
- Add security, RBAC, and data governance.

## License
Apache 2.0 or MIT recommended.

---

**Ready to customize for your farm, region, or research. Contribute and expand!**