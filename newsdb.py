# "Database code" for the DB News.

import psycopg2

DBNAME = "news"

def test():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from authors;")
    result = c.fetchAll()
    db.close()
    return result
