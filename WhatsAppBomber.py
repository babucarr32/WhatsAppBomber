import WhatsAppBomberBanner
from WhatsAppBomberBanner import style
from selenium import webdriver
import config
import time
import platform, os

print(WhatsAppBomberBanner.banner)
print(style.GREEN)


def main():
    try:
        CHROME_PROFILE_PATH = config.CHROME_PROFILE_PATH

        options = webdriver.ChromeOptions()
        options.add_argument(CHROME_PROFILE_PATH)
        
        platformFinder = platform.system()
        pwd = os.getcwd()
        if platformFinder == "Windows":
            path = pwd + "\Whatsapp\chromedriver.exe"
            browser = webdriver.Chrome(executable_path=os.path.realpath(path), options=options)
            browser.get('https://web.whatsapp.com/')

        elif platformFinder == "Linux":
            path = pwd + "/Whatsapp/chromedriver"
            browser = webdriver.Chrome(executable_path=os.path.realpath(path), options=options)
            browser.maximize_window()

            browser.get('https://web.whatsapp.com/')
        time.sleep(15)

        target_name = input("Enter target Full Xpath: ")
        browser.find_element_by_xpath(target_name).click()  # finding the name of target
        time.sleep(2)
        print(style.MAGENTA)
        confirm = input("Please confirm the target Yes/no: ")
        print(style.BLUE)
        message = input("Enter message to send: ")
        thread = int(input("Enter thread amount: "))

        if confirm == "Yes":
            for i in range(thread):
                print(style.RED)
                print(f"[+]Messages sent {i}")
                browser.find_element_by_xpath(
                    '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(
                    message)  # send message
                browser.find_element_by_xpath(
                    '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]/button').click()  # send message
                time.sleep(3)
        else:
            pass
    except Exception as e:
        print(e)
        # if "'chromedriver' executable needs to be in PATH." in e:
        #     print("Make sure you have the chromedriver that matches with your Chrome browser in this folder. https://chromedriver.chromium.org/home")
main()
