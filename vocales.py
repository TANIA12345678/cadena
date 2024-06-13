# Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.
def contar_vocales (cadena):
    
    vocales = "aeiou"
    
    contador = 0 
    
    for caracter in cadena :
        
        if caracter in vocales:
            contador += 1
            
    print (f"El numero de vocales en la cadena es : {contador} ")

# Solicitar la cadena al usuario
cadena = input("Ingrese una cadena: ")
contar_vocales(cadena)
    
    
    