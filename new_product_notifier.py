# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
import telepot


def check_new_item(int_new_count):
    """
    인자값 : 신상품의 갯수
    설 명 : 품절을 제외한 신상품이 있는지 체크
    """
    li = soup.find_all(name='li', attrs={"class": "item xans-record-"})
    num_new_item_count = 0
    for i in range(0, int_new_count):
        soldout_img = li[i].find(name='img', attrs={"class": "icon_img"})
        if soldout_img != None: continue
        num_new_item_count += 1

    num_new_item_count = True if num_new_item_count == 0 else False
    return num_new_item_count


def get_item_list(int_new_count):
    """
    인자값 : 신상품의 갯수
    설 명 : 신상품의 갯수를 입력받아서 가장 최신 페이지의 상품 정보들을 return
    """
    arr = ["오 떴다!"]
    li = soup.find_all(name='li', attrs={"class": "item xans-record-"})

    for i in range(0, int_new_count):
        soldout_img = li[i].find(name='img', attrs={"class": "icon_img"})

        if soldout_img != None: continue
        str_base_url = soup.find("link")["href"]
        str_brand_name = li[i].find("p").find("a").text.replace(" : ", "")
        str_item_url = str_base_url + li[i].find("a")["href"]  # root path + IMG URL
        str_item_img = li[i].find("img")['src']

        item = "상품명: " + str_brand_name + "\n " + str_item_url + "\n " + str_item_img
        arr.append(item)

    rtn_str = ''.join(arr)
    return rtn_str


# URL을 열어서 html로 파싱한다.
res = urlopen(
    'http://www.bazal.co.kr/product/search.html?view_type=&supplier_code=&category_no=&keyword=%28250%29&product_price1=&product_price2=&order_by=recent&x=138&y=19').read()
soup = BeautifulSoup(res, 'html.parser')

# 쇼핑몰의 현재 상품의 총 갯수.
int_now_total = int(soup.find(name="p", attrs={"class": "record"}).find(name="strong").get_text())

#####################################
# 가장 최근에 입력한상품의 총 갯수. 
# (지금은 테스트이므로 값을 박아서 사용중)
#####################################
int_last_total = int(int_now_total) - 1

# 갯수의 차 (신상품의 갯수 - 솔드아웃 포함)
int_new_count = (int(int_now_total) - int(int_last_total))

# 신상품이 있는지 확인 (품절까지)
bool_new_item = check_new_item(int_new_count)

if int_last_total >= int_now_total or bool_new_item:
    print("총 상품 갯수가 그대로이거나 갯수가 다르지만 이미 품절인 상품이 포함되어있습니다.")


    # 테스트 코드
    bot = telepot.Bot('264003371:AAGrB2T34VSCM5_yw5UagxnvPWTS0JmkfJI')
    show_keyboard = {'keyboard': [['시작'], ['정지'], ['현재 상태 확인'],['예약시시간 설정']]}  # 나중에 상수로 변경
    bot.sendMessage(210535889, '메뉴를 선택하세요',reply_markup=show_keyboard)



elif int_last_total < int_now_total or bool_new_item:
    print("총 상품 갯수가 다르다.")

    # 신상품 리스트 받기
    item_list = get_item_list(int_new_count)

    # 인증키 받기
    bot = telepot.Bot('264003371:AAGrB2T34VSCM5_yw5UagxnvPWTS0JmkfJI')

    # 봇에게 마지막 신상품 결과값을 전달
    bot.sendMessage(210535889, item_list)
    quit()
# DB에 최신값 update
