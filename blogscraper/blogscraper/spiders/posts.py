import scrapy


class PostsSpider(scrapy.Spider):
    name = 'postsspider'

    start_urls = ['https://www.zyte.com/blog']


    def start_request(self):
        for url in start_urls:
            yield scrapy.Request(url = url, callback = self.parse)
    
    def parse(self, response):
        titles = response.xpath('//*/a[@class="oxy-post-title"]/text()').getall()
        authors = response.xpath('//*/div[@class="oxy-post-meta"]/div[1]/text()').getall()
        permalinks = response.xpath('//*/a[@class="oxy-read-more"]/@href').getall()
        dates = response.xpath('//*/div[@class="oxy-post-image-date-overlay"]/text()').getall()
        images = response.xpath('//*/div[@class="oxy-post-image-fixed-ratio"]/@style').getall()

        for i in range(len(titles)):
            yield {
                'title': titles[i],
                'author': authors[i],
                'permalink': permalinks[i],
                'published_date': dates[i],
                'image': images[i]
            }