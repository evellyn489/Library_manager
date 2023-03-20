from Double_list import *
from time import sleep

print('\033[31mSEJA BEM VINDO AO "LIBRARY MANAGER", ESPERO SER ÚTIL E AJUDÁ-LO NO QUE PRECISAR ;)\033[m')

books = DoubleLinkedList()

while True:

    sleep(5)
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
        livro = input('Qual livro você deseja adicionar à coleção? ').strip().title()
        autor = input('Autor(a) do livro: ').strip().title()
        data_publicação = input('Data de publicação?: ')
        genero = input('Gênero: ').strip().title()
        isbn = input('Código de ISBN: ')

        books.append(livro, autor, data_publicação, genero, isbn)       
        print(f'Livro "\033[31m{livro}\033[m" adiconado com sucesso!')

    elif escolha == '2':
        excluir = input('Qual livro você deseja remover? ').strip().title()

        books.remove(excluir)
        
        
    elif escolha == '5':
        if len(books) == 0:
            print('Ainda não há livros nessa biblioteca!')
        else:
            print(books)
    
    elif escolha == '3':
        busca = input('Qual livro você procura? ').strip().title()
        books.search(busca)


    elif escolha == '4':
        print(f'Esta biblioteca possui ao todo {len(books)} livros.')

    elif escolha == '5':
        if len(books) == 0:
            print('Ainda não há livros nessa biblioteca')
        print(books)
    
    elif escolha == '6':
        break

print('\033[31mEspero que tenha gostado :) Volte sempre!\033[m')