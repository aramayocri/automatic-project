from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

EXTENSION_PATH = 'C:/Users/Crih/Documents/consola/automatic-project/metamask/10.17.0-Crx4Chrome.com.crx'

opt = Options()
opt.add_extension(EXTENSION_PATH)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)

driver.switch_to.window(driver.window_handles[0])
original_window = driver.current_window_handle


def test():
    # Get Started
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/button"))).click()
    # Import Wallet
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button"))).click()
    #Donate Data. No thanks!
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]"))).click()

    time.sleep(1)

    # Seed phrase
    driver.find_element(By.ID, "import-srp_srp-word-0").send_keys("FIRST WORD")
    driver.find_element(By.ID, "import-srpsrp-word-1").send_keys("SECOND WORD")
    driver.find_element(By.ID, "import-srpsrp-word-2").send_keys("THIRD WORD")
    driver.find_element(By.ID, "import-srpsrp-word-3").send_keys("FOURTH WORD")
    driver.find_element(By.ID, "import-srpsrp-word-4").send_keys("FIFTH WORD")
    driver.find_element(By.ID, "import-srpsrp-word-5").send_keys("SIXTH WORD")
    driver.find_element(By.ID, "import-srpsrp-word-6").send_keys("SEVENTH WORD")
    driver.find_element(By.ID, "import-srpsrp-word-7").send_keys("EIGHTH WORD")
    driver.find_element(By.ID, "import-srpsrp-word-8").send_keys("NINTH WORD")
    driver.find_element(By.ID, "import-srpsrp-word-9").send_keys("TENTH WORD")
    driver.find_element(By.ID, "import-srpsrp-word-10").send_keys("ELEVENTH WORD")
    driver.find_element(By.ID, "import-srp_srp-word-11").send_keys("TWELFTH WORD")

    # Passwords
    driver.find_element(By.ID, "password").send_keys("password")
    driver.find_element(By.ID, "confirm-password").send_keys("password")

    # Agree to T&Cs & Submit
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='create-new-vault__terms-checkbox']"))).click()

    # Import Button
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div[2]/form/button"))).click()

    # Congratulations page
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/button"))).click()

    # Intro pop-up box
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popover-content']/div/div/section/div[2]"))).click()

if __name__ == '__main__':
    test()

