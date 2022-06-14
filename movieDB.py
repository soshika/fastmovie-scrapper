import sqlite3

def CreateTable():
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS movies
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
                    generes VARCHAR(255))''')
    con.commit()
    con.close()


def CreateTableFilimo():
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS filimo_movies
                (
                    id INTEGER PRIMARY KEY,
                    title VARCHAR(255),
                    is_movie BOOL,
                    quality varchar(32),
                    season integer,
                    episode integer,
                    generes VARCHAR(64))''')
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

def DropTable():
    con = sqlite3.connect('fastmovie-online.db')
    cur = con.cursor()

    cur.execute('DROP TABLE movies')
    con.commit()
    con.close()

if __name__ == "__main__":
    # CreateTable()
    # DropTable()
    CreateTableFilimo()