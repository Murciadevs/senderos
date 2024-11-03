from data.SqliteClient import SqliteClient


class Route():
    def __init__(self, name:str):
        self.name=name
        


class RoutesModel(SqliteClient):
    def __init__(self, version:int):
        super().__init__(version)


    def insert(self, name:str):
        # latLong=LatLong(lat, long)
        self.cursor.execute("INSERT INTO routes (name) VALUES (?)", (name,))
        self.conn.commit()

    def getAll(self):
        self.cursor.execute("SELECT * FROM routes")
        return self.cursor.fetchall()
        #fechone regresa solo un registro
        #print(c.fetchone())
        #fechmany regresa varios registros
        #print(c.fetchmany(2))
        #fechall regresa todos los registros
        #print(c.fetchall())
    def getName(self, name:str):
        self.cursor.execute("SELECT * FROM routes WHERE name = ?", (name,))
        return self.cursor.fetchone()   
    def getById(self, id:int):
        self.cursor.execute("SELECT * FROM routes WHERE id = ?", (id,))
        return self.cursor.fetchone()
    def getByName(self, name:str):
        self.cursor.execute("SELECT * FROM routes WHERE name= ?", (name,))
        return self.cursor.fetchone()
    def delete(self, id:int):
        self.cursor.execute("DELETE FROM routes WHERE id = ?", (id,))
        self.conn.commit()
    def check_exists_by_name(self, name:str):
        self.cursor.execute("SELECT * FROM routes WHERE name = ?", (name,))
        if self.cursor.fetchone():
            return True
        else:
            return False
    def check_exists_by_id(self, id:int):
        self.cursor.execute("SELECT * FROM routes WHERE id = ?", (id,))
        if self.cursor.fetchone():
            return True
        else:
            return False
        
    