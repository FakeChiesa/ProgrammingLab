class Model():

    def fit(self, data):
        raise NotImplementedError ('metodo non implementato')

    def previsione(self, data):
        raise NotImplementedError ('metodo non implementato')


class IncrementedModel(Model):

    def previsione(self, data, mesi):

        somma = 0
         
        lunghezza=len(data)

        for i in range (lunghezza-mesi, lunghezza-1):

            #previsione in base agli ultimi mesi indicati

            implemento = data[i+1] - data[i]

            somma=somma+implemento

        implemento_medio = somma / (mesi-1)

        prediction = data[lunghezza-1] + implemento_medio

        #il -1 serve perche i dati partono da zero mentre la len va da 1 in poi es un array da un el lo scrivi a[0] e ha comunque lunghezza 1 

        return prediction



class FitIncrementedModel(IncrementedModel):



    def previsione(self, data, mesi):


        previs = super().previsione(data, mesi)

        lunghezza = len(data)

        #togli alla previsione il valore per avere solo l'incremento in previsione

        incremento = previs - data[(lunghezza-1)]

        try:

            previsione_finale = ((self.dati_fit + incremento)/2) + data[(lunghezza-1)]

        
        except:
            print('il fit non è implementato')

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
        




#------------------------------
#PROGRAMMA PRINCIPALE
#------------------------------


lista = [8, 19, 31, 41, 50, 52, 60]

lista1 = [10, 20, 30, 40, 50 , 60]

Modello = IncrementedModel ()

mesi = 3

ModelloFittato = FitIncrementedModel ()

#ModelloFittato.fit (lista1, mesi)

print(ModelloFittato.previsione(lista, mesi))
