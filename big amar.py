import os
import csv
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# تنظیمات فایرفاکس برای حالت headless
options = Options()
options.headless = True

# راه‌اندازی مرورگر فایرفاکس
driver = webdriver.Firefox(options=options)

# آدرس صفحه وب
url = "https://myket.ir/video/list/automated_genre_animation_trending"
driver.get(url)

# افزودن زمان انتظار برای بارگذاری کامل صفحه و مشاهده تغییرات
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # زمان انتظار برای اعمال تغییرات دستی

# استخراج لینک‌های انیمیشن‌ها
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# بستن مرورگر
driver.quit()

# ذخیره لینک‌ها در یک فایل CSV در دسکتاپ
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")


# تنظیمات فایرفاکس برای حالت headless
options = Options()
options.headless = True

# راه‌اندازی مرورگر فایرفاکس
driver = webdriver.Firefox(options=options)

# آدرس صفحه وب
url = "https://myket.ir/video/list/automated_genre_animation_2023"
driver.get(url)

# افزودن زمان انتظار برای بارگذاری کامل صفحه و مشاهده تغییرات
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(30)  # زمان انتظار برای اعمال تغییرات دستی

# استخراج لینک‌های انیمیشن‌ها
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# بستن مرورگر
driver.quit()

# ذخیره لینک‌ها در یک فایل CSV در دسکتاپ
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links2.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")
import os
import csv
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# تنظیمات فایرفاکس برای حالت headless
options = Options()
options.headless = True

# راه‌اندازی مرورگر فایرفاکس
driver = webdriver.Firefox(options=options)

# آدرس صفحه وب
url = "https://myket.ir/video/list/automated_mixedgenres_animation_adventure"
driver.get(url)

# افزودن زمان انتظار برای بارگذاری کامل صفحه و مشاهده تغییرات
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # زمان انتظار برای اعمال تغییرات دستی

# استخراج لینک‌های انیمیشن‌ها
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# بستن مرورگر
driver.quit()

# ذخیره لینک‌ها در یک فایل CSV در دسکتاپ
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links3.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")


# تنظیمات فایرفاکس برای حالت headless
options = Options()
options.headless = True

# راه‌اندازی مرورگر فایرفاکس
driver = webdriver.Firefox(options=options)

# آدرس صفحه وب
url = "https://myket.ir/video/list/automated_mixedgenres_animation_comedy"
driver.get(url)

# افزودن زمان انتظار برای بارگذاری کامل صفحه و مشاهده تغییرات
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # زمان انتظار برای اعمال تغییرات دستی

# استخراج لینک‌های انیمیشن‌ها
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# بستن مرورگر
driver.quit()

# ذخیره لینک‌ها در یک فایل CSV در دسکتاپ
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links4.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")

# تنظیمات فایرفاکس برای حالت headless
options = Options()
options.headless = True

# راه‌اندازی مرورگر فایرفاکس
driver = webdriver.Firefox(options=options)

# آدرس صفحه وب
url = "https://myket.ir/video/list/automated_mixedgenres_animation_family"
driver.get(url)

# افزودن زمان انتظار برای بارگذاری کامل صفحه و مشاهده تغییرات
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # زمان انتظار برای اعمال تغییرات دستی

# استخراج لینک‌های انیمیشن‌ها
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# بستن مرورگر
driver.quit()

# ذخیره لینک‌ها در یک فایل CSV در دسکتاپ
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links5.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")

# تنظیمات فایرفاکس برای حالت headless
options = Options()
options.headless = True

# راه‌اندازی مرورگر فایرفاکس
driver = webdriver.Firefox(options=options)

# آدرس صفحه وب
url = "https://myket.ir/video/list/automated_mixedgenres_animation_fantasy"
driver.get(url)

# افزودن زمان انتظار برای بارگذاری کامل صفحه و مشاهده تغییرات
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # زمان انتظار برای اعمال تغییرات دستی

# استخراج لینک‌های انیمیشن‌ها
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# بستن مرورگر
driver.quit()

# ذخیره لینک‌ها در یک فایل CSV در دسکتاپ
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links6.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")

# تنظیمات فایرفاکس برای حالت headless
options = Options()
options.headless = True

# راه‌اندازی مرورگر فایرفاکس
driver = webdriver.Firefox(options=options)

# آدرس صفحه وب
url = "https://myket.ir/video/list/automated_mixedgenres_animation_action"
driver.get(url)

# افزودن زمان انتظار برای بارگذاری کامل صفحه و مشاهده تغییرات
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # زمان انتظار برای اعمال تغییرات دستی

# استخراج لینک‌های انیمیشن‌ها
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# بستن مرورگر
driver.quit()

# ذخیره لینک‌ها در یک فایل CSV در دسکتاپ
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links7.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")

# تنظیمات فایرفاکس برای حالت headless
options = Options()
options.headless = True

# راه‌اندازی مرورگر فایرفاکس
driver = webdriver.Firefox(options=options)

# آدرس صفحه وب
url = "https://myket.ir/video/list/automated_mixedgenres_animation_sci-fi"
driver.get(url)

# افزودن زمان انتظار برای بارگذاری کامل صفحه و مشاهده تغییرات
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # زمان انتظار برای اعمال تغییرات دستی

# استخراج لینک‌های انیمیشن‌ها
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# بستن مرورگر
driver.quit()

# ذخیره لینک‌ها در یک فایل CSV در دسکتاپ
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links8.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")

# تنظیمات فایرفاکس برای حالت headless
options = Options()
options.headless = True

# راه‌اندازی مرورگر فایرفاکس
driver = webdriver.Firefox(options=options)

# آدرس صفحه وب
url = "https://myket.ir/video/list/automated_mixedgenres_animation_drama"
driver.get(url)

# افزودن زمان انتظار برای بارگذاری کامل صفحه و مشاهده تغییرات
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # زمان انتظار برای اعمال تغییرات دستی

# استخراج لینک‌های انیمیشن‌ها
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# بستن مرورگر
driver.quit()

# ذخیره لینک‌ها در یک فایل CSV در دسکتاپ
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links9.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")


