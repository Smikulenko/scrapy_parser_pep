import csv
from collections import Counter
from datetime import datetime as dt
from pep_parse.constants import FILE_NAME, DT_FORMAT, RESULT_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = Counter()

    def process_item(self, item, spider):
        self.counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        time = dt.now().strftime(DT_FORMAT)
        file_path = RESULT_DIR / FILE_NAME.format(time)
        with open(file_path, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(['Cтатус', 'Количество'])
            for key, value in self.counter.items():
                writer.writerow([key, value])
            writer.writerow(['Total', sum(self.counter.values())])
