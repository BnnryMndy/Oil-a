<h4>Реализованная функциональность</h4>
<ul>
    <li></li>
    <li></li>
    <li></li>
</ul> 
<h4>Особенность проекта в следующем:</h4>
<ul>
 <li></li>
 <li></li>
 </ul>
<h4>Основной стек технологий:</h4>
<ul>
    <li></li>
	<li></li>
	<li></li>
	<li></li>
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

<P>Кристина Жаткина teamlead https://t.me/kriszhatkina</P>
<P>Янина Смирнова analyst https://t.me/YaninaSmirnova</P>
<P>Коновалова Настасья designer  https://t.me/NastasyaK</P>
<P>Евгений Ершов frontend https://t.me/evgforte</P>
<P>Лазарев Антон backend https://t.me/Anton_web_Lazarev</P>
