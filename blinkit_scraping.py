from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, csv, os, codecs

driver = webdriver.Chrome(
    service=Service(r"C:\Users\ampik\Downloads\chromedriver.exe"),
    options=Options().add_argument("--no-sandbox")
)
driver.get("https://blinkit.com/cn/fresh-vegetables/cid/1487/1489")
time.sleep(3)

# Scroll to load all products
while True:
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height: break

products = []
for div in driver.find_elements(By.XPATH, "//div[contains(@class, 'line-clamp-2')]"):
    try:
        name = div.text.strip()
        container = div.find_element(By.XPATH, "./ancestor::div[4]")
        sp = container.find_element(By.XPATH, ".//div[contains(text(),'₹')]").text.strip()
        try:
            op = container.find_element(By.XPATH, ".//div[contains(@class,'line-through')]").text.strip()
        except:
            op = sp
        try:
            sp_num, op_num = float(sp.strip('₹')), float(op.strip('₹'))
            discount = f"{int(round((op_num - sp_num) / op_num * 100))}% OFF"
        except:
            discount = ""
        products.append((name, sp, op, discount))
    except:
        continue

driver.quit()

path = os.path.join(os.path.expanduser("~"), "Desktop", "blinkit_products.csv")
with codecs.open(path, "w", encoding="utf-8-sig") as f:
    csv.writer(f).writerows([["Name", "Selling Price", "Original Price", "Discount"]] + products)

print(f"✅ {len(products)} products saved to {path}")