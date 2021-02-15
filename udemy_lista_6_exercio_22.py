nota = int(input("Digite sua nota: "))
m_nota = []
m_nota.append(nota)

while True: 
	nota = int(input("Digite sua nota: "))
	m_nota.append(nota)

	if nota in range(10, 21):
		nota = int(input("Digite sua nota: "))
		m_nota.append(nota)

	else:
		del m_nota[-1]
		break

m_nota_1 = (sum(m_nota)) / (len(m_nota))

print(f'Média = {m_nota_1}')
