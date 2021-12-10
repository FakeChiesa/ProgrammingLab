class Model():

    def fit(self, data):
        raise NotImplementedError ('metodo non implementato')

    def previsione(self, data):
        raise NotImplementedError ('metodo non implementato')


class IncrementedModel(Model):

    def previsione (self, data):
        
        somma = 0
         
        lunghezza=len(data)

        for i in range (0, lunghezza-1):

            implemento = data[i+1] - data[i]

            somma=somma+implemento

        implemento_medio = somma / (lunghezza-1)

        prediction = data[lunghezza-1] + implemento_medio

        #il -1 serve perche i dati partono da zero mentre la len va da 1 in poi es un array da un el lo scrivi a[0] e ha comunque lunghezza 1 

        return prediction

#------------------------------
#PROGRAMMA PRINCIPALE
#------------------------------


lista = [50, 52, 60]

Modello = IncrementedModel ()

print(Modello.previsione(lista))




