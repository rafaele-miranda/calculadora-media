nome = str(input(f"Digite seu nome: "))
idade = int(input(f"Digite sua idade: "))

nota1 = float(input(f"Digite a primeira nota: "))
nota2 = float(input(f"Digite a segunda nota: "))
nota3 = float(input(f"Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
situacao = "Aprovado(a)" if media >= 7 else "Reprovado(a)"

print(f"Nome: {nome}\n"
      f"Idade: {idade}\n"
      f"Notas: {nota1}, {nota2}, {nota3}\n"
      f"Situação: {situacao}")