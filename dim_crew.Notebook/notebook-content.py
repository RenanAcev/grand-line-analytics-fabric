# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "warehouse": {
# META       "default_warehouse": "93115745-3406-465e-a825-858d336775fc",
# META       "known_warehouses": [
# META         {
# META           "id": "93115745-3406-465e-a825-858d336775fc",
# META           "type": "Lakewarehouse"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df_silver = spark.table("OnePieceLakehouse.silver_characters")
df_silver.printSchema()
display(df_silver.limit(10))


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
