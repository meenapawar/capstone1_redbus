# Punjab

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

url = "https://www.redbus.in/online-booking/pepsu"


# main func to  Initialize driver and scrape bus details
def scrape_bus_data(url):
    driver = webdriver.Chrome()

    def open_web(driver, url):
        driver.get(url)
        time.sleep(5)

    # scrape the bus route names and links
    def bus_route_url(driver):
        link_elements = driver.find_elements(By.CSS_SELECTOR, "a.route")
        link_texts = [i.text for i in link_elements]
        link_urls = [i.get_attribute('href') for i in link_elements]
        return link_texts, link_urls

    # scrape the bus details
    def bus_details(driver, link_text, link_url):
        driver.get(link_url)
        time.sleep(3)

        try:  # try clicking on the view buses button
            view_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button"))
            )
            driver.execute_script("arguments[0].click();", view_button)
            time.sleep(5)
            # Scroll for loading page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

            Bus_name = driver.find_elements(By.CSS_SELECTOR, "div.travels.lh-24.f-bold.d-color")
            Bus_Type = driver.find_elements(By.CSS_SELECTOR, "div.bus-type.f-12.m-top-16.l-color.evBus")
            D_Time = driver.find_elements(By.CSS_SELECTOR, "div.dp-time.f-19.d-color.f-bold")
            Duration = driver.find_elements(By.CSS_SELECTOR, "div.dur.l-color.lh-24")
            A_Time = driver.find_elements(By.CSS_SELECTOR, "div.bp-time.f-19.d-color.disp-Inline")
            Rating = driver.find_elements(By.XPATH, "//div[@class='rating-sec lh-24']")
            Price = driver.find_elements(By.CSS_SELECTOR, "div.fare.d-block span")
            Seats = driver.find_elements(By.CSS_SELECTOR, "div.seat-left")

            bus_data = []

            for i in range(len(Bus_name)):
                bus_data.append({
                    'state_name': 'Punjab',
                    'route_name': link_text,
                    'route_link': link_url,
                    'busname': Bus_name[i].text,
                    'bustype': Bus_Type[i].text,
                    'departing_time': D_Time[i].text,
                    'duration': Duration[i].text,
                    'reaching_time': A_Time[i].text,
                    'star_rating': Rating[i].text if i < len(Rating) else 'N/A',
                    'price': Price[i].text,
                    'seats_available': Seats[i].text.split()[0]
                })

            return bus_data
        except Exception as e:
            print(f"Error clicking 'View Buses' button on {link_url}: {e}")
            return []

    # scrape along pages
    def scrape_pages(driver):
        all_bus_details = []
        for page_num in range(1, 3):
            try:
                open_web(driver, url)
                if page_num > 1:
                    page_button = driver.find_element(By.XPATH,
                                                      f"//div[contains(@class, 'DC_117_pageTabs')][text()='{page_num}']")
                    driver.execute_script("arguments[0].click();", page_button)
                    time.sleep(5)

                bus_links, bus_routes = bus_route_url(driver)
                # Iterate over each bus route
                for link_url, link_text in zip(bus_routes, bus_links):
                    bus_data1 = bus_details(driver, link_text, link_url)
                    all_bus_details.extend(bus_data1)

            except Exception as e:
                print(f"Error occurred while accessing page {page_num}: {str(e)}")

        return all_bus_details

    open_web(driver, url)
    all_bus_details = scrape_pages(driver)
    bus_data_all = pd.DataFrame(all_bus_details)

    driver.quit()
    return bus_data_all


bus_df = scrape_bus_data(url)
bus_df.to_csv('punjab.csv', index=False)
