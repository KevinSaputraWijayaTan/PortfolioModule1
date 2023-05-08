import random

# Define the teams by continent
africa = ['Morocco', 'Senegal', 'Tunisia', 'Algeria', 'Egypt', 'Nigeria', 'Cameroon', 'Ivory Coast', 'Burkina Faso', 'Mali']
asia = ['Japan', 'IR Iran', 'Korea Republic', 'Australia', 'Saudi Arabia', 'Qatar', 'Iraq', 'UAE']
europe = ['France', 'Belgium', 'England', 'Netherlands', 'Croatia', 'Italy', 'Portugal', 'Spain', 'Switzerland', 'Germany', 'Denmark', 'Sweden', 'Poland', 'Serbia', 'Wales', 'Ukraine']
north_america = ['United States', 'Mexico', 'Costa Rica', 'Canada', 'Panama', 'Jamaica']
south_america = ['Argentina', 'Brazil', 'Uruguay', 'Colombia', 'Peru', 'Chile', 'Ecuador']
oceania = ['New Zealand']

# Combine all teams
teams = africa + asia + europe + north_america + south_america + oceania

# Define the groups
groups = ["Group A", "Group B", "Group C", "Group D", "Group E", "Group F", "Group G", "Group H", "Group I", "Group J", "Group K", "Group L"]

# Shuffle the teams
random.shuffle(teams)

# Perform the group stage drawing and check the continent for each team
group_stage = {}
europe_teams_drawn = 0
for group in groups:
    group_stage[group] = []
    for i in range(4):
        while True:
            if len(teams) > 0:
                team = teams.pop(0)
            if team in europe:
                if europe_teams_drawn < 2:
                    group_stage[group].append(team)
                    europe_teams_drawn += 1
                    break
            else:
                if not any([team in group_stage[group] for group in group_stage]) and all([len([team for team in group_stage[group] if team in continent]) < 2 for continent in [africa, asia, europe, north_america, south_america, oceania]]):
                    group_stage[group].append(team)
                    break

# Print the group stage
for group in group_stage:
    print(group)
    print("-" * 10)
    for team in group_stage[group]:
        print(team)
    print()