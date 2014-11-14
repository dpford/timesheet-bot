import os
from selenium import webdriver
import datetime

driver = webdriver.PhantomJS()

UNANET_URL = os.environ.get('UNANET_URL')
UNANET_USERNAME = os.environ.get('UNANET_USERNAME')
UNANET_PASSWORD = os.environ.get('UNANET_PASSWORD')
UNANET_PROJECT = os.environ.get('UNANET_PROJECT')
UNANET_TASK = os.environ.get('UNANET_TASK')
UNANET_HOURS = os.environ.get('UNANET_HOURS')

# Login
driver.get(UNANET_URL)
elem = driver.find_element_by_name('username')
elem.send_keys(UNANET_USERNAME)
passw = driver.find_element_by_name('password')
passw.send_keys(UNANET_PASSWORD)
login = driver.find_element_by_xpath('//button[@title="Ok"]')
login.click()

# Edit the active timesheet
# TODO: Add case where there's no active timesheet
edit_link = driver.find_element_by_xpath(
    '//a[starts-with(@title, "Edit timesheet for")]')
edit_link.click()

# Checks to see if any hours were entered for the day
# If not, enter hours for your project and save
day = datetime.date.today().day - 1
position = driver.find_element_by_xpath(
    '//span[text()={}]/..'.format(str(day))).get_attribute('id').split('_')[1]
if driver.find_element_by_name('t__{}'.format(position)).get_attribute('value'):
    with open('timesheets.log', 'a+') as f:
        f.write('{}: You already entered hours for {} on {}!\n'.format(
            datetime.datetime.now(),
            UNANET_PROJECT,
            datetime.date.today() - datetime.timedelta(days=1)))
else:
    for row in driver.find_elements_by_xpath('//tr[@title="{}"]'.format(UNANET_PROJECT)):
        row_id = row.get_attribute('id')
        if driver.find_element_by_xpath('//tr[@id="{}"]/td[@class="task"]/select/option[@selected]'.format(row_id)).text != UNANET_TASK:
            continue
        cell = row.find_element_by_name('d_{}_{}'.format(row_id, position))
        cell.send_keys(UNANET_HOURS)
        driver.find_element_by_xpath('//button[@title="Save"]').click()
        with open('timesheets.log', 'a+') as f:
            f.write('{}: Added 8 hours to {} for {}\n'.format(
                datetime.datetime.now(),
                UNANET_PROJECT,
                datetime.date.today() - datetime.timedelta(days=1)))
