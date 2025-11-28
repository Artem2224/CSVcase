# Скрипт для обработки CSV-файла

Скрипт выводит в консоль отчёт со следующими полями: номер, позиция, средняя эффективность.  
Отчёт сортируется по эффективности.

---

## Установка зависимостей

```bash
python -m venv venv
venv\Scripts\activate        # для Windows
# или для Linux/macOS:
# source venv/bin/activate
pip install -r requirements.txt
```

## Запуск скрипта
```bash
cd main
python main.py --files employees1.csv employees2.csv --report performance
```

## Параметры запуска
--files: один или несколько CSV-файлов с данными
--report: название отчета (по-умолчанию performance)

## Пример запуска скрипта
<img width="946" height="279" alt="Скрин" src="https://github.com/user-attachments/assets/3fcaaa63-0460-43bd-ab92-ef6e97a045f2" />
