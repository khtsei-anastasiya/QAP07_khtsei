# 0. Обязательно к прочтению Дзен python.
# 1. Создать несколько функций на проверку введённых данных:
# - Проверка имени
# - Проверка возраста
# Функции должны возвращать строку с ошибкой. Если функции вернули ошибки, нужно вывести пользователю ошибки.
# 2. Улучшить проверку имени: в имени допускается только 1 пробел.
# 3. Сделать совет по получению или замене паспорта (эта задача больше не является со звездочкой) в отдельной функции,
# которая возвращает строку с советом или ничего не возвращает.
# 4. Создать функцию main, в которой будут вызовы всех остальных функций, ввод данных и прочее.
# 5. Создать цикл до тех пор, пока пользователь не введёт верные данные без ошибок.
# 6. Создать функцию, которая очищает введённые данные от лишних пробелов в начале и в конце строки.
# 7. Все функции должны иметь документацию (docstring) (вспоминаем второй урок) и аннотации.


def check_name(name: str) -> str:
    """This function validates name for nonempty state, min length and spaces and returns error if so. If validation
    pass, there are no error message. """
    if not name:
        err_message = f'You haven\'t provided your name. '
        return err_message
    if name.count(' ') > 1:
        err_message = f'Only one space is allowed. Ex. "Lora Lee" '
        return err_message
    if len(name) < 3:
        err_message = f'Your name is less than 3 letters. '
        return err_message
    return ''


def check_age(age: int) -> str:
    """This function validates age for nonempty state and min available age and returns error if so. If validation pass,
    there are no error message."""
    if not age:
        err_message = f'You haven\'t provided your age'
        return err_message
    if int(age) < 14:
        err_message = f'Sorry, you cannot use the program. Your age is less than 14'
        return err_message
    return ''


def suggestion(age: int) -> str:
    """This function validates age for certain intervals to release id and returns suggestion message if so.
     If age is outside the intervals, there are no suggestion message."""
    if 16 <= int(age) <= 17:
        message = f'Don\'t forget to release your first id'
        return message
    if 25 <= int(age) <= 26:
        message = f'Don\'t forget to reissue your id'
        return message
    if 45 <= int(age) <= 46:
        message = f'Don\'t forget to reissue your id again'
        return message
    return ''


def main_input():
    """This is main function which invokes input for name and age till it will be filled correctly"""
    err_message = ' '
    while err_message != '' '':
        name = input('What\'s your name?: ').strip()
        age = input('How old are you?: ')
        err_message = check_name(name) + check_age(age)
        if err_message == '' '':
            err_message = f'Hey, "{name.title()}"! You are {age} y.o! {suggestion(age)}'
            print(err_message)
            break
        else:
            print(check_name(name), check_age(age))


main_input()
