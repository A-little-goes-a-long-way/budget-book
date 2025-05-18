import tkinter as tk
import expenses, cal, deposit

def openDeposit():
   deposit.deposit(main_frame)

def openExpenses():
    expenses.expenses(main_frame) #expenses 파일에 expenses()함수 실행. "지출" 메뉴 선택 시, `expenses` 모듈의 함수를 호출하여 프레임 변경

def openCal():
    cal.calendar(main_frame)

w = tk.Tk()
w.title("티끌모아 태산")
w.geometry("900x600")
main_frame = tk.Frame(w)
main_frame.pack(fill="both", expand=True)

menubar = tk.Menu(w)

menu1 = tk.Menu(menubar, tearoff=False)
menu1.add_cascade(label="수입", command=openDeposit)
menu1.add_cascade(label="지출", command=openExpenses) #하위 메뉴
menubar.add_cascade(label="기록", menu=menu1) #상위 메뉴

menubar.add_command(label="캘린더", command=openCal)
menubar.add_command(label="통계")
menubar.add_command(label="예산 설정")

w.config(menu=menubar)
w.mainloop()