livros = [
    [1, "Dom Casmurro", "Machado de Assis", 1899],
    [2, "O Pequeno Principe", "Antoine de Saint-Exupéry", 1943],
    [3, "1984", "George Orwell", 1949]
]

for livro in livros: 
    id_livro, titulo, autor, ano = livro
    print(f"ID: {id_livro} | o livro \"{titulo}\" foi escrito por {autor} em {ano}.")