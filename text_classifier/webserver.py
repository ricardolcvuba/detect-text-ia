import uvicorn
import joblib
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from pathlib import Path

from models import ClassificationResult, TextToClassify, PredictionEnum


class AITextDetectorServer:
    def __init__(self, model_path: str, vectorizer_path: str):
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Configuración para servir archivos estáticos
        self.base_dir = Path(__file__).parent
        self.app.mount("/static", StaticFiles(directory=str(self.base_dir / "static")), name="static")

        self._load_components(model_path, vectorizer_path)
        self._register_routes()

    def _load_components(self, model_path: str, vectorizer_path: str):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def _register_routes(self):
        @self.app.get("/")
        def index():
            return FileResponse(self.base_dir / "templates" / "index.html")

        @self.app.post("/predict", response_model=ClassificationResult)
        def predict(payload: TextToClassify):
            text_as_vector = self.vectorizer.transform([payload.text])
            predicted_value = int(self.model.predict(text_as_vector)[0])
            prediction_label = PredictionEnum.AI if predicted_value == 1 else PredictionEnum.Human
            return ClassificationResult(prediction=prediction_label)

    def run(self, host: str = "127.0.0.1", port: int = 8000):
        uvicorn.run(self.app, host=host, port=port)


if __name__ == "__main__":
    import os

    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8000"))

    web_server = AITextDetectorServer(
        model_path="model-RandomForest.joblib",
        vectorizer_path="tfidf_vectorizer.joblib"
    )
    web_server.run(host=host, port=port)
