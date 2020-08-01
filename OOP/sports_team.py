class School:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def get_total_player_in_school(self):
        return sum(t.get_number_of_players() for t in self.teams)


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def get_number_of_players(self):
        return len(self.players)


class Player:
    def __init__(self, id, name, team_name):
        self.ID = id
        self.name = name
        self.team_name = team_name


p1 = Player(1, "Harris", "Red")
p2 = Player(2, "Carol", "Red")
p3 = Player(1, "Johnny", "Blue")
p4 = Player(2, "Sarah", "Blue")

red_team = Team("Red Team")
red_team.add_player(p1)
red_team.add_player(p2)

blue_team = Team("Blue Team")
blue_team.add_player(p2)
blue_team.add_player(p3)


mySchool = School("My School")
mySchool.add_team(red_team)
mySchool.add_team(blue_team)

print("Total players in mySchool:", mySchool.get_total_player_in_school())
