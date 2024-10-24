from selenium import webdriver
from selenium.webdriver.common.by import By
import time

fichier_usernames = 'resultat.txt'

driver = webdriver.Chrome()  

with open(fichier_usernames, 'r') as file:
    usernames = file.readlines()

driver.get('https://www.tiktok.com')

time.sleep(5)


for username in usernames:
    username = username.strip()
    url = f'https://www.tiktok.com/@{username}'
    
    driver.get(url)
    time.sleep(3) 
    try:
        follow_button = driver.find_element(By.CSS_SELECTOR, "button[data-e2e='follow-button']")
        follow_button.click()
        print(f'a Follow : {username}')
        
        time.sleep(2)
    except Exception as e:
        print(f'na pas reussi a follow : {username}: {e}')

driver.quit()