import customtkinter
import tkinter
import subprocess



def hibernation():
    command = "powercfg -h off"
    print("sdasd")
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def hibernation_off():
    command = "powercfg -h on"

    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def reserv_storage():
    command = "DISM /Online /Set-ReservedStorageState /State:Enabled"
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
def reserv_storage_off():
    command = "DISM /Online /Set-ReservedStorageState /State:Disabled"
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def cache():
    command = [
        "cls",
        "net stop wuauserv >nul",
        "cd %windir%\SoftwareDistribution\Download\ >nul",
        "del /q /f /s %windir%\SoftwareDistribution\Download\*.* >nul",
        "rd /q /s %windir%\SoftwareDistribution\Download\ >nul",
        ]
    for i in command:
        subprocess.run(i, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def temp():
    command = "cleanmgr /sageset:1"
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


# config
config_button = {
    "color": "#6e5ed5",
    "corned":10,
    "text_color":"white",
    }

config_text = {
    "fg_color": "#584baa",
    "x":140,
    "y":18,
    "corned":8,
    "text_color":"white",
    }

# -----------------------------------------------
if __name__ == "__main__":
    cb = config_button
    ct = config_text


    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    customtkinter.deactivate_automatic_dpi_awareness()
    root = customtkinter.CTk()
    root.geometry("350x400")

    clear_txt = customtkinter.CTkLabel(
        master=root,
        text="Clear",
        text_color=ct["text_color"],
        width=ct["x"],
        height=ct["y"],
        fg_color=ct["fg_color"],
        corner_radius=ct["corned"]
    )
    clear_txt.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    button_temp = customtkinter.CTkButton(
        width=170,
        master=root, text="Temp", command=temp, fg_color=cb["color"]
    )
    button_temp.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    button_cache = customtkinter.CTkButton(
        master=root,
        width=170,

        text="Cache system update",
        command=cache,
        fg_color=cb["color"],
    )
    button_cache.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)


    # text 
    other_text = customtkinter.CTkLabel(
        master=root,
        text="Reserv storage",
        text_color=ct["text_color"],
        width=ct["x"],
        height=ct["y"],
        fg_color=ct["fg_color"],
        corner_radius=ct["corned"]
    )
    other_text.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    button_reserv_storage_off = customtkinter.CTkButton(
        master=root,
        width=77,
        text="Disable",
        command=reserv_storage_off,
        fg_color=cb["color"],
    )
    button_reserv_storage_off.place(relx=0.62, rely=0.5, anchor=tkinter.CENTER)

    button_reserv_storage_on = customtkinter.CTkButton(
        master=root,
        width=77,
        text="Enable",
        command=reserv_storage,
        fg_color=cb["color"],
    )
    button_reserv_storage_on.place(relx=0.38, rely=0.5, anchor=tkinter.CENTER)
    # text 
    other_text = customtkinter.CTkLabel(
        master=root,
        text="Hibernation",
        text_color=ct["text_color"],
        width=ct["x"],
        height=ct["y"],
        fg_color=ct["fg_color"],
        corner_radius=ct["corned"]
    )
    other_text.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    button_hibernation_off = customtkinter.CTkButton(
        master=root,
        width=77,
        text="Disable",
        command=hibernation_off,
        fg_color=cb["color"],
    )
    button_hibernation_off.place(relx=0.62, rely=0.7, anchor=tkinter.CENTER)

    button_hibernation_on = customtkinter.CTkButton(
        master=root,
        width=77,
        text="Enable",
        command=hibernation,
        fg_color=cb["color"],
        
    )
    button_hibernation_on.place(relx=0.38, rely=0.7, anchor=tkinter.CENTER)

    root.mainloop()

