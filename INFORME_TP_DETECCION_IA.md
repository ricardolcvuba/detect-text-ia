# Informe del Trabajo Práctico: Detección de Essays Académicos en Inglés Generados por IA

## Resumen Ejecutivo

Este trabajo práctico implementa un sistema de clasificación automática para distinguir entre essays académicos largos en inglés escritos por humanos y essays generados por inteligencia artificial. El proyecto utiliza técnicas de procesamiento de lenguaje natural y aprendizaje automático, específicamente un clasificador Random Forest con características TF-IDF, logrando una precisión del 99% en la detección de essays académicos en inglés.

## 1. Introducción

### 1.1 Objetivo del Proyecto
El objetivo principal es desarrollar un sistema capaz de identificar automáticamente si un texto ha sido generado por una IA o escrito por un ser humano. Esta capacidad es cada vez más relevante en el contexto actual donde los modelos de lenguaje generativo están proliferando.

### 1.2 Motivación
- **Detección de contenido generado por IA**: Necesidad de identificar contenido sintético en plataformas educativas, medios de comunicación y redes sociales.
- **Transparencia**: Garantizar que los usuarios puedan distinguir entre contenido humano y generado por máquinas.
- **Aplicaciones educativas**: Prevenir el uso no autorizado de IA en tareas académicas, especialmente en el contexto de essays académicos en inglés.

### 1.3 Alcance del Modelo
El modelo está específicamente diseñado y entrenado para:
- **Idioma**: Essays en inglés únicamente
- **Tipo de contenido**: Essays académicos y formales
- **Longitud**: Essays largos (múltiples párrafos)
- **Dominio**: Contenido educativo y académico

**Limitaciones importantes**: El modelo no está optimizado para textos cortos, informales, en otros idiomas, o contenido no académico.

## 2. Metodología

### 2.1 Dataset
- **Fuente**: Dataset "AI vs Human Text" de Kaggle (https://www.kaggle.com/datasets/shanegerami/ai-vs-human-text)
- **Contenido**: Essays académicos en inglés
- **Tamaño**: 487,235 essays
- **Distribución original**:
  - 37.24% essays generados por IA
  - 62.76% essays escritos por humanos
- **Muestreo balanceado**: Se seleccionaron 10,000 ejemplos de cada clase para evitar sesgos

### 2.2 Preprocesamiento
- **Limpieza básica**: Eliminación de espacios múltiples y normalización
- **División de datos**: 80% entrenamiento, 10% validación, 10% prueba
- **Estratificación**: Mantenimiento de la proporción de clases en cada conjunto

### 2.3 Extracción de Características
- **Vectorización TF-IDF**: 
  - Máximo 50,000 características
  - N-gramas de 1-2 palabras
  - Captura patrones léxicos y sintácticos

### 2.4 Modelo de Clasificación
- **Algoritmo**: Random Forest Classifier
- **Optimización**: Randomized Search con validación cruzada
- **Parámetros optimizados**:
  - `n_estimators`: 300
  - `max_depth`: None (sin límite)
  - `min_samples_split`: 5
  - `min_samples_leaf`: 1
  - `bootstrap`: False

## 3. Resultados

### 3.1 Rendimiento del Modelo
```
              precision    recall  f1-score   support

         0.0       0.98      0.99      0.99      1000
         1.0       0.99      0.98      0.99      1000

    accuracy                           0.99      2000
   macro avg       0.99      0.99      0.99      2000
weighted avg       0.99      0.99      0.99      2000
```

### 3.2 Análisis de Resultados
- **Precisión global**: 99%
- **F1-score**: 0.99 para ambas clases
- **Balance**: Excelente equilibrio entre precisión y recall
- **Robustez**: Resultados consistentes en validación cruzada (F1: 0.982)

### 3.3 Casos de Prueba
- **Essay 1** (humano): "The use of this technology to great the emotional expressions..." → **Predicción: Humano (0.0)**
- **Essay 2** (IA): "In a sentence if we are going to use all 3 pronouns..." → **Predicción: IA (1.0)**

## 4. Implementación del Sistema

### 4.1 Arquitectura del Servidor Web
El proyecto incluye una implementación completa con API REST:

```python
# Estructura del servidor
class AITextDetectorServer:
    - Carga del modelo y vectorizador
    - Endpoint POST /predict
    - Respuesta estructurada con Pydantic
```

### 4.2 Tecnologías Utilizadas
- **Machine Learning**: scikit-learn, joblib
- **API Web**: FastAPI, uvicorn
- **Validación de datos**: Pydantic
- **Procesamiento**: pandas, numpy

### 4.3 Estructura del Proyecto
```
detect-text-ia/
├── detect_text_ia.ipynb          # Notebook principal
├── text_classifier/
│   ├── model-RandomForest.joblib # Modelo entrenado
│   ├── tfidf_vectorizer.joblib   # Vectorizador
│   ├── webserver.py              # Servidor API
│   ├── models.py                 # Modelos de datos
│   └── requirements.txt          # Dependencias
```

## 5. Análisis Técnico

### 5.1 Ventajas del Enfoque
- **TF-IDF**: Captura patrones léxicos y de frecuencia
- **Random Forest**: Robusto a overfitting, maneja bien características numéricas
- **N-gramas**: Detecta patrones de secuencia de palabras
- **Optimización automática**: Randomized Search encuentra hiperparámetros óptimos

### 5.2 Limitaciones Identificadas
- **Dependencia del dataset**: El modelo puede no generalizar a otros dominios
- **Evolución de IA**: Los modelos de lenguaje evolucionan constantemente
- **Contexto cultural**: Puede tener sesgos hacia ciertos estilos de escritura
- **Alcance lingüístico**: Limitado a essays en inglés únicamente
- **Tipo de contenido**: Optimizado para essays académicos largos, no para contenido informal o corto
- **Dominio específico**: Puede no funcionar bien en textos técnicos, creativos o periodísticos

### 5.3 Posibles Mejoras
- **Embeddings contextuales**: BERT, GPT embeddings
- **Análisis semántico**: Captura de significado más profundo
- **Ensemble methods**: Combinación de múltiples modelos
- **Análisis de estilo**: Características estilométricas

## 6. Conclusiones

### 6.1 Logros Principales
1. **Alta precisión**: 99% de precisión en la clasificación
2. **Sistema completo**: Desde entrenamiento hasta API web
3. **Metodología sólida**: Validación cruzada y optimización de hiperparámetros
4. **Implementación práctica**: Servidor web funcional

### 6.2 Impacto y Aplicabilidad
- **Educación**: Detección de plagio con IA en essays académicos
- **Medios**: Verificación de contenido periodístico
- **Investigación**: Análisis de tendencias en generación de contenido
- **Empresas**: Control de calidad en plataformas de contenido

### 6.3 Trabajo Futuro
- **Actualización continua**: Reentrenamiento con nuevos datos
- **Análisis multimodal**: Integración de imágenes y texto
- **Detección de evasión**: Identificación de técnicas para evadir detección
- **Explicabilidad**: Modelos interpretables para transparencia

## 7. Referencias Técnicas

### 7.1 Bibliotecas Principales
- scikit-learn: Machine learning framework
- FastAPI: Framework web moderno
- TF-IDF: Extracción de características textuales
- Random Forest: Algoritmo de ensemble learning

### 7.2 Métricas de Evaluación
- **Precisión**: Proporción de predicciones correctas
- **Recall**: Sensibilidad del modelo
- **F1-Score**: Media armónica de precisión y recall
- **Validación cruzada**: Estimación robusta del rendimiento

---

**Fecha de entrega**: [Fecha actual]  
**Autor**: [Nombre del estudiante]  
**Asignatura**: Aprendizaje Automático  
**Institución**: FIUBA 