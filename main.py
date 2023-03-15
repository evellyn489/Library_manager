from Double_list import *

print('SEJA BEM VINDO AO "LIBRARY MANAGER", ESPERO SER ÚTIL E AJUDÁ-LO NO QUE PRECISAR ;)')

lista_livros = DoubleLinkedList()
lista_autores = DoubleLinkedList()
lista_datas = DoubleLinkedList()
lista_genero = DoubleLinkedList()
lista_isbn = DoubleLinkedList()

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
        excluir = input('Qual livro você deseja remover? ')

        index_remover = lista_livros.index(excluir)

        try:        
            lista_livros.remove(index_remover)
            lista_autores.remove(index_remover)
            lista_datas.remove(index_remover)
            lista_genero.remove(index_remover)
            lista_isbn.remove(index_remover)

            print(f'Livro "{excluir}" removido com sucesso!')

        except TypeError:
            print(f'O livro "{excluir} não existe nesta biblioteca, logo, não tem como removê-lo')


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
            for p in range(len(lista_livros)):
                print(f'{p+1} - {lista_livros[p]}') #Precisa analisar quando remover o primeiro

    elif escolha == '6':
        break

print('Espero que tenha gostado :) Volte sempre!')