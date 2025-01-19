import xml.etree.ElementTree as ET

# Carregar o arquivo XML
tree = ET.parse('dados.xml')
root = tree.getroot()  # Certifique-se de que 'root' corresponde ao nome do elemento raiz

# Extrair os valores de faturamento
valores = [float(row.find('valor').text) for row in root.findall('row') if float(row.find('valor').text) > 0]

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
