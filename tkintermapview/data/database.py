import sqlite3
import datetime


class LatLong():
    def __init__(self, lat:str, long:str):
        self.lat=lat
        self.long=long


class SqliteClient():
    def __init__(self, version:int):
        self.version=version
        self.conn=sqlite3.connect("database.db")
        self.cursor=self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS coordinates (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        lat REAL,
                        long REAL
                    )""")
        
        if self.version==1:
        
            #1 Forma de insertar datos
            self.cursor.execute("INSERT INTO coordinates (lat, long) VALUES (38.01549,-1.16946)")
            self.cursor.execute("INSERT INTO coordinates (lat, long) VALUES (37.99246,-1.12863)")
            self.cursor.execute("INSERT INTO coordinates (lat, long) VALUES (37.9236,-1.1106)")

            self.conn.commit()
          
            """
            #2 forma de insertar datos
            latLong1=LatLong("coco","coco.png")
            latLong2=LatLong("pop","popo.png")
            latLong3=LatLong("kikin","kikin.png")
            self.cursor.execute("INSERT INTO coordinates (lat, long) VALUES (?,?)", (latLong1.lat, latLong1.long))
            self.cursor.execute("INSERT INTO coordinates (lat, long) VALUES (?,?)", (latLong2.lat, latLong2.long))
            self.cursor.execute("INSERT INTO coordinates (lat, long) VALUES (?,?)", (latLong3.lat, latLong3.long))
            """
            """
            #3 Forma de insertar datos
            image_File1=LatLong("coco","coco.png")
            image_File2=LatLong("pop","popo.png")
            image_File3=LatLong("kikin","kikin.png")
            self.cursor.execute("INSERT INTO coordinates (lat, long) VALUES (:name,:date,:path_image_file)", {
                "name":image_File1.name, 
                "date":image_File1.date,
                "path_image_file":image_File1.path_image_file
                }
            )
            self.cursor.execute("INSERT INTO coordinates (lat, long) VALUES (:lat,:long)", {
                "lat":image_File2.name,
                "date":image_File2.date, 
                "path_image_file":image_File2.path_image_file
                }
            )
            self.cursor.execute("INSERT INTO coordinates (lat, long) VALUES (:name,:date,:path_image_file)", {
                "name":image_File3.name, 
                "date":image_File3.date,
                "path_image_file":image_File3.path_image_file
                }
            )

            """

            """
            #4 Forma de insertar datos
            many_coordinates=[
                ("coco","10/10/2020","coco.png"),
                ("pop","01/01/2024","popo.png"),
                ("kikin","21/01/2023","kikin.png")
            ]
        
            self.cursor.executemany("INSERT INTO coordinates (name, date, path_image_file) VALUES (:name, :date, :path_image_file)", many_coordinates )
            """


    def close(self):
        self.conn.close()
    def insert(self, lat:float, long:float):
        #latLong=LatLong(lat, long)
        self.cursor.execute("INSERT INTO coordinates (lat, long) VALUES (?, ?)", (lat, long))
        self.conn.commit()

    def getAll(self):
        self.cursor.execute("SELECT * FROM coordinates")
        return self.cursor.fetchall()
        #fechone regresa solo un registro
        #print(c.fetchone())
        #fechmany regresa varios registros
        #print(c.fetchmany(2))
        #fechall regresa todos los registros
        #print(c.fetchall())
    def getName(self, name:str):
        self.cursor.execute("SELECT * FROM coordinates WHERE name = ?", (name,))
        return self.cursor.fetchone()   
    def getById(self, id:int):
        self.cursor.execute("SELECT * FROM coordinates WHERE id = ?", (id,))
        return self.cursor.fetchone()
    def delete(self, id:int):
        self.cursor.execute("DELETE FROM coordinates WHERE id = ?", (id,))
        self.conn.commit()
    def check_exists_by_name(self, name:str):
        self.cursor.execute("SELECT * FROM coordinates WHERE name = ?", (name,))
        if self.cursor.fetchone():
            return True
        else:
            return False
    def check_exists_by_id(self, id:int):
        self.cursor.execute("SELECT * FROM coordinates WHERE id = ?", (id,))
        if self.cursor.fetchone():
            return True
        else:
            return False
        
    