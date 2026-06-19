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

from pyspark.sql.functions import col

df_silver_crews = spark.table("silver_crews")

df_fact_crew_summary = (
    df_silver_crews
    .select(
        col("crew_id").cast("int").alias("crew_id"),
        col("total_bounty_amount").cast("bigint").alias("total_bounty_amount"),
        col("crew_members_count").cast("int").alias("crew_members_count")
    )
)

df_fact_crew_summary.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .format("delta") \
    .saveAsTable("fact_crew_summary")

display(df_fact_crew_summary)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""
SELECT
    c.crew_name,
    c.is_yonko,
    f.crew_members_count,
    f.total_bounty_amount
FROM dim_crew c
LEFT JOIN fact_crew_summary f
    ON c.crew_id = f.crew_id
ORDER BY f.total_bounty_amount DESC
LIMIT 20
""").show(20, False)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
