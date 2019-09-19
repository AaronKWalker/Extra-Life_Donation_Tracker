from dd_GET import get_it_testing, get_it
import donation_math

events_url = 'https://extra-life.donordrive.com/api/events'
team_url = 'https://extra-life.donordrive.com/api/teams/44111'
participants_url = 'https://extra-life.donordrive.com/api/teams/44111/participants'
donation_url = 'https://extra-life.donordrive.com/api/teams/44111/donations'

# get_it_testing(events_url)
# get_it_testing(team_url, 'TEAM', 'dict')
# get_it_testing(participants_url, 'PARTICIPANTS', 'dict')

donation_goal = donation_math.get_donation_goal(participants_url)
print(donation_goal)

total_donations = donation_math.get_total_donations(donation_url)
print(total_donations)