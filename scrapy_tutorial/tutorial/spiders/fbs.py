# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


class FbsSpider(scrapy.Spider):
    name = "fbs"
    allowed_domains = ["facebook.com"]
    start_urls = (
        'http://www.facebook.com/',
    )

    def parse(self, response):
        pass
