# requests : http요청을 보내는 라이브러리 
import requests
# BeautifulSoup : HTML을 파싱하는 라이브러리
from bs4 import BeautifulSoup
import pandas as pd

# 크롤링 함수
def crawl_website():
    url = 'https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1'  # 크롤링할 웹페이지 URL
    response = requests.get(url)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        # 'Myform' ID를 가진 form 요소 찾기
        form = soup.find('form', id='Myform')
        if form is None:
            print("Error: 'form#Myform'를 찾을 수 없습니다.")
            return
        print(form.select('div > table > tbody > tr > td > table > tbody > tr > td'))
        # 제목이 있는 요소 선택
        titles = form.select('div > table > tbody > tr > td > table > tbody > tr > td > div > ul > li > a > b')
        if not titles:
            print("Error: 타이틀을 찾을 수 없습니다. 선택자를 다시 확인하세요.")
            return
        
        # 제목 추출 및 출력
        title_list = []
        for title in titles:
            title_text = title.get_text(strip=True)  # 공백 제거한 텍스트 추출
            print(title_text)
            title_list.append(title_text)

        # DataFrame으로 변환
        df = pd.DataFrame(title_list, columns=['Title'])

        # CSV 파일로 저장
        df.to_csv('crawled_data.csv', index=False)
        print("데이터 크롤링 완료 및 저장 완료")

    else:
        print(f"HTTP 요청 실패: {response.status_code}")

if __name__ == "__main__":
    crawl_website()
