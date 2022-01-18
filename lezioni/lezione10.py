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




class IncrementedModel(Model):

    def previsione (self, data, mesi):

        somma = 0.0
         
        lunghezza=len(data)

        implemento_medio = 0.0

        prediction = 0.0

        counter = 0

        errore = 0.0

        conta = 0


        while conta < 12 :

            for i in range (lunghezza+conta-mesi-1-3, lunghezza+conta-mesi-1):

                #previsione in base agli ultimi mesi indicati

                implemento = data[i] - data[i-1]

                print (data [i])

                somma=somma+implemento


            implemento_medio = somma / (2)

            somma = 0

            print (data[lunghezza-mesi+conta-1])

            prediction = data[lunghezza-mesi+conta-1] + implemento_medio

            print ('predict {}' .format(prediction))

            print (data[lunghezza -mesi + conta])

            print ('\n')

            errore = errore + abs(prediction - data[lunghezza - mesi + conta])

            conta = conta + 1

        #il -1 serve perche i dati partono da zero mentre la len va da 1 in poi es un array da un el lo scrivi a[0] e ha comunque lunghezza 1 
        
        erroremedio = errore / (lunghezza)    


        return erroremedio





class FitIncrementedModel(IncrementedModel):



    def previsione(self, data, mesi):


        previs = super().previsione(data, mesi)

        lunghezza = len(data)

        #togli alla previsione il valore per avere solo l'incremento in previsione

        incremento = previs - data[(lunghezza-1)]


        self.fit(data, mesi)

        previsione_finale = ((self.dati_fit + incremento)/2) + data[(lunghezza-1)]

        
        #calcoli il valore finale che dovrebbe esserci

        return previsione_finale





    def fit(self, data, mesi):

        somma = 0

        lunghezza = len(data)

        #calcolo della fittazione dei mesi precedenti

        for i in range(0, lunghezza-mesi-1):
            
            implemento = data[i+1] - data[i]

            somma += implemento

        self.dati_fit = somma / (lunghezza-mesi-1)






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

#print ('il nome è: {} \n' .format(my_file.name))

#print('contenuto è:\n {} \n' .format(my_file.get_data()))



#file_numerico = NuemricalCSVFile (name = 'shampoo_sales_1.csv')

#print ('il nome è: {}' .format(file_numerico.name))

#print('contenuto è: {}' .format(file_numerico.get_data()))

#test_predict_data = [50,52,60]

predict = IncrementedModel()

mesi = 12

#prediction = predict.previsione(test_predict_data, mesi)

#if not prediction == 65:
    #raise Exception('IncrementModel sul dataset di test non mi torna 65 ma "{}"'.format(prediction))
#else:
    #print('IncrementModel test passed')


#print ('errore medio previsto : {}' .format (predict.previsione(my_file.get_data(), mesi)))

#print ( 'per il prossimo mese la previsione in base agli ultimi {} la previsione è : {}' .format((mesi), (predict.previsione(my_file.get_data(), mesi) )))



#ModelloFittato = FitIncrementedModel ()

#ModelloFittato.fit (my_file.get_data(), mesi)

#print(ModelloFittato.previsione(my_file.get_data(), mesi))
