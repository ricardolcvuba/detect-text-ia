import joblib
import uvicorn
from fastapi import FastAPI

from models import ClassificationResult, TextToClassify, PredictionEnum


class AITextDetectorServer:
    def __init__(self, model_path: str, vectorizer_path: str):
        self.app = FastAPI()
        self._load_components(model_path, vectorizer_path)
        self._register_routes()

    def _load_components(self, model_path: str, vectorizer_path: str):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def _register_routes(self):
        @self.app.post("/predict", response_model=ClassificationResult)
        def predict(payload: TextToClassify):
            text_as_vector = self.vectorizer.transform([payload.text])
            predicted_value = int(self.model.predict(text_as_vector)[0])
            prediction_label = PredictionEnum.AI if predicted_value == 1 else PredictionEnum.Human
            return ClassificationResult(prediction=prediction_label)

    def run(self, host: str = "127.0.0.1", port: int = 8000):
        uvicorn.run(self.app, host=host, port=port)


if __name__ == "__main__":
    web_server = AITextDetectorServer(
        model_path="model-RandomForest.joblib",
        vectorizer_path="tfidf_vectorizer.joblib"
    )
    web_server.run()
