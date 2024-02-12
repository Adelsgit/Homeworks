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


batman = SuperHero('Брюс Уэйн', 'batman', 'money', 100, 'im batman' )

print(batman)
print(batman.double_health())
print(batman.__len__())