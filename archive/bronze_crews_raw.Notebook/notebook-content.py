# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "6940c3c8-dda0-4a36-b5c5-981e73d670b9",
# META       "default_lakehouse_name": "OnePieceLakehouse",
# META       "default_lakehouse_workspace_id": "3dfb0c31-32fd-4d32-8709-91dea585a17f",
# META       "known_lakehouses": [
# META         {
# META           "id": "6940c3c8-dda0-4a36-b5c5-981e73d670b9"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "known_warehouses": []
# META     }
# META   }
# META }

# CELL ********************

import requests
import json
from datetime import datetime
from pyspark.sql import Row

url = "https://api.api-onepiece.com/v2/crews/en"

response = requests.get(url)
response.raise_for_status()

data = response.json()

rows = [
    Row(
        source_system="api-onepiece",
        entity_name="crews",
        ingestion_timestamp=str(datetime.utcnow()),
        raw_json=json.dumps(record)
    )
    for record in data
]

df_bronze_crews = spark.createDataFrame(rows)

df_bronze_crews.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("OnePieceLakehouse.bronze_crews_raw")

display(df_bronze_crews)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
