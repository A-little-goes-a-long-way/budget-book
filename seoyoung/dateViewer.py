import tkinter as tk
from tkinter.ttk import LabelFrame
from tkcalendar import Calendar


def showDateView(frame):
    for widget in frame.winfo_children():  # 기존 프레임 초기화
        widget.destroy()

