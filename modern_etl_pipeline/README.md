# Modern Data Pipeline
This project demonstrates a data pipeline using **AWS RDS**, **Fivetran**, **Databricks**, **dbt**, and **Apache Iceberg**. The pipeline includes batch processing of synthetic data and real-time streaming with **AWS Kinesis** as a placeholder.

# Architecture Overview
1. **Synthetic Data**: Generate synthetic data using Python in CSV format.
2. **AWS RDS**: Load dataset into **PostgreSQL**.
3. **Fivetran**: Replicate data from AWS RDS to **AWS S3** (raw data) in real-time.
4. **Databricks**: Process the raw data using **Databricks**, perform transformations, and write the processed data back to S3 via **Apache Iceberg** (for schema evolution and partitioning).
5. **dbt**: Transform the processed data in S3 to apply business logic, clean, and aggregate data for consumption.
6. **AWS Kinesis (placeholder)**: Stream real-time data into Databricks via **AWS Kinesis**, process it, and store the results in **AWS S3** for real-time consumption.

# Data Flow
```mermaid
graph TD;
    Synthetic_Data[Synthetic Data] -- Insert into RDS --> AWS_RDS;
    AWS_RDS -- Replicates Data --> Fivetran;
    Fivetran -- Syncs Raw Data --> AWS_S3_Raw;
    AWS_S3_Raw(AWS S3: Raw Data) -- Reads & Processes --> Databricks;
    Databricks -- Writes Processed Data (via Iceberg) --> AWS_S3_Processed;
    AWS_S3_Processed(AWS S3: Processed Data via Iceberg) -- Optionally Loaded into --> Redshift;
    Redshift(Redshift: Data Warehouse) -- Transformed by --> dbt;
    dbt -- Applies Business Logic & Aggregates --> AWS_S3_Final;
    AWS_S3_Final(AWS S3: Final Data for Consumption) -- Consumed by --> Data_Consumers;

    Source(Data Source: Placeholder) -- Ingest Data --> Kinesis;
    Kinesis(Kinesis Data Streams) -- Streams Real-Time Data --> Databricks;
    Databricks -- Processes Real-Time Data --> AWS_S3_RealTime;
    AWS_S3_RealTime(AWS S3: Real-Time Processed Data) -- Consumed by --> Data_Consumers;

    classDef awsColor fill:#3498DB,stroke:#333,stroke-width:2px;
    classDef fivetranColor fill:#F39C12,stroke:#333,stroke-width:2px;
    classDef dbtColor fill:#F85C50,stroke:#333,stroke-width:2px;
    classDef generalColor fill:#2ECC71,stroke:#333,stroke-width:2px;

    Synthetic_Data(Synthetic Data):::generalColor;
    AWS_RDS(AWS RDS: PostgreSQL):::awsColor;
    Fivetran(Fivetran: Data Replication):::fivetranColor;
    AWS_S3_Raw(AWS S3: Raw Data):::awsColor;
    Databricks(Databricks: Data Processing & Transformation with Iceberg):::awsColor;
    AWS_S3_Processed(AWS S3: Processed Data via Iceberg):::awsColor;
    Redshift(Redshift: Data Warehouse):::awsColor;
    dbt(dbt: Data Transformation):::dbtColor;
    AWS_S3_Final(AWS S3: Final Data for Consumption):::awsColor;
    AWS_S3_RealTime(AWS S3: Real-Time Processed Data):::awsColor;
    Kinesis(Kinesis Data Streams):::awsColor;
    Data_Consumers(Business, BI Tools, ML Models):::generalColor;
```

# Setup Instructions
## Step 1: Generate Synthetic Data
1. Install dependencies ```pip install faker pandas```
2. Run ```generate.py``` to generate CSV files
## Step 2: Set Up AWS RDS
1. Create a PostgreSQL RDS instance.
2. Ensure public access and configure security groups for inbound connections on port 5432.
3. Load CSV data into RDS using psql or a database client.
## Step 3: Set Up Fivetran
1. Sign up for Fivetran and create a PostgreSQL connector.
2. Enter RDS credentials (hostname, username, password) and connect Fivetran.
3. Set up an S3 bucket as the destination and configure sync frequency.
