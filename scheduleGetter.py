from selenium import webdriver
import sys
import time

# false = headless browser window, otherwise browser window is shown
DEBUG = False

keyword = sys.argv[1]

print("Getting your desired data...")
# open website using firefox driver
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.headless = not DEBUG
driver = webdriver.Firefox(options=fireFoxOptions)
driver.get("https://www.google.co.in/search?q=" + "latech+" + keyword.replace(" ", "+"))

# delays for loading and selects top result from search
time.sleep(2)
link = driver.find_element_by_xpath('//h3[@class="LC20lb DKV0Md"]').click()

# delays for loading and scrapes schedule data
time.sleep(2)
content = driver.find_element_by_xpath('//td[@class="block_content_outer"]')

# below is just to make it easier to read
table = content.text.split("\n")
table = table[1:]

schedule = ""
for data in table:
    if (len(data) > 7):
        schedule += data + "\n"
    else:
        schedule += data + " | "

# tries to save to a file, unless an error is raised
try:
    with open(keyword.replace(" ", "") + "_Schedule", 'w', encoding="utf-8") as file:
        file.write(schedule)
        print("Successfully saved schedule contents to " + keyword.replace(" ", "") + "_Schedule")

except:
    print("Unsuccessful in saving schedule contents to file")

driver.quit()
