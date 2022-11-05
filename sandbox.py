from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = 'https://www.amazon.com/atolla-Charging-Splitter-Individual-Switches/dp/B083XTKV8V/ref=pd_day0fbt_img_2/134-3733739-5805861?pd_rd_w=RPVwd&pf_rd_p=bcb8482a-3db5-4b0b-9f15-b86e24acdb00&pf_rd_r=BSQ0EHFJGZMF37NQ4MXZ&pd_rd_r=7f2f2d26-1b52-467a-b2d1-1a3bb2eb28aa&pd_rd_wg=bTYbS&pd_rd_i=B083XTKV8V&psc=1'
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)
price = driver.find_element(By.CSS_SELECTOR, 'span.a-price')
print(f'Price: {price.text}')
time.sleep(3)

driver.quit()

# driver.close() closes one tab
