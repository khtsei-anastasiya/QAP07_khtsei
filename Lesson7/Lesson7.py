# Домашка до четверга:
# 1. Реализовать абстрактный класс машины (придумайте какие методы у машины есть, какие нужно у
# всех дочерних классов переопределять, а какие будут общие с готовой реализацией)
# 2. Реализовать несколько классов
# разных марок машин, наследуемых от базовой машины. Переопределить абстрактные методы, свойства. Придумать новые
# методы, которые есть только в конкретных марках машин.
# 3. Реализовать класс абстрактный класс самолета. Должно быть
# как минимум один или несколько одноименных атрибутов класса машины. Тоже самое из п.1
# 4. Реализовать несколько классов разных марок самолетов. Тоже самое из п.2 5. Создать несколько экземпляров каждой
# машины, каждого самолета,
# вызвать различные методы у этих объектов. «Поиграться», скажем так. А затем сделать коллекцию из этих объектов и
# через цикл пройтись по каждому из этих объектов и вызвать те методы, которые есть во всех классах.

class BasicCar:

    def __init__(self, model='', engine_type='', max_speed='', ):
        self.model = model
        self.engine_type = engine_type
        self.max_speed = max_speed

    def info(self):
        print(f'Car model is "{self.model}" \n'
              f'Engine type is "{self.engine_type}" \n'
              f'Max speed is "{self.max_speed}" km/h')

    def drive_type(self):
        pass

    def autopilot(self):
        pass


class Tesla(BasicCar):
    def __init__(self, battery_pover: int = 60, gear_type='1-speed fixed gear ratio'):
        self.battery_pover = battery_pover
        self.gear_type = gear_type
        super().__init__(model='Tesla S', engine_type='Electric', max_speed=249)

    def autopilot(self):
        if self.battery_pover > 60:
            print('Autopilot version 2')
        else:
            print('Autopilot version 1')

    def drive_type(self):
        print('Roads driving\n')

    @property
    def full_car_info(self):
        return self.info(), self.autopilot()


class LandRover(BasicCar):
    def __init__(self, engine_pover: int = 400, gear_type='Gear type is Automatic'):
        super().__init__(model='LandRover Sport', engine_type='Petrol', max_speed=190)
        self.gear_type = gear_type
        self.engine_pover = engine_pover

    def geartype(self):
        if self.engine_pover > 400:
            self.gear_type = self.gear_type
            print(self.gear_type)
        else:
            print('Gear type is Manual')

    def drive_type(self):
        print('Off-roads driving\n')

    @property
    def full_car_info(self):
        return self.info(), self.geartype()


new_tesla = Tesla(battery_pover=90)
new_land_rover = LandRover(engine_pover=500)


for cars in (new_tesla, new_land_rover, ):
    cars.full_car_info
    cars.drive_type()

