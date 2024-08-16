# Comparador de Piezas

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-yellowgreen)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)

## Descripción
Este proyecto se realizo con el fin de solucionar le incoveniente de revisar manualmente pieza por pieza, a la hora de enviar a procesar y fabricar las piezas demandadas. Existia el problema que luego de modelar
y diseñar las maquinas, se proceguia a procesar las piezas para enviar a cortar y fabrica, en dicho paso siempre existia el error de saltearse alguna pieza, lo que generaba que faltaran a la hora de fabrica y eso generar incovenientes en la produccion y demoras. 
Esta aplicacion se realizo con el fin de solucionar y automatizar este proceso repetitivo.

**Comparador de Piezas** es una aplicación gráfica desarrollada en Python utilizando Tkinter que permite comparar dos listas de piezas provenientes de archivos Excel. 
La aplicación muestra las piezas faltantes y presenta ambas listas de manera ordenada en columnas, permitiendo una visualización clara de las diferencias.

## Características

- **Carga de Archivos Excel**: Carga dos archivos Excel, uno como referencia y otro para comparar.
- **Comparación Automática**: Detecta y muestra las piezas que están presentes en la lista original pero que faltan en la lista a comparar.
- **Interfaz Gráfica**: Interfaz amigable y moderna con soporte para modo oscuro.
- **Soporte de Imagen**: Incluye la posibilidad de mostrar un logotipo personalizado.

## Capturas de Pantalla

![Captura de pantalla 2024-08-16 175647](https://github.com/user-attachments/assets/7e6c83bb-c545-49ae-afa8-6e97342e0323)

![Captura de pantalla 2024-08-16 175713](https://github.com/user-attachments/assets/372b4bc4-72bd-4685-979a-7e77e011a4f6)

![Captura de pantalla 2024-08-16 180027](https://github.com/user-attachments/assets/9271cd5b-9ecb-483b-9e4b-09230d91ba54)


## Requisitos

- Python 3.8+
- Pandas
- Tkinter
- Pillow

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tuusuario/comparador-de-piezas.git
    ```
2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:
    ```bash
    python comparador_de_piezas.py
    ```
2. Carga el archivo Excel original.
3. Carga el archivo Excel a comparar.
4. Visualiza los resultados en la interfaz.

## Estructura del Proyecto

```plaintext
comparador-de-piezas/
│
├── comparador_de_piezas.py  # Código principal de la aplicación
├── README.md                # Archivo que estás leyendo
├── requirements.txt         # Dependencias del proyecto
└── logo.png                 # Logotipo utilizado en la interfaz
