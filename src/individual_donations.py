from src.dd_GET import get_it

def ind_don(tp, base):
    participants = get_it(tp)
    team_participants_info = []
    for participant in participants:
        information = {
            'name': participant['displayName'],
            'donation_goal': participant['fundraisingGoal'],
            'num_donations': participant['numDonations'],
            'donation_total': participant['sumDonations'],
            'pledges_total': participant['sumPledges'],
            'participant_id': participant['participantID']
        }
        team_participants_info.append(information)
    
    individual_participant_donations = []
    for part in team_participants_info:
        info = get_it(f'{base}/participants/{part["participant_id"]}/donations')
        if len(info) >0:
            for i in info:
                if i.get('displayName', 'noDisplayName') == 'noDisplayName':
                    i.update({'displayName': 'Unknown'})
                i.update({'d_amount': '${:,.2f}'.format(i['amount'])})
            info.insert(0, part['name'])
            individual_participant_donations.append(info)
    return individual_participant_donations