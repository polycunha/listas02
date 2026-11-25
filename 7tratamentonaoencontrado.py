livros = [
    [1, "Dom Casmurro", "Machado de Assis", 1899],
    [2, "O Pequeno Principe", "Antoine de Saint-Exupéry", 1943],
    [3, "1984", "George Orwell", 1949]
]

id_procurado = 99
encontrado = False 

for livro in livros:
    if livro[0] == id_procurado:
        print("livro localizado!")
        encontrado = True
        break
    if not encontrado:
        print("livro nao encontrado")