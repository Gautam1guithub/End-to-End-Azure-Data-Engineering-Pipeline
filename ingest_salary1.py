# Databricks notebook source
dbutils.widgets.text("p_data_source", "")
v_data_source = dbutils.widgets.get("p_data_source")

# COMMAND ----------

# MAGIC %run "/Workspace/project mysql adf/include/configuration"

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType,DoubleType,DateType

# COMMAND ----------

salary_schema = StructType([
    StructField("emp_no", IntegerType(), True),
    StructField("salary", IntegerType(), True),
    StructField("from_date", DateType(), True),
    StructField("to_date", DateType(), True)
])

# COMMAND ----------

salary_df = (
    spark.read
    .option("header", True)
    .schema(salary_schema)
    .csv(f"{raw_folder_path}/{v_data_source}"))


# COMMAND ----------

display(salary_df)

# COMMAND ----------

salary_df.write.mode("append").format("delta").save("/mnt/azuremysqlstorage/processed/inc_salary1")