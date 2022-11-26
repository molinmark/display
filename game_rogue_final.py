import random
from random import randint
from math import fabs

key_list = ['w', 'a', 's', 'd']


class room:
    def __init__(self):
        self.X = random.randint(8, 16)
        self.Y = random.randint(6, 12)
        self.f_item_coord = 0
        self.s_item_coord = 0
        self.matrix = [[' '] * self.X for i in range(self.Y)]

    def generation(self):
        self.Y0 = random.randint(1, self.Y - 2)
        self.X0 = 1

        self.exit = [self.X, random.randint(1, self.Y - 2)]
        self.input = [0, self.Y0]
        self.matrix[self.Y0][self.X0] = '๏'
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if i == 0 or j == 0 or i == len(self.matrix) - 1 or j == len(self.matrix[i]) - 1:
                    self.matrix[i][j] = '╬'
        self.matrix[self.input[1]][self.input[0]] = ' '
        self.matrix[self.exit[1]][self.X - 1] = ' '
        self.cord0 = [self.X0, self.Y0]
        self.cord = [self.X, self.Y]
        """
        начальная кордината монстра
        """
        while True:
            self.Y0_monster0 = random.randint(1, self.Y - 2)
            self.X0_monster0 = random.randint(3, self.X - 2)
            self.cord_monster0 = [self.X0_monster0, self.Y0_monster0]
            if self.matrix[self.cord_monster0[1]][self.cord_monster0[0]] != '๏':
                self.matrix[self.cord_monster0[1]][self.cord_monster0[0]] = '☿'
                break
        return self.f_item_coord, self.s_item_coord

    def update_character(self, new_cord):
        self.matrix[self.Y0][self.X0] = ' '
        self.Y0 = new_cord[1]
        self.X0 = new_cord[0]
        self.matrix[self.Y0][self.X0] = '๏'

    def item_coord(self):
        return self.f_item_coord, self.s_item_coord

    def update_monster(self, new_cord_monster, alive_or_ded):
        self.matrix[self.Y0_monster0][self.X0_monster0] = ' '
        if alive_or_ded == 'жив':
            self.Y0_monster0 = new_cord_monster[1]
            self.X0_monster0 = new_cord_monster[0]
            self.matrix[self.Y0_monster0][self.X0_monster0] = '☿'
        else:
            self.matrix[self.Y0_monster0][self.X0_monster0] = '†'

    def display(self):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()
        print()


class Character:
    def __init__(self, name, type_of_person):
        self.type_of_person = type_of_person
        self.name = name
        self.health = 0
        self.armor = 0
        self.attack_range = 0
        self.attack_damage = 0
        self.speed = 0

    def get_health(self):
        if self.type_of_person == ('человек' or 'Человек'):
            self.health = 100
        elif self.type_of_person == ('эльф' or 'Эльф'):
            self.health = 90
        elif self.type_of_person == ('гном' or 'Гном'):
            self.health = 120
        return self.health

    def get_armor(self):
        if self.type_of_person == ('человек' or 'Человек'):
            self.armor = 10
        elif self.type_of_person == ('эльф' or 'Эльф'):
            self.armor = 8
        elif self.type_of_person == ('гном' or 'Гном'):
            self.armor = 12
        return self.armor

    def get_speed(self):
        if self.type_of_person == ('человек' or 'Человек'):
            self.speed = 1
        elif self.type_of_person == ('эльф' or 'Эльф'):
            self.speed = 2
        elif self.type_of_person == ('гном' or 'Гном'):
            self.speed = 1
        return self.speed

    def get_damage_range(self):
        if self.type_of_person == ('человек' or 'Человек'):
            self.attack_range = 1
        elif self.type_of_person == ('эльф' or 'Эльф'):
            self.attack_range = 2
        elif self.type_of_person == ('гном' or 'Гном'):
            self.attack_range = 1
        return self.attack_range

    def get_attack_damage(self):
        if self.type_of_person == ('человек' or 'Человек'):
            self.attack_damage = 20
        elif self.type_of_person == ('эльф' or 'Эльф'):
            self.attack_damage = 25
        elif self.type_of_person == ('гном' or 'Гном'):
            self.attack_damage = 22
        return self.attack_damage

    def start_defence(self, another):
        number = random.randint(0, 20)
        if self.armor >= number:
            self.health += another.attack_damage
            print(f'Защита проведена успешно, здоровье персонажа: {self.health}')

    """
    последствие атаки с изменением урона
    """
    def attack_result(self, another):
        number = random.randint(0, 30)
        if number < 25:
            another.health -= self.attack_damage
        elif number >= 25:
            another.health -= 2 * self.attack_damage  # это шанс на критический урон
            print(f'{self.name } нанес критический урон')

    def move(self, direction, cord0, cord, exit, input, cord_monster0):
        cord1 = [cord0[0], cord0[1]]
        if direction == ('w' or 'W'):
            cord0[1] -= 1
        elif direction == ('a' or 'A'):
            cord0[0] -= 1
        elif direction == ('s' or 'S'):
            cord0[1] += 1
        elif direction == ('d' or 'D'):
            cord0[0] += 1
        else:
            print('Некорректное направление')

        if exit[0] - 1 == cord0[0] and exit[1] == cord0[1]:
            pass
        elif input[0] == cord0[0] and input[1] == cord0[1]:
            pass
        elif cord0[1] < cord[1] - 1 and cord0[0] < cord[0] - 1 and cord0[1] >= 1 and cord0[0] >= 1:
            pass
        else:
            cord0[0] = cord1[0]
            cord0[1] = cord1[1]
        if cord0[0] == cord_monster0[0] and cord0[1] == cord_monster0[1]:
            cord0[0] = cord1[0]
            cord0[1] = cord1[1]
        return cord0


class Monster(Character):
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.armor = 0
        self.attack_damage = 0
        self.attack_range = 0
        self.speed = 0

    def get_monster_health(self):
        if self.name == 'Гоблин':
            self.health = 40
        elif self.name == 'Орк':
            self.health = 80
        elif self.name == 'Разбойник':
            self.health = 55
        return self.health

    def get_monster_damage(self):
        if self.name == 'Гоблин':
            self.attack_damage = 5
        elif self.name == 'Орк':
            self.attack_damage = 20
        elif self.name == 'Разбойник':
            self.attack_damage = 15

        return self.attack_damage

    def get_monster_range(self):
        if self.name == 'Гоблин':
            self.attack_range = 1
        elif self.name == 'Орк':
            self.attack_range = 1
        elif self.name == 'Разбойник':
            self.attack_range = 2
        return self.attack_range

    def get_monster_armor(self):
        if self.name == 'Гоблин':
            self.armor = 3
        elif self.name == 'Орк':
            self.armor = 8
        elif self.name == 'Разбойник':
            self.armor = 4
        return self.armor

    def get_monster_speed(self):
        if self.name == 'Гоблин':
            self.speed = 1
        elif self.name == 'Орк':
            self.speed = 1
        elif self.name == 'Разбойник':
            self.speed = 2
        return self.speed

    def move(self, cord_monster0, cord, new_cord):
        cord_monster1 = [cord_monster0[0], cord_monster0[1]]
        global key_list, direction

        if (fabs(cord_monster0[0] - new_cord[0]) <= 5 and fabs(
                cord_monster0[1] - new_cord[1]) <= 5):  # здесь задаётся радиус обнаружения
            if cord_monster0[0] > new_cord[0]:
                cord_monster0[0] -= 1
            elif cord_monster0[0] < new_cord[0]:
                cord_monster0[0] += 1
            elif cord_monster0[1] > new_cord[1]:
                cord_monster0[1] -= 1
            elif cord_monster0[1] < new_cord[1]:
                cord_monster0[1] += 1
        else:
            direction = random.choices(key_list)[0]
            if direction == 'w':
                cord_monster0[1] -= 1
            elif direction == 'a':
                cord_monster0[0] -= 1
            elif direction == 's':
                cord_monster0[1] += 1
            elif direction == 'd':
                cord_monster0[0] += 1

        if cord_monster0[1] < cord[1] - 1 and cord_monster0[0] < cord[0] - 1 and cord_monster0[1] >= 1 and \
                cord_monster0[0] >= 1:
            pass
        else:
            cord_monster0[0] = cord_monster1[0]
            cord_monster0[1] = cord_monster1[1]
        if cord_monster0[0] == new_cord[0] and cord_monster0[1] == new_cord[1]:
            cord_monster0[0] = cord_monster1[0]
            cord_monster0[1] = cord_monster1[1]

        return cord_monster0

    def alive_or_ded(self):
        if self.health <= 0:
            return 'мёртв'
        else:
            return 'жив'


class Items:
    def __init__(self, name_items):
        self.name_items = name_items
        self.state = 'лежит'
       # if name_items == 'Кинжал' or name_items =='Великий меч':
       #     self.property = 'рукопашное'
       # if name_items == 'Короткий лук' or name_items =='Длинный лук':
       #     self.property = 'дальнобойное'
    """
    предметы будут исчезать после их поднятия
    """
    def parametres(self):
        if self.name_items == 'Кинжал':
            self.damage = 35
            self.range_attack = 1

        elif self.name_items == 'Короткий лук':
            self.damage = 25
            self.range_attack = 2

        elif self.name_items == 'Длинный лук':
            self.damage = 30
            self.range_attack = 3

        elif self.name_items == 'Великий меч':
            self.damage = 50
            self.range_attack = 1

    def loot(self,new_cord_monster,new_cord,alive_or_ded):
        if (fabs(new_cord_monster[0]-new_cord[0]) <= 1 and fabs(new_cord_monster[1]-new_cord[1]) <= 1) and alive_or_ded=='мёртв':
            self.action_predmet = input(f'Хотите взять {self.name_items} ? Да/нет')
            if self.action_predmet == ('да' or 'Да'):
                self.state = 'взят'

def privetstvie():
    global type_of_person, name_person
    print('''Добро пожаловать в подземелье, 
Выбор расы во многом поможет Вам справиться с трудностями
Отличительные черты человека: защита и урон; эльфа - скорость, а гнома - уровень здооровья''')

    rases = ['человек', 'Человек', 'эльф', 'Эльф', 'гном', 'Гном']
    # type_of_person = str(input(f'Выберите расу персонажа: человек, эльф или гном '))
    type_of_person = 'эльф'

    if type_of_person not in rases:
        while type_of_person not in rases:
            print("Вы некорректно выбрали расу персонажа ")
            type_of_person = str(input(f'Выберите расу персонажа: человек, эльф или гном '))
    #name_person = input('Назовите Вашего персонажа: ')
    name_person = 'Маркон '

def making_character():
    """
    создаёт монстра, ккоторого помещаю в main
    """
    personx = Character(name_person, type_of_person)  # создаём экземпляр класса
    personx.get_armor()
    personx.get_attack_damage()
    personx.get_damage_range()
    personx.get_speed()
    personx.get_health()
    return personx

def making_monster():
    """
    создаёт монстра, ккоторого помещаю в main
    """
    list_enemy = ('Гоблин', 'Орк', 'Разбойник')
    name_enemy = random.choice(list_enemy)
    monsterX = Monster(name_enemy)
    monsterX.get_monster_health()
    monsterX.get_monster_damage()
    monsterX.get_monster_armor()
    monsterX.get_monster_range()
    monsterX.get_monster_speed()
    monsterX.alive_or_ded()
    return monsterX