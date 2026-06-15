"""
AGENTE 1 - NORMALIZADOR
Funciones: limpia, imputa, escala, codifica
Salida: dataset limpio
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder


class Agente1Normalizador:
    def __init__(self, dataframe, target_col):
        self.df = dataframe.copy()
        self.target = target_col
        self.num_cols = []
        self.cat_cols = []
    
    def limpiar(self):
        print("\n→ limpia")
        
        columnas_eliminar = ['page_id', 'urlslug', 'nombre', 'name']
        for col in columnas_eliminar:
            if col in self.df.columns:
                self.df = self.df.drop(columns=[col])
                print(f"   Eliminada: {col}")
        
        antes = len(self.df)
        self.df = self.df.dropna(subset=[self.target])
        print(f"   Eliminadas {antes - len(self.df)} filas sin '{self.target}'")
        
        antes = len(self.df)
        self.df = self.df.drop_duplicates()
        print(f"   Eliminados {antes - len(self.df)} duplicados")
        
        self.num_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        self.cat_cols = self.df.select_dtypes(include=['object']).columns.tolist()
        
        return self
    
    def imputar(self):
        print("\n→ imputa")
        
        for col in self.num_cols:
            if col != self.target and self.df[col].isnull().sum() > 0:
                mediana = self.df[col].median()
                self.df[col].fillna(mediana, inplace=True)
                print(f"   {col}: imputada con mediana={mediana:.2f}")
        
        for col in self.cat_cols:
            if self.df[col].isnull().sum() > 0:
                moda = self.df[col].mode()[0] if len(self.df[col].mode()) > 0 else "DESCONOCIDO"
                self.df[col].fillna(moda, inplace=True)
                print(f"   {col}: imputada con moda='{moda}'")
        
        return self
    
    def escalar(self):
        print("\n→ escala")
        
        num_cols_escalar = [col for col in self.num_cols if col != self.target]
        
        if len(num_cols_escalar) > 0:
            scaler = StandardScaler()
            self.df[num_cols_escalar] = scaler.fit_transform(self.df[num_cols_escalar])
            print(f" Escaladas {len(num_cols_escalar)} columnas")
        else:
            print("  No hay columnas numéricas para escalar")
        
        return self
    
    def codificar(self):
        print("\n→ codifica")
        
        cat_cols_codificar = [col for col in self.cat_cols if col != self.target]
        
        for col in cat_cols_codificar:
            le = LabelEncoder()
            self.df[col] = self.df[col].fillna('DESC').astype(str)
            self.df[col] = le.fit_transform(self.df[col])
            print(f"   {col}: codificada en {len(le.classes_)} categorías")
        
        return self
    
    def obtener_dataset_limpio(self):
        
        print("AGENTE 1 COMPLETADO")
        print("→ dataset limpio")
        
        print(f"   Dataset final: {self.df.shape}")
        return self.df


def ejecutar_agente1(df, target):
    agente1 = Agente1Normalizador(df, target)
    df_limpio = agente1.limpiar().imputar().escalar().codificar().obtener_dataset_limpio()
    return df_limpio


if __name__ == "__main__":
    
    print("AGENTE 1 - NORMALIZADOR")
    
    print("Módulo de normalización de datos Marvel/DC")