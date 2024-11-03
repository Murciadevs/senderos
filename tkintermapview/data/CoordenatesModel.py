from data.SqliteClient import SqliteClient


class Coordenate():
    def __init__(self, lat:float, long:float):
        self.lat=lat
        self.long=long


class CoordenatesModel(SqliteClient):
    def __init__(self, version:int):
        super().__init__(version)

    def insert(self, lat:float, long:float, id_route:int):
        # latLong=LatLong(lat, long)
        self.cursor.execute("INSERT INTO coordinates (lat, long, id_route) VALUES (?, ?, ?)", (lat, long, id_route))
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
    def getByIdRoute(self, id_route:int):
        self.cursor.execute("SELECT * FROM coordinates WHERE id_route = ?", (id_route,))
        return self.cursor.fetchall()
    def delete(self, id:int):
        self.cursor.execute("DELETE FROM coordinates WHERE id = ?", (id,))
        self.conn.commit()
    def deleteByRouteId(self, id_route:int):
        self.cursor.execute("DELETE FROM coordinates WHERE id_route = ?", (id_route,))
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
        
    