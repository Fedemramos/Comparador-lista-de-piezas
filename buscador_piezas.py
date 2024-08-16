import pandas as pd

# Cargar los archivos Excel
archivo1 = 'file_o.xlsx'
archivo2 = 'file_cut.xlsx'

df1 = pd.read_excel(archivo1)
df2 = pd.read_excel(archivo2)

def lista_piezas(lista, nombre):
    print(nombre)
    count = 0
    for pieza in lista:
        print(pieza)
        count += 1    
    print(f"cantidad de piezas: {count}")


def piezas_faltantes(a, b):
    
    piezas_1 = set(a)
    piezas_2 = set(b)
    
    
    faltantes_en_2 = piezas_1 - piezas_2

    if len(faltantes_en_2) == 0:
        print("La lista esta completa, no le falta ninguna pieza")
    else:
        print("Piezas faltantes son: ")
        for pieza in faltantes_en_2:
            print(f"{pieza[0]} de {pieza[1]} maquina: {pieza[2]}")
        print(f"Cantidad de piezas {len(faltantes_en_2)}")

# Asumiendo que las listas de piezas están en las columnas 'Pieza', 'Espesor', y 'Maquina'
piezas_1 = list(zip(df1['Pieza'], df1['Espesor'], df1['Maquina']))
piezas_2 = list(zip(df2['Pieza'], df2['Espesor'], df2['Maquina']))

lista_piezas(piezas_1, "archivo original")
print()
lista_piezas(piezas_2, "piezas del cut")
print()
piezas_faltantes(piezas_1, piezas_2)
