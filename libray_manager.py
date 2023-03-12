class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, elemento): #[9, 10, 8]
        new_node = Node(elemento)
        if self.head == None:
            self.head = new_node
        else:
            pointer = self.head

            while pointer.next != None:
                pointer = pointer.next
            pointer.next = new_node
        self.size += 1

    def __len__(self):
        return self.size
    def __repr__(self):
        r = ''
        pointer = self.head

        while pointer != None:
            r += str(pointer.data) + '\n'
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()

print('SEJA BEM VINDO AO "LIBRARY MANAGER", ESPERO SER ÚTIL E AJUDÁ-LO NO QUE PRECISAR ;)')

lista = DoubleList()

while True:

    print('='*50)
    print('''O QUE VOCÊ DESEJA FAZER?
        1) Adicionar um novo livro
        2) Remover/reservar/emprestar um livro da coleção
        3) Buscar livro
        4) Visualizar a quantidade de livros disponíveis
        5) Visualizar todos os livros disponíveis
        6) SAIR
        ''')
    escolha = input('Selecione uma opção: ')
    print('='*50)

    if escolha == '1':
        adiciona = input('Qual livro você deseja adicionar à coleção? ')
        lista.append(adiciona)
        print(f'Livro "{adiciona}" adiconado com sucesso!')
    elif escolha == '2':
        remove = input('Qual livro você deseja remover? ')
    elif escolha == '3':
        busca = input('Qual livro você procura? ')
    elif escolha == '4':
        print(f'Esta biblioteca possui ao todo {len(lista)} livros.')
    elif escolha == '5':
        print(lista)
    elif escolha == '6':
        break

print('Espero que tenha gostado :) Volte sempre!')