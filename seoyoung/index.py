import tkinter as tk
import expenses, cal, deposit
from datetime import datetime

# 현재 날짜를 반환하는 함수 정의
def get_date():
    return datetime.now().strftime("%Y-%m-%d")

def openCal():
    cal.calendar(main_frame)

def openDE():
    for widget in main_frame.winfo_children():
        widget.destroy()

    # 수입 영역 추가
    deposit_frame = tk.LabelFrame(main_frame, text="수입")
    deposit_frame.grid(row=0, column=0)
    deposit.deposit(deposit_frame, get_date)

    # 지출 영역 추가
    expenses_frame = tk.LabelFrame(main_frame, text="지출")
    expenses_frame.grid(row=0, column=1)
    expenses.expenses(expenses_frame, get_date)
    # expenses 파일에 expenses()함수 실행. "지출" 메뉴 선택 시, `expenses` 모듈의 함수를 호출하여 프레임 변경



w = tk.Tk()
w.title("티끌모아 태산")
w.geometry("900x600")
main_frame = tk.Frame(w)
main_frame.pack(fill="both", expand=True)

menubar = tk.Menu(w)

menu1 = tk.Menu(menubar, tearoff=False)

menubar.add_command(label="수입/지출", command=openDE)
menubar.add_command(label="캘린더", command=openCal)
menubar.add_command(label="통계")
menubar.add_command(label="예산 설정")

w.config(menu=menubar)
w.mainloop()