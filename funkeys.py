# requests : http요청을 보내는 라이브러리 
import requests
# BeautifulSoup : HTML을 파싱하는 라이브러리
from bs4 import BeautifulSoup
import time
import pandas as pd

# 크롤링 함수
def funkeys_website():
    url = 'https://www.swagkey.kr/21'
    # 사람이라는걸 티내야함.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        # print(soup)
        div = soup.find('div', id='container_w202406097eb40c015dfa1')
        if div is None:
            print("찾을 수 없습니다.")
            return
        # print(div.select('div > div.item-detail > a > div > h2'))
        #container_w202406097eb40c015dfa1 > div:nth-child(1) > div.item-detail > a > div > div.item-pay-detail > p.pay.inline-blocked
        products = div.select('div > div.item-detail > a > div > h2')
        prices = div.select('div > div.item-detail > a > div > div.item-pay-detail > p.pay.inline-blocked')
        if not products or prices:
            print("제품 및 가격을 찾을 수 없습니다.")
            return
        
        products_list = []
        for product in products:
            product_text = product.get_text(strip=True)
            products_list.append(product_text)
        
        df = pd.DataFrame(products_list, columns=['Product'])
        df.to_csv('crawled_data.csv', index=False)    
        print("데이터 크롤링 완료 및 저장 완료")
        
    elif response.status_code == 429:
        print("요청이 너무 많습니다. 잠시 후 다시 시도하세요.")
        # 1초 동안 대기 후 재시도
        time.sleep(1)
        return funkeys_website()  # 재귀적으로 다시 호출    

if __name__ == "__main__":
    funkeys_website()
