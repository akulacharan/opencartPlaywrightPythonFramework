
import time

import pytest
import os

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from playwright.sync_api import expect
from utilities.data_reader_util import read_json_data, read_csv_data, read_excel_data



#Load/read the data from the test data files

from pathlib import Path

# Automatically finds your 'testdata' folder relative to this script
csv = os.path.abspath("C:\\Users\\charanteja\\PycharmProjects\\opencartPlaywrightPythonFramework\\testdata\\logindata.csv")
csv_data=read_csv_data(csv)
json = os.path.abspath("C:\\Users\\charanteja\\PycharmProjects\\opencartPlaywrightPythonFramework\\testdata\\logindata.json")
json_data=read_json_data(json)
excel = os.path.abspath("C:\\Users\\charanteja\\PycharmProjects\\opencartPlaywrightPythonFramework\\testdata\\logindata.xlsx")
excel_data=read_excel_data(excel)
print(excel_data)

#@pytest.mark.datadriven
@pytest.mark.parametrize("testName,email,password,expected",csv_data)
def test_login_data_driven(page,testName,email,password,expected):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page=MyAccountPage(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.login(email,password)
    time.sleep(3)

    if expected=="success":
        expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)
    else:
        expect(login_page.get_login_error()).to_be_visible(timeout=3000)
