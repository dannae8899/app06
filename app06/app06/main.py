import flet as ft
import random


def main(page: ft.Page):
global numero_secreto,entrada_numero,texto_resultado
page.title= "adivina el numero"

#generar un numero secreto aleatorio entre 1 y 100

numero_Secreto= random.randint(1,100)

#crear los elementos de la interfaz
titulo=ft.Text("adivina el numero entre 1 y 100" size=20,color="white")
entreda_numero=ft.TextField(label="Tu adivinanza",width=150)
boton_adivinar=ft.ElevatedButton("adivinar",on_click=lambda e: verificar_adivinanza(e,page))
texto_resultado=ft.Text("", color="white")

#crear el contenedor principal con fondo negro
contenedor_principal= ft.container(
    content=ft.column(
        controls=[
            titulo,
            entrada_numero,
            boton_adivinnar
            texto_resultado,
            ft.image(
                src="https://i.ibb.co/Gxgryg9/laser.gif",
                fit=ft.ImageFit.COVER,
                width=350
            )
        ]
    )
)
ft.app(main)
