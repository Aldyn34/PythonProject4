# Парсер КиноПоиск для фильмов с рейтингами 2010-2015 годов

## Постановка задачи
Цель проекта — создание парсера, который извлекает информацию о фильмах с наивысшими рейтингами на КиноПоиск в период с 2010 по 2015 годы. Парсер должен собирать информацию о названии фильма, рейтинге и годе, а затем экспортировать эти данные в форматы CSV или JSON.

## Инструкция по сборке и запуску

1. Установите необходимые зависимости:
    ```bash
    pip install requests beautifulsoup4
    ```

2. Скачайте проект и добавьте необходимые файлы в ваш проект.

3. Запустите парсер:
    ```python
    parser = KinoPoiskParser()
    parser.fetch_movies()  # Получить фильмы за 2010-2015 годы
    parser.export_to_csv('movies_2010_2015.csv')  # Экспорт в CSV
    parser.export_to_json('movies_2010_2015.json')  # Экспорт в JSON
    ```

## Пример результатов работы парсера

После выполнения парсера, вы получите файлы `movies_2010_2015.csv` или `movies_2010_2015.json` с данными:

**Пример CSV:**

```csv
title,rating,year
"Интерстеллар",8.6,2014
"Начало",8.8,2010
"Темный рыцарь",9.0,2008
