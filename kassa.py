print('importeren..')

class Kassabon:
    def __init__(self):
        self.totaal = 0.0
        self.klantnummer = 1
        self.boodschappen = []


import tkinter as tk
from functools import reduce
versie = 'Alpha 3'
subtotaal = ''
klantnummer = 1
kassabon = Kassabon()

print('klaar!')
print('kassa versie ' + versie)
#START#


class Product:
    def __init__(self, prijs, naam):
        self.prijs = prijs
        self.naam = naam


producten = {}
producten['7584185114255'] = Product(0.95, "zakgeldpotje")
producten['9789054516200'] = Product(100.01, "Des vacanses mouvementees")
producten['9789001887292'] = Product(25.0, "Het verraad van WaterDunen - Rob Ruggenberg")


def product_opzoeken(barcode):
    return producten[barcode]


def werkbonbij():
    totaalLabel.configure(text=totaalveldtekst())

def add(event):
    erbij = product_opzoeken(barcodeVeld.get())

    kassabon.boodschappen.append(erbij)
    kassabon.totaal = kassabon.totaal + erbij.prijs
    barcodeVeld.delete(0, 'end')

    werkbonbij()


def totaalveldtekst():
    bonregels = ['EUR {:5,.2f} {:s}'.format(x.prijs, x.naam) for x in kassabon.boodschappen]
    bontekst = reduce(lambda x, y: x + "\n" + y, bonregels, "")
    return 'totaal: EUR {:5,.2f}'.format(kassabon.totaal) + '\n\n' + bontekst

def nieuweKlant():
    kassabon.totaal = 0.0
    kassabon.klantnummer = kassabon.klantnummer + 1
    kassabon.boodschappen = []
    werkbonbij()
    print('klantnummer: ' + str(kassabon.klantnummer))


scherm = tk.Tk()
scherm.title('kassasysteem')
totaalLabel = tk.Label(scherm)
werkbonbij()

totaalLabel.grid(row=0, column=0)
barcodeVeld = tk.Entry(scherm)
barcodeVeld.grid(row=1, column=0)
leegmaken = tk.Button(scherm, text="Nieuwe klant", width=15, height=3, command= nieuweKlant)
leegmaken.grid(row=0, column=1)
barcodeVeld.bind("<Return>", add)


scherm.mainloop()