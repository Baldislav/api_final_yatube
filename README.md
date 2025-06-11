Описание. API-сервис Yatube предоставляет функциональность социальной сети: создание и просмотр постов, подписки на пользователей, комментирование записей, а также получение персонализированной ленты.

Установка. Как развернуть проект на локальной машине

git clone git@github.com:baldislav/api_final_yatube.git
1. cd api_final_yatube
2. python -m venv venv
3. . venv/Scripts/activate
4. pip install -r requirements.txt
5. cd yatube_api
6. python manage.py makemigrations python manage.py runserver
7. python manage.py migrate
8. python manage.py makemigrations
9. python manage.py runserver

Примеры. Некоторые примеры запросов к API.

Получение списка групп пользователей
GET api/v1/groups
[
    {
        "id": 1,
        "title": "TestGroup",
        "slug": "test-group",
        "description": "Some text."
    }
]

Получение токена
POST api/v1/jwt/create
{
    "username": "regular_user",
    "password": "iWannaBeAdmin"
}

Обновление поста
PUT api/v1/posts/76/
{
    "text": "Обновленный текст через PUT-запрос",
    "group": null
}