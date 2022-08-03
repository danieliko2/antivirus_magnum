import csv
import selenium
import time


# def testPage(page):
#     browser.get(page)
#     wait.until(visible((By.ID, "video-title")))
#     browser.find_element_by_id("video-title").click()
#     browser.minimize_window()
#     time.sleep(7)
#     browser.quit()

# testPage("http://www.google.com")

def print_me(me):
    print(me)

print("")

def add_ip(ipData):
    with open("data/data.csv", "a") as f:
        write = csv.writer(f)
        write.writerow(ipData)
