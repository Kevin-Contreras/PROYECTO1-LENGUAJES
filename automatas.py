""" SE CREARA EL AUTOMATA"""
import re

arreglo2=[];
arreglo = []

print("INGRESE LOS NOMBRES DE LOS ARCHIVOS O EL NOMBRE DEL ARCHIVO")
archivos = input()
def automata (comandos):
  """ -------------------COMANDO 11 SCRIPT----------------------------------- """
  numero=0;
  numero2 =0;
  numero3 = 0;
  numero4 = 0;
  numero5=0;

  guardar = ""
  for comando in comandos:
    arreglo2.append(comando)
  for i in range(7):
    if(i<7): 
      arreglo2.pop(0)
      
  for e in arreglo2:
    if(e.find(",")==0):
      arreglo2.pop(numero2)
    numero2=numero2+1;
    
    if(arreglo2[numero4].isspace()==True):
      arreglo.append(guardar)
      
      guardar=""
      
    else:
      guardar= guardar + arreglo2[numero3];
      numero5 = numero5 +1;
      if(numero5<2):
        arreglo2.append(" ")
    numero3=numero3+1;
    numero4=numero4+1;
 
  print(arreglo)
  """ ------------------------COMANDO 11 SCRIPT------------------ """
automata(archivos);
