# Databricks notebook source
dbutils.widgets.text("p_data_source", "")
v_data_source = dbutils.widgets.get("p_data_source")

# COMMAND ----------

# MAGIC %run "/Workspace/project mysql adf/include/configuration"

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType,DoubleType,DateType

# COMMAND ----------

departments_schema = StructType([
    StructField("dept_no", StringType(), True),
    StructField("dept_name", StringType(), True)
])

# COMMAND ----------

dept_df = (
    spark.read
    .option("header", True)
    .schema(departments_schema)
    .csv(f"{raw_folder_path}/{v_data_source}"))


# COMMAND ----------

display(dept_df)

# COMMAND ----------

dept_df.write.mode("append").format("delta").save("/mnt/azuremysqlstorage/processed/inc_dept")