from flask import render_template
from app import app
from src import dd_GET
from src import donation_math
from src import individual_donations

base_url = 'https://extra-life.donordrive.com/api/'
team_ID = '44111'
team_participants_url = f'{base_url}/teams/{team_ID}/participants'
donations_url = f'{base_url}/teams/{team_ID}/donations'


@app.route('/')
def main():
    dd_total_donations = donation_math.get_total_donations(donations_url)
    dd_total_donations_int = donation_math.get_total_donations_int(donations_url)
    print(dd_total_donations_int)
    dd_team_goal = donation_math.get_donation_goal(team_participants_url)
    dd_team_goal_int = donation_math.get_donation_goal_int(team_participants_url)
    print(dd_team_goal_int)
    dd_donation_breakdown = individual_donations.ind_don(team_participants_url, base_url)
    print(dd_total_donations_int / dd_team_goal_int)
    return render_template(
        'main.html', title = 'Main', 
        page_title = 'Main Page', 
        donation_total = dd_total_donations,
        donation_total_int = dd_total_donations_int, 
        donation_goal = dd_team_goal,
        donation_goal_int = dd_team_goal_int, 
        participants = dd_donation_breakdown,)
