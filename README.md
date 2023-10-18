![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=yellow)
![Django](https://img.shields.io/badge/Django-2.2.6-red?style=for-the-badge&logo=django&logoColor=blue)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![SQLite](https://img.shields.io/badge/SQLite-grey?style=for-the-badge&logo=postgresql&logoColor=yellow)
 
## Описание 
 
YaMDb - это проект, на котором люди могут оставлять отзывы о книгах, фильмах, музыке и других произведениях. Произведения разделены на категории и им можно присвоить жанр. Администраторы могут добавлять новые произведения, категории и жанры. Пользователи могут оставлять свои отзывы и ставить оценки произведениям и комментировать отзывы других пользователей.

 
### Доступный функционал 
 
- Для аутентификации используются JWT-токены. 
- У не аутентифицированных пользователей доступ к API только на уровне чтения. 
- Создание объектов разрешено только аутентифицированным пользователям. На прочий функционал наложено ограничение в виде 
  административных ролей и авторства. 
- Управление пользователями. 
- Получение списка всех категорий и жанров, добавление и удаление. 
- Получение списка всех произведений, их добавление. Получение, обновление и удаление конкретного произведения. 
- Получение списка всех отзывов, их добавление. Получение, обновление и удаление конкретного отзыва. 
- Получение списка всех комментариев, их добавление. Получение, обновление и удаление конкретного комментария. 
- Возможность получения подробной информации о себе и удаления своего аккаунта. 
- Фильтрация по полям. 
 
#### Документация к API доступна по адресу [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) после запуска сервера с проектом 

 
#### Запуск проекта в dev-режиме 
 
- Склонируйте репозиторий:   
  ```git clone git@github.com:EdmondKoko/yamdb_final.git``` 
- Установите зависимости из файла requirements.txt:    
  ```pip install -r requirements.txt``` 
- Перейдите в папку api_yamdb/api_yamdb. 
- Примените миграции:    
  ```python manage.py migrate``` 
- Выполните команду:    
  ```python manage.py runserver``` 
 
#### Запуск приложения в контейнерах 
 
- из директории nginx/ 
  ```docker-compose up -d --build``` 
- Выполнить миграции: 
  ```docker-compose exec web python manage.py migrate``` 
- Создать суперпользователя: 
  ```docker-compose exec web python manage.py createsuperuser``` 
- Собрать статику: 
  ```docker-compose exec web python manage.py collectstatic --no-input``` 
- Остановить приложение в контейнерах: 
  ```docker-compose down -v``` 
- Запуск pytest: 
  ```docker-compose run web pytest``` 
- Шаблон наполнения env-файла: 
  - DB_ENGINE=<...> # указываем, что работаем с postgresql 
  - DB_NAME=<...> # имя базы данных 
  - POSTGRES_USER=<...> # логин для подключения к базе данных 
  - POSTGRES_PASSWORD=<...> # пароль для подключения к БД (установите свой) 
  - DB_HOST=<...> # название сервиса (контейнера) 
  - DB_PORT=<...> # порт для подключения к БД 
  - SECRET_KEY=<...> # ключ из settings.py 
- Скопировать файл базы данных в контейнер 
  ```docker cp fixtures.json <id>:app/``` 
- Заполнение базы данных 
  ```docker-compose exec web python manage.py loaddata fixtures.json``` 
 
#### Примеры некоторых запросов API 
 
Регистрация пользователя:   
  ``` POST /api/v1/auth/signup/ ```   
Получение данных своей учетной записи:   
  ``` GET /api/v1/users/me/ ```   
Добавление новой категории:   
  ``` POST /api/v1/categories/ ```   
Удаление жанра:   
  ``` DELETE /api/v1/genres/{slug} ```   
Частичное обновление информации о произведении:   
  ``` PATCH /api/v1/titles/{titles_id} ```   
Получение списка всех отзывов:   
  ``` GET /api/v1/titles/{title_id}/reviews/ ```    
Добавление комментария к отзыву:   
  ``` POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/ ``` 
 
#### Автор 
 
Трофимов Руслан - [https://github.com/EdmondKoko](https://github.com/EdmondKoko)
