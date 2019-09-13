import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries, copy_table_queries, insert_table_queries
import argparse

def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()
        
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    parser = argparse.ArgumentParser(description='Sparkify extract, transform, load program')
    parser.add_argument("--drop", help="Specify --drop 1 if you want to drop tables first")
    args = parser.parse_args()
    
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    if args.drop:
        print("Dropping tables first")
        drop_tables(cur, conn)
    
    print("Create tables")
    create_tables(cur, conn)
    
    print("Load staging tables")
    load_staging_tables(cur, conn)
    
    #Check how many elements in staging tables
    cur.execute("SELECT COUNT(*) FROM staging_events")
    conn.commit()
    print("We now have ", cur.fetchone()[0], " elements in staging_events table")
    
    cur.execute("SELECT COUNT(*) FROM staging_songs")
    conn.commit()
    print("We now have ", cur.fetchone()[0], " elements in staging_songs table")
    
    print("Inert into facts and dimension tables")
    insert_tables(cur, conn)
    
    #Check how many elements in facts and dimension tables
    cur.execute("SELECT COUNT(*) FROM songplay_table")
    conn.commit()
    print("We now have ", cur.fetchone()[0], " elements in songplay_table")
    
    cur.execute("SELECT COUNT(*) FROM user_table")
    conn.commit()
    print("We now have ", cur.fetchone()[0], " elements in user_table table")
    
    cur.execute("SELECT COUNT(*) FROM song_table")
    conn.commit()
    print("We now have ", cur.fetchone()[0], " elements in song_table table")
    
    cur.execute("SELECT COUNT(*) FROM artist_table")
    conn.commit()
    print("We now have ", cur.fetchone()[0], " elements in artist_table table")
    
    cur.execute("SELECT COUNT(*) FROM time_table")
    conn.commit()
    print("We now have ", cur.fetchone()[0], " elements in time_table table")

    conn.close()


if __name__ == "__main__":
    main()