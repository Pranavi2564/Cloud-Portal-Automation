from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def read_config(config_file):
    config = {}
    with open(config_file, 'r') as file:
        for line in file:
            line = line.strip()
            if '=' in line:
                name, value = line.split('=', 1)
                config[name.strip()] = value.strip()
            elif line:
                print(f"Warning: Skipping malformed line: {line}")
    return config

def register_devices(username, password, filepath):
    driver=None
    try:
        driver=webdriver.Chrome()
        driver.get('https://abc@example.com/') # the name/link of the website
        time.sleep(2)

        wait=WebDriverWait(driver, 10)

        email_input=wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        password_input=driver.find_element(By.XPATH, '__')

        time.sleep(2)
        email_input.send_keys(username)
        time.sleep(2)
        password_input.send_keys(password)
        time.sleep(2)

        sign_in_button=driver.find_element(By.XPATH,'__')
        sign_in_button.click()

        time.sleep(2)
        manage_devices=wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        time.sleep(2)
        manage_devices.click()
        register_devices_button=wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        time.sleep(2)
        register_devices_button.click()

        add_devices=wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        time.sleep(2)
        add_devices.click()
        add_manage_device=wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        time.sleep(2)
        add_manage_device.click()
        
        # Scroll into view and click
        driver.execute_script("arguments[0].scrollIntoView(true);", add_manage_device)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", add_manage_device)

        
        #driver.execute_script("arguments[0].scrollIntoView(true);", add_manage_device)
        #time.sleep(1)
        #driver.execute_script("arguments[0].click();", add_manage_device)


        file_input = wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        file_input.send_keys(filepath)
        time.sleep(2)
        success_message=wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        time.sleep(2)

    except Exception as e:
        print("An error occurred", e)
    finally:
        print("Press Enter to close the browser")
        driver.quit()

if __name__ == "__main__":
    config = read_config("register_devices.txt") #file consisting of the required values
    site_username=config.get('username')
    site_password=config.get('password')
    file_path=config.get('file_path')
    register_devices(site_username, site_password, file_path)

