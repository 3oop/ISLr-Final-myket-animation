import os
import csv
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Firefox settings for headless mode
options = Options()
options.headless = True

# Launch Firefox browser
driver = webdriver.Firefox(options=options)

# Webpage URL
url = "https://myket.ir/video/list/automated_genre_animation_trending"
driver.get(url)

# Add a wait time for the page to fully load and observe changes
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # Wait time for manual changes

# Extract animation links
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# Close the browser
driver.quit()

# Save links in a CSV file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")


# Firefox settings for headless mode
options = Options()
options.headless = True

# Launch Firefox browser
driver = webdriver.Firefox(options=options)

# Webpage URL
url = "https://myket.ir/video/list/automated_genre_animation_2023"
driver.get(url)

# Add a wait time for the page to fully load and observe changes
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 35 ثانیه زمان دارید...")
time.sleep(35)  # Wait time for manual changes

# Extract animation links
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# Close the browser
driver.quit()

# Save links in a CSV file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links2.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")

# Firefox settings for headless mode
options = Options()
options.headless = True

# Launch Firefox browser
driver = webdriver.Firefox(options=options)

# Webpage URL
url = "https://myket.ir/video/list/automated_mixedgenres_animation_adventure"
driver.get(url)

# Add a wait time for the page to fully load and observe changes
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # Wait time for manual changes

# Extract animation links
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# Close the browser
driver.quit()

# Save links in a CSV file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links3.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")


# Firefox settings for headless mode
options = Options()
options.headless = True

# Launch Firefox browser
driver = webdriver.Firefox(options=options)

# Webpage URL
url = "https://myket.ir/video/list/automated_mixedgenres_animation_comedy"
driver.get(url)

# Add a wait time for the page to fully load and observe changes
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # Wait time for manual changes

# Extract animation links
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# Close the browser
driver.quit()

# Save links in a CSV file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links4.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")

# Firefox settings for headless mode
options = Options()
options.headless = True

# Launch Firefox browser
driver = webdriver.Firefox(options=options)

# Webpage URL
url = "https://myket.ir/video/list/automated_mixedgenres_animation_family"
driver.get(url)

# Add a wait time for the page to fully load and observe changes
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # Wait time for manual changes

# Extract animation links
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# Close the browser
driver.quit()

# Save links in a CSV file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links5.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")

# Firefox settings for headless mode
options = Options()
options.headless = True

# Launch Firefox browser
driver = webdriver.Firefox(options=options)

# Webpage URL
url = "https://myket.ir/video/list/automated_mixedgenres_animation_fantasy"
driver.get(url)

# Add a wait time for the page to fully load and observe changes
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # Wait time for manual changes

# Extract animation links
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# Close the browser
driver.quit()

#  Save links in a CSV file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links6.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")

# Firefox settings for headless mode
options = Options()
options.headless = True

# Launch Firefox browser
driver = webdriver.Firefox(options=options)

# Webpage URL
url = "https://myket.ir/video/list/automated_mixedgenres_animation_action"
driver.get(url)

# Add a wait time for the page to fully load and observe changes
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # Wait time for manual changes

# Extract animation links
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# Close the browser
driver.quit()

#  Save links in a CSV file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links7.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")

# Firefox settings for headless mode
options = Options()
options.headless = True

# Launch Firefox browser
driver = webdriver.Firefox(options=options)

# Webpage URL
url = "https://myket.ir/video/list/automated_mixedgenres_animation_sci-fi"
driver.get(url)

# Add a wait time for the page to fully load and observe changes
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # Wait time for manual changes

# Extract animation links
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# Close the browser
driver.quit()

# Save links in a CSV file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links8.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")

# Firefox settings for headless mode
options = Options()
options.headless = True

# Launch Firefox browser
driver = webdriver.Firefox(options=options)

# Webpage URL
url = "https://myket.ir/video/list/automated_mixedgenres_animation_drama"
driver.get(url)

# Add a wait time for the page to fully load and observe changes
print("مرورگر باز شد. تغییرات لازم را اعمال کنید. 20 ثانیه زمان دارید...")
time.sleep(20)  # Wait time for manual changes

# Extract animation links
elements = driver.find_elements(By.CSS_SELECTOR, "#main-Content a")
links = [element.get_attribute("href") for element in elements]
links = ["https://myket.ir" + link for link in links]

# Close the browser
driver.quit()

# Save links in a CSV file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop_path, "animation_links9.csv")

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in links:
        writer.writerow([link])

print(f"Links have been saved to {csv_file_path}")


