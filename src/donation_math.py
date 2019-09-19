from src.dd_GET import get_it

def get_total_donations(url):
    all_donors = get_it(url)
    donation_toal = 0
    for donor in all_donors:
        donation_toal += donor['amount']
    return '${:,.2f}'.format(donation_toal)

def get_donation_goal(url):
    all_participants = get_it(url)
    donation_goal = 0
    for participant in all_participants:
        donation_goal += participant['fundraisingGoal']
    return '${:,.2f}'.format(donation_goal)