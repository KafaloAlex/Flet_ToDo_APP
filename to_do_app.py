import flet as ft
import time

def main(page: ft.Page):
    BG = '#041955'
    FWG = '#97B4FF'
    FG = '#3450A1'
    PINK = '#EB06FF'

    # Section des cartes 
    categories_card = ft.Row(
        scroll='auto'
    ) 

    categories_progress = {
        'Business': 50, 
        'Data Science': 20, 
        'Economy': 60, 
        'Industry': 35
    }

    for category, progress in categories_progress.items():
        categories_card.controls.append(
            ft.Container(
                bgcolor=BG,
                height=105,
                width=160,
                border_radius=20,
                padding=13,
                content=ft.Column(
                    controls=[
                        ft.Text('20 Tasks'),
                        ft.Text(category),
                        ft.Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=ft.padding.only(right=progress),
                            content=ft.Container(
                                bgcolor=PINK
                            )
                        )
                    ]
                )
            )
        )
        
    # Tasks
    # tasks = None
    # End Tasks

    first_page_content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment="spaceBetween",
                    controls=[
                        ft.Container(
                            content=ft.Icon(ft.icons.MENU)
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.SEARCH),
                                ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]
                ),
                ft.Container(height=10),
                ft.Text("What's up, John!", size=20),
                ft.Text("CATEGORIES"),
                ft.Container(
                    content=categories_card
                ),
                ft.Container(height=20),
                ft.Text("TODAY'S TASKS"),
                ft.Stack(
                    controls=[
                        # tasks,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD
                        )
                    ]
                )
            ]
        )
    )

    # Création des pages
    page_1 = ft.Container()

    page_2 = ft.Row(
        controls=[
            ft.Container(
                width=300, 
                height=600,
                border_radius=35,
                bgcolor=FG,
                padding=ft.padding.only(top=50, left=20, right=20, bottom=5),
                content=ft.Column(
                    controls=[
                        first_page_content
                    ]
                )
            )
        ]
    )

    container = ft.Container(
        width=300, 
        height=600, 
        bgcolor=BG,
        border_radius=35, 
        content=ft.Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )    

    page.add(container)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)