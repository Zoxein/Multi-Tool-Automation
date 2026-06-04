import os
import sys
import tkinter as tk
from tkinter import messagebox, filedialog
from modules.network import NetworkTools
from modules.file_manager import FileManager

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class AutomationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Zoxein Automation Tool")
        self.root.geometry("450x350")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)

        icon_path = get_resource_path("app.ico")
        if os.path.exists(icon_path):
            try:
                self.root.iconbitmap(icon_path)
            except Exception as e:
                print(f"[!] Target icon failed to load into window: {e}")
        else:
            print(f"[!] Warning: 'app.ico' not found at {icon_path}")

        title_label = tk.Label(
            root, text="ZOXEIN AUTOMATION TOOL", 
            font=("Arial", 16, "bold"), bg="#2c3e50", fg="#ecf0f1"
        )
        title_label.pack(pady=20)

        self.btn_net = tk.Button(
            root, text="🚀 Run Network Ping Checker", font=("Arial", 11, "bold"),
            bg="#2980b9", fg="white", width=30, height=2, bd=0,
            command=self.run_network_checker
        )
        self.btn_net.pack(pady=10)

        self.btn_file = tk.Button(
            root, text="🛠️ Run File Organizer", font=("Arial", 11, "bold"),
            bg="#27ae60", fg="white", width=30, height=2, bd=0,
            command=self.run_file_organizer
        )
        self.btn_file.pack(pady=10)

        self.btn_exit = tk.Button(
            root, text="EXIT", font=("Arial", 10, "bold"),
            bg="#c0392b", fg="white", width=10, height=1, bd=0,
            command=root.quit
        )
        self.btn_exit.pack(pady=25)

    def run_network_checker(self):
        messagebox.showinfo("Network Checker", "Check your terminal to input host.")
        NetworkTools.ping_checker()

    def run_file_organizer(self):
        folder_selected = filedialog.askdirectory(title="Select Folder to Organize")
        if folder_selected:
            print(f"[ * ] Path: {folder_selected}")
            FileManager.organize_folder()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationGUI(root)
    root.mainloop()