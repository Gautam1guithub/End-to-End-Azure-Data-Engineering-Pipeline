# End-to-End-Azure-Data-Engineering-Pipeline
A production-grade cloud data engineering project built on the Employees HR Database (~300MB across 9 tables) — covering the complete data engineering lifecycle from MySQL ingestion and Azure Blob Storage landing to PySpark-based transformation in Databricks and analytics-ready tables served via Azure Synapse to Power BI.

🧭 Project Overview
This project simulates a real-world enterprise data pipeline where raw HR data from a MySQL database is automatically ingested, processed, and served to business stakeholders — entirely on the Azure cloud stack.
The dataset contains over 300MB of employee records across 9 relational tables — covering employees, salaries, titles, departments, and managerial assignments. The goal was to build a fully automated, metadata-driven pipeline that dynamically discovers, ingests, and processes every table without any hardcoded logic — and delivers clean, queryable data to Power BI through Azure Synapse Analytics.

The workflow includes:

Extracting raw CSV data from MySQL into Azure Blob Storage using Azure Data Factory
Processing and schema-validating each file using PySpark notebooks in Azure Databricks
Storing structured output in a processed container as Parquet/Delta format
Registering all tables as external tables in Azure Synapse (processedLakeDB)
Connecting Synapse tables directly to Power BI for reporting and dashboards

🔧 Technologies Used

Azure Data Factory (ADF)
Azure Blob Storage
Azure Databricks (PySpark / Python)
Azure Synapse Analytics
MySQL
Power BI

🔄 Project Workflow

MySQL Database (9 HR Tables)
        │
        ▼
Azure Data Factory — Pipeline 1
(Lookup + ForEach + Copy Activity)
        │
        ▼
Azure Blob Storage — raw-files container (CSV)
        │
        ▼
Azure Data Factory — Pipeline 2
(Get Metadata + ForEach + Databricks Notebook Activity)
        │
        ▼
Azure Databricks — PySpark Notebooks
(Schema Enforcement + Incremental Processing)
        │
        ▼
Azure Blob Storage — processed container (Parquet)
        │
        ▼
Azure Synapse Analytics — processedLakeDB
(9 External Tables Registered)
        │
        ▼
Power BI Dashboard
(Connected via Synapse Serverless SQL Pool)

📈 Key Engineering Work Performed

Metadata-driven Ingestion — ADF pipelines use Lookup + ForEach to dynamically discover and copy all 9 tables without any hardcoded table names
Parameterized Datasets — MySQL and CSV datasets are fully parameterized using @dataset().tablename and @dataset().fileName expressions
PySpark Schema Enforcement — Each Databricks notebook defines and applies a strict StructType schema before reading CSVs, ensuring data quality at ingestion
Incremental Folder Structure — Processed data is written into inc_* prefixed folders (e.g. inc_employees, inc_salaries) for incremental load tracking
Dynamic Notebook Orchestration — ADF Pipeline 2 uses Get Metadata on the Blob container and dynamically triggers the correct Databricks notebook for each file via @concat(pipeline().parameters.baseNotebookPath, ...)
Synapse External Table Registration — All 9 processed tables are registered as external tables in processedLakeDB using PySpark inside Azure Synapse, making them directly queryable via SQL
Power BI Integration — Power BI connects to Synapse via the serverless SQL pool, loading all inc_* tables for dashboard reporting.

🎯 Project Outcome
Delivered a fully automated, cloud-native data engineering pipeline that ingests 300MB+ of raw HR data from MySQL, processes it through schema-validated PySpark notebooks in Databricks, and surfaces 9 clean, analytics-ready tables in Azure Synapse — all orchestrated end-to-end by Azure Data Factory with zero hardcoded logic. The final data is directly consumed by Power BI for business reporting.
