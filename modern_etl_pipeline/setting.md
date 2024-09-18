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