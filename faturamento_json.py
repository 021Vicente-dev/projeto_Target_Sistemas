import json

# Carregar o arquivo JSON
with open('dados.json', 'r') as file:
    dados = json.load(file)

# Filtrar dias com faturamento maior que zero
valores = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Calcular o menor, maior e a média
menor = min(valores)
maior = max(valores)
media = sum(valores) / len(valores)

# Contar os dias acima da média
dias_acima_media = sum(1 for valor in valores if valor > media)

# Exibir resultados
print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
