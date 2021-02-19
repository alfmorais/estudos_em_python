# Armazenando informações de alienígena

alien_0 = {'color': 'green', 'points': 5}

# Acessando valores de um dict
print(alien_0['color'])
print(alien_0['points'])

# Acessando valores de um dict e usando print
new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')

# Definindos novas chaves e valores p/ alien_0
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Criando um dict vazio
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

# Modificando valores em um Dict
alien_0 = {'color': 'green'}
print('The alien is ' + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + '.')
