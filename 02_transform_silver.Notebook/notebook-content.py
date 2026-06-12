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
# META     }
# META   }
# META }

# CELL ********************

#Librerías

from pyspark.sql.functions import col, get_json_object, current_timestamp

df_bronze = spark.table("bronze_characters_raw")

df_silver = (
    df_bronze.select(get_json_object(col("raw_json"), "$.id").cast("int").alias("character_id"),
        get_json_object(col("raw_json"), "$.name").alias("character_name"),
        get_json_object(col("raw_json"), "$.job").alias("job"),
        get_json_object(col("raw_json"), "$.size").alias("size"),
        get_json_object(col("raw_json"), "$.age").alias("age"),
        get_json_object(col("raw_json"), "$.bounty").alias("bounty"),
        col("source_system"),
        col("ingestion_timestamp"),
        current_timestamp().alias("silver_processed_timestamp")
    )
    .dropDuplicates(["character_id"])
)

df_silver.write.mode("overwrite").format("delta").saveAsTable("silver_characters")

display(df_silver)

spark.sql("""
SELECT 
    COUNT(*) AS total_characters,
    COUNT(DISTINCT character_id) AS distinct_characters
FROM silver_characters
""").show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
