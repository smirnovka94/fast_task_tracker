## Установка и использование
Клонируем репозиторий

#### Устанавливаем виртуальное окружение 
```
python -m venv env
```
#### Запускаем Виртуальное окружение
```
env\Scripts\activate.bat
```
#### Устанавливаем библиотеки
```
pip install -r requirements.txt
```
#### Создаем файл<.env>
.env.template переименовать на .env,  
ввести пароль Postgres

#### Запуск приложения
```
uvicorn main:app --reload
```
