'''
Created on Jul 17, 2016

@author: eli
'''

import matplotlib.pyplot as plt
import numpy as np


class CreateHeatMap:
    '''
    classdocs
    '''


    def __init__(self, districtList , crimelist , datalist):
        '''
        Constructor
        '''
        column_labels = sorted(districtList)
        row_labels = crimelist
        data = np.array(datalist)
        fig, ax = plt.subplots()
        heatmap = ax.pcolor(data, cmap=plt.cm.Blues)
        
        #legend
        cbar = plt.colorbar(heatmap)
       
        fig = plt.gcf()
        fig.set_size_inches(5,5)
        
        # turn off the frame
        ax.set_frame_on(False)
        
        # put the major ticks at the middle of each cell
        ax.set_xticks(np.arange(data.shape[1])+0.5, minor=False)
        ax.set_yticks(np.arange(data.shape[0])+0.5, minor=False)
        
        # want a more natural, table-like display
        ax.invert_yaxis()
        ax.xaxis.tick_top()
        
        
        ax.set_xticklabels(row_labels, minor=False,rotation=90,fontsize='x-small')
        ax.set_yticklabels(column_labels, minor=False)
        
        ax.grid(False)
        
        # Turn off all the ticks
        ax = plt.gca()
        
        for t in ax.xaxis.get_major_ticks(): 
            #t.label.set_fontsize(6) 
            t.tick1On = False 
            t.tick2On = False 
            t.tick3On = False 
        for t in ax.yaxis.get_major_ticks(): 
            t.tick1On = False 
            t.tick2On = False  
            
        plt.margins(0.05)
        # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(  top = 0.7)
        
        plt.show()
        
        #=======================================================================
        # import pandas as pd
        #  
        # import seaborn as sns
        #  
        # # import the data directly into a pandas dataframe
        # df = DataFrame(data)
        # df = df.transpose()
        # # remove index title
        # df.index.name = ""
        # # normalize data columns
        # df_norm = (df - df.mean()) / (df.max() - df.min())
        # # relabel columns
        # labels = ['Games', 'Minutes', 'Points', 'Field goals made', 'Field goal attempts', 'Field goal percentage', 'Free throws made', 
        #           'Free throws attempts', 'Free throws percentage','Three-pointers made', 'Three-point attempt', 'Three-point percentage', 
        #           'Offensive rebounds', 'Defensive rebounds', 'Total rebounds', 'Assists', 'Steals', 'Blocks', 'Turnover', 'Personal foul']
        # nba_norm.columns = crimelist
        # # set appropriate font and dpi
        # sns.set(font_scale=1.2)
        # sns.set_style({"savefig.dpi": 100})
        # # plot it out
        # ax = sns.heatmap(df_norm, cmap=plt.cm.Blues, linewidths=.1)
        # # set the x-axis labels on the top
        # ax.xaxis.tick_top()
        # # rotate the x-axis labels
        # plt.xticks(rotation=90)
        # # get figure (usually obtained via "fig,ax=plt.subplots()" with matplotlib)
        # fig = ax.get_figure()
        # # specify dimensions and save
        # fig.set_size_inches(15, 20)
        # fig.savefig("nba.png")
        #=======================================================================