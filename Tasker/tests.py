from django.test import TestCase
from datetime import date, datetime
from time import sleep
import os
import unittest
import pathlib

from selenium import webdriver

# Create your tests here.

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

# Create a task

class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("templates/Tasker/index.html"))
        self.assertEqual(driver.title, "")

    def test_archive(self):
        driver.get(file_uri("templates/Tasker/index.html"))
        task = driver.find_element_by_class_name("checkmark")
        task.click()
        self.assertTrue(task.is_selected, True)

    def test_archive_site(self):
        driver.get(file_uri("templates/Tasker/archive.html"))
        archive = driver.find_element_by_name("delete_task")
        archive.click()
        self.assertTrue(archive.is_selected, True)

if __name__ == "__main__":
    unittest.main()

