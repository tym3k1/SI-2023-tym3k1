import gradio as gr
import pandas as pd



def plot(csv_text, n, queries=""):
    df = pd.read_csv(csv_text)
    df.dropna(axis=0, inplace=True)
    df = df.head(int(n))
    class_shape_int = df.shape
    perc =[.20, .40, .60, .80]
    class_count = df.iloc[:, -1].value_counts()
    if queries == "":
        desc = df.describe(percentiles = perc)
        class_shape = f"Liczba atrybutow: {class_shape_int[1]}, liczba obiektow: {class_shape_int[1]*class_shape_int[0]}"
        return class_shape, df, desc
    if queries == "ile klas decyzyjnych":
        txt_up =  f"ile klas decyzyjnych"
        txt_down = f"Liczba klas decyzyjnych: {len(class_count)}"
        return txt_up, df, txt_down
    if queries == "wielkość każdej klasy decyzyjnej":
        txt_up = "wielkość każdej klasy decyzyjnej"
        txt_down = f"wielkości klas decyzyjnych: {class_count.to_dict()}"
        return txt_up, df, txt_down
    else:
        txt_up = "xdd"
        txt_down = "xdddd"
        return txt_up, df, txt_down

    


inputs = [gr.Textbox(label="CSV Text"), 
          gr.Number(default=10, label="Number of Rows"),
          gr.inputs.Dropdown(["ile klas decyzyjnych", "wielkość każdej klasy decyzyjnej", ""], label="Pytanie")]
outputs = [gr.outputs.Textbox(label="Wynik"),
           gr.outputs.Dataframe(label="Wynik", type='pandas'),
           gr.outputs.Textbox(label="Wynik")]

gr.Interface(plot, inputs=inputs, outputs=outputs, title="Supersoaker Failures Analysis Dashboard").launch()
