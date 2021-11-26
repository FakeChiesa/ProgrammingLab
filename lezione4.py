class CSVFile():

    def __init__(self, name):
        self.name=name

    def get_data(self):
        lista = []

        my_file = open('shampoo_sales.csv', 'r') 

        for line in my_file:
            if line != 'Date,Sales\n':
                lista.append(line)
        my_file.close()

my_file = CSVFile ('shampoo_sales.csv')

my_file.get_data()

print(my_file.name)
print(my_file.get_data())