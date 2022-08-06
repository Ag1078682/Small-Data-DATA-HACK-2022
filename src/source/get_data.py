import json
import psycopg2
from src.log.log import log



def get_data():
    raw_data = connect()
    ##todo data enrichment
    data = enrich(raw_data)
    return data


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
    with open('src/params/query.json') as f:
        config = json.load(f)
        query = config["params"]["query"]
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    log("Fetch data from postgres source")
    return data


def enrich(raw_data):
    data = raw_data
    return data

