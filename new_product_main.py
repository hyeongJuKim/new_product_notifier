# pa.py
import telepot, time


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    from_id = msg['from']['id']
    text = msg['text']

    # 텍스트일때만 동작
    if content_type == 'text':
        print('text: ',text)

        # 각 명령어에 따른 분기
        if text == '/메뉴':
            show_keyboard = {'keyboard': [['시작'], ['정지'], ['현재 상태 확인'],['예약시시간 설정']]}  # 나중에 상수로 변경
            bot.sendMessage(from_id, '메뉴를 선택하세요', reply_markup=show_keyboard)
        elif text == '/상태':
            bot.sendMessage(from_id, '현재 상태: 타겟 사이트, 예약시간, ')
        else:
            print(text, '라는 명령어를 찾지 못했습니다: ')
            bot.sendMessage(from_id, '명령어를 찾지 못했습니다: ')


# 봇 생성, loop
bot = telepot.Bot('264003371:AAGrB2T34VSCM5_yw5UagxnvPWTS0JmkfJI')
bot.message_loop(handle)
print ('Listening...')

# 반복
while 1:
    time.sleep(10)
