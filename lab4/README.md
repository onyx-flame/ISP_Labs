# Lab4

Docker-образ: https://hub.docker.com/repository/docker/onyx11/flask_site

Запуск:
```
docker-compose pull
docker-compose up
```
С помощью `pull` тянем с докерхаба образы, связанные с сервисом: `mysql` и `flask_site`

После этого прописываем команду `up`, запуская сервисы.

После запуска сайт станет доступным по этой ссылке: http://localhost:5000/

Остановить сайт:
```
docker-compose down    (без удаления БД)
docker-compose down -v (с удалением БД)
```
