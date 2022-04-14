# 1.Создать 3 переменных с одинаковыми данными с одинаковыми идентификаторами

age_one = age_two = age_three = 20

print(age_one, id(age_one))
print(age_two, id(age_two))
print(age_three, id(age_three))

# 2.Создать 2 перменных с одинаковыми данными с разными идентификаторами
age_four = [1, 2, 3]
print(age_four, id(age_four))
age_five = [1, 2, 3]
print(age_five, id(age_five))

# 3.Поменять их типы так, чтобы у 1х трех были разные идентификаторы,а у 2х последних были одинаковые
age_one = '20'
age_two = 20.0
age_three = 20
print(age_one, id(age_one))
print(age_two, id(age_two))
print(age_three, id(age_three))


age_four = 257
age_five = 257
print(age_four, id(age_four))
print(age_five, id(age_five))
