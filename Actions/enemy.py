from Database.pokefire import OS_CLEAN,pokemon_health
from Actions.pokemon_actions import get_min_level,life_bar_battle
import os,random


#ataque del enemigo
def enemy_attack(player_pokemon,enemy_pokemon,name):
    os.system(OS_CLEAN)
    available_attacks = [attack for attack in enemy_pokemon["attacks"] if get_min_level(attack["min_level"]) <= enemy_pokemon["level"]]
    attack_enemy=random.choice(available_attacks)
    print(" {}  enemmigo ha usado {}\n".format(enemy_pokemon["name"],attack_enemy["name"]))
    player_pokemon["current_health"] -= attack_enemy["damage"]
    if player_pokemon["current_health"]<0: player_pokemon["current_health"]=0
    pokemon_health(name,player_pokemon["name"],player_pokemon["current_health"])
    life_bar_battle(enemy_pokemon["name"], enemy_pokemon["current_health"], enemy_pokemon["base_health"])
    life_bar_battle(player_pokemon["name"], player_pokemon["current_health"], player_pokemon["base_health"])
    input("Enter para continuar....\n\n")
    os.system(OS_CLEAN)


#curar pokemon
def cure_pokemon_enemy(enemy_pokemon,player_pokemon,potions):
      if potions>0:
        print("Entrenador enemigo ha usado una pocion")
        enemy_pokemon["current_health"] += 50
        if enemy_pokemon["current_health"] > 100: enemy_pokemon["current_health"]=100
        potions-=1
        print(f"{enemy_pokemon['name']} se ha recuperado\n")
        life_bar_battle(enemy_pokemon["name"], enemy_pokemon["current_health"], enemy_pokemon["base_health"])
        life_bar_battle(player_pokemon["name"], player_pokemon["current_health"], player_pokemon["base_health"])

      input("Enter para continuar....\n\n")
      return potions

#cambiar pokemon
def change_pokemon(enemy_pokemon,list_pokemon):
    if enemy_pokemon["current_health"]>0:
        print(f"{enemy_pokemon['name']} regresa")
        enemy_pokemon=random.choice(list_pokemon)
        print(f"Ve {enemy_pokemon['name']}")
    return enemy_pokemon

#selecciona al azar las acciones del entrendor enemigo
def select_actions_enemy(enemy_pokemon,player_pokemon,name,list_pokemon_enemy,potions):

    list_actions=['cure','attack','change']
    action=random.choice(list_actions)

    if action=="cure":
         cure_pokemon_enemy(enemy_pokemon,player_pokemon,potions)
         os.system(OS_CLEAN)

    elif action=="attack":
        enemy_attack(player_pokemon,enemy_pokemon,name)

    elif action=="change":
       new_enemy= change_pokemon(enemy_pokemon,list_pokemon_enemy)
       return new_enemy


