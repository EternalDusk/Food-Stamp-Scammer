#selenium_imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#colorama imports
from colorama import Fore, Back, Style, init

#python imports
import json
import random
import string
import time



init(autoreset=True)

browser = webdriver.Chrome(executable_path=r"chromedriver.exe")
browser.get("https://american-assist.org/food/v3/")

#load names
names = json.loads(open('names.json').read())

SPAM_COUNT = 100

def enter_info(name, xpath, sent):
    print(Fore.YELLOW + "Sent: " + Style.RESET_ALL + sent + " to " + name)
    name = browser.find_element_by_xpath(xpath)
    name.clear()
    name.send_keys(sent)
    
    time.sleep(1)

def enter_dropdown(name, xpath, select):
    print(Fore.YELLOW + "Sent: " + Style.RESET_ALL + select + " to " + name)
    name = browser.find_element_by_xpath(xpath)
    name.click()
    for option in name.find_elements_by_tag_name('option'):
        if option.text == select:
            option.click()
    time.sleep(1)

def click_button(name, xpath):
    print(Fore.YELLOW + "Clicked: " + Style.RESET_ALL + name)
    name = browser.find_element_by_xpath(xpath)
    name.click()
    time.sleep(1)


for i in range(SPAM_COUNT):
    random_name = random.randint(0, 50)
    random_last_name = random.randint(0, 90)
    
    #first_page_variables
    enter_info("first_name_entry", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[4]/div/input[1]", names[random_name])
    enter_info("last_name_entry", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[5]/div/input", names[random_last_name])
    email = names[random_name] + "." + names[random_last_name] + "." + str(random.randint(0, 9000000)) + "@gmail.com"
    enter_info("email_entry", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[7]/div/input", email)
    zip = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    enter_info("zip_entry", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[9]/div/input", zip)
    click_button("continue_button", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[11]/button")
    time.sleep(1)
    
    #second_page_variables
    enter_info("street_address_entry", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[4]/div/input[1]", "6669 FU SCAMMER Street")
    enter_info("city_entry", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[5]/div/input", "Farmington")
    enter_dropdown("state_entry", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[6]/div/select", "Virginia")
    click_button("continue_button_2", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[7]/button")
    time.sleep(1)
    
    
    #third_page_variables
    enter_info("phone_entry", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[4]/div/input[1]", "8002655328")
    click_button("confirm_eula_entry", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[5]/p/label/input")
    click_button("continue_button_3", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[6]/button")
    
    
    #fourth_page_variables
    enter_dropdown("month_entry", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[4]/div/div/div[1]/select", "June")
    enter_dropdown("day_entry", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[4]/div/div/div[2]/select", "8")
    enter_dropdown("year_entry", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[4]/div/div/div[3]/select", "1984")
    enter_dropdown("gender_entry", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[5]/div/select", "Male")
    click_button("continue_button_4", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[6]/button")
    
    #fifth_page
    click_button("full_time", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[1]")
    
    #sixth_page
    click_button("ownrent", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[1]")
    
    #seventh_page
    click_button("purchase", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[4]")
    
    #eigth_page
    click_button("insurance", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[5]")
    
    #ninth_page
    click_button("funeral", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[2]")
    
    #tenth_page
    click_button("veteran", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[2]")
    
    #eleventh_page
    click_button("skip", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[2]")
    
    #twelfth page
    click_button("car", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[3]")
    
    #thirteenth page
    click_button("card", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[4]")
    
    #fourteenth page
    click_button("pain", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/label[5]/input")
    click_button("continue_5", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[8]/button")
    
    #fifteenth page
    click_button("no", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[2]")
    
    #sixteenth page
    click_button("no_again", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[2]")
    
    #seventeenth page
    click_button("no_but_again", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[2]")
    
    #eighteenth page
    click_button("rent_to_own", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[2]")
    
    #nineteenth page
    click_button("phone", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[2]")
    
    #twentieth page
    click_button("assets", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[2]")
    
    try:    
        #twenty-first page
        click_button("loan", "/html/body/section[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/form/div[1]/div/div[3]/div[6]/button[5]")
    
    except:
        k=1
    time.sleep(1)
    browser.get("https://american-assist.org/food/v3/")
    time.sleep(2)
