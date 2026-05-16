# Databricks notebook source
from pyspark.sql import SparkSession

# COMMAND ----------

tables = [
    "inc_current_dept",
    "inc_dept",
    "inc_dept_emp",
    "inc_dept_emp_latest_date",
    "inc_dept_manager",
    "inc_salaries",
    "inc_salary1",
    "inc_titles",
    "inc_employees"
]

# COMMAND ----------

base_path = "/mnt/azuremysqlstorage/processed/"
target_base = "/mnt/azuremysqlstorage/cdf_changes/"

# COMMAND ----------

spark.read.format("delta").load(src).write.format("delta").mode("overwrite").save(tgt)
print("Initial data copied. Future changes will come via CDF.")

# COMMAND ----------

for t in tables:
    src = f"{base_path}{t}"
    tgt = f"{target_base}{t}"

    print(f"\n Processing table: {t}")

    try:
        # Find CDF-enabled version
        history_df = spark.sql(f"DESCRIBE HISTORY delta.`{src}`")
        history = history_df.collect()

        cdf_enabled_version = None
        for row in history:
            if "delta.enableChangeDataFeed" in str(row.operationParameters) and "true" in str(row.operationParameters):
                cdf_enabled_version = row.version
                break

        if cdf_enabled_version is None:
            print(f"CDF not enabled for {t}. Skipping.")
            continue

        print(f" CDF enabled from version {cdf_enabled_version} for {t}")

        # Read only from CDF-active version
        df = (
            spark.read.format("delta")
            .option("readChangeData", "true")
            .option("startingVersion", cdf_enabled_version)
            .load(src)
        )

        if df.count() > 0:
            df.write.format("delta").mode("append").save(tgt)
            print(f"Changes stored at: {tgt}")
        else:
            print(f" No new changes yet for {t}")

    except Exception as e:
        print(f" Error processing {t}: {e}")


# COMMAND ----------

for t in tables:
    src = f"/mnt/azuremysqlstorage/processed/{t}"
    try:
        spark.sql(f"""
            ALTER TABLE delta.`{src}`
            SET TBLPROPERTIES (delta.enableChangeDataFeed = true)
        """)
        print(f" Enabled Change Data Feed for {t}")
    except Exception as e:
        print(f" Could not enable CDF for {t}: {e}")


# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY delta.`/mnt/azuremysqlstorage/processed/inc_employees`
# MAGIC

# COMMAND ----------

