import scrapy
from ..items import KongaItem
from scrapy.loader import ItemLoader
from scrapy_splash import SplashRequest

lua_script = """
function main(splash, args)
    assert(splash:go(args.url))

  while not splash:select('li.bbe45_3oExY._22339_3gQb9') do
    splash:wait(0.1)
    print('waiting...')
  end
  return {html=splash:html()}
end
"""


class kongaPhoneSpyder(scrapy.Spider):
    name = "kongaphone"
    page_num = 1

    custom_settings = {
        "BOT_NAME": "web crawler bot",
   
        # Crawl responsibly by identifying yourself (and your website) on the user-agent
        "USER_AGENT": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        ),
        # Obey robots.txt rules
        "ROBOTSTXT_OBEY": False,
        # Splash Server Endpoint
        "SPLASH_URL": "http://3.142.211.239:8050/",
        # Set settings whose default value is deprecated to a future-proof value
        "REQUEST_FINGERPRINTER_IMPLEMENTATION": "2.7",
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "FEED_EXPORT_ENCODING ": "utf-8",
        # Enable or disable downloader middlewares
        # See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
        "DOWNLOADER_MIDDLEWARES": {
            # "jumia.middlewares.JumiaDownloaderMiddleware": 543,
            "scrapeops_scrapy.middleware.retry.RetryMiddleware": 550,
            "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
            "scrapy_splash.SplashCookiesMiddleware": 723,
            "scrapy_splash.SplashMiddleware": 725,
            "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
        },
        # Enable or disable spider middlewares
        # See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
        "SPIDER_MIDDLEWARES": {
            "scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
            # "jumia.middlewares.JumiaSpiderMiddleware": 543,
        },
        # Define the Splash DupeFilter
        "DUPEFILTER_CLASS ": "scrapy_splash.SplashAwareDupeFilter",
        "HTTPCACHE_STORAGE ": "scrapy_splash.SplashAwareFSCacheStorage",
        # Configure item pipelines
        # See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
        "ITEM_PIPELINES ": {
             #"scrapy_jumia.pipelines.Remove_Items_withNoDiscount_Pipeline": 100,
             #"scrapy_jumia.pipelines.Remove_Items_NotinStock_Pipeline": 150,
            "scrapy_jumia.pipelines.Remove_Duplicate_item_Pipeline": 200,
             "scrapy_jumia.pipelines.SavingToDbpostgres": 250,
        },
        "SCRAPEOPS_API_KEY": "c0f1d288-cbe4-464c-9e22-59881bd08841",
        # Enable or disable extensions
        # See https://docs.scrapy.org/en/latest/topics/extensions.html
        "EXTENSIONS ": {
            #    "scrapy.extensions.telnet.TelnetConsole": None,
            #'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500,
        },
    }

    def start_requests(self):
        url = "https://www.konga.com/category/phones-tablets-5294?konga_fulfilment_type=CWK"
        yield SplashRequest(
            url,
            callback=self.parse,
            endpoint="execute",
            args={
                "wait": 5,
                "lua_source": lua_script,
                url: "https://www.konga.com/category/phones-tablets-5294?konga_fulfilment_type=CWK",
            },
        )

    def parse(self, response):
        products = response.css("li.bbe45_3oExY._22339_3gQb9")

        for product in products:
            l = ItemLoader(item=KongaItem(), selector=product)
            l.add_css("url", " div._4941f_1HCZm ::attr(href)")
            l.add_css("name", "div.af885_1iPzH ::text"),
            l.add_css("discount_price", "span.d7c0f_sJAqi"),
            l.add_css("original_price", "span.f6eb3_1MyTu"),
            l.add_css("discount_percent", "span._4472a_zYlL-._6c244_q2qap ::text"),
            l.add_css("image", "div._7e903_3FsI6 ::attr(data-src)"),
            l.add_value("category", "smartphones"),
            l.add_value("store", "Konga"),
            l.add_value("stock", "Add To Cart"),
            

            yield l.load_item()

        self.page_num += 1

        next_page = response.css("a._08932_1bhTj._4c4d8_1SOeS")
        if next_page is not None:
            url = f"https://www.konga.com/category/phones-tablets-5294?konga_fulfilment_type=CWK&page={self.page_num}"
            yield SplashRequest(
                url,
                callback=self.parse,
                endpoint="execute",
                args={"wait": 5, "lua_source": lua_script, "url": url},
            )


