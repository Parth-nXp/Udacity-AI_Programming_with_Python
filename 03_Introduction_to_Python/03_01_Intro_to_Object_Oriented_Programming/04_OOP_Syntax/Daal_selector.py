import random

dal = ['Moong Dhuli', 'Moong Chilka', 'Moong Sabut', 'Urad Dhuli', 'Urad Chilka', 'Urad Sabut', 'Arhar',
        'Channa', 'Rajmah', 'Black channa', 'White Channa', 'Urad Rajmah', 'Urad channa']

schedule = []

for i in range(100):
    new_dal = random.choice(dal)
    if new_dal not in schedule:
        schedule.append(new_dal)

print(schedule)