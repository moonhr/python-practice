import subprocess

# ollama 모델 실행 함수
def run_ollama_model(model_name, prompt):
    try:
        # ollama run 명령어 실행
        result = subprocess.run(
            ['ollama', 'run', model_name, prompt],  # ollama 명령어와 인자들
            capture_output=True,  # 출력 캡처
            text=True  # 텍스트로 결과 받기
        )

        # 실행 성공 시 응답 출력
        if result.returncode == 0:
            return result.stdout.strip()  # 모델의 응답
        else:
            return f"Error: {result.stderr}"  # 오류 발생 시 오류 메시지 출력

    except FileNotFoundError:
        return "Ollama CLI가 설치되어 있지 않습니다. Ollama를 설치하고 다시 시도하세요."

# 사용자 입력 받기
model_name = 'llama3.1'  # 실행할 모델 이름
prompt = input("질문을 입력하세요: ")  # 사용자로부터 질문을 입력받음

# 모델 실행
response = run_ollama_model(model_name, prompt)
print("LLM 응답:", response)
