import dlt
import pandas as pd
from dlt.sources.helpers import requests
from dotenv import load_dotenv
import os

# Charger le contenu du fichier .env
load_dotenv()

owid_disasters_csv = "./tourists_places.csv"
df = pd.read_csv(owid_disasters_csv, sep=";")
data = df.to_dict(orient="records")

API_KEY = os.getenv("API_KEY_GEOCODE")

def get_tourists_places():
    for place in data:
        url = f"https://api.geoapify.com/v1/geocode/search?text={place["Adresse"]}&apiKey={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        page_json = response.json()
        if page_json:
            yield page_json
        else:
            break


pipeline = dlt.pipeline(
    pipeline_name="tourists_places_pipeline",
    destination=dlt.destinations.duckdb("./test.duckdb"),
    dataset_name="public",
)
load_info = pipeline.run(
    get_tourists_places(), table_name="tourists_places", write_disposition="replace"
)

print(load_info)
