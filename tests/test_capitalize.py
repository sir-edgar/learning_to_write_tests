# Нажмите кнопку Run чтобы запустить тесты.

# Файлы с исходным кодом можно посмотреть на вкладке "Files":
# src/capitalize.py        - тестируемая функция
# tests/test_capitalize.py - тесты функции

# Попробуйте изменять код функции/тестов, запуская проверки заново.

from src.capitalize import capitalize

assert capitalize('hello') == 'Hello'

assert capitalize('') == ''

print('Все тесты пройдены!')

