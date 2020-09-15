try: 

    import requests 

except ImportError: 

    os.system('pip install requests') 

    print('Installing requests...') 

    print('Ejecuta de nuevo tu script...') 

    exit()
try: 

    import os 

except ImportError: 

    os.system('pip install os') 

    print('Installing os...') 

    print('Ejecuta de nuevo tu script...') 

    exit()
try: 

    import sys 

except ImportError: 

    os.system('pip install sys') 

    print('Installing sys...') 

    print('Ejecuta de nuevo tu script...') 

    exit() 
try: 

    from bs4 import BeautifulSoup as bs 

except ImportError: 

    os.system('pip install bs4') 

    print('Installing bs4...') 

    print('Ejecuta de nuevo tu script...') 

    exit() 
try: 

    import webbrowser 

except ImportError: 

    os.system('pip install webbrowser') 

    print('Installing webbrowser...') 

    print('Ejecuta de nuevo tu script...') 

    exit() 

## Homero Alejandro Martínez Díaz

## Este script pregunta dos numeros al usuario que seran los limites del rango de paginas en las que se buscaran noticias en donde se mencione o tengan que ver
## con la dependencia la cual tambien es pedida al usuario, posteriormente si se encuentran paginas que contengan la dependencia introducida son abiertas en el
## buscador predeterminado del usuario y continuara buscando hasta que llegue al limite introducido para despues cerrar el script, si no encuentra ninguna pagina
## se imprime que no se encontro.

print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
    

