# Test-task-service-insurance

Тестовое задание - REST API сервис для расчета стоимости страхования грузов.

# Технологии
- FastAPI
- Tortoise ORM
- Postgresql
- Docker

Тариф загружается из файла tariff.json.
-Cодержимое файла: 
```{
    "2020-06-01": [
        {
            "cargo_type": "Glass",
            "rate": "0.04"
        },
        {
            "cargo_type": "Other",
            "rate": "0.01"
        }
    ],
    "2020-07-01": [
        {
            "cargo_type": "Glass",
            "rate": "0.04"
        },
        {
            "cargo_type": "Other",
            "rate": "0.015"
        }
    ]
}
```
# Инструкция

Для того чтобы запустить проект нужно клонировать репозиторий на ваш локальный компьютер. Используя команду:
```git clone https://github.com/Maratq/Test-task-service-insurance.git```

Для локального тестирования необходимо создать виртуальное окружение командой bash ```python3 -m venv venv``` и активировать его. Команда ```venv\Scripts\activate.bat``` - для Windows; ```source venv/bin/activate``` - для Linux и MacOS.

Затем необходимо перейти в папку с нужным уроком и установить зависимости командой ```pip install -r requirements.txt```

Затем необходимо перейти в папку ```src``` командой ```cd src``` и запустить команду ```uvicorn main:app --reload``` для запуска сервера uvicorn.

После этого можно зайти в браузере по адресу ```http://localhost:8000/docs``` для просмотра доступных эндпоинтов.
