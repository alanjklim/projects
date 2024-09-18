i have a few questions:
fivetran - can this tool do data transformations? what do you mean by fivetran manages the pipeline and schema changes automatically, please give example. so the purpose hear is that is replicates source data?

databricks - what does it mean by processing raw data into raw data layer? im tring to visualise how databricks work. is it a container around aws or the other way around? can databricks store Transformed Data Layer like a datawarehouse? what is the purpose of using databricks here?

am i correct is saying that the flow looks like this:
fivetran (data replication from source) >
aws s3 raw data storage >
databricks - unsure what this does from s3
dbt - staging the data? >
redshift - clean data >
data consumers - use data


fivetran - if a schema change is detected, what behaviour is done to the history if a column is added for example? also explain other scenarios where schema changes occur and how fivetran deal with this? is it possible to connect from local db on postgres? i do not have a online source database.

when data is replcated by fivetran, does it overwrite the s3 data? what do companies typically do here? do hey ingest and store data daily in partitions? plese also explain if the process is the same for databricks where processing it stored daily in partitions.

please clarify this part year=2024/month=09/day=12/, is data replication occuring at intervals and appends using delta and batch?

what is iceburg?

still confused, is iceburg a better replacement for s3? using mermaid, draw me a system design where iceburg is used.
what is the difference between data lake and data warehouse?
what is flink?

what is the dfference between a database like orace, sql server, postgres and data warehouse then? 
what kind of processing does databricks do? give examples and use case


# rds connections
endpoint: bank-postgres-db.c56o0miocxo2.ap-southeast-2.rds.amazonaws.com
username: postgres
password: 14170793
port: 5432

# fivetran policy json
{
    "Version": "2012-10-17",
    "Statement": [
        {
          "Sid": "SetupFormTest",
          "Effect": "Allow",
          "Action": [
              "glue:DeleteDatabase"
           ],
           "Resource": [
               "arn:aws:glue:ap-southeast-2:534455458037:database/fivetran*",
               "arn:aws:glue:ap-southeast-2:534455458037:catalog",
               "arn:aws:glue:ap-southeast-2:534455458037:table/fivetran*/*",
               "arn:aws:glue:ap-southeast-2:534455458037:userDefinedFunction/fivetran*/*"
           ]
       },
       {
          "Sid": "AllConnectors",
          "Effect": "Allow",
          "Action": [
              "glue:GetDatabase",
              "glue:UpdateDatabase",
              "glue:CreateTable",
              "glue:GetTables",
              "glue:CreateDatabase",
              "glue:UpdateTable",
              "glue:BatchDeleteTable",
              "glue:DeleteTable",
              "glue:GetTable"
           ],
           "Resource": [
               "arn:aws:glue:ap-southeast-2:534455458037:*"
           ]
       }
    ]
}

