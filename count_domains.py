import sqlite3

conn=sqlite3.connect('counts_domains.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT,count INTEGER )')

fname=input("Enter the name of the file:")
if len(fname)<1: fname='mbox.txt'
fhand=open(fname)

for line in fhand:
    if not line.startswith('From: '):continue
    linelist=line.split()
    email=linelist[1].split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?',(email,))
    count_col=cur.fetchone()
    if count_col is None:
        cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(email,))
    else:
        cur.execute('UPDATE Counts SET count=count + 1 WHERE org = ?',(email,))
conn.commit()

selcomm='SELECT org, count FROM Counts ORDER BY count'
for row in cur.execute(selcomm):
    print(str(row[0]),row[1])
cur.close()

