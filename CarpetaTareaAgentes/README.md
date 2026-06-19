# Predicción de Apariciones de Personajes Marvel/DC

# Descripción de este proyecto
Este proyecto implementa 3 agentes que trabajan en secuencia para predecir el número de "apariciones en cómics" de los personajes de Marvel y DC utilizando Machine Learning.

# Los 3 Agentes
 ____________________________________________________________________________________________________________________________
| Agente                  | Función                                       | Entrada                    | Salida             |
|_________________________|_______________________________________________|____________________________|____________________|
| Agente 1 - Normalizador | Limpia, imputa, escala, codifica              | Datos sin procesar         | Dataset limpio     |
| Agente 2 - Entrenar     | Aplica validación, entrena, selecciona modelo | Datos procesados y limpios | Métricas + modelo  |
| Agente 3 - Comunicador  | Genera reporte en lenguaje natural            | Métricas + modelo          | Reporte explicativo|
|___________________________________________________________________________________________________________________________|

# La finalidad de este proyecto es
Predecir cuántas "apariciones en cómics" tendrá un personaje basándose en estas características:
- Editorial: Marvel o DC
- Alineación: Bueno, Malo, Neutral o Reformado
- Estado de identidad: Secreto, Público o Conocido
- Características físicas: Color de ojos, color de cabello, sexo
- Año de la primera aparición: Cuándo debutó el personaje
- Estado actual: Vivo o fallecido 
- Grupo LGBT: Si pertenece a esa comunidad 

# Tecnologías utilizadas de este proyecto
 ___________________________________________________________________________________________
| Herramienta             | Versión | Uso                                                   |
|_________________________|_________|_______________________________________________________|
| Python                  | 3.10    | Es un lenguaje principal utilizada de la programación |
| Pandas                  | 2.0.3   | Se utiliza para la manipulación y limpieza de datos   |
| NumPy                   | 1.24.3  | Se utiliza para las operaciones matemáticas y arrays  |
| Scikit-learn            | 1.3.0   | Se utiliza para Machine Learning y preprocesamiento   |
| Random Forest Regressor |   -     | Utilizado para el Modelo de predicción                |  
|___________________________________________________________________________________________|

