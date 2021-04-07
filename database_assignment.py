import sqlite3 #imports sqlite3

conn = sqlite3.connect('test3.db') #creates and accesses test3 database

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_files TEXT)") #creates table within test3.db with one column
    conn.commit() #commits command

conn = sqlite3.connect('test3.db')

fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg')

for x in fileList: #loops through each object within the tuple to find any that end with '.txt'
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        #connects tuple to tbl_files and the specific column
        # creates a one element tuple for each document ending with '.txt'
            cur.execute("INSERT INTO tbl_files (col_files) VALUES (?)", (x,))
            print(x)
conn.close()

