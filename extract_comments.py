from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def extract_comments(url):
    options = webdriver.ChromeOptions() # Setup Chrome options
    #options.add_argument("--headless")  # Run in headless mode to avoid UI pop-ups
    options.add_argument("--disable-blink-features=AutomationControlled")  # Helps prevent bot detection

    driver = webdriver.Chrome(options=options)  # Initialize Chrome driver
    driver.get(url) # Open YouTube video URL

    time.sleep(5)  # Allow the page to load

    # Scroll multiple times to load all comments
    comment_section = driver.find_element(By.TAG_NAME, 'body')
    for _ in range(30):  # Increased scrolling attempts, defaulit range - 20
        comment_section.send_keys(Keys.END)
        time.sleep(2)  # Adding delay to prevent detection

    comments = []

    # Locate YouTube comment elements properly
    try: # Get all comment elements
        elements = driver.find_elements(By.CSS_SELECTOR, "#content-text")  # Correct selector for YouTube comments

        # Filter only Chinese/Japanese comments
        for element in elements:
            text = element.text.strip()
            if any("\u4e00" <= char <= "\u9fff" for char in text):  # Checks for Chinese/Japanese characters
                comments.append(text)

    except Exception as e:
        print("Error extracting comments:", str(e))

    driver.quit()  # Close browser
    return comments

