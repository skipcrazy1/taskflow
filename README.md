# TaskFlow — Kanban доска для управления задачами

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-4.x-green)
![DRF](https://img.shields.io/badge/DRF-3.x-red)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)

TaskFlow — это веб-приложение для организации командной работы по методологии Kanban. Проект разработан в учебных целях для демонстрации навыков бэкенд-разработки на Django и Django REST Framework.

## ✨ Функциональность

- ✅ Создание проектов (канбан-досок)
- ✅ Управление задачами (создание, редактирование, удаление)
- ✅ Назначение исполнителей и приоритетов задач
- ✅ Комментарии к задачам
- ✅ Профили пользователей с дополнительной информацией
- ✅ Полноценная админ-панель Django
- ✅ REST API для всех моделей

## 🛠 Технологический стек

| Категория | Технологии |
|-----------|------------|
| **Язык** | Python 3.11 |
| **Фреймворки** | Django 4.x, Django REST Framework |
| **Базы данных** | PostgreSQL, Redis |
| **Инфраструктура** | Docker, Docker Compose, Nginx |
| **Фоновые задачи** | Celery, Celery Beat |
| **Тестирование** | Pytest |
| **Документация** | Swagger (drf-yasg) |

## 📁 Структура проекта
taskflow/
├── backend/ # Django приложение
│ ├── apps/ # Все приложения
│ │ ├── accounts/ # Профили пользователей
│ │ │ ├── models.py # Модель Profile
│ │ │ ├── serializers.py # ProfileSerializer
│ │ │ ├── views.py # ProfileViewSet
│ │ │ └── urls.py # Маршруты для профилей
│ │ ├── projects/ # Управление проектами
│ │ │ ├── models.py # Модель Project
│ │ │ ├── serializers.py # ProjectSerializer
│ │ │ ├── views.py # ProjectViewSet
│ │ │ └── urls.py # Маршруты для проектов
│ │ └── tasks/ # Задачи и комментарии
│ │ ├── models.py # Модели Task и Comment
│ │ ├── serializers.py # TaskSerializer, CommentSerializer
│ │ ├── views.py # TaskViewSet, CommentViewSet
│ │ └── urls.py # Маршруты для задач
│ ├── config/ # Настройки Django
│ │ ├── settings.py # Основные настройки
│ │ ├── urls.py # Главные маршруты
│ │ └── wsgi.py
│ ├── manage.py
│ └── requirements.txt # Зависимости
├── docker-compose.yml # Оркестрация контейнеров
├── .env.example # Пример переменных окружения
└── README.md # Документация

## 🚀 Быстрый старт

### Предварительные требования

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Git

### Установка и запуск

1. **Клонировать репозиторий**
   ```bash
   git clone https://github.com/skipcrazy1/taskflow.git
   cd taskflow
   ```
Создать файл с переменными окружения

cp .env.example .env
При необходимости отредактируйте .env.

Запустить контейнеры

docker-compose up -d --build
Применить миграции

docker-compose exec web python manage.py migrate
Создать суперпользователя для админки

docker-compose exec web python manage.py createsuperuser
Открыть в браузере

Админка: http://localhost:8000/admin

API проектов: http://localhost:8000/api/projects/

API задач: http://localhost:8000/api/tasks/

API профилей: http://localhost:8000/api/profiles/

📋 API Endpoints
Проекты
Метод	URL	Описание
GET	/api/projects/	Список всех проектов
POST	/api/projects/	Создать новый проект
GET	/api/projects/{id}/	Получить проект по ID
PUT	/api/projects/{id}/	Полностью обновить проект
PATCH	/api/projects/{id}/	Частично обновить проект
DELETE	/api/projects/{id}/	Удалить проект

Задачи
Метод	URL	Описание
GET	/api/tasks/	Список всех задач
POST	/api/tasks/	Создать новую задачу
GET	/api/tasks/{id}/	Получить задачу по ID
PUT	/api/tasks/{id}/	Обновить задачу
DELETE	/api/tasks/{id}/	Удалить задачу

Комментарии
Метод	URL	Описание
GET	/api/comments/	Список всех комментариев
POST	/api/comments/	Добавить комментарий к задаче
GET	/api/comments/{id}/	Получить комментарий
DELETE	/api/comments/{id}/	Удалить комментарий
Профили
Метод	URL	Описание
GET	/api/profiles/	Список всех профилей
GET	/api/profiles/{id}/	Получить профиль пользователя

##🧪 Примеры запросов
Создание проекта
curl -X POST http://localhost:8000/api/projects/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Мой первый проект", "description": "Описание проекта"}'

Создание задачи
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{
    "headline": "Сделать задачу",
    "description": "Нужно реализовать функционал",
    "status": "TODO",
    "priority": "HIGH",
    "project": 1
  }'

Добавление комментария
curl -X POST http://localhost:8000/api/comments/ \
  -H "Content-Type: application/json" \
  -d '{
    "task": 1,
    "text": "Новый комментарий к задаче"
  }'


##🔮 Планы по развитию
JWT-аутентификация

Система прав доступа (участники проектов)

Асинхронные уведомления через Celery

Загрузка файлов к задачам

WebSocket для real-time обновлений

##👨‍💻 Автор
Мурад Галиев

GitHub: @skipcrazy1
Telegram: @columbiuss