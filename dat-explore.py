# Databricks notebook source
dbutils.fs.ls('s3://databricks-workspace-stack-d50d7-bucket/unity-catalog/3770040687353055/prod_volume/rows.csv')


# COMMAND ----------

df = spark.sql("""
SELECT * 
FROM read_files('s3://databricks-workspace-stack-d50d7-bucket/unity-catalog/3770040687353055/prod_volume/rows.csv', format => 'CSV') 
LIMIT 10
""")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from read_files('s3://databricks-workspace-stack-d50d7-bucket/unity-catalog/3770040687353055/prod_volume/rows.csv', format => 'CSV') LIMIT 10
# MAGIC
