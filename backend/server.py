import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

def cargar():
    modelo = joblib.load('logreg_model.pkl')
    columnas = joblib.load('columnas.pkl')
    return modelo, columnas

def evaluar(entrada, modelo, columnas, umbral=0.5):
    entrada = entrada.reindex(columns=columnas, fill_value=0)
    prob = modelo.predict_proba(entrada)[0][1]
    print("Probabilidad de clase 1 (Positivo):", prob)
    return 1 if prob > umbral else 0

def test():
    df = pd.read_csv('./out.csv')
    dfFinal = df.drop('Diabetes_binary_1.0', axis=1)
    reales = df['Diabetes_binary_1.0'].values

    modelo, columnas = cargar()
    aciertos = 0
    positivos_correctos = []

    for i in range(len(dfFinal)):
        fila = dfFinal.iloc[i:i+1]
        pred = evaluar(fila, modelo, columnas)
        if pred == reales[i]:
            aciertos += 1
            if pred == 1:
                positivos_correctos.append(fila)

    print(f'Accuracy: {aciertos / len(dfFinal):.2%}')

    if positivos_correctos:
        with open("positivos_correctos.txt", "w", encoding="utf-8") as f:
            for fila in positivos_correctos:
                fila_dict = fila.to_dict(orient='records')[0]
                f.write(str(fila_dict) + "\n")
        print("Guardado en positivos_correctos.txt")
    else:
        print("No hubo positivos correctamente clasificados.")

def predecir(datos, umbral=0.5):
    if 'BMI' in datos:
        datos['BMI'] = (datos['BMI'] - 29.1297) / 5.6938

    modelo, columnas = cargar()
    entrada = pd.DataFrame([datos])
    entrada = entrada.reindex(columns=columnas, fill_value=0)

    print("\nEntrada procesada:")
    print(entrada)

    print("\nComparando con columnas del modelo:")
    print("Faltantes:", set(columnas) - set(entrada.columns))
    print("Extras:", set(entrada.columns) - set(columnas))

    prob = modelo.predict_proba(entrada)[0][1]
    print("Probabilidad de clase 1 (Positivo):", prob)

    return prob > umbral

def verificar_positivos_guardados(umbral=0.5):
    try:
        df = pd.read_csv('positivos_correctos.csv')
    except FileNotFoundError:
        print("No se encontró el archivo 'positivos_correctos.csv'. Ejecuta test() primero.")
        return

    modelo, columnas = cargar()
    negativos_actuales = 0

    for i in range(len(df)):
        fila = df.iloc[i:i+1]
        prob = modelo.predict_proba(fila.reindex(columns=columnas, fill_value=0))[0][1]
        if prob <= umbral:
            negativos_actuales += 1
            print(f"Fila {i} ya no clasifica como positivo (prob = {prob:.4f})")

    print(f"\nTotal filas: {len(df)}")
    print(f"Ya no clasifican como positivos: {negativos_actuales}")

def basic_test():
    resultado = predecir({
        'BMI': 0.5,
        'HighBP_1.0': True,
        'HighChol_1.0': False,
        'PhysActivity_1.0': True,
        'Fruits_1.0': True,
        'Veggies_1.0': True,
        'HvyAlcoholConsump_1.0': False,
        'Sex_1.0': True,
        'Age_10.0': False,
        'Age_11.0': False,
        'Age_12.0': True,
        'Age_13.0': False,
        'Age_2.0': False,
        'Age_3.0': False,
        'Age_4.0': False,
        'Age_5.0': False,
        'Age_6.0': False,
        'Age_7.0': False,
        'Age_8.0': False,
        'Age_9.0': False
    }, umbral=0.5)

    print("\nPredicción:", "Positivo" if resultado else "Negativo")

app = Flask(__name__)
CORS(app) 

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json()
    print(data)
    resultado = predecir(data, umbral=0.5)
    return jsonify({"resultado": "Positivo" if resultado else "Negativo"})

@app.route('/test', methods=['GET'])
def test_route():
    test()
    return jsonify({"status": "Test completado y resultados guardados."})

@app.route('/verificar', methods=['GET'])
def verificar_route():
    verificar_positivos_guardados()
    return jsonify({"status": "Verificación completada."})

@app.route('/basic-test', methods=['GET'])
def basic_test_route():
    basic_test()
    return jsonify({"status": "Basic test ejecutado."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)