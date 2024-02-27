class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def double_health(self):
        return self.health_points * 2

    def __str__(self):
        return f'{self.nickname} {self.superpower} {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


batman = SuperHero('Брюс Уэйн', 'batman', 'money', 100, 'im batman')

print(batman)
print(batman.double_health())
print(batman.__len__())


class EarthHero(SuperHero):
    earth = 'earth'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.fly = True
        return self.health_points ** 2

    def smile(self):
        return f'{self.fly} in the {self.fly}_phrase'


class SkyHero(SuperHero):
    sky = 'sky'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        SuperHero.__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.fly = True
        return self.health_points ** 2

    def smile(self):
        return f'{self.fly} in the {self.fly}_phrase'


class SpaceHero(SuperHero):
    space = 'space'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        SuperHero.__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.fly = True
        return self.health_points ** 2

    def smile(self):
        return f'{self.fly} in the {self.fly}_phrase'


space_hero_example = SpaceHero(
    name="Galactic Guardian",
    nickname="Star Voyager",
    superpower="Cosmic Energy Manipulation",

    health_points=500,
    catchphrase="To infinity, and beyond!",
    damage=75,
    fly=True  # This can be omitted to use the default value of False
)
class Villain(EarthHero):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=True):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)  # Corrected call

    def gen_x(self):
        pass

    def crit(self, cls):
        return self.damage * self.damage


villain_example = Villain(name='Jack Napie', nickname='Joker', superpower='smile', health_points=60,
                          catchphrase='hahaahhahah', damage=15)

villain_example.crit(SkyHero)
