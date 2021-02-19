filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))

# Seu aniversario contido em PI?

aniversario = input('Qual é a data do seu nascimento?')

if aniversario in pi_string:
    print('Seu aniversário está contido no PI de 1 Milhão')
else:
    print('Seu aniversário não está contido no PI de 1 Millhão')
