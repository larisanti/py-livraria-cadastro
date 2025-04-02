# Variáveis globais
lista_livros = [] # Lista de dicionários para armazenar livros
id_global = 0 # Contador para id dos livros

# Função cadastrar_livro
def cadastrar_livro(id_livro):
  print('\n---MENU CADASTRAR LIVRO---')
  id = input('Id do livro: ')
  nome = input('Por favor, entre com o nome do livro: ')
  autor = input('Por favor, entre com o autor do livro: ')
  editora = input('Por favor, entre com a editora do livro: ')

# Dicionário com os dados do livro
  livro = {
    'id': id,
    'nome': nome,
    'autor': autor,
    'editora': editora
  }

  # Adiciona o livro na lista global
  lista_livros.append(livro)
  print('Livro cadastrado com sucesso!')


# Função consultar_livro
def consultar_livro():
  while True:
    print('\n---MENU CONSULTAR LIVRO---')
    print('1 - Consultar Todos os Livros')
    print('2 - Consultar Livro por id')
    print('3 - Consultar Livro(s) por autor')
    print('4 - Retornar')

    opcao = input('Escolha a opção desejada: ')

    # Opção 1
    if opcao == '1':
      print('\n---CONSULTAR TODOS OS LIVROS---')
      if not lista_livros:
        print('Nenhum livro cadastrado.')
      else:
        for livro in lista_livros:
          print(f"Id: {livro['id']}")
          print(f"Nome: {livro['nome']}")
          print(f"Autor: {livro['autor']}")
          print(f"Editora: {livro['editora']}")
          print('-' * 30)

    # Opção 2
    elif opcao == '2':
      id_busca = input('Por favor, entre com o id do livro que deseja consultar: ')
      livro_encontrado = False
      for livro in lista_livros:
        if str(livro['id']) == id_busca:
          print('\n---LIVRO ENCONTRADO---')
          print(f"Id: {livro['id']}")
          print(f"Nome: {livro['nome']}")
          print(f"Autor: {livro['autor']}")
          print(f"Editora: {livro['editora']}")
          livro_encontrado = True
          break
      if not livro_encontrado:
        print('Nenhum livro encontrado com o id informado.')

    # Opção 3
    elif opcao == '3':
      autor_busca = input('Por favor, entre com o autor do livro que deseja consultar: ')
      livros_autor = [livro for livro in lista_livros if livro['autor'].lower() == autor_busca.lower()]
      if not livros_autor:
        print('Nenhum livro encontrado com o autor informado.')
      else:
        print('----------------')
        for livro in livros_autor:
          print(f"Id: {livro['id']}")
          print(f"Nome: {livro['nome']}")
          print(f"Autor: {livro['autor']}")
          print(f"Editora: {livro['editora']}")
          print('-' * 30)

    # Opção 4
    elif opcao == '4':
      break
    else:
      print('Por favor, escolha uma opção válida.')


# Função remover_livro
def remover_livro():
  while True:
    print('\n---MENU REMOVER LIVRO---')
    if not lista_livros:
      print('Livro não cadastrado.')
      return

    id_remover = input('Digite o id do livro a ser removido: ')

    livro_encontrado = False
    for i, livro in enumerate(lista_livros):
      if str(livro['id']) == id_remover:
        del lista_livros[i]
        print('Livro removido com sucesso!')
        livro_encontrado = True
        return

    if not livro_encontrado:
      print('Nenhum livro encontrado com o id informado.')


# Programa principal
print('\nBem-vindo à Livraria da Larissa de Santi')
while True:
  print('\n---MENU PRINCIPAL---')
  print('1 - Cadastrar Livro')
  print('2 - Consultar Livro(s)')
  print('3 - Remover Livro')
  print('4 - Sair')

  opcao = input('Escolha a opção desejada: ')

  if opcao == '1':
    cadastrar_livro(id_global)
  elif opcao == '2':
    consultar_livro()
  elif opcao == '3':
    remover_livro()
  elif opcao == '4':
    print('Obrigado por usar a Livraria da Larissa de Santi. Até mais!')
    break # Fecha o loop e encerra o programa
  else:
    print('Por favor, escolha uma opção válida.')
