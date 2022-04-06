print('Bem-vindo(a)! \nPor favor, digite a quantidade de votos para cada dia da semana.')

seg = int(input('Segunda-feira: '))
ter = int(input('Terça-feira: '))
qua = int(input('Quarta-feira: '))
qui = int(input('Quinta-feira: '))
sex = int(input('Sexta-feira: '))

semana = [seg, ter, qua, qui, sex]

print(f'Quantidade de votos:\nSegunda-feira: {seg} | Terça-feira: {ter}')
print(f'Quarta-feira: {qua} | Quinta-feira: {qui}\nSexta-feira: {sex}\n')

maior = max(semana)

print(f'O dia escolhido recebeu {maior} votos.')

if (seg == maior):
    print('As lives acontecerão na segunda-feira!')
elif (ter == maior):
    print('As lives acontecerão na terça-feira!')
elif (qua == maior):
    print('As lives acontecerão na quarta-feira!')
elif (qui == maior):
    print('As lives acontecerão na quinta-feira!')
elif (sex == maior):
    print('As lives acontecerão na sexta-feira!')


