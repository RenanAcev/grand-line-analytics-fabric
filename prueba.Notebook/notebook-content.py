# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

spark.sql("""
SELECT
    c.character_name,
    c.job,
    b.bounty_amount
FROM dim_character c
LEFT JOIN fact_bounty b
    ON c.character_id = b.character_id
ORDER BY b.bounty_amount DESC
LIMIT 20
""").show(20, False)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
