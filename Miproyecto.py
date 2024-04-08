# Hola, este programa tiene como objetivo analizar y extraer información relevante de una página web sobre ciberseguridad.


import requests  # Importa la librería requests para realizar solicitudes HTTP
from bs4 import BeautifulSoup  # Importa BeautifulSoup para analizar el contenido HTML
from fpdf import FPDF  # Importa FPDF para generar el reporte en formato PDF

# Define una clase PDF que hereda de FPDF para personalizar el formato del PDF

class PDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agrega las fuentes 'DejaVu' al PDF para utilizarlas en el texto
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', uni=True)
        self.add_font('DejaVu', 'I', 'DejaVuSansCondensed-Oblique.ttf', uni=True)
        self.set_font('DejaVu', '', 14)  # Establece la fuente predeterminada del PDF

    # Define el encabezado del PDF
    def header(self):
        self.set_font('DejaVu', 'B', 12)
        self.cell(0, 10, 'Reporte de Análisis de Contenido Web', 0, 1, 'C')

    # Define el pie de página del PDF
    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

# Define una función para generar el reporte en formato PDF
def generar_reporte_pdf(informacion_relevante, nombre_archivo='reporte_web.pdf'):
    pdf = PDF()  # Crea una instancia de la clase PDF
    pdf.add_page()  # Añade una página al PDF
    for info in informacion_relevante:
        # Ajusta los márgenes y utiliza multi_cell para añadir texto al PDF
        pdf.set_margins(10, 10, 10)
        pdf.multi_cell(0, 10, info, 0, 1)
    pdf.output(nombre_archivo, 'F')  # Guarda el PDF con el nombre especificado

# Define una función para analizar el contenido web en busca de palabras clave
def analizar_contenido_web(url, palabras_clave):
    try:
        response = requests.get(url)  # Realiza una solicitud GET a la URL proporcionada
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
    except requests.ConnectionError:
        print('Error de conexión a la página.')
        exit()
    except requests.HTTPError as e:
        print(f'Error HTTP: {e}')
        exit()

    if response.status_code == 200:  # Verifica si la respuesta es válida (código 200)
        soup = BeautifulSoup(response.text, 'html.parser')  # Utiliza BeautifulSoup para analizar el HTML
        elementos = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'meta'])  # Encuentra elementos relevantes en el HTML
        informacion_relevante = []  # Lista para almacenar la información relevante encontrada

        for elemento in elementos:
            texto_elemento = elemento.text if elemento.name != 'meta' else elemento.get('content', '')  # Obtiene el texto del elemento HTML
            if any(palabra.lower() in texto_elemento.lower() for palabra in palabras_clave):  # Verifica si alguna palabra clave está presente en el texto
                informacion_relevante.append(f'Información relevante encontrada: {texto_elemento}')  # Agrega la información relevante a la lista
        return informacion_relevante  # Devuelve la lista de información relevante
    else:
        print(f'Error al obtener la página: {response.status_code}')
        return []  # Si ocurre un error, devuelve una lista vacía
    
  # Programa principal
    
if __name__ == "__main__":
    # Solicita al usuario que ingrese la URL de la página web a analizar
    url = input('Introduce la URL: ')

    # Palabras clave a buscar en el análisis de contenido
    palabras_clave = ['ciberseguridad', 'seguridad informática', 'ataque cibernético', 'hackeo', 'ataque informático', 'ataque de inteligencia artificial', 'ataque de inteligencia', 'robo de datos', 'robo de información', 'ciberdelincuencia', 'ciberdelincuente']

    # Realiza el análisis del contenido de la página web y obtiene la información relevante
    informacion_relevante = analizar_contenido_web(url, palabras_clave)

    # Genera un reporte en formato PDF con la información relevante encontrada
    if informacion_relevante:
        generar_reporte_pdf(informacion_relevante)
    else:
        print("No se encontró información relevante.") # Si no se encontró información relevante


#Fin del programa