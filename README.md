# Банкетам.Нет

Информационная система для бронирования помещений под банкеты: зал, ресторан, летняя и закрытая веранда.

## Требования

- Python 3.10+
- Django 4.2+

## Установка и запуск локально

```powershell
cd "C:\Users\user\Desktop\Aysheev_Kostya"
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

Сайт: http://127.0.0.1:8000/

Остановка сервера: `Ctrl+C` или `Ctrl+Break`.

### Администратор (необязательно)

```powershell
py manage.py createsuperuser
```

Админка: http://127.0.0.1:8000/admin/

## Страницы

| URL | Описание |
|-----|----------|
| `/` | Редирект на вход |
| `/login/` | Вход |
| `/register/` | Регистрация |
| `/cabinet/` | Личный кабинет (только для авторизованных) |
| `/admin/` | Панель администратора |

## Структура проекта

```
├── manage.py              — главный исполняемый файл Django
├── requirements.txt       — зависимости
├── db.sqlite3             — база данных (создаётся после migrate)
├── banquetam/             — настройки проекта
├── accounts/              — регистрация, вход, кабинет
├── templates/             — HTML-шаблоны
└── static/                — CSS, JS, изображения слайдера
```

## База данных

СУБД: **SQLite**, файл `db.sqlite3`.

### Сущность User (`accounts_user`)

Кастомная модель пользователя на базе `AbstractUser`.

| Поле | Описание |
|------|----------|
| `id` | Первичный ключ |
| `username` | Логин (уникальный, латиница и цифры, от 6 символов) |
| `password` | Хэш пароля |
| `full_name` | ФИО |
| `phone` | Контактный телефон |
| `email` | E-mail |
| `is_active` | Активность учётной записи |
| `is_staff` | Доступ к админке |
| `is_superuser` | Права суперпользователя |
| `date_joined` | Дата регистрации |
| `last_login` | Последний вход |

### Служебные таблицы Django

- `django_session` — сессии
- `django_admin_log` — журнал админки
- `django_content_type` — типы моделей
- `auth_group`, `auth_permission` — группы и права
- `accounts_user_groups`, `accounts_user_user_permissions` — связи пользователя

### Дамп данных

Экспорт пользователей:

```powershell
py manage.py dumpdata accounts.User --indent 2 > dump_users.json
```

Полный дамп:

```powershell
py manage.py dumpdata --indent 2 > dump_all.json
```

## Клонирование с GitHub

```powershell
git clone https://github.com/asukiri232/demo.git
cd demo
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

`db.sqlite3` не хранится в репозитории — после клонирования выполните `migrate` и зарегистрируйте пользователей.

## Основные команды

| Команда | Назначение |
|---------|------------|
| `py manage.py runserver` | Запуск сервера |
| `py manage.py migrate` | Применить миграции |
| `py manage.py makemigrations` | Создать миграции |
| `py manage.py createsuperuser` | Создать администратора |
| `py manage.py dumpdata` | Экспорт данных из БД |
