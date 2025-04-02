# **Sistema de Cadastro para Livraria**
---
Atividade prática desenvolvida para a disciplina de **Lógica de Programação e Algoritmos** do Bacharelado em Engenharia de Software.

---
### Objetivos
Implementar um sistema de cadastro de livros para uma livraria:
- Adicionar, alterar e deletar itens do acrevo.
- Implementar consulta por ID único.
- Criar e manipular variáveis globais:

```python
lista_livros = [] # Lista de dicionários para armazenar livros
id_global = 0 # Contador para id dos livros
```

---
### Competências Desenvolvidas
- Variáveis globais.
- Estrutura e manipulação de dados.
- Funcionalidades CRUD.

```python
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
```

---
### Execução do Programa
![Saída de console esperada](https://github.com/larisanti/py-livraria-cadastro/blob/main/outputs/1.png)

---
### Como Executar
```bash
python3 livraria_cadastro.py
```
