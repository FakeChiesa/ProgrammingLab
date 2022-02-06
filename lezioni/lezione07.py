class CSVFile():
    
    def __init__(self, name):
        # Programmazione dell'attributo "name"
        self.name = name

    def get_data(self, start = None, end = None):

        # Istanziamento della Lista (è una lista di lista)
        file = open(self.name, "r")

        i=0

        if start>end:#controllo alcune caratteristiche dello start e dell' end 
            raise Exception('Il valore di partenza non può essere MAGGIORE di quello di arrivo')
            #tiro su l'errore e lo printo per dare chiarezza al Programmazione



        # Lettura del file, linea per linea
        listoflist = []

        for line in file:
        # Istanziamento di elementi (che andranno nella lista)
            i=i+1

            elements=line.split(',')

            elements[-1]=elements[-1].strip()
            # Salvataggio dei termini (esclusa l'intestazione) del file negli elementi

            if elements[0] != 'Date':
                lista=[]
                dato = elements[0]
                lista.append(dato)

                for element in elements[1:2]:
                    value = float(element)
                    # Aggiunta degli elementi alla lista con split di ogni riga su ","
                    lista.append(value)
                listoflist.append(lista)

        if (i<(end-start)):
            raise Exception('Il file ha meno righe di quelle intese stampare:{}' .format(i))

        # Chiusura del file
        file.close()
        listoflist = listoflist[start : end+1]
        return (listoflist)



# --- PROGRAMMA PRINCIPALE ---
my_file = CSVFile('shampoo_sales.csv')

print('Nome del file: {}'.format(my_file.name))

inizio=1
fine=20

print('Elementi del file: {}'.format(my_file.get_data(inizio, fine)))
