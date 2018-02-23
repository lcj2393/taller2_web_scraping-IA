
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests

print ("ANALISIS SITIOS WEB")
URL = input("Digite el sitio web a Analizar: ")

#petición a la página web ingresada
req = requests.get(URL)

# Comprobamos que la petición nos devuelve un Status Code = 200 si es correcto.
estado = req.status_code
if estado == 200:

    # Parseo del sitio con BeautifulSoup()
    html = BeautifulSoup(req.text, "html.parser")

    # Devuelve los divs donde están las entradas requeridas
    entradas = html.find_all('head')

    # Recorremos todas las entradas para extraer el título
    for i, entrada in enumerate(entradas):
        
        # Con el método "getText()" no nos devuelve el HTML
        titulo = entrada.find('title').getText()
        
        # Imprimo el Título y URL de las entradas
        print("%d - %s" % (i+1, titulo))
        #Apertura del Archivo Tutulos.txt
        with open("titulos.txt") as f:
            for j, linea in enumerate(f):
                if titulo in linea:
                    j
                else:
                    with open("titulos.txt", "a") as archivo:
                        archivo.write("%s - " % (titulo))
                    archivo.close   
        #Cerrado del archivo Titulos.txt            
        f.close
        #Apertura del Archivo Paginas.txt
        with open("paginas.txt") as f:
            for k, linea in enumerate(f):
                if URL in linea:
                    k
                else:
                    with open("paginas.txt", "a") as archivo:
                        archivo.write("%s - " % (URL))
                    archivo.close
        #Cerrado del archivo Paginas.txt 
        f.close
else:
    print(estado, "URL No Valida.")

