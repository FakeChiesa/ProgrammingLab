class CSVFile():
    
    def __init__(self, name):
        # Programmazione dell'attributo "name"
        self.name = name
    
    def get_data(self, list):
        # Istanziamento della Lista (è una lista di lista!)
        listoflist = []
        # Aggiunta degli elementi di una lista alla Lista
        for elements in list:
            listoflist.extend(list)
            # Stampa della Lista (comando alternativo: return print('La lista è:\n{}'.format(listoflist))
            return print('\n'.join([str(element) for element in listoflist]))

# --- PROGRAMMA PRINCIPALE ---
my_file = CSVFile('shampoo_sales.csv')
print(my_file)
print('Nome del file: {}'.format(my_file.name))

# Programmazione di una lista di un file
# Istanziamento di una lista per salvare i valori
list_1 = []
# Apertura del file
file = open("shampoo_sales.csv", "r")
# Lettura del file, linea per linea
for line in file:
    # Istanziamento di elementi (che andranno nella lista)
    elements = line
    # Salvataggio dei termini (esclusa l'intestazione) del file negli elementi
    if elements[0] != 'Date':
        date = elements[0]
        value = elements[1]
        # Aggiunta degli elementi alla lista con split di ogni riga su ","
        for elements in file:
            list_1.append(elements[0:-1].split(','))
# Chiusura del file
file.close()

my_file.get_data(list_1)