from prettytable import PrettyTable

class Book:
    def __init__(self, nome, autor, publicacao, genero, ibsn):
        self.nome = nome
        self.autor = autor
        self.publicacao = publicacao
        self.genero = genero
        self.ibsn = ibsn
        self.previous = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.previous = None
        self.size = 0

    def append(self, nome, autor, publicacao, genero, ibsn):
        new_book = Book(nome, autor, publicacao, genero, ibsn)

        if self.head == None:
            self.head = new_book
            self.previous = new_book
        else:
            new_book.next = self.head
            self.head.previous = new_book
            self.head = new_book
        self.size += 1

    def remove(self, livro):
        pointer = self.head
        encontrado = False

        while pointer != None and not encontrado:
            if pointer.nome == livro:
                encontrado = True
            else:
                pointer = pointer.next

        if pointer == None:
            print ("Livro não encontrado na biblioteca.")
            
        else:
            if pointer == self.head:
                self.head = pointer.next
                if self.head != None:
                    self.head.previous = None
                else:
                    self.previous = None

            elif pointer == self.previous:
                self.previous = pointer.previous
                self.previous.next = None

            else:
                pointer.previous.next = pointer.next
                pointer.next.previous = pointer.previous

            print(f'Livro "{livro} removido com sucesso!')
            self.size -= 1

    def __len__(self):
        return self.size
    
    def search(self, livro):
        pointer = self.head
        encontrado = False
        while pointer != None and not encontrado:
            if pointer.nome == livro:
                encontrado = True
            else:
                pointer = pointer.next
        if pointer == None:
            print("Livro não encontrado na biblioteca.")
        else:
            table = PrettyTable(["\033[1;31mNome do livro\033[m", "\033[1;31mAutor\033[m", "\033[1;31mAno de publicação\033[m", "\033[1;31mGênero\033[m", "\033[1;31mIBSN\033[m"])
            table.add_row([str(pointer.nome), str(pointer.autor), str(pointer.publicacao), str(pointer.genero), str(pointer.ibsn)]) 
            print(table)
    
    def __repr__(self):
        table = PrettyTable(["\033[1;31mNome do livro\033[m", "\033[1;31mAutor\033[m", "\033[1;31mAno de publicação\033[m", "\033[1;31mGênero\033[m", "\033[1;31mIBSN\033[m"])
        pointer = self.head

        while pointer != None:
            table.add_row([str(pointer.nome), str(pointer.autor), str(pointer.publicacao), str(pointer.genero), str(pointer.ibsn)]) 
            pointer = pointer.next
        
        return str(table)
    
    def __str__(self):
        return self.__repr__()
    
