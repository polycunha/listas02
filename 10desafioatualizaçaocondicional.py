funcionarios = []
funcionarios.append([1, "Ana Silva", "Desenvolvedora", 4500.00])
funcionarios.append([2, "Carlos Souza", "Analista de Suporte", 3200.00])

for i, funcionario in enumerate(funcionarios):
    if funcionario[0] == 2:
        funcionarios[i][3] += 500.00
        print(f"Salario atualizado com sucesso! Novo salario de {funcionarios[i][1]}: R$ {funcionarios[i][3]:.2f}")
        break