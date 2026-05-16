# Databricks notebook source
dbutils.widgets.text("p_data_source", "")
v_data_source = dbutils.widgets.get("p_data_source")

# COMMAND ----------

# MAGIC %run "/Workspace/project mysql adf/include/configuration"

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType,DoubleType,DateType

# COMMAND ----------

titles_schema = StructType([
    StructField("emp_no", IntegerType(), True),
    StructField("title", StringType(), True),
    StructField("from_date", DateType(), True),
    StructField("to_date", DateType(), True)
])

# COMMAND ----------

titles_df = (
    spark.read
    .option("header", True)
    .schema(titles_schema)
    .csv(f"{raw_folder_path}/{v_data_source}"))


# COMMAND ----------

display(titles_df)

# COMMAND ----------

titles_df.write.mode("append").format("delta").save("/mnt/azuremysqlstorage/processed/inc_titles")