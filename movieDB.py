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

def InsertTableEmi(sialink, link, size, quality):
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()
    data = [sialink, link, size, quality]
    cur.execute('''INSERT INTO emi
                    (sialink, link, filesize, quality)
                    VALUES(?, ?, ?, ?);''', data)

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

def InsertTableCnamaSeries(download_link, link, quality, subtitle, hash, size, season, episode):
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()
    data = [download_link, link, quality, subtitle, hash, size, season, episode]
    cur.execute('''INSERT INTO cnama_series
                    (download_link, link, quality, subtitle, hash, size, season, episode)
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?);''', data)

    con.commit()
    con.close()

def InsertTableCnamaSeriesSkylink(skylink, link, quality, subtitle, hash, size, season, episode):
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()
    data = [skylink, link, quality, subtitle, hash, size, season, episode]
    cur.execute('''INSERT INTO cnama_series_skylink
                    (skylink, link, quality, subtitle, hash, size, season, episode)
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?);''', data)

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
    cur.execute('''INSERT INTO telegram
                    (download_link, description)
                    VALUES(?, ?);''', data)

    con.commit()
    con.close()

def DropTable():
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()

    cur.execute('DROP TABLE cnama_series')
    con.commit()
    con.close()


def selectTable():
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM cnama")

    rows = cur.fetchall()

    return rows

def selectSeriesTable():
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM cnama_series")

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
                    link VARCHAR(255),
                    filesize REAL,
                    quality varchar(32))'''


    cnama_movies_table_sql = '''CREATE TABLE IF NOT EXISTS cnama
                (
                    id INTEGER PRIMARY KEY,
                    download_link TEXT,
                    link VARCHAR(255))'''

    cnama_series_table_sql = '''CREATE TABLE IF NOT EXISTS cnama_series
                (
                    id INTEGER PRIMARY KEY,
                    download_link TEXT,
                    link VARCHAR(255),
                    quality VARCHAR(64),
                    subtitle TEXT,
                    hash VARCHAR(32),
                    size REAL,
                    episode INTEGER, 
                    season INTEGER
                )'''

    cnama_series_skylink_table_sql = '''CREATE TABLE IF NOT EXISTS cnama_series_skylink
                (
                    id INTEGER PRIMARY KEY,
                    skylink TEXT,
                    link VARCHAR(255),
                    quality VARCHAR(64),
                    subtitle TEXT,
                    hash VARCHAR(32),
                    size REAL,
                    episode VARCHAR(4), 
                    season VARCHAR(4)
                )'''
    telegram_table_sql = '''CREATE TABLE IF NOT EXISTS telegram
                ( 
                    id INTEGER PRIMARY KEY,
                    download_link TEXT,
                    description TEXT)'''
                
    
    conn = create_connection(database)

    if conn is not None:
        # create movies table
        create_table(conn, movies_table_sql)

        # create emi-movie table
        create_table(conn, emi_movies_table_sql)

        # create cnama-movies
        create_table(conn, cnama_movies_table_sql)

        create_table(conn, cnama_series_table_sql)

        # create table telegram
        create_table(conn,telegram_table_sql)

        # create cnama-skylink table
        create_table(conn, cnama_series_skylink_table_sql)

    else:
        print("Error! cannot create the database connection.")
    

if __name__ == "__main__":
    main()
    # DropTable()

    # for i in range(122, 123):
    #     delete_task(i)
