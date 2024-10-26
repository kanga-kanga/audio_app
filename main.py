import flet as ft
import threading
import time

def main(page: ft.Page):
    # Ajouter PermissionHandler à la page
    ph = ft.PermissionHandler()
    page.overlay.append(ph)

    
    # page.theme_mode = ft.ThemeMode.LIGHT

    def toggle_theme_mode(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        lightMode.icon = (
            ft.icons.WB_SUNNY_OUTLINED if page.theme_mode == "light" else ft.icons.WB_SUNNY
        )
        page.update()

    lightMode = ft.IconButton(
        ft.icons.WB_SUNNY_OUTLINED if page.theme_mode == "light" else ft.icons.WB_SUNNY,
        on_click=toggle_theme_mode,
    )

    page.appbar = ft.AppBar(title=ft.Text("Music Player"), center_title=True, bgcolor="green", actions=[lightMode])



    # def on_permission_result(permission, status):
    #     try : 
    #         if status == ft.PermissionStatus.GRANTED:
    #             # Permissions granted, continue with accessing files
    #             # access_files()
    #             pass
    #         else:
    #             # Permissions denied, show a message to the user
    #             page.add(ft.Text("Permissions denied. Cannot access files."))
    #     except Exception as e :
    #         print(e)

    def request_storage_permission(e):
        try :
            ph.request_permission(ft.PermissionType.STORAGE)#, on_permission_result)
            page.add(ft.Text(f"Requested {ft.PermissionType.STORAGE.name} :"))
            page.update()
            # on_permission_result
        except Exception as erreur :
            snack_bar = ft.SnackBar(ft.Text(value = f"{erreur}", font_family="times new roman", size=18, text_align=ft.TextAlign.CENTER), bgcolor=ft.colors.RED_ACCENT, margin=10, behavior=ft.SnackBarBehavior.FLOATING, width = 500, padding = 10)
            page.snack_bar = snack_bar
            page.snack_bar.open = True
            page.update()


    def get_all_mp3_file_autre_chemin(e):
        e=0
        close_banner(e)
        time.sleep(3)
        try : 

            import os
            mp3_files = []
            for root, dirs, files in os.walk("storage/emulated/0/"):
                for file in files:
                    if file.endswith(".mp3"):
                        mp3_files.append(os.path.join(root, file))
            file_list = ft.ListView(
                controls=[ft.Text(file) for file in mp3_files]
            )
            page.add(file_list)

            if len(mp3_files) == 0 :
                
                page.open(banner)

        except Exception as erreur :
            snack_bar = ft.SnackBar(ft.Text(value = f"{erreur}", font_family="times new roman", size=18, text_align=ft.TextAlign.CENTER), bgcolor=ft.colors.RED_ACCENT, margin=10, behavior=ft.SnackBarBehavior.FLOATING, width = 500, padding = 10)
            page.snack_bar = snack_bar
            page.snack_bar.open = True
            page.update()



    def close_banner(e):
        page.close(banner)
        page.update()
        page.update()

    banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_OUTLINED, color=ft.colors.AMBER, size=40),
        content = ft.Text(
            value=f"Aucun audio trouvé ! veuillez autoriser l'application a acceder aux fichier multimedia de votre appareil !",
            color = ft.colors.BLACK
        ),
        actions=[
            ft.TextButton(text = "Autoriser !", on_click=request_storage_permission),
            ft.TextButton(text = "Reesayer", on_click=get_all_mp3_file_autre_chemin),
            ft.TextButton(text = "D'accord", on_click=close_banner)
        ]
    )

    
    def get_all_mp3_file() :
        time.sleep(3)
        try : 

            import os
            mp3_files = []
            for root, dirs, files in os.walk("/storage/emulated/0/"):
                for file in files:
                    if file.endswith(".mp3"):
                        mp3_files.append(os.path.join(root, file))
            file_list = ft.ListView(
                controls=[ft.Text(file) for file in mp3_files]
            )
            page.add(file_list)

            if len(mp3_files) == 0 :
                
                page.open(banner)

        except Exception as erreur :
            snack_bar = ft.SnackBar(ft.Text(value = f"{erreur}", font_family="times new roman", size=18, text_align=ft.TextAlign.CENTER), bgcolor=ft.colors.RED_ACCENT, margin=10, behavior=ft.SnackBarBehavior.FLOATING, width = 500, padding = 10)
            page.snack_bar = snack_bar
            page.snack_bar.open = True
            page.update()

    # Bouton pour demander la permission de stockage
    # request_button = ft.OutlinedButton(
    #     text="Request Storage Permission",
    #     on_click=request_storage_permission
    # )
    # page.add(request_button)

    page.add(ft.Text(value="Bonjour"))

    thread_continue = threading.Thread(target = get_all_mp3_file)
    thread_continue.start()

ft.app(target=main)
