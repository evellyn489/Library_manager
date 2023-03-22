# Library_manager
 __"Library Manager"__  é um gerenciador de biblioteca digital que tem como principais funções o armazenamento, remoção e busca de livros que fazem parte da coleção. Inicialmente, esta biblioteca possui cinco livros específicos que podem ser removidos individualmente pelo usuário, caso deseje.
 
 ### Entradas fornecidas:
 * Nome do livro
 * Autor
 * Ano de publicação
 * Gênero
 * Código de IBSN
 
 ### Funcionalidades:
 
 * Adicionar um novo livro
 * Remover/reservar/emprestar um livro da coleção
 * Buscar livro por nome ou código de IBSN
 * Visualizar a quantidade de livros disponíveis
 * Visualizar todos os livros disponíveis
 * SAIR
 
 ### Instalações necessárias:
 * Python (de preferência o 3.10)
 * Biblioteca externa PrettyTable
 
 Para baixar a biblioteca PrettyTable via pip, basta digitar o seguinte comando no terminal:
 `python -m pip install -U prettytable`
 
 ### Baixar e executar pelo docker:
 
 Para baixar e rodar o programa pelo docker, siga esses passos:
 * Para baixar a imagem, digite o seguinte comando no terminal: 
 `docker pull evellynrodrigues/library_manager:1.0`
 
 * Para executar, digite:
 `docker run -it evellynrodrigues/library_manager:1.0`
 
 ### Créditos:
 Projeto desenvolvido por Evellyn Rodrigues da Rocha para a matéria de Estrutura de Dados na Universidade Federal de Alagoas(UFAL), a fim de praticar listas duplamente encadeadas.
