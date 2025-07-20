import os
import time
import platform

from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import config
import WhatsAppBomberBanner
from WhatsAppBomberBanner import style


def clear_console():
    os.system("cls" if platform.system() == "Windows" else "clear")


def get_driver_path() -> str:
    driver_name = "chromedriver.exe" if platform.system() == "Windows" else "chromedriver"
    return os.path.realpath(os.path.join(os.getcwd(), "driver", driver_name))


def launch_browser(driver_path: str, profile_path: str) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.add_argument(profile_path)
    service = Service(driver_path)
    browser = webdriver.Chrome(service=service, options=options)

    browser.get("https://web.whatsapp.com/")
    if platform.system() != "Windows":
        browser.maximize_window()

    return browser


def confirm_target(browser: Any) -> bool:
    target_xpath = input("Enter target Full XPath: ")
    try:
        browser.find_element(By.XPATH, target_xpath).click()
        time.sleep(2)
    except Exception:
        print(style.RED + "❌ Invalid XPath provided.")
        return False

    print(style.MAGENTA)
    confirm = input("Please confirm the target (yes/no): ").strip().lower()
    return confirm in {"yes", "y"}


def send_messages(browser: Any):
    print(style.BLUE)
    message = input("Enter message to send: ")
    count = int(input("Enter amount: "))

    for i in range(count):
        print(style.RED + f"[+] Messages sent: {i + 1}")

        try:
            input_box = browser.find_element(By.XPATH,
                '/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div/div[3]/div')
            send_button = browser.find_element(By.XPATH,
                '/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div/div[4]')
        except Exception:
            print(style.RED + "❌ Unable to locate input or send button.")
            return

        input_box.send_keys(message)
        send_button.click()
        time.sleep(3)

    print(style.GREEN + "✅ Done..." + style.RESET)


def interactive_loop(browser: Any):
    while True:
        try:
            if confirm_target(browser):
                send_messages(browser)
            else:
                print(style.RED + "Target not confirmed. Try again.")
        except Exception as e:
            print(style.RED + f"Error: {e}" + style.RESET)
            continue


def main():
    clear_console()
    print(WhatsAppBomberBanner.banner)
    print(style.GREEN)

    try:
        driver_path = get_driver_path()
        profile_path = config.CHROME_PROFILE_PATH
        browser = launch_browser(driver_path, profile_path)
        time.sleep(15)
        interactive_loop(browser)
    except Exception as e:
        print(style.RED + f"Fatal error: {e}" + style.RESET)
    finally:
        try:
            browser.quit()
        except:
            pass


if __name__ == "__main__":
    main()
