import dlt
import pandas as pd

owid_disasters_csv = "./tourists_places.csv"
df = pd.read_csv(owid_disasters_csv, sep=";")
data = df.to_dict(orient="records")

pipeline = dlt.pipeline(
    pipeline_name="test",
    destination="duckdb",
    dataset_name="public",
)
load_info = pipeline.run(
    data, table_name="tourists_places", write_disposition="replace"
)

print(load_info)
