"""
AGENTE 2 - ENTRENADOR
Funciones: aplica validación, entrena, selecciona modelo
Salida: métricas + modelo
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


class Agente2Entrenador:
    def __init__(self, dataframe, target_col):
        self.df = dataframe
        self.target = target_col
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.modelo = None
        self.scores = None
        self.metricas = {}
        self.y_pred = None
    
    def preparar_datos(self):
        print("\n→ preparando datos")
        self.X = self.df.drop(columns=[self.target])
        self.y = self.df[self.target]
        print(f"   Características (X): {self.X.shape}")
        print(f"   Objetivo (y): {self.y.shape}")
        return self
    
    def dividir_datos(self, test_size=0.2):
        print("\n→ dividiendo datos")
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=42
        )
        print(f"   Entrenamiento: {len(self.X_train)} personajes (80%)")
        print(f"   Prueba: {len(self.X_test)} personajes (20%)")
        return self
    
    def aplicar_validacion(self, cv=5):
        print("\n→ aplica validación")
        
        modelo_temp = RandomForestRegressor(n_estimators=100, random_state=42)
        self.scores = cross_val_score(modelo_temp, self.X_train, self.y_train, 
                                      cv=cv, scoring='r2')
        
        print(f"   Validación cruzada ({cv} folds):")
        print(f"   R² por fold: {[round(s, 4) for s in self.scores]}")
        print(f"   R² promedio: {self.scores.mean():.4f}")
        print(f"   Desviación: ±{self.scores.std():.4f}")
        
        self.metricas['validacion_cruzada'] = {
            'media': self.scores.mean(),
            'std': self.scores.std(),
            'scores': self.scores
        }
        return self
    
    def entrenar(self):
        print("\n→ entrena")
        
        self.modelo = RandomForestRegressor(
            n_estimators=100,
            max_depth=15,
            random_state=42
        )
        self.modelo.fit(self.X_train, self.y_train)
        
        print("Modelo Random Forest entrenado")
        return self
    
    def seleccionar_modelo(self):
        print("\n→ selecciona modelo")
        
        self.y_pred = self.modelo.predict(self.X_test)
        
        r2 = r2_score(self.y_test, self.y_pred)
        rmse = np.sqrt(mean_squared_error(self.y_test, self.y_pred))
        mae = mean_absolute_error(self.y_test, self.y_pred)
        
        self.metricas['r2'] = r2
        self.metricas['rmse'] = rmse
        self.metricas['mae'] = mae
        
        print(f"   Modelo seleccionado: Random Forest Regressor")
        print(f"   R² en prueba: {r2:.4f} ({r2*100:.2f}%)")
        print(f"   RMSE: {rmse:.2f}")
        print(f"   MAE: {mae:.2f}")
        
        return self
    
    def obtener_resultados(self):
        
        print("AGENTE 2 COMPLETADO")
        print("→ métricas + modelo")
        
        
        return {
            'modelo': self.modelo,
            'metricas': self.metricas,
            'X_train': self.X_train,
            'X_test': self.X_test,
            'y_train': self.y_train,
            'y_test': self.y_test,
            'y_pred': self.y_pred
        }


def ejecutar_agente2(df_limpio, target):
    agente2 = Agente2Entrenador(df_limpio, target)
    resultados = (agente2
                  .preparar_datos()
                  .dividir_datos()
                  .aplicar_validacion()
                  .entrenar()
                  .seleccionar_modelo()
                  .obtener_resultados())
    return resultados


if __name__ == "__main__":
    
    print("AGENTE 2 - ENTRENADOR")
    
    print("Módulo de entrenamiento para predicción de apariciones Marvel/DC")