from database.DB_connect import DBConnect
from model.libro_DTO import Libro
"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""
class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def leggi_libro_db(self):
        db = DBConnect()
        connessione = db.get_connection()
        if connessione is None:
            print("Errore: impossibile connettersi al database")
            return []
        libri = []
        cursore = connessione.cursor(dictionary=True)
        query = "SELECT * FROM libro"
        cursore.execute(query)

        for riga in cursore:
            libro = Libro(id= int(riga['id']),
                          titolo = riga['titolo'],
                          autore = riga['autore'],
                          genere=riga['genere'],
                          anno_pubblicazione=riga['anno_pubblicazione'],
                          id_biblioteca=int(riga['id_biblioteca']))
            libri.append(libro)

        cursore.close()
        connessione.close()
        return libri

    def get_libri_filtrati(self, id_biblioteca, genere):
        db = DBConnect()
        connessione = db.get_connection()
        if connessione is None:
            print("Errore: impossibile connettersi al database")
            return []

        libri_filtrati = []
        cursore = connessione.cursor(dictionary=True)
        query = """ SELECT * FROM libro
                         WHERE (id_biblioteca = COALESCE(%s, id_biblioteca))
                         AND (genere = COALESCE(%s,genere)) """

        cursore.execute(query, (id_biblioteca, genere))
        for riga in cursore:
            libro = Libro(
                id=int(riga['id']),
                titolo=riga['titolo'],
                autore=riga['autore'],
                genere=riga['genere'],
                anno_pubblicazione=riga['anno_pubblicazione'],
                id_biblioteca=int(riga['id_biblioteca'])
            )
            libri_filtrati.append(libro)

        cursore.close()
        connessione.close()
        return libri_filtrati

    def get_generi(self):
        db = DBConnect()
        connessione = db.get_connection()
        if connessione is None:
            print("Errore: impossibile connettersi al database")
            return []
        generi = []
        cursore = connessione.cursor(dictionary=True)
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL"
        cursore.execute(query)
        for riga in cursore:
            generi.append(riga['genere'])
        cursore.close()
        connessione.close()
        return generi