import numpy as np
import pandas as pd


df = pd.read_csv('mls-salaries-2017.csv')


def team_report(team_name, df):
    team_df=df[df['club'] == team_name]
    
    if team_df.empty: 
        return {
            "team_name": team_name,
            "total_salary": 0,
            "average_salary": 0,
            "players_count": 0,
            "max_salary": 0,
            "min_salary": 0,
            "max_player_first_name": "",
            "max_player_last_name": "",
            "min_player_first_name": "",
            "min_player_last_name": ""
        }
    
    team_name = team_df['club'].values[0]
    total_salary = team_df['base_salary'].sum()
    average_salary = team_df['base_salary'].mean()
    players_count = team_df['base_salary'].count()
    max_salary = team_df['base_salary'].max()
    max_player = team_df[team_df['base_salary'] == max_salary]
    max_player_first_name = max_player['first_name'].values[0]  
    max_player_last_name = max_player['last_name'].values[0]
    min_salary = team_df['base_salary'].min()
    min_salary_player = team_df[team_df['base_salary'] == min_salary]
    min_player_first_name = min_salary_player['first_name'].values[0]   
    min_player_last_name = min_salary_player['last_name'].values[0]
    
    
       
    return {
        "team_name": team_name,
        "total_salary": total_salary, 
        "average_salary": average_salary,
        "players_count": players_count,
        "max_salary": max_salary,
        "min_salary": min_salary,
        "max_player_first_name": max_player_first_name,
        "max_player_last_name": max_player_last_name,
        "min_player_first_name": min_player_first_name,
        "min_player_last_name": min_player_last_name
        
    }




# Finding the player with the highest base salary
max_salary = df['base_salary'].max()
max_player=df[df['base_salary'] == max_salary]
max_player_club = max_player['club'].values[0]
max_player_first_name = max_player['first_name'].values[0]
max_player_last_name = max_player['last_name'].values[0]
max_player_position = max_player['position'].values[0]
max_player_base_salary = max_player['base_salary'].values[0]

# Finding the player with the lowest base salary
min_salary = df['base_salary'].min()
min_player=df[df['base_salary'] == min_salary]
min_player_club = min_player['club'].values[0]
min_player_first_name = min_player['first_name'].values[0]
min_player_last_name = min_player['last_name'].values[0]
min_player_position = min_player['position'].values[0]
min_player_base_salary = min_player['base_salary'].values[0]


teams = df['club'].unique()




with open('mls-salaries.txt', 'w') as file:
    file.write("MLS Salaries Analysis\n")
    file.write("=====================\n\n")
    file.write("Highest Paid Player:\n")
    file.write(f"Player: {max_player_first_name} {max_player_last_name}\n")
    file.write(f"Club: {max_player_club}\n")
    file.write(f"Maximum Salary: ${max_salary}\n")
    file.write(f"Position: {max_player_position}\n")
    
    file.write("\nLowest Paid Player:\n")
    file.write(f"Player: {min_player_first_name} {min_player_last_name}\n")
    file.write(f"Club: {min_player_club}\n")
    file.write(f"Minimum Salary: ${min_salary}\n")
    file.write(f"Position: {min_player_position}\n")
    
    file.write("\nThe gap between the highest and lowest salaries is: ${}\n".format(max_salary - min_salary))
    
    file.write("\nTeams in the MLS:\n")
    for team in teams:
        report=team_report(team, df)
        if report['players_count'] == 0:
            continue    
        
        file.write(f"\nTeam: {report['team_name']}\n")
        file.write(f"Total Salary: ${report['total_salary']}\n")
        file.write(f"Average Salary: ${report['average_salary']:.2f}\n")
        file.write(f"Number of Players: {report['players_count']}\n")
        file.write(f"Maximun Paid Player: {report['max_player_first_name']} {report['max_player_last_name']} ${report['max_salary']}\n")
        file.write(f"Minimum Paid Player: {report['min_player_first_name']} {report['min_player_last_name']} ${report['min_salary']}\n")
        file.write(f"Salary Gap: ${report['max_salary'] - report['min_salary']}\n")
        file.write("=====================\n") 
        
    


