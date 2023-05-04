import pandas as pd
import numpy as np

class Database:
    def __init__(self):
        self.shotData = pd.read_csv('shotdata.csv')
        self.shotData = self.shotData.rename(columns={'Dist.':'averageDistance', 'Tm':'team', 'Pos':'position', 'Player':'player', 'G':'gamesPlayed', 'MP':'minutes', 'Age':'age'})
        self.shotData.fillna(0.0, inplace = True)
        
        self.teamNames = {
            'Atlanta Hawks':'ATL',
            'Boston Celtics':'BOS',
            'Charlotte Hornets':'CHA',
            'Chicago Bulls':'CHI',
            'Cleveland Cavaliers':'CLE',
            'Dallas Mavericks':'DAL',
            'Denver Nuggets':'DEN',
            'Detroit Pistons':'DET',
            'Golden State Warriors':'GSW',
            'Houston Rockets':'HOU',
            'Indiana Pacers':'IND',
            'Los Angeles Clippers':'LAC',
            'Los Angeles Lakers':'LAL',
            'Memphis Grizzlies':'MEM',
            'Miami Heat':'MIA',
            'Milwaukee Bucks':'MIL',
            'Minnesota Timberwolves':'MIN',
            'New Orleans Pelicans':'NOP',
            'New York Knicks':'NYK',
            'Brooklyn Nets':'BKN',
            'Oklahoma City Thunder':'OKC',
            'Orlando Magic':'ORL',
            'Philadelphia 76ers':'PHI',
            'Phoenix Suns':'PHO',
            'Portland Trail Blazers':'POR',
            'Sacramento Kings':'SAC',
            'San Antonio Spurs':'SAS',
            'Toronto Raptors':'TOR',
            'Utah Jazz':'UTA',
            'Washington Wizards':'WAS',
            'Traded Players':'TOT'
            }
        
        self.positions = {
            'Point Guards':'PG',
            'Shooting Guards':'SG',
            'All Guards':'G',
            'Small Forwards':'SF',
            'Power Forwards':'PF',
            'All Forwards':'F',
            'Centers':'C'
            }
        
    def getLeagueAverages(self):
        return np.array([
            self.shotData.loc[:,"0-3 FG%"].mean(),
            self.shotData.loc[:,"3-10 FG%"].mean(),
            self.shotData.loc[:,"10-16 FG%"].mean(),
            self.shotData.loc[:,"16-3P FG%"].mean(),
            self.shotData.loc[:,"3P FG%"].mean(),
            ])
    
    def getWeightedAverages(self):
        return np.array([
            self.shotData.loc[:,"% of 0-3"].mean(),
            self.shotData.loc[:,"% of 3-10"].mean(),
            self.shotData.loc[:,"% of 10-16"].mean(),
            self.shotData.loc[:,"% of 16-3P"].mean(),
            self.shotData.loc[:,"% of 3P"].mean(),
            ])
    
    def findPlayer(self,getWeights=False):
        playerName = self.getPlayer()
        player = self.shotData.loc[self.shotData['player'] == playerName]
        
        playerAverages = np.array([
            player["0-3 FG%"].values[0],
            player["3-10 FG%"].values[0],
            player["10-16 FG%"].values[0],
            player["16-3P FG%"].values[0],
            player["3P FG%"].values[0]
            ])
        
        playerWeights = np.array([
            player["% of 0-3"].values[0],
            player["% of 3-10"].values[0],
            player["% of 10-16"].values[0],
            player["% of 16-3P"].values[0],
            player["% of 3P"].values[0]
            ]) if getWeights else None
        
        return playerName,playerAverages,playerWeights
        
    
    def getPlayer(self):
        while True:
            query = input('Which player(s) do you want to find?: ')
            playerList = self.shotData.loc[self.shotData["player"].str.contains(query,case=False),"player"].values.tolist()
            if len(playerList) == 1:
                return playerList[0]
            elif not playerList:
                print('ERROR - No players found')
                continue
            for i,playerName in enumerate(playerList):
                print(str(i+1).ljust(8),playerName)
            choice = self.getNum(len(playerList))
            return playerList[choice]        
    
    def findTeam(self,getWeights=False):
        for i,team in enumerate(self.teamNames.keys()):
            print(str(i+1).ljust(8),team)
        choice = self.getNum(len(self.teamNames.keys()))
        teamChoice = self.teamNames[list(self.teamNames.keys())[choice]]
        
        teamAverages = np.array([
            self.shotData.loc[self.shotData["team"] == teamChoice,"0-3 FG%"].mean(),
            self.shotData.loc[self.shotData["team"] == teamChoice,"3-10 FG%"].mean(),
            self.shotData.loc[self.shotData["team"] == teamChoice,"10-16 FG%"].mean(),
            self.shotData.loc[self.shotData["team"] == teamChoice,"16-3P FG%"].mean(),
            self.shotData.loc[self.shotData["team"] == teamChoice,"3P FG%"].mean(),
            ])
        
        teamWeights = np.array([
            self.shotData.loc[self.shotData["team"] == teamChoice,"% of 0-3"].mean(),
            self.shotData.loc[self.shotData["team"] == teamChoice,"% of 3-10"].mean(),
            self.shotData.loc[self.shotData["team"] == teamChoice,"% of 10-16"].mean(),
            self.shotData.loc[self.shotData["team"] == teamChoice,"% of 16-3P"].mean(),
            self.shotData.loc[self.shotData["team"] == teamChoice,"% of 3P"].mean(),
            ]) if getWeights else None
        
        return teamChoice,teamAverages,teamWeights
        
    
    def findPosition(self,getWeights=False):
        for i,team in enumerate(self.positions.keys()):
            print(str(i+1).ljust(8),team)
        choice = self.getNum(len(self.positions.keys()))
        positionChoice = self.positions[list(self.positions.keys())[choice]]
        
        posAverages = np.array([
            self.shotData.loc[self.shotData["position"].str.contains(positionChoice,case=True),"0-3 FG%"].mean(),
            self.shotData.loc[self.shotData["position"].str.contains(positionChoice,case=True),"3-10 FG%"].mean(),
            self.shotData.loc[self.shotData["position"].str.contains(positionChoice,case=True),"10-16 FG%"].mean(),
            self.shotData.loc[self.shotData["position"].str.contains(positionChoice,case=True),"16-3P FG%"].mean(),
            self.shotData.loc[self.shotData["position"].str.contains(positionChoice,case=True),"3P FG%"].mean(),
            ])
        
        posWeights = np.array([
            self.shotData.loc[self.shotData["position"].str.contains(positionChoice,case=True),"% of 0-3"].mean(),
            self.shotData.loc[self.shotData["position"].str.contains(positionChoice,case=True),"% of 3-10"].mean(),
            self.shotData.loc[self.shotData["position"].str.contains(positionChoice,case=True),"% of 10-16"].mean(),
            self.shotData.loc[self.shotData["position"].str.contains(positionChoice,case=True),"% of 16-3P"].mean(),
            self.shotData.loc[self.shotData["position"].str.contains(positionChoice,case=True),"% of 3P"].mean(),
            ]) if getWeights else None
        
        return list(self.positions.keys())[choice],posAverages,posWeights
    
    def getNum(self,inputLength):
        while True:
            try:
                choice = int(input('Make your choice by entering the number: '))
                if 1 <= choice <= inputLength:
                    return choice-1
                print('ERROR - Invalid number entered')
            except ValueError:
                print('ERROR - Please enter a number')
                    
        
                    

