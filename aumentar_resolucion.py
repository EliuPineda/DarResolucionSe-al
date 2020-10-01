import pandas as pd
import matplotlib.pyplot as plt


#Multiplicador de resolucion
multiplicador_resolucion = 8

#Leyendo datos
datos = pd.read_csv("DATA_parcial.csv", ";")

#Creando dataframe de salida
datos_out = pd.DataFrame({   
    "n" : [],
    "t" : [],
    "no" : []
    })

#Crear dataframe vacio
for i in range(len(datos)*multiplicador_resolucion-(multiplicador_resolucion-1)):
    datos_out = datos_out.append({'n': i+1}, ignore_index=True)

#Pongo  datos repartidos con el espacio
for i in range(0, len(datos), 1):
    datos_out.t[i*multiplicador_resolucion] = datos.t[i]
    datos_out.no[i*multiplicador_resolucion] = datos.no[i]
    
#Hago una interpolacion de tipo lineal así no deberia afectar los resultados   
datos_out = datos_out.interpolate(method = "linear") 
    
#Print
linea0 = []
for i in range(0, len(datos)*multiplicador_resolucion-(multiplicador_resolucion-1),1):
    linea0.append(0)
plt.plot(datos_out.t, datos_out.no)
#plt.plot(datos.t, datos.no)
plt.plot(datos_out.t, linea0)
plt.show()

#Save new csv
#datos_out.to_csv("C:/Users/ELIU/Desktop/9_Semestre/Rios y Costas/CNM/resolutionplus.csv", header = True, index = False, sep = ";")
datos_out.to_csv("resolutionplus.csv", header = True, index = False, sep = ";")
