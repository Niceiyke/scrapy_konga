# Scrapy settings for scrapy_konga project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy_konga"

SPIDER_MODULES = ["scrapy_konga.spiders"]
NEWSPIDER_MODULE = "scrapy_konga.spiders"

#Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
)

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Splash Server Endpoint
SPLASH_URL = "http://3.142.211.239:8050/"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # "jumia.middlewares.JumiaDownloaderMiddleware": 543,
    "scrapeops_scrapy.middleware.retry.RetryMiddleware": 550,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
    "scrapy_splash.SplashCookiesMiddleware": 723,
    "scrapy_splash.SplashMiddleware": 725,
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    "scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
    # "jumia.middlewares.JumiaSpiderMiddleware": 543,
}

# Define the Splash DupeFilter
DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"

HTTPCACHE_STORAGE = "scrapy_splash.SplashAwareFSCacheStorage"


# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "scrapy_konga.pipelines.Remove_Duplicate_item_Pipeline": 200,
    "scrapy_konga.pipelines.SavingToDbpostgres": 250,
}

SCRAPEOPS_API_KEY = "c0f1d288-cbe4-464c-9e22-59881bd08841"

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    #    "scrapy.extensions.telnet.TelnetConsole": None,
    'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500,
}


# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
