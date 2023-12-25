import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


def get_screenshots(post, id_list):
    driver, wait = driver_setup(post.url)
    post_ss(driver, wait, post)
    comment_ss(driver, wait, id_list)
    driver.quit()


def post_ss(driver, wait, post):
    post = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Post")))
    driver.execute_script("window.focus();")
    ss_name = f"Screenshots/Post-{post.id}.png"
    with open(ss_name, "wb") as file:
        file.write(post.screenshot_as_png)


def comment_ss(driver, wait, id_list):
    for id in id_list:
        comment = wait.until(EC.presence_of_element_located((By.ID, f"t1_{id}")))
        driver.execute_script("window.focus();")
        ss_name = f"Screenshots/comment-{id}.png"
        with open(ss_name, "wb") as file:
            file.write(comment.screenshot_as_png)


def driver_setup(url):
    options = Options()
    options.add_argument(f"user-data-dir={os.getenv('user_data_dir')}")
    options.add_argument("profile-directory=Default")
    service = Service(f"{os.getenv('edge_driver_dir')}")
    driver = webdriver.Edge(service=service, options=options)
    wait = WebDriverWait(driver, timeout=1000)
    driver.set_window_size(width=600, height=800)
    driver.get(url)

    return driver, wait