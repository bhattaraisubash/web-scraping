# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BlogscraperPipeline:
    def process_item(self, item, spider):
        for key, value in item.items():
            if not value:
                item[key] = ''
                continue
            if key == 'image':
                url = value.split(';')[0].split(':')[1].replace('url(', '').replace(')', '')
                item[key] =  url.strip()
            else:
                item[key] = value.strip()

        return item
