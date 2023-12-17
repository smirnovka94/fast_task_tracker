# Установка и использование
Клонируем репозиторий

Устанавливаем виртуальное окружение 
```
python -m venv env
```
Запускаем Виртуальнео окружение
```
env\Scripts\activate.bat
```
Устанавливаем библиотеки
```
pip install -r requirements.txt
```
Запуск приложения
```
uvicorn main:app --reload
```
