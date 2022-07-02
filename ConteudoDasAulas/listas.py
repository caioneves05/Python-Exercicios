# a númeração em python sempre começará pelo 0.

carros = ['Ferrari', 'Lamborghini', 'Camaro']

print("O meu carro favorito é o " + carros[-1].title())

# o -1 representa o último elemento de uma lista.

carros[1] = 'Mustang'
carros.append('BMW')
carros.insert(0, 'Jeep')
carros.extend('Fusca')
del carros[0]
carros.pop(2)
carros.remove('Mustang')
carros.reverse()

print(carros)


# Adicionando elementos ao final da lista com o .append

#inserindo elementos na lista com posição definida utilizando o .insert

# Alterando elementos da lista.

# O .extend separa os caracteres e insere na lista de forma separada.

# O del deleta um elemento da lista de acordo com a posição indicada.

# O .pop deleta o último elemento da lista.

# O .remove procura o elemento e o elimina.

# O .sort reverse=True coloca a lista de trás para frente em ordem alfabética.

# O len serve para saber quantos objetos tem na lista.

#.reverse coloca todos os itens de trás para frente sem etar em ordem alfabética.
