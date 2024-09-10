import subprocess
import pandas as pd

# CSV 파일에서 데이터 불러오기
def load_and_clean_data():
    df = pd.read_csv('crawled_data.csv')

    # 결측값 채우기 또는 기타 정제 작업
    df.fillna("N/A", inplace=True)

    # 필요한 경우 데이터 변환 또는 추가 처리
    return df

# LLM을 사용하여 데이터 정제
def run_ollama_model(prompt):
    try:
        result = subprocess.run(
            ['ollama', 'run', 'llama3.1', prompt],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr}"
    except FileNotFoundError:
        return "Ollama CLI가 설치되어 있지 않습니다."

if __name__ == "__main__":
    # 1. 데이터 불러오기
    df = load_and_clean_data()

    # 2. LLM을 사용하여 데이터 분석/정제
    for index, row in df.iterrows():
        prompt = f"정제된 이름: {row['Name']}, 가격: {row['Price']}"
        response = run_ollama_model(prompt)
        print(f"LLM 응답: {response}")
