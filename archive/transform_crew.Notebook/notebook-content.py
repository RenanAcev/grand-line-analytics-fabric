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

from pyspark.sql.functions import col, get_json_object, regexp_replace, when, current_timestamp

df_bronze_crews = spark.table("bronze_crews_raw")

df_silver_crews = (
    df_bronze_crews
    .select(
        get_json_object(col("raw_json"), "$.id").cast("int").alias("crew_id"),
        get_json_object(col("raw_json"), "$.name").alias("crew_name"),
        get_json_object(col("raw_json"), "$.roman_name").alias("roman_name"),
        get_json_object(col("raw_json"), "$.status").alias("crew_status"),
        get_json_object(col("raw_json"), "$.number").cast("int").alias("crew_members_count"),
        get_json_object(col("raw_json"), "$.is_yonko").cast("boolean").alias("is_yonko"),
        regexp_replace(
            get_json_object(col("raw_json"), "$.total_prime"),
            "[^0-9]",
            ""
        ).cast("bigint").alias("total_bounty_amount"),
        col("source_system"),
        col("ingestion_timestamp"),
        current_timestamp().alias("silver_processed_timestamp")
    )
    .dropDuplicates(["crew_id"])
)

df_silver_crews.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .format("delta") \
    .saveAsTable("silver_crews")

display(df_silver_crews)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
