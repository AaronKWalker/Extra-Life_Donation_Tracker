from dd_GET import get_it_testing, get_it
import donation_math
import pprint
pp = pprint.PrettyPrinter(indent=4)

events_url = 'https://extra-life.donordrive.com/api/events'
team_url = 'https://extra-life.donordrive.com/api/teams/44111'
team_participants_url = 'https://extra-life.donordrive.com/api/teams/44111/participants'
donation_url = 'https://extra-life.donordrive.com/api/teams/44111/donations'
participant_url = 'https://extra-life.donordrive.com/api/participants/'

# get_it_testing(events_url)
# get_it_testing(team_url, 'TEAM', 'dict')
# get_it_testing(participants_url, 'PARTICIPANTS', 'dict')

# donation_goal = donation_math.get_donation_goal(participants_url)
# print(donation_goal)
# total_donations = donation_math.get_total_donations(donation_url)
# print(total_donations)

def indivudual_donation_status(tp=None, ip=None):
    participants = get_it_testing(tp, 'PARTICIPANTS', 'list')
    team_participants_info = []
    for participant in participants:
        info = {
            'name': participant['displayName'],
            'donation_goal': participant['fundraisingGoal'],
            'num_donations': participant['numDonations'],
            'donation_total': participant['sumDonations'],
            'pledges_total': participant['sumPledges'],
            'participant_id': participant['participantID']
        }
        team_participants_info.append(info)
    print('\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    pp.pprint(team_participants_info)
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n')

    participant_donations = []
    for participant in team_participants_info:
        info = get_it_testing(f'{ip}{participant["participant_id"]}/donations', 'DONATIONS', 'list')
        if len(info) > 0:
            for i in info:
                if i.get('displayName', 'Unknown') == 'Unknown':
                    i.update({'displayName': 'Unknown'})
            info.insert(0, participant['name'])
            participant_donations.append(info)
    print('\n????????????????????????????????????????????????????????????????????????')
    pp.pprint(participant_donations)

indivudual_donation_status(team_participants_url, participant_url)
