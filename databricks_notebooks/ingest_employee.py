# Databricks notebook source
dbutils.widgets.text("p_data_source", "")
v_data_source = dbutils.widgets.get("p_data_source")

# COMMAND ----------

# MAGIC %run "/Workspace/project mysql adf/include/configuration"

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType,DoubleType,DateType

# COMMAND ----------

employees_schema = StructType([
    StructField("emp_no", IntegerType(), True),
    StructField("birth_date", DateType(), True),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("hire_date", DateType(), True)
])


# COMMAND ----------

employees_df = (
    spark.read
    .option("header", True)
    .schema(employees_schema)
    .csv(f"{raw_folder_path}/{v_data_source}"))


# COMMAND ----------

display(employees_df)

# COMMAND ----------

employees_df.write.mode("append").format("delta").save("/mnt/azuremysqlstorage/processed/inc_employees")