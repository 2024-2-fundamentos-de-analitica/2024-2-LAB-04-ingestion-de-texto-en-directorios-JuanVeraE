# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    import os
    import pandas as pd
    import zipfile

    # Ruta del archivo zip y las carpetas
    zip_path = "files/input.zip"
    output_folder = "files/output"
    input_folder = "files/input"

    # Descomprimir el archivo ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("files")

    # Función para procesar los archivos y crear el DataFrame
    def create_dataset(folder):
        data = []
        for sentiment in ["negative", "positive", "neutral"]:
            sentiment_folder = os.path.join(folder, sentiment).replace('\\', '/')
            for filename in os.listdir(sentiment_folder):
                file_path = os.path.join(sentiment_folder, filename).replace('\\', '/')
                with open(file_path, 'r', encoding='utf-8') as file:
                    phrase = file.read().strip()
                    data.append({"phrase": phrase, "target": sentiment})
        return pd.DataFrame(data)

    # Crear los DataFrames para train y test
    train_df = create_dataset(os.path.join(input_folder, "train").replace('\\', '/'))
    test_df = create_dataset(os.path.join(input_folder, "test").replace('\\', '/'))

    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    # Guardar los DataFrames en archivos CSV
    train_df.to_csv(os.path.join(output_folder, "train_dataset.csv").replace('\\', '/'), index=False)
    test_df.to_csv(os.path.join(output_folder, "test_dataset.csv").replace('\\', '/'), index=False)

    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    # Guardar los DataFrames en archivos CSV
    train_df.to_csv(os.path.join(output_folder, "train_dataset.csv"), index=False)
    test_df.to_csv(os.path.join(output_folder, "test_dataset.csv"), index=False)

    print("Archivos 'train_dataset.csv' y 'test_dataset.csv' generados en la carpeta 'output'.")

pregunta_01()