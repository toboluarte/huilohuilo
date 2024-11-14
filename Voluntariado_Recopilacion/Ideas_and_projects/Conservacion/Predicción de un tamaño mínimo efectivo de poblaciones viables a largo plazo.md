---
Fecha: 23-06-2022
Locacion: España, Vigo
Institución: Centro de investigación Mariña, Universidad de Vigo, Facultad de Biología, España
Autor: Noelia Perez-Pereira, Jinliang Wang, Huberto Quesada, Armando Caballero
Estado del trabajo: Terminado
Revista: Biodiversity and Conservation
---
#Conservacion #simulación #Computacional

# Resumen
En conservación se ha utilizado el tamaño mínimo viable (MVP) para determinar los riesgos de extinción de las poblaciones y especies. Un consenso para este número es de 50/500 individuos ha sido adquerido, <mark style="background: #FFF3A3A6;">50 es el número de población para evitar la depresión de reproducción en el corto plazo y 500 para sobrevivir en largo plazo </mark>, sin embargo, las cargas reproductivas observadas en la naturaleza han llevado a pensar que estos números deben ser doblados. La purga de mutaciones deleterias puede ser un factor relevante al momento de considerar la re evaluación de estos números. Recientes estudios de simulación sugieren que el número de la población mínima viable se encontraría entre medio. En este estudio realizaron simulaciones de poblaciones bajo la acción de la purga, deriva, mutaciones nuevas y efectos ambientales en el fitness para investigar los tiempos de extinción y la perdida de diversidad genética. Los resultados indican que la purga puede reducir el número de la población mínima viable para persistir en el largo plazo, con estimaciones que se acercan a los 500 indiviudos para especies con tasas de reproducción moderadamente largas y al rededor de 1000 cuando las especies tienen tasas reprductivas bajas
# Introducción
En un mundo donde la biodiversidad éstá decayendo y la actividad humana tiene una presencia impositiva, los <mark style="background: #FFF3A3A6;">indicadores de la resilencia de las poblaciones son necesarios para la administración genética y los planes de conservación para especies en riesgo</mark>, uno de estos indicadores es la población mínima viable, que es la población requerida para evitar la extinción de una población en un determinado tiempo.
Existen diferentes variantes de la población mínima viable, algunas definiciones que dependen de la capacidad de carga, el tamaño de población adulta mínimo. Este número es el tamaño de una población que puede tener el mismo número de endogamia y deriva geníca que la población original. 
Debemos recordar que este número tiene un componente de largo plazo y uno de corto plazo, el de corto plazo está afectado por el decremento en el fitness por endogamia, respecto a la población mínima a largo plazo, una vez que la población haya lidiado con la depresión endogamica y sobrevivido, la perdida de potencial adaptativo por deriva geníca compromete la habilidad de la población de enfrentar cambios ambientales futuros y así la habilidad de persistir en el largo plazo.
La diversidad genética y por tanto el potencial adaptativo se pierde a una tasa de 1/2Ne por generación por deriva en poblaciones aisladas. Con el paso del tiempo se alcanzan equilibrios, donde esta perdida es compensada por la nueva entrada de variedad genética, el establecimiento de la población mínima viable a largo plazo depende de este equilibrio.

# Hipótesis
# Objetivos
## Generales
## Específicos

# Metodología
Se llevaron a cabo simulaciones de poblaciones de diferentes tamaños para evaluar los tiempos de extinción bajo diferentes modelos mutacionales. El proceso de simulación consiste en 2 pasos. Primero se simuló una población grande en el equilibrio entre mutación-selección y deriva para crear poblaciones base grandes con una carga dada de endogamia "B", luego se simularon multiples lineas de diferentes tamaños derivadas de las poblaciones grandes y se mantuvieron por un largo numero de generaciones bajo la acción de selección, deriva, nuevas mutaciones y efectos ambientales en el fitness. El tiempo de extinción, diversidad genética, carga de endogamia y otras propiedades de las lineas sobre las generaciones fueron registradas y analizadas en relación al mvp.
## Modelo genómico y parámetros mutacionales
El genoma consistia de 30.000 locus bi alélicos, de los cuales 1000 eran neutrales y el resto tenian efectos deleterios en el fitness (Alrededor de 28000 locus segregantes deleterios). Asumieron un tamaño de genoma de L =20 Morgans, las mutaciones deleterias surgían a tasa U por genoma haploide y generación. Con coeficiente de selección s obtenido de la distribución gama con forma de parámetro B, coeficiente de dominancia h, obtenido de la distribución uniforme entre 0 y e^-ks, donde k es una constate utilizada para obtener la media del coeficiente de dominancia. Una tasa de mutación Ul fue incluido para agregar una clase de mutación letal (s=1 y h = 0.02). El fitness de un individuo fue calculado multiplicativamente a lo largo del loccus. Se asumió selección suave, en el sentido que la selección actuó sobre el fitness relativo, obtenido dividiendo el fitness de cada individuo en la generación t por el promedio del fitness de la población en la generación 0. La carga de endogamia fue calculada como la suma para todos los loccus de s(1-2h)pq, donde p y q =1-p son la frecuencias alélicas de natural y mutante.
Adoptaron 2 modelos mutacionales, ambos basados en evidencia empirica.

### Modelo 1
La tasa de mutación U fue obtenida desde Keightley para humanos, el coeficiente de selección promedio S y la forma del parámetro B desde Boyko 2008 para mutaciones no sinonimas en humanos, el coeficiente de dominancia medio H fue obtenido de la acumulación de mutaciones en Drosophila Caenorhabditis y levadura (Caballero 2020)
### Modelo 2
Corresponde a un modelo de Caballero 2017. dado que la tasa de endogamia generalmente es encontrada en la naturaleza es de alrededor B= 6, modificaron el U original para ambos modelos de manera que la tasa de mutación finalmente aplicada se aproximara al valor B de las poblaciones B.

Aún cuando ambos modelos asumen bajo efecto de la edad sobre el fitness y el mismo coeficiente de dominancia, difieren principalmente en los valores de las distribuciones de S y H. Estando el modelo 1 caracterizado por una proporción más grande de pequeños efectos de mutación y efectos más pequeños de los coeficientes de dominancia por locus. Mientras que el modelo 2 incluye mutaciones de efectos moderados y una mayor dominancia de los coeficientes de dominancia,  los que pueden ser más facilmente eliminados por purga. Ambos modelos incluyen adicionalmente la misma tasa de mutaciones letales
## Simulación de las poblaciones
10 replicas de las poblaciones bases fueron simuladas por modelo, las cuales se mantuvieron con apareo aleatorio, sin auto reproducción a un tamaño constante de Nb= 10.000 durante 10.000 generaciones.
Para cada población base, una muestra de N individuos variando de 25-1700 llamada Linea, fue obtenida y mantenida durante 1000 generaciones para evaluar el riesgo de extincion y la perdida de diversidad genética medida como la media de heterocigocidad (H).
Para cada escenario, 100 lineas replicas fueron simuladas por población base, un total de 1000 lineas por modelo y escenario cuyos resultados fueron promediados.
El fitness individual fue asumido estar compuesto por 2 rasgos, fertilidad (número de crías producidas, determinado por 1/3 de los loccus simulados) y viabilidad (probabilidad de supervivencia, determinada por 2/3 de los locis simulados). El fitness global fue el producto de la fecundidad (Wf) y viabilidad (Wv). Esto resulto en una carga endogámica inicial de Bf = 2 para la fertilidad y Bv= 4 para la viabilidad  
# Resultados
Las extinciones fueron frecuentes bajo los 2 modelos mutacionales evaluados, particularmente para las lineas con poblaciones efectivas pequeñas y bajas tasas reproductivas. El segundo modelo en general incurrió en más extinciones que el modelo 1. Los tiempos de extincioón eran considerabblemente más cortos en promedio, especialmente cuando las tasas reproductivas eran bajas. En estos casos, todas las poblaciones se extinguieron en las primeras 25 generaciones, independiente de la población inicial Ne y el modelo mutacional. Estas generaciones fueron caracterizadas por depresión endogamica y una larga reducción del tamaño efectivo
## Retención de diversidad genética
En los programas de reproducción en cautiverio es un objetivo común mantener el 90% de la diversidad genética intra población por 100 años. Aún cuando no se simuló el tiempo en años, este objetivo puede pensarse en la generación 40 (figura 4 , linea roja punteada), bajo las condiciones particulares del modelamiento el tamaño efectivo para lograr esto es alrededor de 240 para el modelo 1 y 420 para el modelo 2
# Figuras relevantes


![[Pasted image 20241112225326.png]]
![[Pasted image 20241112225552.png]]
![[Pasted image 20241112225926.png]]
# Conclusiones
