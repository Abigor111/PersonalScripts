import requests
import os

# Pasta de destino
save_folder = 'D:/School/Exames/Matemática A/'

# Garantir que a pasta existe
os.makedirs(save_folder, exist_ok=True)

# Variações dos links
variations = [
    "EX-MatA635-F1-{year}.pdf",
    "EX-MatA635-F1-{year}-V1.pdf",
    "EX-MatA635-F1-{year}-V1-net.pdf"
]

# Loop para baixar os exames de 1997 a 2023
for year in range(1997, 2024):
    for variation in variations:
        url = f'https://iave.pt/wp-content/uploads/{year}/06/{variation}'.format(year=year)
        file_path = os.path.join(save_folder, f'Exame {year} - {variation.format(year=year)}')

        response = requests.get(url)

        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f'✅ Exame {year} ({variation.format(year=year)}) descarregado com sucesso!')
            break  # Para de tentar variações quando encontrar uma válida
        else:
            print(f'❌ Falha ao tentar {url}')
