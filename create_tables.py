import psycopg2
from sql_queries import create_table_queries, database_drop, database_create, drop_table_queries


def create_database():
    """This procedure establishs connection to default database. It then drops/creates a database.

    Returns:
        The cursor and connection variables.
    """
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute(database_drop)
    cur.execute(database_create)

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """This procedure drops tables from the database.

    Args:
        cur: the cursor variable
        conn: the connection variable
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """This procedure creates tables in the database.

    Args:
        cur: the cursor variable
        conn: the connection variable
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """This procedure calls the database drop/create functions."""
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()