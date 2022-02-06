class CSVTimeSeriesFile():
    
    def __init__(self, name):
        
        self.name = name

    def get_data(self):

        
        file = open(self.name, "r")


        listoflist = []

        for line in file:

            elements=line.split(',')

            #elements[-1]=elements[-1].strip()


            if elements[0] != 'date':
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


    for i in range (0,12):

        for j in range (0, fine-inizio):

            for z in range (0,12):

                for element in lista:
                    if z == i:
                        
                        average.append(element[1])
                        
    print(average)






time_series_file = CSVTimeSeriesFile(name='data.csv')

time_series = time_series_file.get_data()

#print(time_series)


computare = compute_avg_monthly_difference(time_series, 1949, 1951)