#En este documento .py se iniciará el estudio del lenguaje de programación python. 

#*************************
from Persona import Persona


a:int = 0 #Esta es la forma de declarar variables y su tipo en Python. 
print(a)

#*************************


lista = [] #Declaración de la lista.
lista_1 = ["Carlos","Javier","Bolaños","Riascos"] #Declaración lista homogénea.
lista_2 = ["Carlos",19,2003,"Ing Sis", False] #Declaración de lista  heterogénea.
print(lista)
print(lista_1)
print(lista_2)


#Métodos sobre listas

print(lista_1.clear()) #El método clear borra todos los elementos de una lista.
print("tamaño lista 1 : " + str(len(lista_1))) #El método len retorna el tamaño de una lista.


#************ Creación de instancia de la clase persona

persona_1 = Persona("carlos",19,"España")
print(persona_1.name)
print(persona_1.age)
print(persona_1.country)

list_new = list()

list_new.insert(0,persona_1)
print(len(list_new))






