class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, elemento): 
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
    
    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            pointer = pointer.next
        return pointer.data

    def index(self, elemento):
        pointer = self.head
        index = 0

        while pointer != None:
            if pointer.data == elemento:
                return index
            pointer = pointer.next
            index += 1
        else:
            print('Ainda não há livros na biblioteca.')

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

lista_livros = DoubleList()
lista_autores = DoubleList()
lista_datas = DoubleList()
lista_genero = DoubleList()
lista_isbn = DoubleList()

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
        livro = input('Qual livro você deseja adicionar à coleção? ')
        autor = input('Autor(a) do livro: ')
        data_publicação = input('Data de publicação?: ')
        genero = input('Gênero: ')
        isbn = input('Código de ISBN: ')

        lista_livros.append(livro)
        lista_autores.append(autor)
        lista_datas.append(data_publicação)
        lista_genero.append(genero)
        lista_isbn.append(isbn)

        print(f'Livro "{livro}" adiconado com sucesso!')

    elif escolha == '2':
        remove = input('Qual livro você deseja remover? ')

    elif escolha == '3':
        busca = input('Qual livro você procura? ')

        try:
            i = lista_livros.index(busca)
            print(f'Livro: {busca}')
            print(f'Autor: {lista_autores[i]}')
            print(f'Data de publicação: {lista_datas[i]}')
            print(f'Gêneros: {lista_genero[i]}')
            print(f'ISBN: {lista_isbn[i]}')

        except TypeError:
            print('Este livro não se encontra na biblioteca.')

    elif escolha == '4':
        print(f'Esta biblioteca possui ao todo {len(lista_livros)} livros.')

    elif escolha == '5':
        if len(lista_livros) == 0:
            print('Ainda não há livros nessa biblioteca')
        else:
            for i in range(len(lista_livros)):
                print(f'{i+1} - {lista_livros[i]}')

    elif escolha == '6':
        break

print('Espero que tenha gostado :) Volte sempre!')