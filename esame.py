class ExamException(Exception):

    pass


class CSVTimeSeriesFile():
    
    def __init__(self, name):
        
        self.name = name

    def get_data(self):

        try:
            file = open(self.name, "r")
            #controllo se il file esiste

        except:
            raise ExamException('file non esistente')

        
        prova = open(self.name, "r")

        try:
            content = prova.read()
            #controllo se il file è leggibile
            
        except:
            raise ExamException('file illeggibile')


        if content == '':
            raise ExamException('file vuoto') 
            #controllo se il file è vuoto           



        listoflist = []

        controllo = []

        annoprecedente = 0

        meseprecedente = 1

        mesi = [1,2,3,4,5,6,7,8,9,10,11,12]


        for line in file:

            if line == '\n':
                pass
                #skippo le linee vuote

            else:

                if ',' not in line:
                    pass
                    #skippo le linee in cui non distingo data e passeggeri


                else:

                    elements=line.split(',')

                    if '-' not in elements[0]:
                        pass
                        #skippo le date non valide


                    else:

                        if elements[0] in controllo:
                            raise ExamException('errore, doppio timestamp')
                        #controllo unicità date e le appendo


                        controllo.append(elements[0])

                        controllo1=0

                        controlli=elements[0].split('-')
                        #splitto date in anni e mesi

                        #if type(controlli[0])!=str:
                            #pass


                        try:
                            years = int(controlli[0])
                            months = int(controlli[1])
                            
                            #controllo convertibilità

                            
                        except:
                            controllo1 = 1


                        if controllo1 == 1:
                            pass

                        else:

                            if months not in mesi:
                                pass

                            else:

                                if annoprecedente > int(controlli[0]):

                                    raise ExamException('annoprecedente maggiore')
                                    #controllo timestamp anno

                                
                                elif annoprecedente == int(controlli[0]):
                                    #print(meseprecedente, ">", controlli[1])

                                    if meseprecedente>int(controlli[1]):

                                        #controllo timestamp mesi

                                        raise ExamException('meseprecedente maggiore')

                                    meseprecedente=int(controlli[1])
                                    #print(meseprecedente)

                                
                                else:
                                    meseprecedente = int(controlli[1])
                                    #inizializzazione primo mese nuovo anno




                                annoprecedente = int(controlli[0])

                                errore=0

                                try:
                                    passeggeri = int(elements[1])
                                
                                except:
                                    errore = 1
                                    #print('err')


                                if errore == 1:
                                    pass

                                else:

                                    if int(elements[1])<=0:
                                        pass

                                    else:

                                        #creo lista da mettere nella lista di liste
                                        lista=[]
                                        dato = elements[0]
                                        lista.append(dato)


                                        value = int(elements[1])

                                        # Aggiunta degli elementi alla lista con split di ogni riga su ","

                                        lista.append(value)

                                        listoflist.append(lista)


        # Chiusura del file

        file.close()

        return (listoflist)




def compute_avg_monthly_difference(lista, inizio, fine):

    average = [] #lista con le medie

    #controllo tipo lista

    if type(lista)!= list:
        raise ExamException('non è stata passata una lista')
        


    #controllo tipo inizio e fine

    if type(inizio) != str:
        raise ExamException('Errore, primo mese non è string')

    if type(fine)!= str:
        raise ExamException('Errore, mese finale non string')


    #controllo convertibilità

    try:
        primo = int(inizio)
        ultimo = int(fine)
        

    except:
        raise ExamException('error, non valido come anno inizio e/o fine')

    if primo>ultimo:
        raise ExamException('error, maggiore primo di ultimo')

    anni = []


    #creo lista con gli anni per controllare che inizio e fine siano presenti

    for i in lista:

        anno=i[0].split('-')

        if anno[0] not in anni:

            anni.append(anno[0])
    

    if inizio not in anni:
        raise ExamException('error, inizio non è tra gli anni iterabili')

    if fine not in anni:
        raise ExamException('error, fine non compreso')

    
    #creo un for che funzioni mese per mese

    for mh in range (1,13):

        #azzero indici per poterli riutilizzare

        counter=0

        somma=0

        media=0   


        #for che cicla tutti gli elementi della lista di liste

        for element in lista:


            #divido anno e mese

            data=element[0].split('-')


            #ciclo solo nell'intervallo richiesto degli anni

            if int(data[0])<int(inizio) or int(data[0])>int(fine):

                pass

            else:

                #ciclo solo sul mese interessato ovvero quello di cui devo fare la media

                if mh == int(data[1]):

                    
                    #altro ciclo per confrontare i mesi interessati
                    for argument in lista:


                        #split per controllare i mesi

                        calendar=argument[0].split('-')


                        #non considero gli anni fuori dall'intervallo

                        if int(calendar[0])<int(inizio) or int(calendar[0])>int(fine):

                            pass

                        else:

                            #prendo solo la riga con il mese uguale e anno che varia di uno

                            if calendar[1]==data[1]:

                                
                                #prendo lo stesso mese di anno i e anno i+1 così da fare la media tra i due
                                if int(calendar[0]) == int(data[0])+1:

                                #sommo alla somma e aumento il counter per dividere

                                    somma=somma+(int(argument[1])-int(element[1]))

                                    counter = counter+1
        
        #metto zero se ho meno di un mese da esaminare

        if counter <1:
            average.append(0)


        #calcolo la media e la appendo
                                    
        else:
            media=somma/counter
            average.append(media)


    #ritorno la lista con le medie
    return average

    