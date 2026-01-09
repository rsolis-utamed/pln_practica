import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

class Preprocesador:
    def __init__(self, max_features=2000, min_df=3, max_df=0.95):
        """
        Inicializa la clase con los parámetros de vectorización 
        vistos en tu notebook.
        """
        self.vectorizer = TfidfVectorizer(
            max_features=max_features, 
            min_df=min_df, 
            max_df=max_df
        )
        self.is_fitted = False

    def clean_text(self, text):
        """
        Realiza el preprocesamiento básico del texto.
        """
        if not isinstance(text, str):
            return ""
        
        # 1. Convertir a minúsculas
        text = text.lower()
        
        # 2. Eliminar caracteres especiales y números (basado en tu limpieza)
        text = re.sub(r'[^a-záéíóúñ\s]', '', text)
        
        # 3. Eliminar espacios extra
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text

    def fit_transform(self, series):
        """
        Limpia los textos y entrena el vectorizador TF-IDF.
        """
        # Aplicar limpieza a toda la serie de datos
        cleaned_series = series.apply(self.clean_text)
        
        # Transformar a matriz numérica (X)
        X = self.vectorizer.fit_transform(cleaned_series)
        self.is_fitted = True
        
        return X, cleaned_series

    def transform(self, series):
        """
        Para transformar nuevos datos sin volver a entrenar el modelo.
        """
        if not self.is_fitted:
            raise Exception("El vectorizador debe ser entrenado con fit_transform primero.")
        
        cleaned_series = series.apply(self.clean_text)
        return self.vectorizer.transform(cleaned_series)
