class CSVFile():
    
    def __init__(self, name):
        # Programmazione dell'attributo "name"
        self.name = name
    
    def get_data(self, start = None, end = None):

    # Istanziamento della Lista (è una lista di lista!)
        file = open("shampoo_sales_1.csv", "r")
        if (start>end):#controllo alcune caratteristiche dello start e dell' end 
            raise Exception('Il valore di partenza non può essere MAGGIORE di quello di arrivo')
            #tiro su l'errore e lo printo per dare chiarezza al Programmazione
            #ripeto il passaggio con i vari errori poccibili immessi da tastiera 

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
                    try:
                        value = float(element)
                        # Aggiunta degli elementi alla lista con split di ogni riga su ","
                        lista.append(value)
                    except ValueError: 
                        print ('Non posso convertire value a valore numerico')
                        print ('Il format è {}' .format(type(element)))
                listoflist.append(lista)
    # Chiusura del file
        file.close()
        listoflist = listoflist[start : end]
        return (listoflist)

class NumericalCSVFile(CSVFile):

    def get_data(self, start, end):
        return super().get_data(start, end)
    

# --- PROGRAMMA PRINCIPALE ---
my_file = CSVFile('shampoo_sales.csv')

file = NumericalCSVFile('shampoo_sales_1.csv')


print('Nome del file: {}'.format(my_file.name))
inizio=1
fine=20
# Programmazione di una lista di un file
# Istanziamento di una lista per salvare i valori
list_1 = []

b = file.get_data(inizio, fine)

a = my_file.get_data(inizio, fine)

print(a)