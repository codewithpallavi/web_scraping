# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()

# query = "laptop"
# driver.get(f"https://www.amazon.in/s?k={query}laptop&crid=39L7SH9JWSY6U&sprefix=laptop%2Caps%2C234&ref=nb_sb_noss_1")
# elem = driver.find_element(By.CLASS_NAME, "puisg-row")
# print(elem.text)
# time.sleep(20)
# driver.quit()





from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

query = "laptop"
file = 0
for i in range(1,20):
    
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=1EK1NGM7OQAYO&qid=1722409413&sprefix=l%2Caps%2C368&ref=sr_pg_2")

    elems = driver.find_elements(By.CLASS_NAME, "puisg-row")
    print(f"{len(elems)}items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open (f"data/{query}_{file}.html", "w", encoding="utf-8") as f:    
            f.write(d)
            file += 1
    time.sleep(20)
driver.close()
