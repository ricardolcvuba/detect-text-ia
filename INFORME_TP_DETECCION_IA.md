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
- **Limpieza mínima**: Solo normalización de espacios (eliminación de espacios múltiples y espacios al inicio/final)
- **División de datos**: 80% entrenamiento, 10% validación, 10% prueba
- **Estratificación**: Mantenimiento de la proporción de clases en cada conjunto
- **Sin limpieza adicional**: No se realizó tokenización, eliminación de stop words, o normalización de texto

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

#### Ejemplos de Essays Humanos (Correctamente Clasificados):
**Essay 1**: 
"I read a post on Askreddit that inquired, "what are some completely legal things that make you a terrible human being." Among the top comments were answers like, standing in the middle of an aisle, not flushing the toilet, or not putting things back where you found them in the grocery store. All these comments had 5 digit upvotes. Are these things somewhat inconsiderate and annoying? Yes. Do they make you a terrible person? No. I feel like these people who view these actions as "terrible" are just looking for any way to feel validated in their perceived moral superiority by barely doing anything at all. They think "I don't stand in people's way, I flush the toilet, I put grocery items back where I found them, I'm a good person and other people are bad". It honestly feels somewhat masturbatory. I think you can do inconsiderate things and even have committed crimes and still be a good person, if you were perfect you wouldn't be human. I can pick apart someone's every action and try to place them neatly into the categories of "good" and "bad" but it probably wouldn't make me any better as a person."
→ **Predicción: Humano (0.0)** ✓

**Essay 2**: 
"I used to rent, so I always used a TV stand. No mess, no stress. But when I finally bought my own place, I figured it was time to do it right and wall-mount the TV. That lasted about two weeks. The height felt off, I couldnt adjust anything without unbolting the whole thing, and dont even get me started on the cable situation. It looked good for about five minutes, then just became a pain. Ended up going back and re-ordering the same fitueyes tv stand I had in my rental. I had left it behind for the next tenant because I thought Id moved on from that phase. Turns out I hadnt. Sometimes the simple option is just... better. Now Im sitting here wondering why wall mounting became the "default" when its such a pain to do right and almost impossible to undo. Feels like we all just accepted it because it looks nice on Instagram. (even though the tv stand can looks nice too?)"
→ **Predicción: Humano (0.0)** ✓

**Essay 3**: 
"I dont know why everyone on Reddit whines and cries about carts not being returned at the supermarket. When I was 15 I had a supermarket job. When I was asked to do carts I was ecstatic, got to go outdoors, got to not deal with annoying customers while bagging. Got to chill with the weird 30 y/o produce guy who hung out under the awning smoking, Why would a kid nowadays want to stay indoors and bag or cashier and deal with annoying people? Just go outside and stretch your legs, maybe sneak over to the other stores in the plaza, whatever. Youre giving these kids something fun to do, whats wrong with that?"
→ **Predicción: Humano (0.0)** ✓

#### Ejemplos de Essays Generados por IA (Correctamente Clasificados):
**Essay 4**: 
"In today's fast-paced and increasingly interconnected global society, the importance of leveraging technological advancements to optimize learning outcomes cannot be overstated. Artificial intelligence, in particular, provides a wide range of opportunities for enhancing educational efficiency, engagement, and accessibility across diverse populations. By integrating adaptive algorithms, data-driven insights, and scalable platforms, institutions can foster a more personalized and inclusive learning environment that aligns with 21st-century skills and evolving industry demands."
→ **Predicción: IA (1.0)** ✓

**Essay 5**: 
"Learning a new language can be both exciting and challenging. Many people find that consistent practice and exposure to real conversations help improve their skills more effectively than just studying grammar rules. Using apps, watching movies, and talking with native speakers are great ways to immerse yourself in the language. Remember, making mistakes is a natural part of the learning process, and patience is key to becoming fluent."
→ **Predicción: IA (1.0)** ✓

**Essay 6**: 
"Traveling to new places is an amazing way to broaden your horizons and learn about different cultures. It allows you to meet new people, try unique foods, and experience traditions that you might never encounter otherwise. Whether it's a weekend getaway or a longer trip abroad, every journey has the potential to teach you something valuable and create lasting memories"
→ **Predicción: IA (1.0)** ✓

**Essay 7**: 
"I didn't expect to enjoy cooking as much as I do now. It started as something I had to do just to get by, but over time, trying out new recipes became something I genuinely look forward to. It's relaxing, and there's a small sense of pride when a dish turns out well—especially when someone else enjoys it too."
→ **Predicción: IA (1.0)** ✓

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
│   ├── index.html                # Interfaz web
│   ├── Dockerfile                # Configuración Docker
│   ├── docker-compose.yml        # Orquestación Docker
│   └── requirements.txt          # Dependencias
```

### 4.4 Interfaz Web y Despliegue

#### 4.4.1 Frontend Web
Se desarrolló una interfaz web moderna y responsiva utilizando HTML5, CSS3 y JavaScript vanilla. La interfaz incluye:

- **Diseño responsivo**: Utiliza Bootstrap 5 para adaptarse a diferentes dispositivos
- **Interfaz intuitiva**: Formulario simple con área de texto y botón de análisis
- **Feedback visual**: Resultados claros con colores diferenciados (verde para humano, rojo para IA)
- **Integración con API**: Comunicación asíncrona con el servidor FastAPI mediante fetch API

#### 4.4.2 Características de la Interfaz
- **Header institucional**: Incluye logos de UBA y FIUBA
- **Área de entrada**: Textarea amplio para ingresar essays
- **Análisis en tiempo real**: Procesamiento inmediato del texto ingresado
- **Manejo de errores**: Alertas informativas para errores de conexión
- **Diseño limpio**: Interfaz minimalista centrada en la funcionalidad

#### 4.4.3 Containerización y Despliegue
El sistema incluye configuración completa para despliegue en contenedores:

- **Dockerfile**: Configuración para imagen Python 3.9-slim
- **Docker Compose**: Orquestación simplificada del servicio
- **Variables de entorno**: Configuración flexible de host y puerto
- **Despliegue automatizado**: Comando único para iniciar el sistema completo

#### 4.4.4 Arquitectura del Sistema Web
```
Cliente Web (index.html)
    ↓ HTTP/JSON
Servidor FastAPI (webserver.py)
    ↓ Modelo ML
Random Forest + TF-IDF
```

La arquitectura sigue un patrón cliente-servidor donde:
1. El frontend envía el texto a través de una petición POST
2. El servidor procesa el texto con el modelo entrenado
3. Se retorna la predicción en formato JSON
4. El frontend muestra el resultado al usuario

## 5. Conclusiones

### 5.1 Logros Principales

Este trabajo práctico ha logrado desarrollar exitosamente un sistema de detección de essays generados por IA con una precisión excepcional del 99%. El modelo Random Forest optimizado con características TF-IDF demostró ser altamente efectivo para distinguir entre essays académicos en inglés escritos por humanos y aquellos generados por inteligencia artificial. La implementación completa del sistema, desde el entrenamiento del modelo hasta el despliegue de una API web funcional, representa un logro significativo en términos de aplicabilidad práctica.

La metodología empleada, que incluye validación cruzada rigurosa y optimización automática de hiperparámetros mediante Randomized Search, garantiza la robustez y confiabilidad del modelo. Los resultados obtenidos en el conjunto de prueba confirman la capacidad del sistema para mantener un rendimiento consistente, con un F1-score de 0.99 para ambas clases, demostrando un equilibrio perfecto entre precisión y recall.

### 5.2 Impacto y Aplicabilidad

El impacto potencial de este sistema de detección se extiende a múltiples dominios de aplicación. En el ámbito educativo, la herramienta puede ser invaluable para identificar essays académicos generados por IA, ayudando a mantener la integridad académica y prevenir el uso no autorizado de tecnologías de generación de texto. Las instituciones educativas pueden implementar este sistema para verificar la autenticidad de los trabajos presentados por los estudiantes.

En el sector de los medios de comunicación, el sistema puede contribuir a la verificación de contenido periodístico, asegurando que los artículos publicados sean de autoría humana cuando sea necesario. Las empresas de tecnología y plataformas de contenido pueden utilizar esta herramienta para implementar controles de calidad y mantener estándares de transparencia en la generación de contenido.

La investigación en el campo de la detección de contenido generado por IA también se beneficia de este trabajo, proporcionando una base sólida para futuros desarrollos y mejoras en el área. El análisis de las tendencias en generación de contenido puede ayudar a comprender mejor cómo evolucionan las tecnologías de IA y sus implicaciones en la sociedad.

### 5.3 Trabajo Futuro

A pesar de los excelentes resultados obtenidos, el trabajo futuro debe abordar varias áreas de mejora para mantener la relevancia del sistema. La actualización continua del modelo es esencial, ya que los modelos de lenguaje generativo evolucionan constantemente, requiriendo reentrenamiento con nuevos datos y técnicas de detección más sofisticadas.

La exploración de análisis multimodal, que integre imágenes y texto, podría expandir significativamente las capacidades del sistema. La detección de técnicas de evasión, donde los usuarios intentan modificar el texto generado por IA para evitar la detección, representa otro desafío importante que requiere investigación adicional.

El desarrollo de modelos más explicables e interpretables es crucial para aumentar la transparencia y confianza en el sistema. La implementación de técnicas de análisis de estilo más avanzadas, como características estilométricas y embeddings contextuales, podría mejorar aún más la precisión del modelo y su capacidad de generalización a diferentes tipos de contenido.

La expansión del sistema para incluir otros idiomas y tipos de contenido más allá de essays académicos en inglés también representa una dirección prometedora para el desarrollo futuro. Esto requeriría la recolección de datasets multilingües y la adaptación de las técnicas de procesamiento de lenguaje natural para diferentes contextos culturales y lingüísticos.