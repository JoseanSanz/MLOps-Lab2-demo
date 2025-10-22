#!/usr/bin/env python

import gradio as gr
import requests

# URL de tu API FastAPI
API_URL = "https://my-fastapi-main-latest.onrender.com"


# Función que se ejecuta al presionar "Calcular"
def calcular(a, b, operacion):
    try:
        payload = {"a": float(a), "b": float(b), "operation": operacion}
        response = requests.post(f"{API_URL}/calculate", json=payload, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("result")
    except requests.exceptions.HTTPError as e:
        return f"Error: {response.json().get('detail', str(e))}"


# Crear interfaz Gradio
iface = gr.Interface(
    fn=calcular,
    inputs=[
        gr.Number(label="Número A"),
        gr.Number(label="Número B"),
        gr.Dropdown(
            choices=["add", "subtract", "multiply", "divide", "power"],
            value="add",
            label="Operación",
        ),
    ],
    outputs=gr.Textbox(label="Resultado"),
    title="Calculadora con FastAPI y Gradio",
    description="Calculadora interactiva que llama a la API FastAPI /calculate",
)

# Lanzar interfaz
if __name__ == "__main__":
    iface.launch()
