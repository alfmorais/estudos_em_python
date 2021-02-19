class Restaurant():
    '''Classe Restaurante'''

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('O nome do Restaurante é: ' + self.restaurant_name)
        print('O tipo da cozinha é: ' + self.cuisine_type)

    def open_restaurant(self):
        print('O ' + self.restaurant_name + ' estará aberto as 17:00.')

restaurante = Restaurant('Bar & Escritório Riachuelo', 'Boteco')
restaurante.describe_restaurant()
restaurante.open_restaurant()
