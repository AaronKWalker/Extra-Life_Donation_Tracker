from src.dd_GET import get_it

def get_total_donations(url):
    all_donors = get_it(url)
    donation_total = 0
    for donor in all_donors:
        donation_total += donor['amount']
    return '${:,.2f}'.format(donation_total)

def get_donation_goal(url):
    all_participants = get_it(url)
    donation_goal = 0
    for participant in all_participants:
        donation_goal += participant['fundraisingGoal']
    return '${:,.2f}'.format(donation_goal)

def get_total_donations_int(url):
    all_donors = get_it(url)
    donation_total_int = 0
    for donor in all_donors:
        donation_total_int += donor['amount']
    return round(donation_total_int, 2)

def get_donation_goal_int(url):
    all_participants = get_it(url)
    donation_goal_int = 0
    for participant in all_participants:
        donation_goal_int += participant['fundraisingGoal']
    return round(donation_goal_int, 2)