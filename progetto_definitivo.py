class CSVFile():
    #definisco classe

    def __init__(self, name):
    #definizione di attributi(?): nome

        self.name = name

    def get_data(self):
        #definisco il get data per leggere le righe

        dati=[]

        file = open(self.name, "r")
        #apro il file

        for line in file:

            elements = line.split(',')

            elements[-1]=elements[-1].strip()

            if elements[0] != 'Date':

                dati.append(elements)

        file.close()

        return dati 
                


#------------------------------------
#PROGRAMMA PRINCIPALE
#------------------------------------


my_file = CSVFile (name='shampoo_sales.csv')

print (my_file.name)

print('contenuto è: {}' .format(my_file.get_data()))
