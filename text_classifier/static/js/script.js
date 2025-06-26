document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('detector-form');
    const resultadoDiv = document.getElementById('resultado');
    const resultadoHumano = document.querySelector('.resultado-humano');
    const resultadoIA = document.querySelector('.resultado-ia');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const texto = document.getElementById('texto').value.trim();
        
        if (!texto) {
            alert('Por favor, ingresa un texto para analizar.');
            return;
        }
        
        // Mostrar indicador de carga
        resultadoDiv.style.display = 'block';
        resultadoHumano.style.display = 'none';
        resultadoIA.style.display = 'none';
        
        // Crear elemento de carga
        const loadingDiv = document.createElement('div');
        loadingDiv.className = 'loading';
        loadingDiv.innerHTML = '<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Cargando...</span></div>';
        resultadoDiv.querySelector('.card-body').appendChild(loadingDiv);
        
        // Enviar solicitud a la API
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: texto })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor');
            }
            return response.json();
        })
        .then(data => {
            // Eliminar indicador de carga
            if (loadingDiv) {
                loadingDiv.remove();
            }
            
            // Mostrar resultado
            if (data.prediction === 'AI') {
                resultadoHumano.style.display = 'none';
                resultadoIA.style.display = 'block';
            } else {
                resultadoHumano.style.display = 'block';
                resultadoIA.style.display = 'none';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            
            // Eliminar indicador de carga
            if (loadingDiv) {
                loadingDiv.remove();
            }
            
            // Mostrar mensaje de error
            const errorDiv = document.createElement('div');
            errorDiv.className = 'alert alert-danger';
            errorDiv.textContent = 'Ocurrió un error al procesar la solicitud. Por favor, intenta nuevamente.';
            resultadoDiv.querySelector('.card-body').appendChild(errorDiv);
            
            // Eliminar mensaje de error después de 5 segundos
            setTimeout(() => {
                errorDiv.remove();
            }, 5000);
        });
    });
});
