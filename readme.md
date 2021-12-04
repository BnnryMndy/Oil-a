<h4>Основной стек технологий:</h4>
<ul>
    <li>Python</li> 
    <li>JavaScript</li>
    <li>PostgreSQL</li>
    <li>Pipeline U-Net / DeepLabV3</li>
    <li>Django</li> 
</ul>

<h4>функционал:</h4>
<ul>
    <li>формирование отчета по аварии в формате PDF</li>
    <li>модуль загрузки данных со спутниковых снимков `load_data.ipynb`</li>
</ul>


СРЕДА ЗАПУСКА
------------
1) требуется установленный django;
3) требуется установленная СУБД postreSQL (версия 13.4 или новее);

УСТАНОВКА
------------
1) скачать репозиторий любым удобным способом
2) поместить папку проекта в корень сайта
3) создать пустую базу данных, а подключение к базе прописать в конфигурационный файл сервиса по адресу: /oila/oila/settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'oila_db',
        'USER' : 'postgres',
        'PASSWORD' : 'postgres',
        'HOST' : '127.0.0.1',
        'PORT' : '5432',
    }
}
```
4) выполнить миграции, запустив в корне проекта
```
python manage.py migrate
```

5) запустить веб-сервер командой
```
python manage.py runserver
```
 



<h4>Разработчики</h4>

<P>Кристина Жаткина https://t.me/kriszhatkina</P>
<P>Янина Смирнова https://t.me/YaninaSmirnova</P>
<P>Коновалова Настасья https://t.me/NastasyaK</P>
<P>Евгений Ершов https://t.me/evgforte</P>
<P>Лазарев Антон https://t.me/Anton_web_Lazarev</P>
