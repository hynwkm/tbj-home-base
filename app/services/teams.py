from .players import parse_player
from .stats_api import fetch_stats_api


def get_teams():
    data = fetch_stats_api("/teams", {"sportId": "1"})
    return data.get("teams", [])


def get_team_lookup():
    teams = get_teams()

    return {
        team["id"]: {
            "team_id": team["id"],
            "abbreviation": team["abbreviation"],
            "name": team["teamName"],
            "full_name": team["name"],
        }
        for team in teams
    }


def get_team_roster_stats(team_id):
    data = fetch_stats_api(
        f"/teams/{team_id}/roster/Active",
        {"hydrate": "person(stats(type=season))"},
    )
    roster = data.get("roster", [])

    roster_stats = [parse_player(player) for player in roster]

    hitters = [player for player in roster_stats if not player["is_pitcher"]]
    pitchers = [player for player in roster_stats if player["is_pitcher"]]

    return {
        "hitters": hitters,
        "pitchers": pitchers,
    }


# http://statsapi.mlb.com/api/v1/people/592450?hydrate=stats(type=[yearByYear,yearByYearAdvanced,projected,career]),team,currentTeam

# response
# pitcher or hitter
# pos abb
# jersery number
# player id
# player last name
# player first name
# age
# height
# weight
# SO% - strikeout percentage = SO / PA or SO / BF
# BB% - walk percentage = BB / PA  or BB / BF
# OPS - on base plus slugging
# drafted year
# B - bats left or right
# T - throws left or right
# PA - plate appearances
# H - hits
# R - runs
# 2B - doubles
# 3B - triples
# HR - home runs
# SB - stolen bases
# AVG - batting average
# OBP - on base percentage
# SLG - slugging percentage
# BABIP - batting average on balls in play
# G - games
# IP - innings pitched
# BF - batters faced
# ERA - earned run average
# SO - strikeouts
# BB - base on balls
# CS - caught stealing
