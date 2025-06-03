document.getElementById('prediccionForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const datos = {};

    // Mostrar el mensaje de carga
    const mensajeCarga = document.getElementById('mensajeCarga');
    mensajeCarga.style.display = 'block';
    mensajeCarga.textContent = 'Cargando...';

    // Procesar cada entrada
    for (let [key, value] of formData.entries()) {
        if ([
            'HighBP_1.0','HighChol_1.0','PhysActivity_1.0',
            'Fruits_1.0','Veggies_1.0','HvyAlcoholConsump_1.0', 'Sex_1.0',
        ].includes(key)) {
            datos[key] = (value === '1');
        } else if (key === 'Age') {
            const ageMap = {
                '10':'Age_10.0','11':'Age_11.0','12':'Age_12.0','13':'Age_13.0',
                '2':'Age_2.0','3':'Age_3.0','4':'Age_4.0','5':'Age_5.0',
                '6':'Age_6.0','7':'Age_7.0','8':'Age_8.0','9':'Age_9.0',
                '1':'Age_1.0'
            };
            Object.values(ageMap).forEach(k => datos[k] = false);
            datos[ageMap[value]] = true;
        } else if (!isNaN(value)) {
            datos[key] = parseFloat(value);
        } else {
            datos[key] = value;
        }
    }

    try {
        const respuesta = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(datos)
        });
        const { resultado } = await respuesta.json();
        document.getElementById('respuestaAPI').textContent = `Resultado: ${resultado}`;
    } catch (error) {
        document.getElementById('respuestaAPI').textContent = 'Error: ' + error.message;
    } finally {
        // Ocultar el mensaje de carga
        mensajeCarga.style.display = 'none';
    }
});
