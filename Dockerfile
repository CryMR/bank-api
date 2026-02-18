# 1. Используем официальный стабильный образ Python (slim-версия весит в разы меньше)
FROM python:3.11-slim

# 2. Устанавливаем системные зависимости для psycopg2 (нужны для сборки драйвера БД)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 3. Устанавливаем рабочую директорию
WORKDIR /app

# 4. Сначала копируем только файл с зависимостями (это ускоряет пересборку благодаря кэшу)
# Создай файл requirements.txt, если его еще нет
COPY requirements.txt .

# 5. Устанавливаем Python-библиотеки
RUN pip install --no-cache-dir -r requirements.txt

# 6. Копируем весь остальной код проекта в контейнер
COPY . .

# 7. Открываем порт 8000 (стандарт для FastAPI)
EXPOSE 8000

# 8. Запускаем приложение через uvicorn
# В продакшене лучше использовать uvicorn напрямую вместо fastapi dev
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]