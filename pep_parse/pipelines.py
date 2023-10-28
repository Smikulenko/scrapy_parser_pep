import csv
from collections import Counter
from datetime import datetime as dt

from pathlib import Path

FILE_NAME = 'status_summary_{}.csv'
DT_FORMAT = '%Y-%m-%d_%H-%M-%S'
BASE_DIR = Path(__file__).parent.parent
RESULT = 'results'


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = Counter()

    def process_item(self, item, spider):
        self.counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        time = dt.now().strftime(DT_FORMAT)
        file_path = BASE_DIR / RESULT / FILE_NAME.format(time)
        with open(file_path, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(['Cтатус', 'Количество'])
            for key, value in self.counter.items():
                writer.writerow([key, value])
            writer.writerow(['Total', sum(self.counter.values())])
