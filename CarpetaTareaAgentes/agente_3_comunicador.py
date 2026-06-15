"""
AGENTE 3 - COMUNICADOR
Función: genera reporte en lenguaje natural
Salida: reporte en texto
"""

import pandas as pd


class Agente3Comunicador:
    def __init__(self, resultados, target_col, X):
        self.resultados = resultados
        self.target = target_col
        self.X = X
        self.metricas = resultados['metricas']
        self.modelo = resultados['modelo']
    
    def generar_reporte(self):
        print("\n→ genera reporte en lenguaje natural")
        
        r2 = self.metricas['r2']
        mae = self.metricas['mae']
        cv_mean = self.metricas['validacion_cruzada']['media']
        
        importancias = self.modelo.feature_importances_
        imp_df = pd.DataFrame({'Característica': self.X.columns, 'Importancia': importancias})
        imp_df = imp_df.sort_values('Importancia', ascending=False)
        
        reporte = f"""

              REPORTE EN LENGUAJE NATURAL                       
         Predicción de {self.target} - Marvel/DC                 


OBJETIVO DEL MODELO

Este modelo predice cuántas apariciones en cómics tiene un personaje de Marvel o DC, basándose en sus características.

RENDIMIENTO DEL MODELO


Validación Cruzada (5 folds):
   • R² promedio: {cv_mean:.4f} ({cv_mean*100:.2f}%)
   
Evaluación en Datos de Prueba:
   • R²: {r2:.4f} ({r2*100:.2f}%)
   • Error promedio (MAE): {mae:.2f} apariciones

INTERPRETACIÓN


"""

        if r2 > 0.7:
            reporte += "✓ EXCELENTE: El modelo explica más del 70% de la variabilidad.\n"
        elif r2 > 0.5:
            reporte += "✓ BUENO: El modelo explica más del 50% de la variabilidad.\n"
        elif r2 > 0.3:
            reporte += "✓ MODERADO: El modelo explica más del 30% de la variabilidad.\n"
        else:
            reporte += "LIMITADO: El modelo explica menos del 30% de la variabilidad.\n"

        reporte += f"\nEn promedio, las predicciones se equivocan por {mae:.1f} apariciones.\n"

        reporte += f"""

FACTORES MÁS IMPORTANTES

"""

        for i in range(min(5, len(imp_df))):
            row = imp_df.iloc[i]
            reporte += f"{i+1}. {row['Característica']}: {row['Importancia']*100:.1f}%\n"

        reporte += f"""
        
CONCLUSIONES

✓ Los 3 agentes completaron su trabajo exitosamente
✓ El modelo Random Forest está listo para hacer predicciones


Reporte generado automáticamente por AGENTE 3 - COMUNICADOR

"""
        return reporte
    
    def guardar_reporte(self, nombre_archivo="reporte_modelo.txt"):
        reporte = self.generar_reporte()
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(reporte)
        print(f"\n Reporte guardado como '{nombre_archivo}'")
        return reporte


def ejecutar_agente3(resultados, target, X):
    agente3 = Agente3Comunicador(resultados, target, X)
    reporte = agente3.guardar_reporte()
    return reporte


if __name__ == "__main__":
    
    print("AGENTE 3 - COMUNICADOR")
    
    print("Módulo de generación de reportes en lenguaje natural")