from Double_list import *

print('SEJA BEM VINDO AO "LIBRARY MANAGER", ESPERO SER ÚTIL E AJUDÁ-LO NO QUE PRECISAR ;)')

books = DoubleLinkedList()

while True:

    print('='*50)
    print('''O QUE VOCÊ DESEJA FAZER?
        1) Adicionar um novo livro
        2) Remover/reservar/emprestar um livro da coleção
        3) Buscar livro por nome
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

        books.append(livro, autor, data_publicação, genero, isbn)       
        print(f'Livro "{livro}" adiconado com sucesso!')

    elif escolha == '2':
        excluir = input('Qual livro você deseja remover? ')

        books.remove(excluir)
        
        
    elif escolha == '5':
        if len(books) == 0:
            print('Ainda não há livros nessa biblioteca!')
        else:
            print(books)
    
    elif escolha == '3':
        busca = input('Qual livro você procura? ')
        books.search(busca)


    elif escolha == '4':
        print(f'Esta biblioteca possui ao todo {len(books)} livros.')

    elif escolha == '5':
        if len(books) == 0:
            print('Ainda não há livros nessa biblioteca')
        print(books)
    
    elif escolha == '6':
        break

print('Espero que tenha gostado :) Volte sempre!')