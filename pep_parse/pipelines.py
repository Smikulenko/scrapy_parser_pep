# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from collections import Counter
from datetime import datetime as dt


from pathlib import Path

FILE_NAME = 'status_summary_{}.csv'
DT_FORMAT = '%Y-%m-%d_%H-%M-%S'
BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = Counter()
        
    def process_item(self, item, spider):
        self.counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        time = dt.now().strftime(DT_FORMAT)
        result_dir = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)
        file_path = result_dir / FILE_NAME.format(time)
        self.counter['Total'] = sum(self.counter.values())
        with open(file_path, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(['Cтатус', 'Количество'])
            writer.writerow(self.counter.items())
