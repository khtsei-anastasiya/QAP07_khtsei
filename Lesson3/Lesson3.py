# Написать программу, которая
# - Запрашивает у пользователя имя и возраст;
# - Проверяет минимальный возраст 14;
# - Проверяет, что имя введено и минимальное количество символов в имени — 3;
# - Проверяет возраст на отрицательное число или 0;
# - Проверяет имя на пустоту;
# * Проверяет, что возраст возраст 16-17 лет и нужно не забыть получить первый паспорт; возраст 25-26 лет и нужно заменить паспорт;
# возраст 45-46 лет и нужно второй раз заменить паспорт;
# - Выводит либо текст с ошибкой (по каждому условию разный текст ошибки), либо приветствие пользователя с его именем (с заглавной буквы),
# указанием возраста и *советом получить/заменить паспорт (если совет актуален).
# * Совет с паспортом выводить только в том случае, если отображается приветствие.

# Ограничения:
# - только один раз можно использовать print


name = input('What\'s your name?: ')
age = input('How old are you?: ')
name = name.strip()
if not name:
    name = f'You haven\'t provided your name'
elif name.__len__() >= 3:
    name = f'Nice to meet you "{name.capitalize()}"'
else:
    name = f'Your name is less than 3 letters'

if not age:
    age = f'You haven\'t provided your age'
elif int(age) < 14:
    age = f'Sorry, you cannot use the program. Your age is less than 14'
elif 16 <= int(age) <= 17:
    age = f'Don\'t forget to release your first id because you have {age} y.o'
elif 25 <= int(age) <= 26:
    age = f'Don\'t forget to reissue your id because you have {age} y.o'
elif 45 <= int(age) <= 46:
    age = f'Don\'t forget to reissue your id again because you have {age} y.o'
else:
    age = f'You are {age} y.o'

if name == f'You haven\'t provided your name':
    result = f'You cannot use program without name'
elif name == f'Your name is less than 3 letters':
    result = f'Your name is less than 3 letters, you cannot use program without correct name'
else:
    result = f'{name},\n {age}'

print(result)
