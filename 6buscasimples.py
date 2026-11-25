livros = [
    [1, "Dom Casmurro", "Machado de Assis", 1899],
    [2, "O Pequeno Principe", "Antoine de Saint-Exupéry", 1943],
    [3, "1984", "George Orwell", 1949]
]

titulo_procurado = "1984"

for livro in livros:

    if livro[1] == titulo_procurado:
        print("livro localizado!")
        break