# Blackcoffer Project

## Step 1 - Select the Python Environment
Activate the appropriate Python environment for this project.

## Step 2 - Clone the Project
Clone the project from GitHub using the following command:

```bash
git clone https://github.com/ParitKansal/blackcoffer
```

## Step 3 - Install the Required Python Modules
Navigate to the project directory and install the required Python modules:

```bash
pip install -r requirements.txt
```

## Step 4 - Update `settings.py`
Ensure that the `settings.py` file is correctly configured:

1. **For `ScrapeOpsFakeBrowserHeaderAgentMiddleware`:**

   - Add or update the following settings:
     ```python
     SCRAPEOPS_API_KEY = 'your_scrapeops_api_key_here'
     SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT = "https://headers.scrapeops.io/v1/browser-headers"
     SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True
     SCRAPEOPS_NUM_RESULTS = 50
     ```
   - If the middleware is not required, comment out or remove the following line from the `DOWNLOADER_MIDDLEWARES` list:
     ```python
     'Scraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware': 700,
     ```

2. **For `MyProxyMiddleware`:**

   - Add or update the following settings:
     ```python
     PROXY_USER = 'your_proxy_user_here'
     PROXY_PASSWORD = 'your_proxy_password_here'
     PROXY_ENDPOINT = 'your_proxy_endpoint_here'
     PROXY_PORT = 'your_proxy_port_here'
     ```
   - If the middleware is not required, comment out or remove the following lines from the `DOWNLOADER_MIDDLEWARES` list:
     ```python
     'Scraper.middlewares.MyProxyMiddleware': 610,
     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 650,
     ```

---

## Step 5 - Run the Project
After the necessary modules are installed, you can run the Python Scrapy Spider as follows:

Run the specific spider (i.e., `websiteSpider`):

    ```bash
    scrapy crawl websiteSpider
    ```

---
