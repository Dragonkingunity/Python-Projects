import random

#Players stats
starting_stats = [1, 2, 3]

#Enemy and stats
enemy_stats = [1, 2]

playing = True

stats = 'Magic,' 'Strength,' 'Ranged'

enemies = 'Mage', 'Ranger', 'Fighter'



name = input('Whats your characters name?')

print(f'Hello {name} welcome to the game\n')

#Player stats
strength_stat = random.choice(starting_stats)
magic_stat = random.choice(starting_stats)
ranged_stat = random.choice(starting_stats)

#Enemy stats
mage_power = random.choice(enemy_stats)
fighter_power = random.choice(enemy_stats)
ranger_power = random.choice(enemy_stats)

print('The match ups are below learn them.', '\nMagic > Strength \nStrength > Ranged \nRanged > Magic\n')

print('Your starting stats are as follows', f'\nStrength: {strength_stat}\nMagic: {magic_stat}\nRanged: {ranged_stat}\n')

while playing:
    stat_choice = None
    fight_choice = None

    print('These are the enemy stats.', f'\nMage stats: {mage_power}\nFighter stats: {fighter_power}\nRanger stats: {ranger_power}')

    while stat_choice not in stats:
        stat_choice = input('\nWhat stat are you using to fight?').capitalize()

    while fight_choice not in enemies:
        fight_choice = input('\nWho are you fighting?').capitalize()



    #print(fight_choice)

    if fight_choice == 'Ranger' and stat_choice == 'Strength':
        fight = strength_stat - ranger_power
        print(fight)








