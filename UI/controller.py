import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        biblioteche = self._model.get_biblioteche()
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(
                ft.dropdown.Option(text=b.nome, data=b)
            )

        generi = self._model.get_generi()
        for g in generi:
            if g is not None:
                self._view.dd_genere.options.append(
                    ft.dropdown.Option(text=str(g), data=g)
                )
        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def read_biblioteca(self, e):
        if e.control.value is None or e.control.value == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            for opt in self._view.dd_biblioteca.options:
                if opt.text == e.control.value:
                    self.biblioteca_selezionata = opt.data

    def read_genere(self, e):
        if e.control.value is None or e.control.value == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    # TODO
    def handle_cerca(self, e):
        self._view.txt_risultato.controls.clear()
        id_biblio = None
        if self.biblioteca_selezionata is not None:
            id_biblio = self.biblioteca_selezionata.id

        libri = self._model.get_libri_filtrati(id_biblio, self.genere_selezionato)

        if len(libri) == 0:
            self._view.txt_risultato.controls.append(
                ft.Text("Nessun libro trovato con i filtri selezionati.")
            )
        else:
            for libro in libri:
                self._view.txt_risultato.controls.append(
                    ft.Text(f"{libro.titolo} - {libro.autore} ({libro.genere})")
                )
        self._view.update()
