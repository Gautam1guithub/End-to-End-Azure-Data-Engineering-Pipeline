# Databricks notebook source
dbutils.widgets.text("p_data_source", "")
v_data_source = dbutils.widgets.get("p_data_source")

# COMMAND ----------

# MAGIC %run "/Workspace/project mysql adf/include/configuration"

# COMMAND ----------

raw_folder_path

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType,DoubleType,DateType

# COMMAND ----------

current_dept_emp_schema = StructType([
    StructField("emp_no", IntegerType(), True),
    StructField("dept_no", StringType(), True),
    StructField("from_date", DateType(), True),
    StructField("to_date", DateType(), True)
])

# COMMAND ----------

current_dept_df = (
    spark.read
    .option("header", True)
    .schema(current_dept_emp_schema)
    .csv(f"{raw_folder_path}/{v_data_source}")
)

# COMMAND ----------

display(current_dept_df)

# COMMAND ----------

current_dept_df.write.mode("append").format("delta").save("/mnt/azuremysqlstorage/processed/inc_current_dept")

# COMMAND ----------

