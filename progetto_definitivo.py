class CSVFile():
    #definisco classe

    def __init__(self, name):
    #definizione di attributi(?): nome

        self.name = name

    def get_data(self):
        #definisco il get data per leggere le righe

        dati = []

        solo_soldi = []

        # if type(self.name) != 'str' :
            # raise Exception ('il nome deve essere di tipo stringa mentre questo è di tipo {}' .format(type(self.name)))
      #da completare ----------------------------------------------------------


        file = open(self.name, "r")
        #apro il file

        for line in file:

            elements = line.split(',')

            elements[-1]=elements[-1].strip()

            if elements[0] != 'Date':

                dati.append(elements)

                solo_soldi.append(float(elements[1]))

        file.close()

        return solo_soldi



class Model ():

    def fit (self, data):
        raise NotImplementedError ('Metodo non implementato')

    def previsione (self, data):
        raise NotImplementedError ('Metodo non implementato')


from lezione09 import IncrementedModel

from lezione09 import FitIncrementedModel



#sottoclasse figlia che eredita get_data

class NuemricalCSVFile(CSVFile):
    
    def get_data(self):
        
        convertitore = super().get_data()

        dati_stringa = []

        for string_row in convertitore:
            colonna_numerica = []

            for i,elements in enumerate(string_row):

                if i==0:
                    colonna_numerica.append(elements)

                else:
                    try:
                        value = float(elements)
                        colonna_numerica.append(value)

                    except Exception as e:
                        print('non sono riuscito a convertire {} in float: {}' .format(elements, e))
                        break

            if len(colonna_numerica) == len(string_row):
                dati_stringa.append(colonna_numerica)

        return dati_stringa
                




#------------------------------------
#PROGRAMMA PRINCIPALE
#------------------------------------







my_file = CSVFile (name='shampoo_sales.csv')

print ('il nome è: {} \n' .format(my_file.name))

#print('contenuto è:\n {} \n' .format(my_file.get_data()))



#file_numerico = NuemricalCSVFile (name = 'shampoo_sales_1.csv')

#print ('il nome è: {}' .format(file_numerico.name))

#print('contenuto è: {}' .format(file_numerico.get_data()))

predict = IncrementedModel ()

mesi = 12


print ( 'per il prossimo mese la previsione in base agli ultimi {} la previsione è : {}' .format((mesi), (predict.previsione(my_file.get_data(), mesi) )))



ModelloFittato = FitIncrementedModel ()

ModelloFittato.fit (my_file.get_data(), mesi)

print(ModelloFittato.previsione(my_file.get_data(), mesi))