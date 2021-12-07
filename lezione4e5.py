class CSVFile():
    
    def __init__(self, name):
        # Programmazione dell'attributo "name"
        self.name = name
    
    def get_data(self):
    # Istanziamento della Lista (è una lista di lista!)
        try:
            file = open("shampo_sales.csv", "r")
        except:
            print('mona il file non esiste, apro quello giusto')
            file = open("shampoo_sales.csv", "r")
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
        return (listoflist)
        


# --- PROGRAMMA PRINCIPALE ---
my_file = CSVFile('shampoo_sales.csv')
print(my_file)
print('Nome del file: {}'.format(my_file.name))


a=my_file.get_data()
print(a)