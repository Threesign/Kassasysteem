print('importeren..')

class Kassabon:
    def __init__(self):
        self.totaal = 0

import tkinter as tk
versie = 'Alpha 1'
subtotaal = ''
totaal = 10

kassabon = Kassabon()

print('klaar!')
print('kassa versie ' + versie)
#START#


class Product:
    def __init__(self, prijs, naam):
        self.prijs = prijs
        self.naam = naam

producten = {}
producten['7584185114255'] = Product(1, "zakgeldpotje")
producten['9789054516200'] = Product(100, "boek")

def product_opzoeken(barcode):
    return producten[barcode]

def add(event):
    erbij = product_opzoeken(barcodeVeld.get())

    kassabon.totaal = kassabon.totaal + erbij.prijs
    totaalLabel.configure(text=totaalveldtekst())
    barcodeVeld.delete(0, 'end')


def totaalveldtekst():
    return 'totaal: ' + str(kassabon.totaal) + ' EUR'


scherm = tk.Tk()
scherm.title('kassasysteem')
totaalLabel = tk.Label(scherm, text=(totaalveldtekst()))
totaalLabel.grid(row=0, column=0)
barcodeVeld = tk.Entry(scherm)
barcodeVeld.grid(row=1, column=0)

barcodeVeld.bind("<Return>", add)

scherm.mainloop()