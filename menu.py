import data
import graph

class Menu:
    
    def __init__(self):
        self.options = [('Get Player Shot Chart',0),('Get Position Shot Chart',1),('Get Team Shot Chart',2)]
        self.weighted = [('Not Weighted to Attempts',False),('Weighted to Attempts',True)]
        self.compare = [('Don\'t Compare to League',False),('Compare to League',True)]
        self.d = data.Database()
        self.g = graph.GraphPlotter(self.d.getLeagueAverages(), self.d.getWeightedAverages())
        
    def getNum(self,inputLength):
        while True:
            try:
                choice = int(input('Make your choice by entering the number: '))
                if 1 <= choice <= inputLength:
                    return choice-1
                print('ERROR - Invalid number entered')
            except ValueError:
                print('ERROR - Please enter a number')
        
    def printer(self,arr):
        for i, option in enumerate(arr):
            print(str(i+1).ljust(8),option[0])
        print('-'*60)
        choice = arr[self.getNum(len(arr))][1]
        print('-'*60)
        return choice
    
    def display(self):
        print('main menu'.upper())
        print('='*60)
        mainMenuChoice = self.printer(self.options)
        print('weighted'.upper())
        print('='*60)
        weightChoice = self.printer(self.weighted)
        print('compare'.upper())
        print('='*60)
        compareChoice = self.printer(self.compare)
        
        if mainMenuChoice == 0:
            name, shotPercentages, weights = self.d.findPlayer(weightChoice)
        elif mainMenuChoice == 1:
            name, shotPercentages, weights = self.d.findPosition(weightChoice)
        else:
            name, shotPercentages, weights = self.d.findTeam(weightChoice)
            
        if weightChoice:
            self.g.drawWeightedPlot(name, shotPercentages, weights, compareChoice)
        else:
            self.g.drawAveragePlot(name, shotPercentages, compareChoice)
