from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl
import undetected_chromedriver as uc
from time import sleep

# I removed some place and state names to save space
places = ['Alaska', 'Alabama Middle', 'Alabama Northern']
states_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']

states = {item: next((state for state in states_list if state in item), '') for item in places}

records = []

options = uc.ChromeOptions()
options.add_argument('-headless')
driver = uc.Chrome(options=options)

for p, place in enumerate(places):
    try:
        place = place.lower().replace(' ', '-')
        # I change the name of the bankruptcy site to protect my intellectual property
        url = f'https://www.uscourts.gov/report-name/bankruptcy-filings/{place}-bankruptcy-cases-filed-in-2023?page=1'
        print(url)
        driver.get(url)
        sleep(5)
        for i in range(1, 51):
            try:
                title = driver.find_element(By.XPATH,
                                            f'//*[@id="__next"]/div/div/div[2]/div[2]/div/table/tbody/tr[{i}]/td[1]').text
                location = driver.find_element(By.XPATH,
                                               f'//*[@id="__next"]/div/div/div[2]/div[2]/div/table/tbody/tr[{i}]/td[2]').text
                case = driver.find_element(By.XPATH,
                                           f'//*[@id="__next"]/div/div/div[2]/div[2]/div/table/tbody/tr[{i}]/td[3]/a').text
                chapter = driver.find_element(By.XPATH,
                                              f'//*[@id="__next"]/div/div/div[2]/div[2]/div/table/tbody/tr[{i}]/td[4]').text
                date = driver.find_element(By.XPATH,
                                           f'//*[@id="__next"]/div/div/div[2]/div[2]/div/table/tbody/tr[{i}]/td[5]').text
                records.append([title, location, case, chapter, date])
            except:
                break
    except Exception as e:
        print(f"An error occurred while processing '{place}': {str(e)}")

driver.quit()

df = pd.DataFrame(records, columns=['Title', 'Location', 'Case', 'Chapter', 'Date'])
df['State'] = df['Location'].apply(lambda x: states.get(x))
df.to_excel('bankruptcies_061423.xlsx', index=False)
print(df.tail())