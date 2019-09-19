from flask import render_template
from app import app
from src import dd_GET
from src import donation_math

base_url = 'https://extra-life.donordrive.com/api/teams/'
team_ID = '44111'
participants_url = f'{base_url}{team_ID}/participants'
donations_url = f'{base_url}{team_ID}/donations'


@app.route('/')
def main():
    dd_total_donations = donation_math.get_total_donations(donations_url)
    dd_team_goal = donation_math.get_donation_goal(participants_url)
    return render_template('main.html', title = 'Main', page_title = 'Main Page', donation_total = dd_total_donations, donation_goal = dd_team_goal)

#remove later
@app.route('/events')
def all_events():
    dd_events = dd_GET.get_it('https://try.donordrive.com/api/events')
    return render_template('events.html', title = 'Events', page_title = 'All Events', events = dd_events)