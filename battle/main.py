from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
        {"name": "Thunder", "cost": 10, "dmg": 124},
        {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("====================================")
    player.choose_action()
    choice = input("Choose action: ")
    print()
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")
    
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("\nChoose magic: ")) - 1

        dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost =player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        '''
        Generate cost of spell damage
        '''
        if(cost > current_mp):
            print(bcolors.FAIL + "Not enough MP" + bcolors.ENDC + "\n")
            continue

        player.reduce_mp(cost)
        
        '''
        Generate spell damage
        '''
        enemy.take_damage(dmg)
        print(bcolors.OKBLUE + spell, "deals", str(dmg) + " points of damage" + bcolors.ENDC + "\n")

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)

    print("Enemy attacks for", enemy_dmg)

    print("====================================")
    print("Enemy HP: " + bcolors.FAIL + str(enemy.get_hp()) + " / " + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    print("Your HP: " + bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP: " + bcolors.OKBLUE + str (player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win" + bcolors.ENDC)

        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        
        running = False