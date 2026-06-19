# Predicción de Apariciones de Personajes Marvel/DC

# Descripción de este proyecto
Este proyecto implementa 3 agentes que trabajan en secuencia para predecir el número de "apariciones en cómics" de los personajes de Marvel y DC utilizando Machine Learning.

# Los 3 Agentes
| Agente | Función | Entrada | Salida |
|--------|---------|---------|--------|
| Agente 1 - Normalizador | Limpia, emputa, escala y codifica los datos | Datos sin procesar | Datos procesados y limpios|
| Agente 2 - Entrenador | Aplica validación, entrena y selecciona modelo | Datos procesados y limpios | Métricas + modelo|
| Agente 3 - Comunicador | Genera reporte en lenguaje natural | Métricas + modelo | Reporte explicativo en texto |

---


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
| Herramienta | Versión | Uso |
|-------------|---------|-----|
| Python | 3.10 | Lenguaje principal utilizado en programación | 
| Pandas | 2.0.3 | Se utiliza para la manipulación y limpieza de datos |
| NumPy | 1.24.3 | Se utiliza para las manipulaciones matemáticas y arrays |
| Scikit-learn | 1.3.0 | Se utiliza para Machine Learning y preprocesamiento | 
| Random Forest Regressor | - | Utilizado para el Modelo de predicción |

---

# Estructura del Proyecto
```
Tarea-Mistral/
│
├── CarpetaTareaAgentes/         
│ ├── agente_1_normalizador.py           
│ ├── agente_2_entrenador.py
│ ├── agente_3_comunicador.py 
│ ├── main.py 
│ ├── requirements.txt 
│ └── README.md 
│
├── data/ 
│ └── 07_Marvel_DC_Comic_Characters.csv
│
├── README.md 
│
└── Tarea_Mistral_fecha_18_05.ipynb 
```

---

# Cómo ejecutar el proyecto
1. Clonar el reporsitorio
git clone https://github.com/denisanna97-rgb/Tarea-Mistral.git

2. Instalar dependencias
pip install -r requirements.txt 

3. Ejecutar el proyecto
python main.py 

---

# Resultados del Proyecto
El modelo de Random Forest Regressor entrega las siguientes métricas:
| Métrica | Interpretación |
|---------|----------------|
| R² | Porcentaje de variabilidad explicada por el modelo |
| MAE | Error promedio en número de apariciones |
| RMSE | Error cuadrático medio (penaliza errores grandes) |

---

# Ejemplo de Reporte Generado
Rendimiento del modelo
- Validación Cruzada (5 folds):
 - R² promedio: 0.6234 (62.34%)

Evaluación en Datos de Prueba:
 - Error promedio (MAE): 42.15 apariciones

---

# Los factores más importantes
1. Primera Aparición / Año: 35.2%
2. Editorial: 18.7%
3. Alinear: 12.4%
4. Vivo: 8.9%
5. ID: 7.6%

---

# Autora
Anna Denis: denisanna97-rgb
