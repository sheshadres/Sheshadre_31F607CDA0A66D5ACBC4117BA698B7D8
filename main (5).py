#Firstly define base class player
class player:
    def play(self):
        print("The player is playing Cricket.")

#defining batsman
class Batsman(player):
    def play(self):
        print("The batsman is batting.")

#defining bowler
class Bowler(player):
    def play(self):
        print("The bowler is bowling.")

#creating objects of batsman and bowler here
batsman = Batsman()
bowler =  Bowler()

#Here lets call batsman first and bowler next
batsman.play()
bowler.play()