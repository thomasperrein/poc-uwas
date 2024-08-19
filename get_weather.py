import dlt
from dlt.sources.helpers import requests

CITY_TO_MAP = {
    "Puy du Fou": {"latitude": 46.892230, "longitude": -0.932460},
    "Disneyland Paris": {"latitude": 48.86694, "longitude": 2.78207},
}


def get_weather_data():
    for city in CITY_TO_MAP:
        latitude = CITY_TO_MAP[city]["latitude"]
        longitude = CITY_TO_MAP[city]["longitude"]
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=Europe%2FLondon"
        # Make a request and check if it was successful
        response = requests.get(url)
        response.raise_for_status()
        page_json = response.json()
        if page_json:
            yield page_json
        else:
            break


pipeline = dlt.pipeline(
    pipeline_name="test",
    destination="duckdb",
    dataset_name="public",
)
load_info = pipeline.run(
    get_weather_data(), table_name="weather", write_disposition="replace"
)

print(load_info)
