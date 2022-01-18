class ExamException(Exception):
    pass

class Diff():

    def __init__(self, ratio=1):

        if type(ratio) not in [int, float]:
            raise ExamException('devo dividere per un qualcosa di numerico')

        if ratio == 0:
            raise ExamException ('non puoi dividere per zero gayyyy')

        if ratio < 0:
            raise ExamException ('non puoi dividere per zero gayyyy')

        self.ratio = ratio

    def compute(self, lista):

        if type(lista) != list: 
            raise ExamException("la lista non esiste")
        
        lunghezza = len(lista)

        if lunghezza == 0: 
            raise ExamException("la lista è vuota")

        if lunghezza == 1:
            raise ExamException("non posso fare la differenza se la lista contiene un solo elemento")

        NuovaLista = []

        for i in range (lunghezza-1):


            differenza = 0

            
            if type(lista[1]) not in [int, float]:
                raise ExamException("Errore, l'elemento {} non è un valore numerico, ma: {}" .format(lista[i], type(lista[i])) )

            if type(lista[i+1]) not in [int, float]:
                raise ExamException("Errore, l'elemento {} non è un valore numerico, ma: {}" .format(lista[i], type(lista[i])) )

            differenza = lista[i+1] - lista[i]

            risultato = differenza / self.ratio

            NuovaLista.append(risultato)

        return NuovaLista




#diff = Diff()

#result = diff.compute([2,4,8,16,32])

#print(result)