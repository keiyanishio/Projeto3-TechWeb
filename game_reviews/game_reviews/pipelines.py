# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GameReviewsPipeline:
    def process_item(self, item, spider):
        item["nota"] = item["nota"].replace("\n","")
        item["nota"] = item["nota"].replace("\t","")
        item["titulo"] = item["titulo"].replace("\u00e9", "e")
        item["publisher"] = item["publisher"].replace("\n","")
        item["publisher"] = item["publisher"].replace("\t", "")
        item["desenvolvedora"] = item["desenvolvedora"].replace("\n","")
        item["desenvolvedora"] = item["desenvolvedora"].replace("\t", "")
        return item
