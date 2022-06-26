import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
        :param db_file: database file
        :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def InsertTableEmi(sialink, link):
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()
    data = [sialink, link]
    cur.execute('''INSERT INTO emi
                    (sialink, link)
                    VALUES(?, ?);''', data)

    con.commit()
    con.close()

def InsertTableCnama(download_link, link):
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()
    data = [download_link, link]
    cur.execute('''INSERT INTO cnama
                    (download_link, link)
                    VALUES(?, ?);''', data)

    con.commit()
    con.close()

def InsertTableCnamaSeries(download_link, link):
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()
    data = [download_link, link]
    cur.execute('''INSERT INTO cnama_series
                    (download_link, link)
                    VALUES(?, ?);''', data)

    con.commit()
    con.close()


def InsertTable(title, duration, quality, imdb_rate, thumbnail, description, date_uploaded, uploaded_by, countries, directors, cast, generes):
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()
    data = [title, duration, quality, imdb_rate, thumbnail, description, date_uploaded, uploaded_by, countries, directors, cast, generes,]
    cur.execute('''INSERT INTO movies
                (title, duration, quality, imdb_rate, thumbnail, description, date_uploaded, uploaded_by, countries, directors, cast, generes) 
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', data)

    con.commit()
    con.close()

def InserTableFilimo(link, details):
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()
    data = [link, details]
    cur.execute('''INSERT INTO filimo_movies
                    (link, details)
                    VALUES(?, ?);''', data)

    con.commit()
    con.close()

def DropTable():
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()

    cur.execute('DROP TABLE emi_movies')
    con.commit()
    con.close()


def selectTable():
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM cnama")

    rows = cur.fetchall()

    return rows


def delete_task(id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    con = sqlite3.connect('fastmovie-online.db')
    sql = 'DELETE FROM cnama WHERE id=?'
    cur = con.cursor()
    cur.execute(sql, (id,))
    con.commit()

def main():
    database = 'fastmovie-online.db'
    movies_table_sql = '''CREATE TABLE IF NOT EXISTS movies
                (
                    id integer PRIMARY KEY, 
                    title VARCHAR(255),
                    duration VARCHAR(64) ,
                    quality VARCHAR(64),
                    release_date DATETIME,
                    imdb_rate VARCHAR(32),
                    favorite BOOL,
                    thumbnail VARCHAR(255),
                    description TEXT,
                    date_uploaded DATETIME,
                    uploaded_by INT,
                    countries VARCHAR(255),
                    directors VARCHAR(255),
                    cast VARCHAR(255),
                    generes VARCHAR(255))'''

    emi_movies_table_sql = '''CREATE TABLE IF NOT EXISTS emi
                (
                    id INTEGER PRIMARY KEY,
                    sialink VARCHAR(255),
                    link VARCHAR(255))'''


    cnama_movies_table_sql = '''CREATE TABLE IF NOT EXISTS cnama
                (
                    id INTEGER PRIMARY KEY,
                    download_link TEXT,
                    link VARCHAR(255))'''

    cnama_series_table_sql = '''CREATE TABLE IF NOT EXISTS cnama_series
                (
                    id INTEGER PRIMARY KEY,
                    download_link TEXT,
                    link VARCHAR(255))'''
    
    conn = create_connection(database)

    if conn is not None:
        # create movies table
        create_table(conn, movies_table_sql)

        # create emi-movie table
        create_table(conn, emi_movies_table_sql)

        # create cnama-movies
        create_table(conn, cnama_movies_table_sql)

        create_table(conn, cnama_series_table_sql)

    else:
        print("Error! cannot create the database connection.")
    

if __name__ == "__main__":
    main()
