import scrapy
import pandas as pd
import os
from urllib.parse import urlparse, urlunparse
from Scraper.items import WebItem

class WebsiteSpider(scrapy.Spider):
    name = "websiteSpider"
    allowed_domains = ["insights.blackcoffer.com"]

    def start_requests(self):
        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the path to the Excel file
        file_path = os.path.join(current_dir, '..', '..', 'Input.xlsx')
        
        # Load the Excel file
        df = pd.read_excel(file_path, header=None)
        
        # Extract URLs from the second column (index 1)
        urls = df.iloc[:, 1].dropna().tolist()  # Drop NaN values and convert to list
        
        for url in urls:
            # Ensure URL has a scheme
            parsed_url = urlparse(url)
            if not parsed_url.scheme:
                url = 'http://' + url  # Default to http if scheme is missing
            
            # Ensure URL is absolute
            if not parsed_url.netloc:
                url = urlunparse(('http', url, '', '', '', ''))
            
            yield scrapy.Request(url=url, callback=self.parse)

    custom_settings = {
        'FEEDS': {
            'output.csv': {'format': 'csv', 'overwrite': True},
        }
    }

    def parse(self, response):
        web_item = WebItem()
        web_item['url'] = response.url
        
        title = response.css('.entry-title::text').get().lower()
        content = " ".join(response.css('div.td-post-content.tagdiv-type ::text').getall())
        web_item['content'] = f"{title} {content}"
        
        yield web_item
