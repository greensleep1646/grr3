import requests
from bs4 import BeautifulSoup

def instagram_eposta_bul(username):
    url = f"https://www.instagram.com/{username}/?__a=1"
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json()
        if 'graphql' in user_data and 'user' in user_data['graphql']:
            user_info = user_data['graphql']['user']
            if 'business_email' in user_info and user_info['business_email']:
                print(f"{username}'ın e-posta adresi: {user_info['business_email']}")
            else:
                print("E-posta bulunamadı.")
        else:
            print("Kullanıcı verisi bulunamadı.")
    else:
        print("Instagram profili bulunamadı.")

username = input("Hedefin Instagram kullanıcı adını gir: ")
instagram_eposta_bul(username)
