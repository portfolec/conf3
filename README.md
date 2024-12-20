# Установка
1. Установка программы и переход в директорию
   ```bash
   git clone <URL репозитория>
   cd <директория проекта>
   ```
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate     # Для Windows
   ```
3. Установите необходимые зависимости :
   ```bash
   Зависимости не требуются
   ```

# Запуск скрипта

Скрипт принимает текст конфигурационного файла через стандартный ввод и выводит xml в стандартный вывод.

```bash
cat input.xml | python hw3.py
```

# Тесты

Шаги запуска тестов:
1. Установить библиотеку pytest (необходимо, если не сделано ранее):
   ```bash
   pip install pytest
   ```
   
2. Для запуска тестирования необходимо запустить следующий скрипт:
   ```shell
   python unittests.py
   ```

   Входные данные
<img width="444" alt="Снимок экрана 2024-12-20 в 15 50 56" src="https://github.com/user-attachments/assets/917119dd-5c05-4df4-bb12-e8ff2fd81b3c" />


   Вывод

<img width="567" alt="Снимок экрана 2024-12-20 в 15 52 36" src="https://github.com/user-attachments/assets/6ba56d37-b4d2-479f-b366-fc5487f4be8c" />

