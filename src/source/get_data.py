import json
import psycopg2
from src.log.log import log



def get_data():
    ##ToDo
    ## the raw_data here comes from postgres
    ## actually, here should be a fork (function) to get it from any source
    raw_data = connect()
    ##ToDo
    ## after getting raw data it should actually go into pandas, so that it can be already standardized
    ## types of data should be converted if necessary
    ## and data enrichment by metainfo should be done here
    ## +
    ## the reason is
    ## if we collect raw data from several sources than we cannot guarantee that
    ## 1) datatypes from those sources are the same
    ## 2) datatypes haven't changed since last time
    ## 3) we have those whatever types in our raw_data DB
    ## so, shouldn't they be explicitly converted?
    ## or should we create a table for every portion of raw_data
    ## and write _everything_ as text?
    data = enrich(raw_data)
    return raw_data


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # get config
        with open('src/params/query.json') as f:
            config = json.load(f)
            connection_params = config["source_database"]["connection_params"]

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host=connection_params["host"],
            port=connection_params["port"],
            database=connection_params["database"],
            user=connection_params["user"],
            password=connection_params["password"])

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        #execute select based on query metadata and params
        data = select(cur)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    return data



def select(cursor):
    ##ToDo:
    ## a function to get right set of data from tables based on recorded metadata
    ## here the query string is hardcoded in params, but it should be generated based on metadata
    with open('src/params/query.json') as f:
        config = json.load(f)
        query = config["params"]["query"]
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    log("Fetch data from postgres source")
    return data


def enrich(raw_data):
    ##ToDo:
    ## a function to enrich data by meta information
    ## (query_id, transaction_id, time_of_query, source)
    data = raw_data
    return data

