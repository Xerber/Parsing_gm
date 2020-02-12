from requests import session
from bs4 import BeautifulSoup as bs
from telebot import TeleBot
from time import localtime
from config import token, chat_id

bot = TeleBot(token)

def weather_quit():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
    r = session().get('https://www.gismeteo.ua/weather-luhansk-5082/tomorrow/',headers=headers)
    soup = bs(r.text, 'lxml')
    divs = soup.find_all('div',attrs={'class':'tabs _center'})
    temperature_all=[]
    temp_quit=[]
    for div in divs:
        weather_today = div.find('a',attrs={'class':'nolink tab tablink tooltip'})['data-text']
        weather_tomorrow = div.find('div',attrs={'class':'tab tooltip'})['data-text']
        temperature_all.append(div.find_all('div',attrs={'class':'value'}))
    for temp in temperature_all:
        for t in temp:
            temp_quit.append(t.find('span',attrs={'class':'unit unit_temperature_c'}).text)
    temp_today = temp_quit[0] + ' ' + temp_quit[1]
    temp_tomorrow = temp_quit[2] + ' ' + temp_quit[3]
    today = weather_today + '\n Температура воздуха: ' + temp_today
    tomorrow = weather_tomorrow + '\n Температура воздуха: ' + temp_tomorrow
    if localtime().tm_hour < 12:
        a = 'Сегодня: \n'+ today +'\n Завтра: \n'+tomorrow
    else:
        a = 'Завтра: \n'+tomorrow
    return a

text_out = weather_quit()
bot.send_message(chat_id=chat_id, text=text_out)
