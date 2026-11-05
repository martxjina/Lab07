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
        db = DBConnect()
        connessione = db.get_connection()
        if connessione is None:
            print("Errore: impossibile connettersi al database")
            return []
        biblioteche = []
        cursore = connessione.cursor(dictionary=True)
        query = "SELECT * FROM biblioteca"
        cursore.execute(query)
        for riga in cursore:
            biblioteca = Biblioteca(id=int(riga['id']),
                                    nome=riga['nome'])
            biblioteche.append(biblioteca)
        cursore.close()
        connessione.close()
        return biblioteche



