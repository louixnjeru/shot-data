import matplotlib.pyplot as plt
import numpy as np

class GraphPlotter:
    def __init__(self,leagueAverages,weightedAverages):
        self.distances = np.array([1.5,6.5,13,20,26])
        self.leagueAverages = np.array(leagueAverages)
        self.weightedAverages = np.array(weightedAverages)*self.leagueAverages
        self.leagueModel = self.createModel(self.distances,self.leagueAverages*100)
        self.weightedLeagueModel = self.createModel(self.distances,self.weightedAverages*100)
        
    def drawAveragePlot(self,name,shotPercentages,compare=False):
        averageModel = self.createModel(self.distances, shotPercentages*100)
        self.drawGraph(name,averageModel,compare)
        
    
    def drawWeightedPlot(self,name,shotPercentages,weights,compare=False):
        weightedPercentages = shotPercentages*weights
        weightedModel = self.createModel(self.distances, weightedPercentages*100)
        self.drawGraph(name,weightedModel,compare,True)
        
    
    def createModel(self,distances,averages):
        coefficients = np.polyfit(distances,averages,3)
        model = np.poly1d(coefficients)
        line = np.linspace(0,30,100)
        curve = model(line)
        return line,curve
    
    def drawGraph(self,name,model,compare,weighted=False):
        w = "Weighted " if weighted else ""
        plt.title(f'{w}Shot Percentages at Distance - {name}')
        plt.xlabel('Shot Distance (ft)')
        plt.ylabel(f'{w}Shot Percentage (%)')
        plt.plot(model[0],model[1],c='r',label=f'Modelled {w}Percentage')
        if compare:
            if weighted:
                plt.plot(self.weightedLeagueModel[0],self.weightedLeagueModel[1],c='g',label=f'{w}League Average Model')
            else:
                plt.plot(self.leagueModel[0],self.leagueModel[1],c='g',label=f'{w}League Average Model')
        plt.legend()
        plt.show()
        
        