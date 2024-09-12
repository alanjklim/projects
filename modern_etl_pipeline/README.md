# **Explanation**:
This diagram represents a data pipeline where:
1. Data is exported from a local database to **AWS RDS**.
2. **Fivetran** replicates data from RDS to **AWS S3 (raw data)**.
3. **Databricks** processes and transforms the raw data from S3 and writes the processed data back to **AWS S3 (processed data)**.
4. The processed data is then consumed by **BI tools, dashboards,** or **machine learning models**.

# Data Pipeline Architecture
```mermaid
graph TD;
    Kaggle_Dataset[Kaggle Dataset] -- Upload to RDS --> AWS_RDS;
    AWS_RDS -- Replicates Data --> Fivetran;
    Fivetran -- Syncs Raw Data --> AWS_S3_Raw;
    AWS_S3_Raw(AWS S3: Raw Data) -- Reads & Processes --> Databricks;
    Databricks -- Writes Processed Data --> AWS_S3_Processed;
    AWS_S3_Processed(AWS S3: Processed Data) -- Consumed by --> Data_Consumers;

    classDef awsColor fill:#3498DB,stroke:#333,stroke-width:2px;
    classDef fivetranColor fill:#F39C12,stroke:#333,stroke-width:2px;
    classDef generalColor fill:#2ECC71,stroke:#333,stroke-width:2px;

    Kaggle_Dataset(Kaggle Dataset):::generalColor;
    AWS_RDS(AWS RDS: PostgreSQL/MySQL):::awsColor;
    Fivetran(Fivetran: Data Replication):::fivetranColor;
    AWS_S3_Raw(AWS S3: Raw Data):::awsColor;
    Databricks(Databricks: Data Processing & Transformation):::awsColor;
    AWS_S3_Processed(AWS S3: Processed Data):::awsColor;
    Data_Consumers(BI Tools, Dashboards, ML Models):::generalColor;
