# flask_api
Test scripts for learn FLASK

Инструкция к API

Установить необходимые зависимости:
pip install -r requirements.txt (или прописать свой путь к файлу)

Проверить соединение с БД и создать необходимые таблицы:

1) Прописать необходимые параметры соединения с таблицей в файле app_config.py
2) Из файла created_db запустить функцию create_tables().
   !!!Функция предварительно запускается в основном файле. В таком случае - не забудьте закоментировать запуск функции после повторных запусков

Создать пользователей:
В POSTMAN или подобном приложении симмитировать POST - запрос с параметрами:
    1) URL - http://<основной_адрес_API>/newuser
    2) тело запроса: 
        {
                "firstname": "<имя_пользователя>",
                "lastname": "<фамилия_пользователя>",
                "age": <возраст_пользователя>,
                "email": "<п/я_пользователя>"
        }

Добавить пост:
В POSTMAN или подобном приложении симмитировать POST - запрос с параметрами:
    1) URL - http://<основной_адрес_API>/add_post
    2) тело запроса: 
        {
                "author": "<имя_пользователя>",
                "description": "<содержимое_поста>",
                "rating": <рейтинг поста>,
                "added": <время_создания(не обязательно)>,
                "updated": <время_обновления(не обязательно)>
        }
    
Обновить пост:
В POSTMAN или подобном приложении симмитировать PUT - запрос с параметрами:
    1) URL - http://<основной_адрес_API>/add_post
    2) тело запроса: 
        {
                "id": <id_поста>,
                "description": "<обновленное_содержимое_поста>",
                "rating": <рейтинг_поста>
        }

Удалить пост:
В POSTMAN или подобном приложении симмитировать DELETE - запрос с параметрами:
    1) URL - http://<основной_адрес_API>/del_post
    2) тело запроса: 
        {
                "id": <id_поста>
        }

Получить пост(-ы):
В POSTMAN или подобном приложении симмитировать GET - запрос с параметрами:
    1) URL - http://<основной_адрес_API>/posts?post_id=<id_поста>&author=<имя_пользователя>