class CSVFile():
    
    def __init__(self, name):
        # Programmazione dell'attributo "name"
        self.name = name

    
    def get_data(self, start = None, end = None):

    # Istanziamento della Lista (è una lista di lista!)
        file = open("shampoo_sales.csv", "r")
        if (start>end):#controllo alcune caratteristiche dello start e dell' end 
            raise Exception('Il valore di partenza non può essere MAGGIORE di quello di arrivo')
            #tiro su l'errore e lo printo per dare chiarezza al Programmazione

    # Lettura del file, linea per linea
        listoflist = []
        for line in file:
    # Istanziamento di elementi (che andranno nella lista)
            elements = line
            elements=elements.split(',')
        # Salvataggio dei termini (esclusa l'intestazione) del file negli elementi
            if elements[0] != 'Date':
                lista=[]
                date = elements[0]
                lista.append(date)
                for element in elements[1:]:
                    value = float(element)
                    # Aggiunta degli elementi alla lista con split di ogni riga su ","
                    lista.append(value)
                listoflist.append(lista)
    # Chiusura del file

        file.close()
        listoflist = listoflist[start : end+1]
        return (listoflist)


# --- PROGRAMMA PRINCIPALE ---
my_file = CSVFile('shampoo_sales.csv')
print(my_file)
print('Nome del file: {}'.format(my_file.name))
inizio=1
fine=3
# Programmazione di una lista di un file
# Istanziamento di una lista per salvare i valori
list_1 = []
# Apertura del file
a=my_file.get_data(inizio, fine)
print(a)