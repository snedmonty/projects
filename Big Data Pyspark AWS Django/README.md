# Big Data 

 Many of Amazon's shoppers depend on product reviews to make a purchase. Amazon makes these datasets publicly available. However, they are quite large and can exceed the capacity of local machines to handle. One dataset alone contains over 1.5 million rows; with over 40 datasets, this can be quite taxing on the average local computer. 

## AWS
Follow code to see how to  perform the ETL process completely in the cloud and upload a DataFrame to an RDS instance. The second goal will be to use PySpark or SQL to perform a statistical analysis of selected data.

Create DataFrames to match production-ready tables from two big Amazon customer review datasets.
Analyze whether reviews from Amazon's Vine program are trustworthy.


### Use the furnished schemata to create tables in your RDS database.

### Create two separate ZEPL notebooks and extract any two datasets from the list at review dataset, one into each notebook.

Note: It is possible to ETL both data sources in a single notebook, but due to the large data sizes, it will be easier to work with these S3 data sources in two separate ZEPL notebooks.

Be sure to handle the header correctly. If you read the file without the header parameter, you may find that the column headers are included in the table rows.

## PySpark
### Count the number of records (rows) in the dataset.

### Transform the dataset to fit the tables in the schema file. Be sure the DataFrames match in data type and in column name.

### Load the DataFrames that correspond to tables into an RDS instance.