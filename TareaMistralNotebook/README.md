# Tarea - Mistral

# Descripción del Proyecto
Este proyecto consiste en un "chatbot conversacional" capaz de responder preguntas en lenguaje natural sobre un archivo de ventas llamada ('sales_data_sample.csv').
El chatbot utiliza un "agente de pandas" con "Mistral AI" y "LangChain" para interpretar preguntas, generar código pandas y devolver respuestas precisas.

---

# Modelo utilizado en el Proyecto
- Modelo: Mistral Small 24B ('mistral-small-latest')

---

# Tecnologías utilizadas
| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.10 | Lenguaje de programacion |
| Pandas | 2.0 | Manipulación de datos |
| LangChain | 0.1 | Framework para agentes de IA |
| Mistral AI | 'mistral-small-latest' | Modelo de lenguaje |
| Google Colab | - | Entorno de ejecución |

---

# Estructura del Proyecto
```
TareaMistralNotebook/
├── Tarea_Mistral_fecha_18_05.ipynb   # Notebook principal con el agente
├── README.md                      # Este archivo
└── sales_data_sample.csv              # Dataset de ventas 
```

---

# Cómo ejecutar el Proyecto
1. Clonar el reporsitorio
git clone https//:github.com/denisanna97-rgb/Tarea-Mistral.git

2. Abrir en Google Colab
- Ve a colab.research.google.com 
- Abre el archivo Tarea_Mistral_fecha_18_05.ipynb

3. Configurar API Key de Mistral
- Ve a Mistral AI Console y create una cuenta gratuita
- Crea una API Key
- En Colab, ve a Secrets para guardarlo y agrega Mistral_API_KEY

4. Ejecutar todas las celdas 

---

# Ejemplos de preguntas para realizarle al chatbot
- "¿Cuántas filas tiene el dataset?"
- "¿Cuál es el total de ventas?"
- "¿Qué producto fue el más vendido en 2003?"
- "¿Cuáles son los 5 clientes que más compraron?"
- "¿Cuál es el promedio de ventas por país?

---

# Resultados del Proyecto
| Tipo de pregunta | Ejemplo | Resultado |
|------------------|---------|-----------|
| Básica | "¿Cuántas filas tiene el dataset | Respuesta correcta |
| Cálculo | "¿Cuál es el total de ventas"? | Cálculo exacto |
| Agrupación | "¿Qué producto fue el más vendido | Identificó el producto correcto | 
| Temporal | "¿Cuál fue el año más vendido?" | Respuesta precisa |
| Múltiple | "¿Cuáles son los 5 clientes que más compraron?" | Lista correcta |

---

# Autora
Anna Denis = denisanna97-rgb 