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

from pyspark.sql.functions import col, regexp_replace, when

df_silver = spark.table("silver_characters")

df_fact_bounty = (
    df_silver
    .select(
        col("character_id").cast("int").alias("character_id"),
        col("bounty").alias("bounty_original")
    )
    .withColumn(
        "bounty_clean",
        regexp_replace(col("bounty_original"), "[^0-9]", "")
    )
    .withColumn(
        "bounty_amount",
        when(col("bounty_clean") == "", None)
        .otherwise(col("bounty_clean").cast("bigint"))
    )
    .select(
        "character_id",
        "bounty_amount"
    )
)

df_fact_bounty.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .format("delta") \
    .saveAsTable("fact_bounty")

display(df_fact_bounty)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""
SELECT
    COUNT(*) AS total_records,
    COUNT(bounty_amount) AS records_with_bounty,
    MIN(bounty_amount) AS min_bounty,
    MAX(bounty_amount) AS max_bounty,
    SUM(bounty_amount) AS total_bounty
FROM fact_bounty
""").show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""
SELECT *
FROM fact_bounty
ORDER BY bounty_amount DESC
LIMIT 20
""").show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
