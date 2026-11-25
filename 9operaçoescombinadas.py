funcionarios = []

funcionarios.append([1, "Ana Silva", "Desenvolvedora", 4500.00])
funcionarios.append([2, "Carlos Souza", "Analista de Suporte", 3200.00])

for funcionario in funcionarios:
    id_func, nome, cargo, salario = funcionario
    print(f"ID: {id_func} | Nome: {nome} | Cargo: {cargo} | Salario: R$ {salario:.2f}")