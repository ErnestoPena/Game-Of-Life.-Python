import pygame
import tkinter as tk
from tkinter import messagebox

def rules():
    # Remove the annoying tkinter root window
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Continue", "ok")
    tk.grab_set_global()
    root.destroy()