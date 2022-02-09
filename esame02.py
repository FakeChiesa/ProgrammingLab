class ExamException(Exception):

    pass


class CSVTimeSeriesFile():
    
    def __init__(self, name):
        
        self.name = name

    def get_data(self):

        try:
            file = open(self.name, "r")

        except:
            raise ExamException('file non esistente')


        listoflist = []

        for line in file:

            if ',' not in line:
                pass


            else:

                elements=line.split(',')

                #elements[-1]=elements[-1].strip()

                errore=0

                try:
                    passeggeri = float(elements[1])
                
                except:
                    errore = 1
                    #print('err')


                if errore == 1:
                    pass

                else:

                    if float(elements[1])<=0:
                        pass

                    else:

                        #if elements[0] != 'date':
                        lista=[]
                        dato = elements[0]
                        lista.append(dato)

                        for element in elements[1:2]:

                            value = float(element)

                                # Aggiunta degli elementi alla lista con split di ogni riga su ","
                            lista.append(value)
                        listoflist.append(lista)


        # Chiusura del file
        file.close()
    
        return (listoflist)




def compute_avg_monthly_difference(lista, inizio, fine):

    average = []

    if type(inizio) != str:
        raise ExamException('Errore, primo mese non è string')

    if type(fine)!= str:
        raise ExamException('Errore, mese finale non string')

    try:
        primo = float(inizio)
        ultimo = float(fine)
        

    except:
        raise ExamException('error, non valido come anno inizio e/o fine')

    if primo>ultimo:
        raise ExamException('error, maggiore primo di ultimo')

    anni = []

    for i in lista:

        anno=i[0].split('-')

        anni.append(anno[0])

    #print(anni)

    if inizio not in anni:
        raise ExamException('error, inizio non è tra gli anni iterabili')

    if fine not in anni:
        raise ExamException('error, fine non compreso')

        


    for element in lista:


        data=element[0].split('-')


        if float(data[0])<float(inizio) or float(data[0])>float(fine):
            #print (data[0], 'fuori')
            pass

        else: 
            #print( data[0],data[1], element[1])

            #print ('giro', data[1], element[1])

            counter=0

            somma=0

            media=0

            #print('giro esterno \n')

            if float(data[0])==float(inizio):

                for argument in lista:

                    calendar=argument[0].split('-')


                    if float(calendar[0])<float(inizio) or float(calendar[0])>float(fine):

                        pass

                    else:

                        if calendar[1]==data[1]:
                            #print('giro interno' , calendar[1],'     ', calendar[0],'    ', argument[1])


                            for oggetti in lista:

                                periodo=oggetti[0].split('-')


                                if float(periodo[0])<float(inizio) or float(periodo[0])>float(fine):

                                    pass

                                else:

                                    if periodo[1] == calendar[1]:

                                        if float(periodo[0]) == float(calendar[0])+1:

                                            #print('giro internissimo', oggetti[1])

                                            somma=somma+(float(oggetti[1])-float(argument[1]))

                                            counter = counter+1

                                            print(counter)

                if counter <=1:
                    average.append(0)
                
                else:
                    media=somma/counter
                    average.append(media)



    return average









time_series_file = CSVTimeSeriesFile(name='data.csv')

time_series = time_series_file.get_data()

#print(time_series)

computare = compute_avg_monthly_difference(time_series, '1949', '1951')

print(computare)