# url_reducer

## Перед началом работы

### Создание виртуального окружения

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Установка пакетов

```bash
pip install -r requirements.txt
```

## Настройка сервиса для локальной разработки

1. Необходимо создать конфигурационный файл `.env` в корневой директории
2. Перенести переменные конфигурации из файла [`.env.copy`](.env.copy) в файл `.env`
3. Задать переменные конфигурации

## Описание переменных конфигурации
### Service
- **SERVICE_HOST**: Адрес сервиса
- **SERVICE_PORT**: Порт на котором работает сервис
- **SERVICE_ORIGINS**: Список разрешенных источников запросов (CORS)
- **SERVICE_MAX_WORKERS_COUNT**: Максимальное количество рабочих процессов сервиса
- **SERVICE_ENV**: Окружение сервиса ("DEV" или "PRODUCTION")
### Postgresql
- **DB_HOST**: Адрес сервера базы данных
- **DB_PORT**: Порт сервера базы данных
- **DB_USERNAME**: Имя пользователя для подключения к базе данных
- **DB_PASSWORD**: Пароль для подключения к базе данных
- **DB_NAME**: Наименование базы данных

## Установка миграций
- **alembic upgrade head**: Запускать из под виртуального окружения