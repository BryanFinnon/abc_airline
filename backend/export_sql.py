import sqlite3

con = sqlite3.connect('db.sqlite3')
with open("db_backup.sql", "w", encoding='utf-8') as f:
    for line in con.iterdump():
        f.write('%s\n' % line)
con.close()