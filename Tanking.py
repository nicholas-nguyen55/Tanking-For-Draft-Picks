#!/usr/bin/env python
# coding: utf-8

# In[1569]:


cd programNick


# In[1570]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn as sns
from datetime import datetime


# In[1571]:


team_record = pd.read_csv('Team_Records.csv')


# In[1572]:


team_record.drop(['Lg', 'SRS', 'Pace', 'Rel_Pace', 'Rel_ORtg', 'Rel_DRtg', 'Coaches', 'Top WS'], axis=1, inplace=True)
team_record


# In[1573]:


#teams that did not make the playoffs had blank cells, added lottery to know which teams made the lottery 
team_record1 = team_record.fillna('Lottery')
team_record1


# In[1574]:


#get teams are in the lottery after the season has finished 
team_record1[team_record1['Playoffs'] == 'Lottery']


# In[1575]:


team_record = team_record1[team_record1['Playoffs'] == 'Lottery']
team_record


# In[1576]:


team_record = team_record.astype(str)


# In[1621]:


#get rid of the seasons that I will not be using for this assignment 
team_record[team_record['Season'].str.contains('1946-47|1947-48|1948-49|1949-50|1950-51|1951-52|1952-53|1953-54|1954-55|1955-56|1956-57|1957-58|1958-59|1959-60|'
                                              +'1960-61|1961-62|1962-63|1963-64|1964-65|1965-66|1966-67|1967-68|1968-69|1969-70|1970-71|1971-72|1972-73|1973-74|'
                                               +'1974-75|1975-76|1976-77|1977-78|1978-79|1979-80|1980-81|1981-82|1982-83|1983-84|1984-85|1985-86|1986-87|1987-88|'
                                               +'1988-89|1989-90|1990-91|1991-92|1992-93|1993-94|1994-95|1995-96|1996-97|1997-98|1998-99|1999-00|2000-01|2001-02|'
                                               +'2002-03|2003-04|2004-05|2005-06|2006-07|2017-18') == False]


# In[1622]:


worst_team = team_record.groupby(['Season', 'Team'])['W/L%'].min()


# In[1623]:


#Sacramento Kings had the worst record this year
worst_team['2008-09']


# In[1624]:


#New Jersey Nets had the worst record this year
worst_team['2009-10']


# In[1625]:


#Minnesota Timberwolves had the worst record this year
worst_team['2010-11']


# In[1626]:


#Charlotte Bobcats had the worst record this year
worst_team['2011-12']


# In[1627]:


#Orlando Magic had the worst record this year
worst_team['2012-13']


# In[1628]:


#Milwaukee Bucks had the worst record this year
worst_team['2013-14']


# In[1629]:


#Minnesota Timberwolves had the worst record this year
worst_team['2014-15']


# In[1630]:


#Philadelphia 76ers had the worst record this year
worst_team['2015-16']


# In[1631]:


#Brooklyn Nets had the worst record this year
worst_team['2016-17']


# In[1704]:


#The following few lines of code are for teams who had the worst record and their records afterwards to see if they got any better or worse
Sacramento = team_record.loc[((team_record['Season'] == '2008-09') & (team_record['Team'] == 'Sacramento Kings'))|((team_record['Season'] == '2009-10') & (team_record['Team'] == 'Sacramento Kings'))|
                                  ((team_record['Season'] == '2010-11') & (team_record['Team'] == 'Sacramento Kings'))|((team_record['Season'] == '2011-12') & (team_record['Team'] == 'Sacramento Kings'))]
Sacramento.sort_values('Season')


# In[1691]:


Nets = team_record.loc[((team_record['Season'] == '2009-10') & (team_record['Team'] == 'New Jersey Nets'))|((team_record['Season'] == '2010-11') & (team_record['Team'] == 'New Jersey Nets'))|
                        ((team_record['Season'] == '2011-12') & (team_record['Team'] == 'New Jersey Nets'))|((team_record['Season'] == '2012-13') & (team_record['Team'] == 'New Jersey Nets'))]
Nets.sort_values('Season')


# In[1692]:


Timberwolves = team_record.loc[((team_record['Season'] == '2010-11') & (team_record['Team'] == 'Minnesota Timberwolves'))|((team_record['Season'] == '2011-12') & (team_record['Team'] == 'Minnesota Timberwolves'))|
                               ((team_record['Season'] == '2012-13') & (team_record['Team'] == 'Minnesota Timberwolves'))|((team_record['Season'] == '2013-14') & (team_record['Team'] == 'Minnesota Timberwolves'))]
Timberwolves.sort_values('Season')


# In[1695]:


Bobcats = team_record.loc[((team_record['Season'] == '2011-12') & (team_record['Team'] == 'Charlotte Bobcats'))|((team_record['Season'] == '2012-13') & (team_record['Team'] == 'Charlotte Bobcats'))|
                          ((team_record['Season'] == '2013-14') & (team_record['Team'] == 'Charlotte Hornets'))|((team_record['Season'] == '2014-15') & (team_record['Team'] == 'Charlotte Hornets'))]
Bobcats.sort_values('Season')


# In[1699]:


Magic = team_record.loc[((team_record['Season'] == '2012-13') & (team_record['Team'] == 'Orlando Magic'))|((team_record['Season'] == '2013-14') & (team_record['Team'] == 'Orlando Magic'))|
                        ((team_record['Season'] == '2014-15') & (team_record['Team'] == 'Orlando Magic'))|((team_record['Season'] == '2015-16') & (team_record['Team'] == 'Orlando Magic'))]
Magic.sort_values('Season')


# In[1700]:


Bucks = team_record.loc[((team_record['Season'] == '2013-14') & (team_record['Team'] == 'Milwaukee Bucks'))|((team_record['Season'] == '2014-15') & (team_record['Team'] == 'Milwaukee Bucks'))|
                        ((team_record['Season'] == '2015-16') & (team_record['Team'] == 'Milwaukee Bucks'))|((team_record['Season'] == '2016-17') & (team_record['Team'] == 'Milwaukee Bucks'))]
Bucks.sort_values('Season')


# In[1701]:


Philly = team_record.loc[((team_record['Season'] == '2015-16') & (team_record['Team'] == 'Philadelphia 76ers'))|((team_record['Season'] == '2016-17') & (team_record['Team'] == 'Philadelphia 76ers'))|
                         ((team_record['Season'] == '2017-18') & (team_record['Team'] == 'Philadelphia 76ers'))]
Philly.sort_values('Season')


# In[1702]:


worst_team_year = team_record.loc[((team_record['Season'] == '2008-09') & (team_record['Team'] == 'Sacramento Kings'))|((team_record['Season'] == '2009-10') & (team_record['Team'] == 'New Jersey Nets'))|
                                 ((team_record['Season'] == '2010-11') & (team_record['Team'] == 'Minnesota Timberwolves'))|((team_record['Season'] == '2011-12') & (team_record['Team'] == 'Charlotte Bobcats'))|
                                 ((team_record['Season'] == '2012-13') & (team_record['Team'] == 'Orlando Magic'))|((team_record['Season'] == '2013-14') & (team_record['Team'] == 'Milwaukee Bucks'))|
                                 ((team_record['Season'] == '2014-15') & (team_record['Team'] == 'Minnesota Timberwolves'))|((team_record['Season'] == '2015-16') & (team_record['Team'] == 'Philadelphia 76ers'))|
                                 ((team_record['Season'] == '2016-17') & (team_record['Team'] == 'Brooklyn Nets'))]


# In[1703]:


#the worst team each year into a dataframe
worst_team_year.sort_values('Season')


# In[1634]:


team_record.set_index(['Season'], drop = True)


# In[1364]:


first_pick_teams = team_record.loc[((team_record['Season'] == '2008-09') & (team_record['Team'] == 'Los Angeles Clippers'))|((team_record['Season'] == '2009-10') & (team_record['Team'] == 'Washington Wizards'))|
                                  ((team_record['Season'] == '2010-11') & (team_record['Team'] == 'Cleveland Cavaliers'))|((team_record['Season'] == '2011-12') & (team_record['Team'] == 'New Orleans Hornets'))|
                                  ((team_record['Season'] == '2012-13') & (team_record['Team'] == 'Cleveland Cavaliers'))|((team_record['Season'] == '2013-14') & (team_record['Team'] == 'Cleveland Cavaliers'))|
                                  ((team_record['Season'] == '2014-15') & (team_record['Team'] == 'Minnesota Timberwolves'))|((team_record['Season'] == '2015-16') & (team_record['Team'] == 'Philadelphia 76ers'))|
                                  ((team_record['Season'] == '2016-17') & (team_record['Team'] == 'Brooklyn Nets'))]


# In[1365]:


#teams that won the lottery 
first_pick_teams.sort_values('Season')


# In[1400]:


#import lottery pick csv
lottery_picks = pd.read_csv('lottery-picks.csv')


# In[1401]:


lottery_picks.rename( columns={'Unnamed: 0':'nickname'}, inplace=True )


# In[1402]:


#dropping unnecessary columns
lottery_picks.drop(['college_name', 'bpm', 'vorp', 'nickname'], axis=1, inplace=True)


# In[1403]:


lottery_picks


# In[1404]:


#picks of the worst team that year
worst_team_picks = lottery_picks.loc[((lottery_picks['Year'] == 2009) & (lottery_picks['team_id'] == 'SAC'))|((lottery_picks['Year'] == 2010) & (lottery_picks['team_id'] == 'NJN'))|
                  ((lottery_picks['Year'] == 2011) & (lottery_picks['team_id'] == 'MIN'))|((lottery_picks['Year'] == 2012) & (lottery_picks['team_id'] == 'CHA'))|
                  ((lottery_picks['Year'] == 2013) & (lottery_picks['team_id'] == 'ORL'))|((lottery_picks['Year'] == 2014) & (lottery_picks['team_id'] == 'MIL'))|
                  ((lottery_picks['Year'] == 2015) & (lottery_picks['team_id'] == 'MIN'))|((lottery_picks['Year'] == 2016) & (lottery_picks['team_id'] == 'PHI'))|
                  ((lottery_picks['Year'] == 2017) & (lottery_picks['team_id'] == 'BOS'))|((lottery_picks['Year'] == 2018) & (lottery_picks['team_id'] == 'PHO'))]


# In[1405]:


worst_team_picks


# In[1406]:


worst_team_bar = worst_team_picks.plot.bar(x='Year', y='ws_per_48', rot=0)


# In[1407]:


#Get the #1 Draft pick of each year from 2009-2018 of teams that won the lottery 
lottery_picks = lottery_picks[lottery_picks['pick_overall'] == 1]
lottery_picks = lottery_picks.drop(labels=[0, 14, 28, 42, 56, 70, 84, 98, 112, 
                                           126, 140, 154, 168, 182, 336, 350], axis=0)
lottery_picks


# In[1426]:


#combine = pd.DataFrame((worst_team_picks, lottery_picks), columns=['pick_overall', 'Year', 'team_id','player','ws_per_48'])


# In[1468]:


picks = pd.concat([worst_team_picks,lottery_picks])
picks.sort_values('Year')


# In[1467]:


picks.plot.bar('player','ws')


# In[1671]:


plt.figure(figsize=(10,8))
sns.barplot(x='Year', y='ws', hue='player',data=picks)
plt.title('Comparing Players Drafted by Worst Team:Winner of Lottery')
plt.xlabel('Year')
plt.ylabel('WS')


# In[ ]:




