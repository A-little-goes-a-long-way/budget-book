# data_handler.py

def load_expenses(file_path):
    """
    지출 데이터를 파일에서 읽어서 날짜별로 정리한 딕셔너리를 반환
    예:
    {
        "2025-05-18": [
            "juice: 3500원",
            "pencil: 800원"
        ]
    }
    """
    expenses = {}  # 날짜별 데이터를 저장할 딕셔너리
    with open(file_path, encoding="utf-8") as file:  # 파일 열기
        date = None  # 현재 날짜를 저장할 변수
        for line in file:  # 파일의 각 줄을 반복 처리
            line = line.strip()  # 줄 끝의 공백 제거
            if line.startswith("총 지출"):  # "총 지출" 줄은 불필요하므로 무시
                continue
            if line.endswith("원"):  # 금액과 지출 항목이 포함된 줄
                if date is not None:  # 날짜가 설정된 경우에만 처리
                    if date not in expenses:
                        expenses[date] = []  # 해당 날짜가 딕셔너리에 없으면 리스트 생성
                    expenses[date].append(line)  # 지출 항목 추가
            elif line.split(":")[0].isdigit():  # 날짜 형식인 경우
                date = line.split(":")[0]  # 날짜를 저장
    return expenses  # 날짜별로 정리된 지출 데이터를 반환


def load_income(file_path):
    """
    수입 데이터를 파일에서 읽어서 날짜별로 정리한 딕셔너리를 반환
    예:
    {
        "2025-05-18": [
            "hello: 900원",
            "good: 1000원"
        ]
    }
    """
    income = {}  # 날짜별 데이터를 저장할 딕셔너리
    with open(file_path, encoding="utf-8") as file:  # 파일 열기
        date = None  # 현재 날짜를 저장할 변수
        for line in file:  # 파일의 각 줄을 반복 처리
            line = line.strip()  # 줄 끝의 공백 제거
            if line.startswith("총 수입"):  # "총 수입" 줄은 불필요하므로 무시
                continue
            if line.endswith("원"):  # 금액과 수입 항목이 포함된 줄
                if date is not None:  # 날짜가 설정된 경우에만 처리
                    if date not in income:
                        income[date] = []  # 해당 날짜가 딕셔너리에 없으면 리스트 생성
                    income[date].append(line)  # 수입 항목 추가
            elif line.split(":")[0].isdigit():  # 날짜 형식인 경우
                date = line.split(":")[0]  # 날짜를 저장
    return income  # 날짜별로 정리된 수입 데이터를 반환
