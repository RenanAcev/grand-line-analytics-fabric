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

from pyspark.sql.functions import monotonically_increasing_id

df_silver = spark.table("silver_characters")

df_dim_character = (
    df_silver.select(   "character_id",
        "character_name",
        "job",
        "age",
        "size"
    )
)

df_dim_character.write\
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("dim_character")

display(df_dim_character)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
