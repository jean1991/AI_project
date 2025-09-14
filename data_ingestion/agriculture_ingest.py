import pandas as pd
import requests

def ingest_sensor_csv(file_path: str) -> pd.DataFrame:
    """Ingest sensor data from a CSV file."""
    return pd.read_csv(file_path)

def ingest_satellite_api(api_url: str, params=None) -> pd.DataFrame:
    """Ingest satellite data from a REST API endpoint."""
    response = requests.get(api_url, params=params)
    data = response.json()
    return pd.DataFrame(data)

def demo_ingest():
    sensor_df = ingest_sensor_csv('data/sensor_data.csv')
    # Example only; replace with real satellite API
    # satellite_df = ingest_satellite_api('https://api.example-satellite.com/ndvi')
    satellite_df = pd.read_csv('data/satellite_data.csv')
    return sensor_df, satellite_df

if __name__ == '__main__':
    sensor, satellite = demo_ingest()
    print(sensor.head())
    print(satellite.head())