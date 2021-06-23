#!/usr/bin/env python
'''
JSON ETL [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"
import json
from typing import Counter
import requests
from requests.api import request

from requests.models import Response

def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->

    json_persona = {
                    "nombre":"Marcos",
                    "apellido":"ludueña",
                    "dni": 34559619,
                    "Prenda":[
                        {
                            "tipo":"pantalon",
                            "cantidad":5
                            
                        },
                        {
                            "tipo":"remera",
                            "cantidad":6
                        },
                        {
                            "tipo":"Medias",
                            "cantidad":5
                        },
                        {
                            "tipo":"camperas",
                            "cantidad":8
                        }
                    ]

    }

      
    with open ('json_persona.json','w') as jsonfile:
        
        json.dump(json_persona,jsonfile, indent=4)
    print(json_persona)

   
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado
    


def ej2():
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    with open ('json_persona.json','r') as jsonfile:
        data= json.load(jsonfile)
    
    json_strings = json.dumps(data,indent=4)
    print (json_strings)
    
    

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1
    


def ej3():
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de torta.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    response = requests.get(url)
    data = response.json()
    

               
    usuarios_completed = {}
    for i in range(len(data)):
        variable = data[i]
        userid= variable['userId']
        completed = variable['completed']

        if (userid in data) == False :
            usuarios_completed['userId ='+ str(userid)]  =0
        if (completed in data) ==True:
                usuarios_completed['userId ='+ str(userid)]  +=1
            




        
        #for variable in data:
        #    if variable.get('completed') == usuarios_completed.get:
        
        #        usuarios_completed['userId ='+ str()]  +=1
                

    print(usuarios_completed) 


                
      



    

            
            


            

           






if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    ej3()
