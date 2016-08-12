"""
nba.py (9 points)
-----

You've been hired as the general manager of the NETS, and it's your job to
figure out which basketball players you want to trade for.  You only want to 
trade for players that make at least 50% of the shots they've tried and have 
played at least 50 games.  You have a list of all players in the league, with 
their names, number of games played, average number of shots attempted (FGA) 
and average number of shots made (FGM).  Create a report for yourself by 
doing the following...

Download the list is located at: 

http://foureyes.github.io/csci-ua.0002-spring2015-007/homework/hw10/stats-clean.txt

(download it to the same directory that your program is in)

Write a program that:

* reads in data from a file called stats-clean.txt, which contains a list of 
  players and their statistics 
	* the first line of the file is the header: NAME,POS,TEAM,GP,FGM,FGA
	* each subsequent row contains player stats
	* the stats are separated by commas
	* for example, in the following line... James Harden,SG,HOU,78,7.5,17.1:
		* Name (NAME) -> James Harden
		* Position (POS) -> SG
		* Team (TEAM) -> HOU
		* Games Played (GP) -> 78
		* Average Shots Made Per Game (FGM) -> 7.5
		* Average Shots Attempted Per Game (FGA) -> 17.1
* calculate a player's shooting percentage by dividing their shots made by 
  their shots attempted (FGM/FGA)
* whittle down this list to only players that:
	* made at least 50% of their shots 
	* have played at least 50 games
* write out the names of these players, along with their shooting percentage into a new file
	* the file should be called report.csv
	* each name and shooting percentage will be on one line
	* ... with a comma separating the two
	* it should look similar to this:

Chris Wilcox,0.72
DeAndre Jordan,0.63
Tyson Chandler,0.64
Greg Smith,0.62
Ryan Hollins,0.63
Andre Drummond,0.61
Hasheem Thabeet,0.63
Brandan Wright,0.6
Nick Collison,0.59
Kosta Koufos,0.57
Dwight Howard,0.58
.
.
.
Kevin Durant,0.51
Chris Kaman,0.51
Andrei Kirilenko,0.5
Larry Sanders,0.51
Ronny Turiaf,0.53
Tim Duncan,0.5
Jason Thompson,0.51
Jan Vesely,0.5
Lance Thomas,0.5
David West,0.5
Kevin Garnett,0.5
Marc Gasol,0.5
Andris Biedrins,0.5

Use the following slides for reference:

http://foureyes.github.io/csci-ua.0002-spring2015-007/classes/23/files.html
"""

all_players = open("stats-clean.txt", "r")

all_player_stats = all_players.readlines()

del all_player_stats[0]

new_stats = open("report.csv", "w")

for player in all_player_stats:
    player = player.split(",")
    if float(player[5]) > 0:
        shooting_percentage = float(player[4]) / float(player[5])
    if shooting_percentage >= .5 and int(player[3]) > 50:
        new_stats.write("%s,%s\n" %(player[0], shooting_percentage))



