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

def automate_site_creation(username, password, site_name, location, site_tag):
    driver=None
    try:
        driver=webdriver.Chrome()
        driver.get("https://abc@example.com/")
        time.sleep(1)

        wait=WebDriverWait(driver,10)
        time.sleep(1)

        email_input=wait.until(EC.presence_of_element_located((By.XPATH, '__' )))
        password_input=driver.find_element(By.XPATH, '__')

        time.sleep(1)
        email_input.send_keys(username)
        time.sleep(1)
        password_input.send_keys(password)

        sign_in_button=driver.find_element(By.XPATH, '__')
        time.sleep(1)
        sign_in_button.click()

        manage_site = wait.until(
            EC.element_to_be_clickable((By.XPATH, '__')))
        time.sleep(1)  
        manage_site.click()

        add_site=wait.until(EC.element_to_be_clickable((By.XPATH, '__')))
        time.sleep(1)
        add_site.click()

        #site_name_details=wait.until(EC.presence_of_all_elements_located((By.XPATH, '__')))
        site_name_input = wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        location_details=driver.find_element(By.XPATH, '__')
        site_tag_details=driver.find_element(By.XPATH, '__')

        time.sleep(2)
        site_name_input.send_keys(site_name)
        time.sleep(2)
        location_details.send_keys(location)
        time.sleep(2)
        site_tag_details.send_keys(site_tag)

        time.sleep(2)
        save_site=driver.find_element(By.XPATH, '__')
        save_site.click()

        success_message = wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        time.sleep(2)  # Wait for 2 seconds

    except Exception as e:
        print("An error occurred", e)
    finally:
        if driver:
            print("Press Enter to close the browser")
            driver.quit()

if __name__ == "__main__":
    config = read_config("site_creation.txt") #file consisting of the required values
    website_username=config.get('username')
    website_password=config.get('password')
    site_name = config.get('site_name')
    site_loc=config.get('site_loc')
    site_desc = config.get('site_desc')
    automate_site_creation(website_username, website_password, site_name, site_loc, site_desc)

