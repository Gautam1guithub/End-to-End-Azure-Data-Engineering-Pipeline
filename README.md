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


## Parameterized MySQL Source Dataset in Azure Data Factory

<img width="1046" height="471" alt="Azure -1" src="https://github.com/user-attachments/assets/dc13b650-f2d8-444f-bb32-bbbf44bde581" />

Configured a parameterized MySQL dataset in Azure Data Factory using @dataset().tablename expressions to enable metadata-driven ingestion of multiple HR tables without hardcoded values.


## Azure Blob Storage CSV Sink Dataset Configuration

<img width="1047" height="472" alt="Azure -2" src="https://github.com/user-attachments/assets/f014d13e-41eb-4dfc-b381-9c2800cfe7e4" />

Configured a parameterized CSV dataset in Azure Data Factory to dynamically generate output files in Azure Blob Storage using @dataset().fileName. This enables scalable ingestion of multiple HR tables into the raw-files container without hardcoded filenames.


## Dynamic Table Ingestion Using Lookup and ForEach Activities

<img width="1045" height="470" alt="Azure -3" src="https://github.com/user-attachments/assets/4814a2cc-d89c-4f48-aaca-c47117ecd193" />

Built a metadata-driven Azure Data Factory pipeline using Lookup and ForEach activities to dynamically iterate through all HR tables and trigger Copy Activities automatically. This design eliminates hardcoded ingestion logic and enables scalable onboarding of new tables.


## Azure Blob Storage Raw Layer for HR Data Ingestion

<img width="1047" height="470" alt="Azure -4" src="https://github.com/user-attachments/assets/61b79ca0-fd71-4c86-a0a2-21db2a9acc4d" />

Successfully ingested all 9 HR tables from MySQL into the raw-files container in Azure Blob Storage as CSV files. This raw landing layer acts as the centralized storage zone for downstream PySpark processing and transformation workflows.


## Parameterized PySpark Ingestion Notebook in Azure Databricks

<img width="1045" height="552" alt="Azure -5" src="https://github.com/user-attachments/assets/0d7b68ba-a58f-4307-8ed2-c3a4ca6a9a22" />

Developed a parameterized PySpark ingestion notebook in Azure Databricks using dbutils.widgets to dynamically receive source file names from Azure Data Factory. Shared configuration notebooks and reusable paths were implemented to standardize ingestion logic across all HR datasets.


## Dynamic Data Validation and Preview in Azure Databricks

<img width="1042" height="556" alt="Azure -6" src="https://github.com/user-attachments/assets/f0e7d2ae-1cae-44f8-8124-0e4ea18edea7" />

Implemented dynamic data validation and preview functionality in Azure Databricks to verify ingested HR datasets before transformation and downstream processing. Parameterized ingestion logic enables dynamic loading and inspection of multiple source files using reusable PySpark workflows, ensuring schema consistency and ingestion accuracy across all HR tables.


## Schema Enforcement and Structured CSV Ingestion Using PySpark

<img width="1046" height="587" alt="Azure -7" src="https://github.com/user-attachments/assets/91ac7b35-cf93-4b16-acfc-e75d28873b84" />

Implemented strict schema enforcement in Azure Databricks using PySpark StructType and StructField definitions to standardize HR dataset ingestion. Explicit data type mapping was applied before reading raw CSV files from Azure Blob Storage, ensuring consistent data quality, accurate column validation, and reliable downstream processing across the pipeline.


## Metadata-Driven Notebook Orchestration Using Azure Data Factory

<img width="1045" height="587" alt="Azure -8" src="https://github.com/user-attachments/assets/b9561020-b805-4420-87ca-814b6cec54f6" />

Implemented a metadata-driven orchestration pipeline in Azure Data Factory using Get Metadata and ForEach activities to dynamically process multiple HR datasets from Azure Blob Storage. The pipeline automatically discovers available source files and triggers parameterized Azure Databricks notebooks for scalable and automated ingestion workflows.


## Dynamic File Discovery Using Get Metadata Activity in Azure Data Factory

<img width="1045" height="502" alt="Azure -9" src="https://github.com/user-attachments/assets/9b4e7696-dcd3-4c02-bd95-f7d3514f2b2f" />

Configured the Get Metadata activity in Azure Data Factory to dynamically retrieve child items from Azure Blob Storage for automated file discovery and pipeline orchestration. This metadata-driven approach enables scalable ingestion by allowing the pipeline to automatically identify and process newly available HR dataset files without manual intervention.


## Dynamic Databricks Notebook Execution Using Parameterized ADF Pipelines

<img width="1047" height="467" alt="Azure -10" src="https://github.com/user-attachments/assets/4828163b-123f-4286-95fc-0301e3d8a55b" />

Implemented dynamic Azure Databricks notebook execution within Azure Data Factory using parameterized notebook paths and metadata-driven orchestration logic. The pipeline dynamically constructs notebook paths using @concat() expressions, enabling scalable and reusable processing for multiple HR datasets without hardcoded notebook references.


## Metadata-Driven Databricks Orchestration Using Azure Data Factory

<img width="1045" height="472" alt="Azure -11" src="https://github.com/user-attachments/assets/f3ff7b25-3370-4f50-a835-7f9fda7455dd" />

This pipeline uses Get Metadata and ForEach activities in Azure Data Factory to automatically run Databricks notebooks for multiple HR files. Notebook paths and file names are passed dynamically using parameters, removing the need for hardcoded values and making the pipeline fully automated.


## Successful End-to-End Notebook Execution in Azure Data Factory

<img width="1047" height="467" alt="Azure -12" src="https://github.com/user-attachments/assets/ec683e8a-da56-499c-86bc-5b631930ee73" />

This output shows the successful execution of the Azure Data Factory pipeline where multiple Databricks notebooks were triggered automatically using the ForEach activity. Each notebook processed HR dataset files successfully, confirming that the pipeline orchestration and dynamic execution flow are working correctly.


## Processed HR Data Stored in Azure Blob Storage

<img width="1045" height="467" alt="Azure -13" src="https://github.com/user-attachments/assets/a9ed395d-e04c-4a56-bd1c-f430933c7e7f" />

This container stores the processed HR datasets generated by Databricks after transformation. Each inc_* folder represents a cleaned and structured table written in incremental format, making the data ready for analytics, Synapse external tables, and Power BI reporting.


## External Tables Created in Azure Synapse Analytics

<img width="1045" height="467" alt="Azure -14" src="https://github.com/user-attachments/assets/41aef2ef-9546-4d43-9de3-de657b58af12" />

This notebook creates and registers external tables in the processedLakeDB database using PySpark in Azure Synapse Analytics. All processed HR datasets stored in Azure Blob Storage are linked as queryable tables, enabling direct SQL analysis and Power BI connectivity.


## Power BI Connected with Azure Synapse Serverless SQL Pool

<img width="1047" height="527" alt="Azure -15" src="https://github.com/user-attachments/assets/d27dc56d-1dc8-43b7-850a-d5328ef41751" />

Power BI is connected directly to Azure Synapse Serverless SQL Pool to load all processed HR tables from processedLakeDB. This setup allows analytics-ready data to be used for dashboard creation, reporting, and business insights.
















