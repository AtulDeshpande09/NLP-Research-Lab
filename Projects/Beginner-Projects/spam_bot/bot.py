import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load video links and comments
with open("links.txt", "r") as f:
    video_links = [line.strip() for line in f if line.strip()]
with open("comments.txt", "r") as f:
    comments = [line.strip() for line in f if line.strip()]

# Firefox profile path (must be logged into YouTube already)
profile_path = "/home/your_user_name/.mozilla/firefox/py5pylwz.bot_profile"
options = Options()
options.profile = profile_path

# Start Firefox browser
driver = webdriver.Firefox(options=options)

# Loop through all video links
for link in video_links:
    try:
        driver.get(link)
        print(f"▶️ Visiting: {link}")

        # Scroll to bottom to trigger comment section load
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Let YouTube load comments

        # Wait for comment box placeholder
        placeholder = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "simplebox-placeholder"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", placeholder)
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, -100);")  # Adjust to avoid overlays
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "simplebox-placeholder")))

        # 💡 JS click avoids overlay issues
        driver.execute_script("arguments[0].click();", placeholder)
        time.sleep(2)

        # Find the text input area
        text_area = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#contenteditable-root[contenteditable='true']"))
        )
        comment = random.choice(comments)
        text_area.send_keys(comment)
        time.sleep(2)

        # Click submit button
        submit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit-button"))
        )
        submit.click()
        print(f"✅ Comment posted: {comment}")

    except Exception as e:
        print(f"❌ Failed to comment on {link}: {e}")
        # Save page source for debugging
        with open("debug_page.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

    # Wait before next video to look human-like
    time.sleep(random.randint(8, 15))

driver.quit()
print("🚀 Done with all videos.")
