from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


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
    url = "https://toscrape.com/"
    driver.get(url)
    res = driver.find_elements(
        By.CSS_SELECTOR, "div.col-md-6")[1].find_elements(By.CSS_SELECTOR, "th")[0]
    all_divs = driver.find_elements(By.CSS_SELECTOR, "div.col-md-6")
    """for divs in all_divs:
        if divs.text:
            print(divs.text)"""
    # Find by CSS
    amount = driver.find_element(By.CSS_SELECTOR, "div.container div.col-md-6 tr td")
    print(amount.text)

    # Xpath full path
    amount_xpath = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]")
    print(f"amaount xpath: {amount_xpath.text}")
    
    # Xpath rel path
    amount_rel_xpath = driver.find_element(By.XPATH, "//div/table/tbody[1]/tr[2]/td[1]")
    print(f"amaount rel_xpath: {amount_rel_xpath.text}")

    # Xpath starts-with
    amount_starts_with = driver.find_element(By.XPATH, "//th[starts-with(@colspan,'2')]")
    print(f"amaount starts-with: {amount_rel_xpath.text}")

    # XPATH Contains
    # Xpath = //tagname[contains(@attribute,'value')]

    # XPATH text()
    # Xpath = //tagname[text()=('ActualText')]

    # XPATH AND & OR
    # Xpath = //tagname[@Attribute='Value' and @Attribute='Value']
    # Xpath = //tagname[@Attribute='Value' or @Attribute='Value']

    # print(f"res {res.text}")

    driver.quit()
