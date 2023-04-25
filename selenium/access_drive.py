from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def iniciar_chrome():
    options = Options()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("start-maximized")
    # options.add_argument("--headless")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-sandbox")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-notifications")
    options.add_experimental_option('detach', True)
    exp_opt = [
        "enable-automation",
        "ignore-certificate-errors",
        "enable-logging"
    ]
    options.add_experimental_option('excludeSwitches', exp_opt)
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "intl.accept_languages": ["es-ES", "es"],
        "credentials_enable_service": False
    }
    options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    return driver


if __name__ == "__main__":
    driver = iniciar_chrome()
    url = "https://drive.google.com"
    driver.get(url)
    time.sleep(5)
    
    driver.quit()