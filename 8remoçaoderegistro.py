livros = [
    [1, "Dom Casmurro", "Machado de Assis", 1899],
    [2, "O Pequeno Principe", "Antoine de Saint-Exupéry", 1943],
    [3, "1984", "George Orwell", 1949]
]

id_remover = 2 

indice_para_remover = -1

for indice, livro in enumerate(livros):
    if livro[0] == id_remover:
        indice_para_remover = indice
        break
    if indice_para_remover != -1:
        livros.pop(indice_para_remover)

    print(livros)