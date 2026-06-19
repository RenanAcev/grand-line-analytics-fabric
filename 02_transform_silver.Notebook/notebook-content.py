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

from pyspark.sql.functions import col, get_json_object, regexp_replace, current_timestamp

df_bronze = spark.table("bronze_characters_raw")

df_silver = (
    df_bronze
    .select(
        get_json_object(col("raw_json"), "$.id").cast("int").alias("character_id"),
        get_json_object(col("raw_json"), "$.name").alias("character_name"),
        get_json_object(col("raw_json"), "$.job").alias("job"),
        get_json_object(col("raw_json"), "$.size").alias("size"),
        get_json_object(col("raw_json"), "$.age").alias("age"),
        get_json_object(col("raw_json"), "$.status").alias("character_status"),
        get_json_object(col("raw_json"), "$.crew.id").cast("int").alias("crew_id"),
        get_json_object(col("raw_json"), "$.crew.name").alias("crew_name"),
        get_json_object(col("raw_json"), "$.fruit.id").cast("int").alias("fruit_id"),
        get_json_object(col("raw_json"), "$.fruit.name").alias("fruit_name"),
        get_json_object(col("raw_json"), "$.fruit.type").alias("fruit_type"),
        regexp_replace(
            get_json_object(col("raw_json"), "$.bounty"),
            "[^0-9]",
            ""
        ).cast("bigint").alias("bounty_amount"),
        col("source_system"),
        col("ingestion_timestamp"),
        current_timestamp().alias("silver_processed_timestamp")
    )
    .dropDuplicates(["character_id"])
)

df_silver.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .format("delta") \
    .saveAsTable("silver_characters")

display(df_silver)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
