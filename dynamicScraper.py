from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Set up headless browser options
options = Options()
options.add_argument("--disable-extensions")       # Disable extensions
options.add_argument("--disable-gpu")             # Disable GPU acceleration
options.add_argument("--disable-dev-shm-usage")   # Reduce shared memory usage
options.add_argument("--window-size=1920,1080")   # Ensure proper rendering
options.add_argument("--headless")                # Run in headless mode
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # macOS user agent

# Initialize the driver
driver = webdriver.Chrome(options=options)

try:
    # Open the webpage
    driver.get("https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-reading-pennsylvania-november-4-2024/")  # Replace with your target URL

    # Wait for the element to load (maximum 300 seconds)
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/main/div[2]/div[2]/div[3]/div/div[2]"))
    )

    # Locate the parent element
    parent_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div[2]/div[2]/div[3]/div/div[2]")

    # Find all direct children
    children = parent_element.find_elements(By.XPATH, "./*")

    # Traverse and process each child
    for idx, child in enumerate(children):
        print(f"Child {idx + 1}: {child.tag_name}, Text: {child.text}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the browser
    driver.quit()
