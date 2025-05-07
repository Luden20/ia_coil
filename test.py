import joblib
import pandas as pd

# Cargar modelo y columnas entrenadas
def cargar():
    modelo = joblib.load('logreg_model.pkl')
    columnas = joblib.load('columnas.pkl')
    return modelo, columnas

# Evaluar una fila con probabilidad
def evaluar(entrada, modelo, columnas, umbral=0.5):
    entrada = entrada.reindex(columns=columnas, fill_value=0)
    prob = modelo.predict_proba(entrada)[0][1]
    print("Probabilidad de clase 1 (Positivo):", prob)
    return 1 if prob > umbral else 0

# Prueba general con out.csv
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
'CholCheck': 1.0, 'BMI': 2.085034159548181, 'Smoker': 1.0, 'Stroke': 0.0, 'HeartDiseaseorAttack': 0.0, 'AnyHealthcare': 1.0, 'NoDocbcCost': 0.0, 'GenHlth': 3.0, 'MentHlth': 0.0, 'PhysHlth': 0.0, 'DiffWalk': 1.0, 'Education': 4.0, 'Income': 1.0, 'HighBP_1.0': True, 'HighChol_1.0': False, 'PhysActivity_1.0': False, 'Fruits_1.0': False, 'Veggies_1.0': False, 'HvyAlcoholConsump_1.0': False, 'Sex_1.0': False, 'Age_10.0': False, 'Age_11.0': False, 'Age_12.0': True, 'Age_13.0': False, 'Age_2.0': False, 'Age_3.0': False, 'Age_4.0': False, 'Age_5.0': False, 'Age_6.0': False, 'Age_7.0': False, 'Age_8.0': False, 'Age_9.0': False    }, umbral=0.5)

    print("\nPredicción:", "Positivo" if resultado else "Negativo")

if __name__ == '__main__':
    #test()
    basic_test()
    #verificar_positivos_guardados()
