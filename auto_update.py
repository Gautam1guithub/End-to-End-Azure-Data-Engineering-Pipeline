# Databricks notebook source
dbutils.fs.ls("/mnt/azuremysqlstorage/processed/")

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE delta.`/mnt/azuremysqlstorage/processed/inc_current_dept`
# MAGIC SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE delta.`/mnt/azuremysqlstorage/processed/inc_dept`
# MAGIC SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE delta.`/mnt/azuremysqlstorage/processed/inc_dept_emp`
# MAGIC SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE delta.`/mnt/azuremysqlstorage/processed/inc_dept_emp_latest_date`
# MAGIC SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE delta.`/mnt/azuremysqlstorage/processed/inc_dept_manager`
# MAGIC SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE delta.`/mnt/azuremysqlstorage/processed/inc_salaries`
# MAGIC SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE delta.`/mnt/azuremysqlstorage/processed/inc_salary1`
# MAGIC SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE delta.`/mnt/azuremysqlstorage/processed/inc_titles`
# MAGIC SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE delta.`/mnt/azuremysqlstorage/processed/inc_employees`
# MAGIC SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS control;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS control.cdf_offsets (
# MAGIC   table_id STRING,
# MAGIC   last_processed_version LONG,
# MAGIC   last_processed_ts TIMESTAMP
# MAGIC ) USING delta;