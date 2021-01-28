from django.test import TestCase
from datetime import date, datetime
from time import sleep
import os
import unittest
import pathlib

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create your tests here.

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome(ChromeDriverManager().install())

# Create a Testss

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

