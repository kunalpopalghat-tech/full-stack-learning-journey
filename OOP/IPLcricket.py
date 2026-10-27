class players:
    def __init__(self,jersey_number,name,runs,wickets,team_name):
        self.jersey_number = jersey_number
        self.name = name
        self.runs = runs
        self.wickets = wickets
        self.team_name = team_name

p1 = players(45,"Rohit sharma",6767,30,"MI")
p2 = players(33,"Hardik pandya",2500,90,"MI")
p3 = players(93,"Jasprit bumrah",200,150,"MI")
p4 = players(63,"Suryakumar",3000,00,"MI")
p5 = players(45,"Tilak verma",2000,10,"MI")

class team:
    def __init__(self , tn , pl):
        self.team_name = tn
        self.players = pl
          
MI_team = []

MI_team.append(p1)
MI_team.append(p2)
MI_team.append(p3)
MI_team.append(p4)
MI_team.append(p5)

for p in MI_team:
    if p.runs > 5000:
        print(p.name ,"----------->",p.runs)

# mi_team = team.("MI", MI_team)