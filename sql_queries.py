# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays (
songplay_id SERIAL PRIMARY KEY,
start_time bigint,
user_id text,
level text,
song_id TEXT,
artist_id TEXT,
session_id int,
location text,
user_agent text
);

CREATE SEQUENCE songplay_id_seq;

ALTER SEQUENCE songplay_id_seq
OWNED BY songplays.songplay_id;
""")

user_table_create = ("""CREATE TABLE users (
user_id text PRIMARY KEY,
first_name text,
last_name text,
gender text,
level text
);
""")

song_table_create = ("""CREATE TABLE songs (
song_id text PRIMARY KEY,
title text,
artist_id text NOT NULL,
year int,
duration decimal
);
""")

artist_table_create = ("""CREATE TABLE artists (
artist_id text PRIMARY KEY,
name text,
location text,
latitude text,
longitude text
);
""")

time_table_create = ("""CREATE TABLE time (
start_time timestamp PRIMARY KEY,
hour int,
day int,
week int,
month int,
year int,
weekday int
);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING;
""")

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""SELECT song_id, artist_id FROM songs s JOIN artists a USING (artist_id) WHERE title = %s AND name = %s AND duration = %s;
""")

# Drop/Create Database

database_drop = "DROP DATABASE IF EXISTS sparkifydb"
database_create = "CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0"

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]