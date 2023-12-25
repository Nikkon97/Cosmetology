# Cosmetology
Дипломный проект "Сайт косметолога". На данный момент реализован просмотр доступных услуг и регистрация на сайте.

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)

## Технологии
- [PostgreSQL](https://www.postgresql.org/)
- [Django](https://www.djangoproject.com/))

## Использование
1. Настроить виртуальное окружение и установить все необходимые зависимости с помощью команд: 

  Команда для Windows: 
```sh
python -m venv venv 
venv\Scripts\activate 
pip install -r requirement.txt
```
  Команда для Unix: 
  ```sh
python3 -m venv venv 
source venv/bin/activate 
pip install -r requirement.txt
```

2. Создать БД:
```python
sudo -u postgres psql
CREATE DATABASE cosmetology; 
```
3. Применить миграции:
```python
 python manage.py makemigrations 
 python manage.py migrate 
```
4. Для работы с переменными окружениями необходимо заполнить файл .env на основе .env.sample

5. Для создания администратора (createsuperuser) заполните поля email, PASSWORD. 
  Команда для Windows:
 ```
  python manage.py csu
```
Команда для Unix:
 ```
  python3 manage.py csu
```
6. Запуск приложения:
Команда для Windows:
 ```
python manage.py runserver
```
 Команда для Unix:
 ```
python3 manage.py runserver
```








