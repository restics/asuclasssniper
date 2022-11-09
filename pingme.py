from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import SMS
import re

course_id = "10456"

# id: 5 digit code in string format
# email: string

def look_up_course_by_id(id, email):
    print(f"Looking up class {id} for email {email}")
    url = "https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=C&honors=F&keywords=" + id + "&promod=F&searchType=all&term=2231"
    browser = wd.Firefox(executable_path=r'geckodriver.exe')

    browser.get(url)
    try:
        print("Waiting for page to load...")
        elem = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "class-results")) 
    )
    finally:
        try:
            html = browser.page_source
            positions = re.search(r'class-results-cell seats', html)
            classes = re.search(r'bold-hyperlink ', html)
            half = html[classes.span()[1]:len(html)-1];

            # search all alphanumeric characters + spaces between > and < characters (get class and professor name)
            matches = re.findall(r'\>([a-zA-Z0-9 ]{1,})\<', half)
        except:
            print("Exception occurred")
            browser.close()

        # basically takes the closest unique identifier that I could find and then shifts the amount of characters needed
        # hacky solution but i found that it works
        if html[positions.span()[1] + 27] != "0":
            print(f"Sending email to {email}")
            SMS.send(f"Your class {matches[2]} with {matches[4]} has an opening! Reserve your spot now!\n\n{url}\n\nclass code: {id}", email)
        
        browser.close()

