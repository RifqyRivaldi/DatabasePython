#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector 

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Create a new database named D3_TI_2023
cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[2]:


import mysql.connector 

# Hubungkan ke database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="D3_TI_2023"
)

# 
cursorObject = dataBase.cursor()

# Buat Table Mahasiswa
cursorObject.execute("CREATE TABLE Mahasiswa (    NIM VARCHAR(10) PRIMARY KEY,     Nama VARCHAR(30),     Alamat VARCHAR(255),     Matkul VARCHAR(10),     Jurusan VARCHAR(25) )")

# Buat Table Dosen
cursorObject.execute("CREATE TABLE Dosen (    NIP VARCHAR(20) PRIMARY KEY,     Nama_Dosen VARCHAR(50),     Matkul VARCHAR(50),     Umur INT(3) )")

# Buat Table Matkul
cursorObject.execute("CREATE TABLE MataKuliah (    Kode_Matkul VARCHAR(10) PRIMARY KEY,     Nama_Matkul VARCHAR(50),     Waktu DATE,     Ruangan VARCHAR(10),     Jurusan VARCHAR(25) )")

# Close the cursor and database connection
cursorObject.close()
dataBase.close()


# In[3]:


import mysql.connector 

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="D3_TI_2023"
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Insert data into Mahasiswa table
sql = "INSERT INTO mahasiswa (NIM, Nama, Alamat, Matkul, Jurusan) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('V3922040', 'Rifqy Rivaldi', 'Jl. Imam Bonjol No. 27', 'MK1', 'TI'),
    ('V3922012', 'Deninda Karunia Putri', 'Jl. Kenangan No. 2', 'MK1', 'SH'),
    ('V3922013', 'Aziz Gagab', 'Jl. Kenangan No. 22', 'MK1', 'SH'),
    ('V3922055', 'Wahyu Rahos', 'Jl. Gajah  No. 40', 'MK3', 'TI'),
    ('V3922066', 'Valdi', 'Jl. Blimbing No. 90', 'MK2', 'SI')
]

cursorObject.executemany(sql, val)

# Commit changes to the database
dataBase.commit()

# Close the cursor and database connection
cursorObject.close()
dataBase.close()


# In[4]:


import mysql.connector 

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="D3_TI_2023"
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Insert data into Mahasiswa table
sql = "INSERT INTO Dosen (NIP, Nama_Dosen, Matkul, Umur) VALUES (%s, %s, %s, %s)"
val = [
    ('A39797899', 'Bambang Marsudi', 'MK2', 80),
    ('A39797890', 'Langgeng Albani', 'MK1', 60),
    ('A39797880', 'Basuki Cahya', 'MK1', 40),
    ('A39797870', 'Muhammad Mudin', 'MK4', 70),
    ('A39797850', 'Charlie Garcia', 'MK5', 38)
]

cursorObject.executemany(sql, val)

# Commit changes to the database
dataBase.commit()

# Close the cursor and database connection
cursorObject.close()
dataBase.close()


# In[7]:


import mysql.connector 

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="D3_TI_2023"
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Insert data into Mahasiswa table
sql = "INSERT INTO mataKuliah (Kode_Matkul, Nama_Matkul, Waktu, Ruangan, Jurusan) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('MK5', 'Statiktika', '2023-01-01', 'A303', 'TI'),
    ('MK4', 'Basis Data', '2023-01-02', 'B304', 'SH'),
    ('MK3', 'Pemrograman Web', '2023-01-03', 'N402', 'SH'),
    ('MK2', 'Wirelles ', '2023-08-04', 'B267', 'TI'),
    ('MK1', 'Pemrograman Python', '2023-01-05', 'B105', 'S1')
]

cursorObject.executemany(sql, val)

# Commit changes to the database
dataBase.commit()

# Close the cursor and database connection
cursorObject.close()
dataBase.close()


# In[8]:


import mysql.connector 

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="D3_TI_2023"
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Execute the SELECT query
sql = "SELECT Mahasiswa.NIM, Mahasiswa.Nama, MataKuliah.Nama_Matkul, Dosen.Nama_Dosen        FROM Mahasiswa        JOIN MataKuliah ON Mahasiswa.Matkul = MataKuliah.Kode_Matkul        JOIN Dosen ON MataKuliah.Kode_Matkul = Dosen.Matkul"

cursorObject.execute(sql)

# Fetch all the rows
result = cursorObject.fetchall()

# Print the result
for row in result:
    print("---------------------------")
    print("NIM             : ", row[0])
    print("NAMA            : ", row[1])
    print("MataKuliah      : ", row[2])
    print("Dosen Pengajar  : ", row[3])
    print("---------------------------")

# Close the cursor and database connection
cursorObject.close()
dataBase.close()


# In[ ]:




