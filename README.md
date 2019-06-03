# data-model-postgres

Our startup called Sparkify wants to analyze the data we've been collecting on songs and user activity on our new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As data engineers, we've been tasked to create a Postgres database with tables designed to optimize queries on song play analysis. This project will create a database schema and ETL pipeline for this analysis. We'll be enabled to test our database and ETL pipeline by running queries given to us by the analytics team and compare our results with their expected results.
Project Description

In this project, we'll apply data modeling with Postgres and build an ETL pipeline using Python. Our first task was to define fact and dimension tables for a star schema for a particular analytic focus. We then wrote an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

# Song Dataset

The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

```
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
```

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

`{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}`

# Log Dataset

The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

The log files in the dataset we'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.

```
log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json
```

# Star Schema

The star schema is the simplest style of data mart schema and is the approach most widely used to develop data warehouses and dimensional data marts. The star schema consists of one or more fact tables referencing any number of dimension tables. The star schema is an important special case of the snowflake schema, and is more effective for handling simpler queries. The star schema separates business process data into facts, which hold the measurable, quantitative data about a business, and dimensions which are descriptive attributes related to fact data. (Wikipedia)

Here is an example query and results used for song play analysis:

`SELECT * FROM songplays LIMIT 5;`

```
songplay_id 	start_time 	user_id 	level 	song_id 	artist_id 	session_id 	location 	user_agent
0 	1542845032796 	15 	paid 	None 	None 	818 	Chicago-Naperville-Elgin, IL-IN-WI 	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36"
1 	1542845350796 	15 	paid 	None 	None 	818 	Chicago-Naperville-Elgin, IL-IN-WI 	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36"
2 	1542845526796 	15 	paid 	None 	None 	818 	Chicago-Naperville-Elgin, IL-IN-WI 	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36"
3 	1542845741796 	15 	paid 	None 	None 	818 	Chicago-Naperville-Elgin, IL-IN-WI 	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36"
4 	1542846220796 	15 	paid 	None 	None 	818 	Chicago-Naperville-Elgin, IL-IN-WI 	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36"
```

1. Run `create_tables.py` to create your database and tables.

2. Run `test.ipynb` to confirm the creation of your tables with the correct columns.

3. Run `etl.py` to process the entire datasets.
