from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca
"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""
class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_biblioteche(self):
        #db = DBConnect()
        #connessione = db.get_connection()
        conn = DBConnect.get_connection()
        if conn is None:
            print("Errore: impossibile connettersi al database")
            return []
        biblioteche = []
        cursore = conn.cursor(dictionary=True)
        query = "SELECT * FROM biblioteca"
        cursore.execute(query)
        for riga in cursore:
            biblioteca = Biblioteca(id=int(riga['id']),
                                    nome=riga['nome'],
                                    indirizzo=riga['indirizzo']
                                    )
            biblioteche.append(biblioteca)
        cursore.close()
        conn.close()
        return biblioteche



