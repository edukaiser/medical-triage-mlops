"""Módulo responsável pelo carregamento de artefatos e inferência do modelo."""

import os
import joblib

from typing import Any


class ModelPredictor:
    """Gerencia o carregamento dos artefatos e a geração de predições."""

    def __init__(
        self: Any,
        model_path: str = "models/model.pkl",
        vectorizer_path: str = "models/tfidf_vectorizer.pkl",
    ) -> None:
        """Inicializa os caminhos e carrega os artefatos do modelo."""
        self.model_path = model_path
        self.vectorizer_path = vectorizer_path
        self.model = None
        self.vectorizer = None
        self._load_artifacts()

    def _load_artifacts(self: Any) -> None:
        """Carrega o modelo e o vetorizador do disco se existirem."""
        if os.path.exists(self.model_path) and os.path.exists(self.vectorizer_path):
            self.model = joblib.load(self.model_path)
            self.vectorizer = joblib.load(self.vectorizer_path)
        else:
            raise FileNotFoundError(
                f"Artefatos não encontrados em '{self.model_path}' ou "
                f"'{self.vectorizer_path}'. Execute o treino primeiro."
            )

    def predict(self: Any, text: str) -> int:
        """Recebe o texto clínico, vetoriza e retorna a classe prevista."""
        if not self.model or not self.vectorizer:
            self._load_artifacts()

        x_vect = self.vectorizer.transform([text])
        prediction = self.model.predict(x_vect)[0]

        return int(prediction)


predictor = ModelPredictor()
