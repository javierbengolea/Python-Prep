import os
import shutil

montañas = {
    "nombre": [
        "Everest",
        "K2",
        "Kanchenjunga",
        "Lhotse",
        "Makalu",
        "Cho Oyu",
        "Dhaulagiri",
        "Manaslu",
        "Nanga Parbat",
        "Annapurna I",
    ],
    "orden": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "cordillera": [
        "Himalaya",
        "Karakórum",
        "Himalaya",
        "Himalaya",
        "Himalaya",
        "Himalaya",
        "Himalaya",
        "Himalaya",
        "Karakórum",
        "Himalaya",
    ],
    "pais": [
        "Nepal",
        "Pakistán",
        "Nepal",
        "Nepal",
        "Nepal",
        "Nepal",
        "Nepal",
        "Nepal",
        "Pakistán",
        "Nepal",
    ],
    "altura": [8849, 8611, 8586, 8516, 8485, 8188, 8167, 8163, 8125, 8091],
}

titulos = list(montañas.keys())
# print(", ".join(titulos))

valores = list(montañas.values())
# l_ocurrencias = len(valores)
# l_titulos = len(valores[0])

# # for i in range(l_titulos):
# #     for j in range(l_ocurrencias):
# #         print(valores[j][i], end=", ")
# #     print()


titulos = ", ".join(titulos) + "\n"

# for i in list(zip(*valores)):
#     texto_guardar += ", ".join(map(str, i))
#     texto_guardar += "\n"

file_name = "montañas.csv"

with open(file_name, "w", encoding="utf8") as f:
        f.write(titulos)
        for i in list(zip(*valores)):
                f.write(", ".join(map(str, i)) + "\n")

f.close()

new_dir = "clase09_montañas_altas"

print(os.path.getsize(file_name))

if not os.path.exists(new_dir):
    os.mkdir(os.path.join(os.getcwd(), "clase09_montañas_altas"))
    
source = ''
destination = new_dir

command = f"copy {file_name} {destination}"
print(command)
# shutil.move(file_name, destination)
os.system(command)

for i in os.listdir(new_dir):
    print(i)

