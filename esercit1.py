class ExamException(Exception):
    pass

class MovingAverage():

    def __init__(self, ratio):
        # Programmazione dell'attributo "name"
        if type(lenght) != int:
            raise ExamException('Errore, la lunghezza delle coppie deve essere inserita in numero intero')

        if lenght < 1:
            raise ExamException("non posso crare grupppi di numeri nulli o negativi")

        self.lenght = lenght

    def compute(self, lista):

        if type(lista) != list: 
            raise ExamException("la lista non esiste")
        
        lunghezza = len(lista)

        if lunghezza == 0: 
            raise ExamException("la lista è vuota")

        if self.lenght > lunghezza:
            raise ExamException("non posso creare gruppi perche la lista è troppo corta")

        NuovaLista = []

        for i in range (lunghezza - self.lenght + 1):

            p=i

            somma = 0

            for e in range (self.lenght):

                if type(lista[p]) not in [int, float]:
                    raise ExamException("Errore, l'elemento {} non è un valore numerico, ma: {}" .format(lista[p], type(lista[p])) )

                somma = somma + lista[p]
                p = p+1

            risultato = somma / self.lenght
            NuovaLista.append(risultato)

        return NuovaLista


#lunghezza_gruppi = 2

#moving_average = MovingAverage(lunghezza_gruppi)

#result = moving_average.compute([2,4,8,16])

#print(result)