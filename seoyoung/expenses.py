import tkinter as tk
from datetime import datetime

def expenses(frame):
    for widget in frame.winfo_children(): # 기존 프레임 위젯 삭제
        widget.destroy()

    def add():
        e_name=name_entry.get() #금액 가져오기
        e_amount=amount_entry.get()
        if e_name and e_amount:
            listbox.insert(tk.END,f"{e_name}: {e_amount}원") #마지막에 값 추가
            name_entry.delete(0, tk.END) #다음 풒목을 입략하기 위해 입력창에 적힌 내용을 처음부터 끝까지 지움
            amount_entry.delete(0, tk.END)
            update_total()

    def update_total():
        total=0
        for item in listbox.get(0, tk.END): #값을 가져옴
            try:
                amount=int(item.split(":")[1].strip().replace("원", "")) #:를 기준으로 list 만들고, 글자 원을 지운다
                total+=amount
            except ValueError:
                pass
        total_label.config(text=f"총 지출: {total: }원")

    def remove():
        selected_index=listbox.curselection() #현재 선택된 항목을 selected_index 저장
        if selected_index:
            listbox.delete(selected_index)
            update_total()

    def save():
        today = datetime.now().strftime("%Y-%m-%d")
        expenses = listbox.get(0, tk.END) #listbox 있는 데이터 가져오기
        currentTotal = int(total_label.cget("text").split(":")[1].strip().replace("원", ""))
        file_name = f"가계부_지출_{today}.txt"
        lastTotal = 0

        try: # 기존 총 지출 값 불러오기
            with open(file_name,"r", encoding="utf-8") as file:
                lines = file.readlines() #파일의 모든 줄 가져오기
                for line in reversed(lines):
                    if line.startswith("총 지출: "): #줄이 '총 지출'로 시작하는지 확인(마지막 총 지출 찾기)
                        lastTotal = int(line.split(":")[1].strip().replace("원", ""))
                        break # 총 지출 값만 읽고 반복 종료
        except FileNotFoundError:
            print(f"{file_name} 파일이 없습니다. 새로 생성합니다.")

        newTotal = lastTotal + currentTotal

        #파일에 저장
        with open(file_name, "a", encoding="utf-8") as file:  # 추가 모드로 열기
            for expen in expenses:  # 리스트 박스의 모든 데이터를 파일에 기록
                file.write(expen + "\n")
            file.write(f"총 지출: {newTotal}원\n\n")  # 최종 총 지출 값 기록

        savedLabel.config(text="저장되었습니다!")  # 저장 확인 메시지
        savedLabel.after(3000, lambda: savedLabel.config(text=""))

    name_label=tk.Label(frame,text="품목") #Label 위젯 설정
    name_label.grid(row=0, column=1) #창에 배치하기
    name_entry=tk.Entry(frame) #입력창
    name_entry.grid(row=0, column=2)

    amount_label=tk.Label(frame,text="금액") #Label 위젯 설정
    amount_label.grid(row=1, column=1)
    amount_entry=tk.Entry(frame) #입력창
    amount_entry.grid(row=1, column=2)

    add_btn=tk.Button(frame,text="추가", command=add) #버튼
    add_btn.grid(row=2, column=1)
    remove_btn=tk.Button(frame, text="삭제", command=remove)
    remove_btn.grid(row=2, column=2)
    save_btn=tk.Button(frame, text="저장", command=save)
    save_btn.grid(row=2, column=3)

    savedLabel = tk.Label(frame, text="")  # 저장 완료 메시지
    savedLabel.grid(row=3, column=1)

    listbox=tk.Listbox(frame,selectmode=tk.SINGLE) #하나의 아이템씩
    listbox.grid(row=4, column=2)

    total_label=tk.Label(frame,text="총 지출: 0원")
    total_label.grid(row=5, column=2)