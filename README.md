# Асинхронный парсер PEP

## Описание проекта:
Пресер  документов PEP создан на базе фреймворка Scrapy.
Парсер, собирает информацию с сайта https://www.python.org/ и выводить собранную информацию в два файла.

##Функций парсера
Парсер получает список PEP, их статусы и ведет подсчет каждого статуса PEP и общее количество полученных документов.

## Результаты
Результаты работы создаються два файла в csv формате в директорию results.
файлы именованы по маске pep_ДатаВремя.csv и status_summary_ДатаВремя.csv:

### pep.csv
Файл pep.csv содержит список  существующих PEP.
В файле три столбца: 
- Номер (number)
- Название (name)
- Статус (status)
### status_summary.csv
содержит сводку по статусам PEP — сколько найдено документов в каждом статусе. И общее количество PEP.
В файле два столбца:
- Статус
- Количество

## Технологии:
- Python
- Scrapy

## Запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Запустить парсер.
```
scrapy crawl pep
```

**Автор**
*Микуленко Софья*
