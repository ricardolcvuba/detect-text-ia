import joblib
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

# Cargar el modelo y el vectorizador
modelo = joblib.load("model-RandomForest.joblib")
vectorizador = joblib.load("tfidf_vectorizer.joblib")

def main():
    print("Detector de texto generado por IA")

    try:
        while True:
            print("Ingrese un texto en ingles (Ctrl+C para salir):\n")
            texto = input(">> ")
            texto_vectorizado = vectorizador.transform([texto])
            prediccion = modelo.predict(texto_vectorizado)[0]
            print(f"Predicción: {prediccion} (0 = humano, 1 = IA)\n")
    except KeyboardInterrupt:
        print("\nSaliendo...")

if __name__ == "__main__":
    main()
