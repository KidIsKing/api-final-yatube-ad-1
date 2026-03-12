# api_final

**api final** - Финальный проект по разработке и работе с API от Яндекс Практикума.


## Запуск

1. Создайте виртуальное окружение
```bash
python -m venv venv
```

2. Активируйте виртуальное окружение и установите зависимости
```bash
source venv/Scripts/activate
```

```bash
pip install -r requirements.txt
```

4. Перейдите в директорию джанго-проекта
```bash
cd yatube_api/
```

5. Выполните миграции

``` bash
python manage.py makemigrations
```

``` bash
python manage.py migrate
```

6. Запустите проект
```bash
python manage.py runserver
```
