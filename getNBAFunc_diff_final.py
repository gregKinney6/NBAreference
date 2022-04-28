from cmath import log

from turtle import home

import requests

from bs4 import BeautifulSoup

import pandas as pd

import math

import random

from numpy import mean



# Teams Abbreviations for collecting Data

# ATL, BOS, CHO, CHI, CLE, DAL, DEN, DET, GSW, HOU, IND, LAC, LAL, MEM, MIA

# MIL, MIN, NOP, NYK, BRK, OKC, ORL, PHI, PHO, POR, SAC, TOR, UTA, WAS



#Stat abbreviations that can be accessed from getRecord()

#stats = ['Wins', 'Losses', 'Away Wins', 'Away Losses', 'Home Wins', 

# 'Home Losses', 'Streak Wins', 'Streak Losses']



#Stats abbreviations from getTeamData()

#['Unnamed: 0', 'G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'FT', 'FTA', 

# 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']



#setting a list of all teams

team_list = ['ATL', 'BOS', 'CHO', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'BRK', 'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']



#function for getting the team records

#call the function into a variable

#I.E. teamRecords = getRecord()

#teamRecords is now a dict of dict. teamRecords has keys of each team with the abbreviations from team_list

#each value in teamRecords is a dict with keys from the stats variable

#Example to grab Portland 'POR' home win values

#teamRecords = getRecord()

#portlandHomeWins = teamRecords['POR']['Home Wins']

def getRecord():

    #stats list for the list of stats that will be returned

    stats = ['Wins', 'Losses', 'Away Wins', 'Away Losses', 'Home Wins', 'Home Losses', 'Streak Wins', 'Streak Losses']



    #url to get to the team schedule table

    url_team_rec = "https://www.basketball-reference.com/teams/{}/2022_games.html#games_link"



    #initializing the team records dict

    team_records = {}



    #for loop to run through each team

    for team in team_list:

        #initializing dict for current team

        current_team = {}



        #formatting the url to make sure we go to the correct teams site

        url = url_team_rec.format(team)



        #b/c the table is recognized in html, using pandas to grab the data

        #need '[0]' at the end in order for it to be a dict

        table = pd.read_html(url, match = 'Regular Season')[0]



        #printing that the function is running

        update = 'Fetching team records for {}'.format(team)

        print(update)



        #initializing each stat

        away_wins = 0

        away_games = 0

        home_wins = 0

        home_games = 0

        total_wins = 0

        total_games = 0

        streak_wins = 0

        streak_losses = 0



        #for loop counting each stat

        for row in range(len(table)):

            #checking if the row is a game or a header, if game, count total game

            if table['G'][row] != 'G':

                total_games += 1

                #if it is one of the last 10 games, start collecting streak data

                if float(table['G'][row]) >= 73:

                    if table['Unnamed: 7'][row] == 'W':

                        streak_wins += 1

                    else:

                        streak_losses += 1



                #checking if away game win/loss

                if table['Unnamed: 5'][row] == '@':

                    away_games += 1

                    if table['Unnamed: 7'][row] == 'W':

                        away_wins += 1

                        total_wins += 1

                #otherwise it is a home game

                else:

                    home_games += 1

                    if table['Unnamed: 7'][row] == 'W':

                        home_wins += 1

                        total_wins += 1



        #calculating losses off of the totals and wins

        total_losses = total_games - total_wins

        away_losses = away_games - away_wins

        home_losses = home_games - home_wins

    

        #stats = ['Wins', 'Losses', 'Away Wins', 'Away Losses', 'Home Wins', 'Home Losses', 'Streak Wins', 'Streak Losses']

        input = [total_wins, total_losses, away_wins, away_losses, home_wins, home_losses, streak_wins, streak_losses]



        #using input to make input into dict

        for x in range(len(stats)):

            current_team[stats[x]] = input[x]



        team_records[team] = current_team

    #returns a dict of the team record

    return team_records



#team 1 is home team, team 2 is away team

def game_probability(home_team, away_team):

    teams = getRecord()

    home = teams.get(home_team)

    away = teams.get(away_team)

    home_total_games = home['Home Wins'] + home['Home Losses']

    away_total_games = away['Away Wins'] + away['Away Losses']

    home_win_perc = home['Home Wins'] / home_total_games

    away_win_perc = away['Away Wins'] / away_total_games

    home_total_win_perc = home['Wins'] / (home['Wins'] + home['Losses'])

    away_total_win_perc = away['Wins'] / (away['Wins'] + away['Losses'])

    home_streak_perc = home['Streak Wins'] / (home['Streak Wins'] + home['Streak Losses'])

    away_streak_perc = away['Streak Wins'] / (away['Streak Wins'] + away['Streak Losses'])



    return 0.6 * prob_helper(home_win_perc, away_win_perc) + 0.3 * prob_helper(home_total_win_perc, away_total_win_perc) + 0.1 * prob_helper(home_streak_perc, away_streak_perc)



def prob_helper(perc1, perc2):

    return (perc1 - (perc1 * perc2)) / (perc1 + (perc2 - (2 * perc1 * perc2)))



def sim_game(team_1, team_2, series_len):

    series_games = []

    win_perc = game_probability(team_1, team_2)

    series_threshold = series_len / 2

    series = [0, 0]

    num_games = 0

    for i in range(series_len):

        game = random.uniform(0.0, 1.0)

        if game <= win_perc:

            series[0] += 1

            series_games.append(team_1)

            print(team_1 + ' wins game ' + str(i + 1))

            if(series[0] > series_threshold):
                
                num_games = i + 1

                break

        else:

            series[1] += 1

            series_games.append(team_2)

            print(team_2 + ' wins game ' + str(i + 1))

            if(series[1] > series_threshold):

                num_games = i + 1

                break

    if series[0] > series[1]:

        return team_1, num_games, series_games

    else:

        return team_2, num_games, series_games



#Function to get data per game for each team over the 2022 season

#call the function into a variable

#I.E. teamData = getTeamData()

#teamData is now a dict of dict. teamData has keys of each team with the abbreviations from team_list

#each value in teamData is a dict with keys from the stats comment above

#Example to grab Portland 'POR' 3-point FG %

#teamPortland = getTeamData()

#portlandThreePerc = teamRecords['POR']['3P%']

def getTeamData():

    #initializng url for team data

    url_team = "https://www.basketball-reference.com/teams/{}/2022.html"



    #initializing dict for them to go into

    all_teams = {}



    for team in team_list:

        #setting url to a certain team

        url = url_team.format(team)

        

        #printing that its working

        update = 'Fetching team data for {}'.format(team)

        print(update)



        #requesting the url, grabbing html, turning to text, and parsing

        s = requests.get(url)

        s_html = s.text

        stats_soup = BeautifulSoup(s_html, "html.parser")



        #Searching object and for team stats

        stats_tables = stats_soup.find(id='all_team_and_opponent')

        

        #finds a table that is not recognized as a table by BS4

        #Turn to string, make a BS object with parsing, search through

        #for the table that can now be recognized

        table_text = str(stats_tables.contents)

        table_soup = BeautifulSoup(table_text,'html.parser')

        team_stats_table = table_soup.find(id='team_and_opponent')



        #taking data and using pandas to read for the table

        stats = pd.read_html(str(team_stats_table))[0]

        

        #setting up empty dict for the team stats

        teamPerGame = {}



        #for each stat, enter it into the dict for the current team

        for key in stats.keys():

            teamPerGame[key]= stats[key][1]



        #add the current team to the overall dict with the key being the current team

        all_teams[team] = teamPerGame

    #Code I added to grab the NBA Averages

    avg_nba = {}



    for key in stats.keys():

        if key == 'Unnamed: 0' or key == 'G':

            avg_nba[key] = '0F'

        else:

            stat_avg = []

            for team in team_list:

                stat_avg.append(float(all_teams[team][key]))

            avg_nba[key] = round(mean(stat_avg), 2)



    all_teams['NBA'] = avg_nba



    return all_teams



#Function takes in the dict returned from the getTeamData() function and the abbreviation of the team

#Returns a list of the 5 stats we want to display in the GUI

#[Field Goal %, 3 Point %, Free Throw %, Turnovers per game, Points Per Game]

def getTeamStats(data, abbr):

    showList = [data[abbr]['FG%'], data[abbr]['3P%'], data[abbr]['FT%'], data[abbr]['TOV'], data[abbr]['PTS']]

    return showList





#teamData = getTeamData()

#teamRecords = getRecord()



#print(teamData['POR']['3P%'])

#print(teamRecords['POR']['Wins'])

#print(teamRecords['POR']['Losses'])



#showing = getTeamStats(teamData,'NBA')



#print(showing)

#print(sim_game('HOU', 'GSW', 7) + ' wins the series!')

