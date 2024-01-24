from pyspark.sql import SparkSession
# Create a new SparkSession
spark = SparkSession.builder.getOrCreate()
# Sample clickstream counts
sample_clickstream_counts = [
    ["other-search", "Hanging_Gardens_of_Babylon", "external", 47000],
    ["other-empty", "Hanging_Gardens_of_Babylon", "external", 34600],
    ["Wonders_of_the_World", "Hanging_Gardens_of_Babylon", "link", 14000],
    ["Babylon", "Hanging_Gardens_of_Babylon", "link", 2500]
]

# Create RDD from sample data
clickstream_counts_rdd = spark.sparkContext.parallelize(sample_clickstream_counts)
# Create a DataFrame from the RDD of sample clickstream counts
clickstream_sample_df = clickstream_counts_rdd.toDF()

# Display the DataFrame to the notebook
clickstream_sample_df.show(5)
# Read the target directory (`./cleaned/clickstream/`) into a DataFrame (`clickstream`)
clickstream = spark.read.option('header', True)\
.option('delimiter','\t')\
.option('inferSchema',True)\
.csv('./cleaned/clickstream/')

# Display the DataFrame to the notebook
clickstream.show(5)
# Display the schema of the `clickstream` DataFrame to the notebook
clickstream.printSchema()
# Drop target columns
clickstream = clickstream.drop("language_code")

# Display the first few rows of the DataFrame
clickstream.show(5)
# Display the new schema in the notebook
clickstream.printSchema()
# Rename `referrer` and `resource` to `source_page` and `target_page`
clickstream = clickstream.withColumnRenamed('referrer', 'source_page')
clickstream = clickstream.withColumnRenamed('resource', 'target_page')
# Display the first few rows of the DataFrame
clickstream.show(5)
# Display the new schema in the notebook
clickstream.printSchema()
# Create a temporary view in the metadata for this `SparkSession` 
clickstream.createOrReplaceTempView('clickstream')
# Filter and sort the DataFrame using PySpark DataFrame methods
clickstream = clickstream.filter(clickstream['target_page'] == 'Hanging_Gardens_of_Babylon')
clickstream = clickstream.orderBy(clickstream['click_count'])
# Filter and sort the DataFrame using SQL
clickstream = spark.sql("SELECT * FROM clickstream WHERE target_page = 'Hanging_Gardens_of_Babylon'")
clickstream = spark.sql("SELECT * FROM clickstream ORDER BY click_count ASC")
# Aggregate the DataFrame using PySpark DataFrame Methods 
click_count = clickstream.groupBy("link_category").sum("click_count").alias("total_click_count")
# Aggregate the DataFrame using SQL
click_count = spark.sql("""
SELECT link_category, SUM(click_count) AS total_click_count
FROM clickstream
GROUP BY link_category
""")
# Create a new DataFrame named `internal_clickstream`
internal_clickstream = clickstream.filter(clickstream['link_category'] == 'link').select('source_page', 'target_page', 'click_count')

# Display the first few rows of the DataFrame in the notebook
internal_clickstream.show(5)
# Save the `internal_clickstream` DataFrame to a series of CSV files
internal_clickstream.write.csv('./results/article_to_article_csv/', header=True)
# Save the `internal_clickstream` DataFrame to a series of parquet files
internal_clickstream.write.parquet('./results/article_to_article_pq/')
# Stop the notebook's `SparkSession` and `SparkContext`
spark.stop()