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

        return prediction

#------------------------------
#PROGRAMMA PRINCIPALE
#------------------------------


lista = [50, 52, 60]

Modello = IncrementedModel ()

print(Modello.previsione(lista))




