my_file = open('schampoo_sales.txt', 'r') #apro il file 
somma = [] #definisco una lista
for line in my_file:
    elements = line.split(',') #splitto dopo la virgola

    if elements[1] != 'Sales\n':
        somma.append(float(elements[1])) #append aggiunge alla fine della lista

        #somma+=float(elements[1])
        #altro modo per farla, senza lista, meno pythonica probabilmente
        #scrivo all'inizio somma = 0

my_file.close()
print(sum(somma)) #printi e usi la built in somma