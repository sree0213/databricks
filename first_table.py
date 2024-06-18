# Databricks notebook source
# MAGIC %sql
# MAGIC USE CATALOG prod_catalog
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS default.department
# MAGIC (
# MAGIC    deptcode   INT,
# MAGIC    deptname  STRING,
# MAGIC    location  STRING
# MAGIC );
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO default.department VALUES
# MAGIC    (10, 'FINANCE', 'EDINBURGH'),
# MAGIC    (20, 'SOFTWARE', 'PADDINGTON');
# MAGIC
