players = [ # name, age, goals
    ["Jürgen", 56, 12],
    ["Walter", 32, 10],
    ["Hans", 31, 2],
    ["Gerd", 35, 20],
    ["Tim", 22, 3],
    ["Sofia", 33, 15],
    ["Berti", 32, 10],
    ["Jo", 44, 2]
]

seniors = [ # name, age, goals, is_active
    ["Fritz", 67, 34, True],
    ["Georg", 71, 25, False],
    ["Winfried", 71, 23, True],
    ["Hans", 68, 33, True]
]

class Player():

    def __init__(self, name: str, age: int, goals: int):
        self.name = name
        self.age = age
        self.goals = goals
        print("""
Hallo, my name is """ + self.name + """,
I'm """ + str(self.age) + """ years old
and I've already made """ + str(self.goals) + """ goals.""")

    def get_goals(self) -> int:
        return self.goals

    def get_name(self) -> str:
        return self.name

    def set_goals(self, goals): # deprecated
        self.goals = goals

class Senior(Player):

    def __init__(self, name: str, age: int, goals: int, is_active: bool):
        super().__init__(name, age, goals)
        self.is_active = is_active
        print("I'm a senior player" + (".", ", but still in action!")[self.is_active])

    def get_is_active(self) -> bool:
        return self.is_active

class Team:

    members = []

    def __init__(self, name: str):
        self.name = name
        print("A new team is born! Welcome " + self.name + "!")

    @classmethod
    def add_member(cls, member: object):
        cls.members.append(member)

    def get_active_seniors(self) -> int:
        sum = 0
        for senior in self.get_seniors():
            if senior.get_is_active():
                sum += 1
        return sum

    def get_first_scorer(self) -> object:
        max = 0
        scorer = None
        for player in self.get_players():
            goals = player.get_goals()
            if goals > max:
                max = goals
                scorer = player
        return scorer

    def get_goals_average(self, exclude_seniors = False) -> float:
        return self.get_goals_sum(exclude_seniors) / len(self.members)

    def get_goals_sum(self, exclude_seniors = False) -> int:
        sum = 0
        for member in self.members:
            if not exclude_seniors or not hasattr(member, 'is_active'):
                sum += member.get_goals()
        return sum

    def get_member_by_name(self, name: str) -> object or None: # X-D
        for member in self.members:
            if member.name == name:
                return member
        return None

    def get_players(self) -> list:
        players = []
        for member in self.members:
            if not hasattr(member, 'is_active'):
                players.append(member)
        return players

    def get_seniors(self) -> list:
        seniors = []
        for member in self.members:
            if hasattr(member, 'is_active'):
                seniors.append(member)
        return seniors

    def print_report(self):
        players = self.get_players()
        amount_players = len(players)
        seniors = self.get_seniors()
        amount_seniors = len(seniors)
        print()
        print("Team " + self.name + " facts:")
        print("- There are " + str(amount_players) + " players:")
        print("  ", end = '')
        for player in players:
            print(player.name, end = '')
            if players.index(player) == amount_players - 1:
                print("..")
            elif players.index(player) == amount_players - 2:
                print(" and ", end = '')
            else:
                print(", ", end = '')
        print("  and " + str(amount_seniors) + " seniors:")
        print("  ", end = '')
        for senior in seniors:
            print(senior.name, end = '')
            if seniors.index(senior) == amount_seniors - 1:
                print(".", end = " ")
            elif seniors.index(senior) == amount_seniors - 2:
                print(" and ", end = '')
            else:
                print(", ", end = '')
        print("(" + str(self.get_active_seniors()) + " of them are still active in team)")
        print("- Players ratio is " + str("%.2f" % self.get_goals_average(True)) + " goals per player! (Total is " + str(self.get_goals_sum(True)) + ")")
        print("- Overall ratio is " + str("%.2f" % self.get_goals_average()) + " goals per member! (Total is " + str(self.get_goals_sum()) + ")")
        sofias_goals = self.get_member_by_name("Sofia").get_goals()
        print("- The only female member of the team, Sofia, has already scored " + str(sofias_goals) + " goals!")
        first_scorer = self.get_first_scorer()
        print("- First active scorer is " + first_scorer.get_name() + ", with " + str(first_scorer.get_goals()) + " goals!")

    @classmethod
    def remove_member(cls, name: str):
        member = cls.get_member_by_name(cls, name)
        if member:
            cls.members.remove(member)
            print("Oh no! " + name + " wurde beurlaubt!")

team = Team("TEAM")

for player in players:
    new_player = Player(player[0], player[1], player[2])
    team.add_member(new_player)

for senior in seniors:
    new_senior = Senior(senior[0], senior[1], senior[2], senior[3])
    team.add_member(new_senior)

team.print_report()

print() # extras..

print("Aktuell haben wir " + str(len(team.get_players())) + " Spieler..")
team.remove_member("Gerd")
print("..und jetzt sind wir zur " + str(len(team.get_players())) + " geblieben!")