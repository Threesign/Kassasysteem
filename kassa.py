print('importeren..')

class Kassabon:
    def __init__(self):
        self.totaal = 0.0
        self.klantnummer = 1

import tkinter as tk
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
producten['9789054516200'] = Product(100.01, "boek")


def product_opzoeken(barcode):
    return producten[barcode]


def werktotaalbij():
    totaalLabel.configure(text=totaalveldtekst())

def add(event):
    erbij = product_opzoeken(barcodeVeld.get())

    kassabon.totaal = kassabon.totaal + erbij.prijs
    barcodeVeld.delete(0, 'end')

    werktotaalbij()


def totaalveldtekst():
    return 'totaal: ' + str(kassabon.totaal) + ' EUR'


def nieuweKlant():
    kassabon.totaal = 0
    kassabon.klantnummer = kassabon.klantnummer + 1
    werktotaalbij()
    print(kassabon.klantnummer)


scherm = tk.Tk()
scherm.title('kassasysteem')
totaalLabel = tk.Label(scherm)
werktotaalbij()

totaalLabel.grid(row=0, column=0)
barcodeVeld = tk.Entry(scherm)
barcodeVeld.grid(row=1, column=0)
leegmaken = tk.Button(scherm, text="Nieuwe klant", width=15, height=3, command= nieuweKlant)
leegmaken.grid(row=0, column=1)
barcodeVeld.bind("<Return>", add)

scherm.mainloop()