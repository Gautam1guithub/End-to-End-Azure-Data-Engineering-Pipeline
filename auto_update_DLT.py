# Databricks notebook source
import dlt
from pyspark.sql.functions import current_timestamp

# COMMAND ----------

@dlt.table(
    name="processed_departments",
    comment="Automatically updated table for departments"
)
def processed_departments():
    df = spark.read.format("delta").load("/mnt/azuremysqlstorage/processed/inc_dept")
    return df.withColumn("processed_time", current_timestamp())

# COMMAND ----------

@dlt.table(
    name="processed_employees",
    comment="Automatically updated table for employees"
)
def processed_employees():
    df = spark.read.format("delta").load("/mnt/azuremysqlstorage/processed/inc_employees")
    return df.withColumn("processed_time", current_timestamp())

# COMMAND ----------

@dlt.table(
    name="processed_salaries",
    comment="Automatically updated table for salaries"
)
def processed_salaries():
    df = spark.read.format("delta").load("/mnt/azuremysqlstorage/processed/inc_salaries")
    return df.withColumn("processed_time", current_timestamp())

# COMMAND ----------

@dlt.table(
    name="processed_salary",
    comment="Automatically updated table for salaries"
)
def processed_salaries():
    df = spark.read.format("delta").load("/mnt/azuremysqlstorage/processed/inc_salary1")
    return df.withColumn("processed_time", current_timestamp())

# COMMAND ----------

@dlt.table(
    name="processed_titles",
    comment="Automatically updated table for titles"
)
def processed_titles():
    df = spark.read.format("delta").load("/mnt/azuremysqlstorage/processed/inc_titles")
    return df.withColumn("processed_time", current_timestamp())

# COMMAND ----------

dbutils.fs.ls("/mnt/azuremysqlstorage/processed/")




# COMMAND ----------

@dlt.table(
    name="processed_inc_current_dept",
    comment="Automatically updated table for titles"
)
def processed_inc_current_dept():
    df = spark.read.format("delta").load("/mnt/azuremysqlstorage/processed/inc_current_dept")
    return df.withColumn("processed_time", current_timestamp())

# COMMAND ----------

@dlt.table(
    name="processed_inc_dept_emp",
    comment="Automatically updated table for titles"
)
def processed_inc_dept_empt():
    df = spark.read.format("delta").load("/mnt/azuremysqlstorage/processed/inc_dept_emp")
    return df.withColumn("processed_time", current_timestamp())

# COMMAND ----------

@dlt.table(
    name="processed_inc_dept_emp_latest_date",
    comment="Automatically updated table for titles"
)
def processed_inc_dept_emp_latest_date():
    df = spark.read.format("delta").load("/mnt/azuremysqlstorage/processed/inc_dept_emp_latest_date")
    return df.withColumn("processed_time", current_timestamp())

# COMMAND ----------

@dlt.table(
    name="processed_inc_dept_manager",
    comment="Automatically updated table for titles"
)
def processed_inc_dept_emp_latest_date():
    df = spark.read.format("delta").load("/mnt/azuremysqlstorage/processed/inc_dept_manager")
    return df.withColumn("processed_time", current_timestamp())