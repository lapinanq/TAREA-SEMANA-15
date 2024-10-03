#CREACION DE UN DICCIONARIO
persona = {
    "Nombre": "Liliana",
    "Apellido": "Piñan",
    "Edad": 39,
    "Sexo": "M",
    "Ciudad": "Shushufindi"
}

#obtener valores
print("Nombre:", persona ["Nombre"])
print("Apellido:", persona ["Apellido"])
print("Edad:", persona ["Edad"])
print("Sexo:", persona ["Sexo"])
print("Ciudad:", persona ["Ciudad"])

#modificar
persona ["Ciudad"]= "Quito"
print(persona)

#agregar nuevo par - clave
persona["Profesion"]= "Auxiliar Contable."
print("todo :", persona)

persona["Telefono"]= "454545454"
print("todo :", persona)

#eliminar par clave
del persona ["Edad"]
print("todo :", persona)

#imprime claves
Claves = persona.keys()
print("Iprime las Claves", Claves)

#imprime valores
Valores= persona.values()
print("Imprime los Valores", Valores)

#recorrer un for
for clave,valor in persona.items():
    print(clave," : ", valor)




