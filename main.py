# 데이터 정제 프레임워크 pandas
import pandas as pd

# 더미 데이터 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Alice'],
    'Age': [25, 30, None, 22, 30, 25],
    'City': ['New York', 'Los Angeles', 'New York', None, 'San Francisco', 'New York'],
    'Salary': [70000, 80000, 50000, 60000, None, 70000]
}

# DataFrame 생성
df = pd.DataFrame(data)

# 더미 데이터 CSV 파일로 저장
df.to_csv('data.csv', index=False)

print("더미 데이터 생성 완료!")

# CSV 파일 읽기
df = pd.read_csv('data.csv')

# 결측값을 0으로 채우기
df.fillna(0, inplace=True)

# 중복된 행 제거
df.drop_duplicates(inplace=True)

# 정제된 데이터 저장
df.to_csv('cleaned_data.csv', index=False)

print("데이터 정제 완료!")
