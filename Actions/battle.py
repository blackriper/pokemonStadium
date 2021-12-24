from Actions.pokemon_actions import get_pokemon_info,choose_pokemon,change_pokemon,life_bar_battle,get_min_level
from Database.pokefire import OS_CLEAN,act_player_inventory,set_pokemon_level,pokemon_health,pokemon_exp,get_one_type
from Actions.enemy import select_actions_enemy
import random,os


#asigna experiencia al terminar el combate
def assign_experience(attack_history,player_profile):
    for pokemon in attack_history:
        points= random.randint(1,5)
        pokemon["current_exp"]+=points
        pokemon_exp(player_profile["player_name"],pokemon["name"],pokemon["current_exp"])

    while pokemon["current_exp"]>20:
        pokemon["current_exp"]-=20
        pokemon["level"]+=1
        pokemon["current_health"]=pokemon["base_health"]
        set_pokemon_level(player_profile["player_name"],pokemon["level"],pokemon["current_exp"],
                                                                              pokemon["current_health"])

        print("Tu pokemon ha subido al nivel {}".format(get_pokemon_info(pokemon)))

    os.system(OS_CLEAN)



#decorador para validar si  el usuario ha escogido un ataque disponible
def error_index(func):
    def is_incorrent(*args):
        try:
            return func(*args)
        except IndexError:
            print("Ataque no valido\n")

    return is_incorrent

#retornar el daño de acuerdo al ataque escogido por el jugador
@error_index
def damage_rival(attack_player,available_attacks,name):
     os.system(OS_CLEAN)
     print(" {} ha usado {}\n".format(name,available_attacks[attack_player]["name"]))
     return available_attacks[attack_player]["damage"]



#atacar a pokemon rival
def player_attack(player_pokemon,enemy_pokemon):
    attack_damage=None
    while attack_damage==None:
        os.system(OS_CLEAN)
        print("-------------------Ataques----------------------\n")
        available_attacks=[attack for attack in player_pokemon["attacks"] if get_min_level(attack["min_level"])<= player_pokemon["level"]]
        print("|***********************************************|")
        for index in range(len(available_attacks)):
            print("{}.- {}".format(index,available_attacks[index]["name"]))
        print("|***********************************************|")
        attack_player_pokemon= int(input("¿Que ataque deseas realizar? "))
        attack_damage=damage_rival(attack_player_pokemon,available_attacks,player_pokemon["name"])
        enemy_pokemon["current_health"]-=attack_damage
        if enemy_pokemon["current_health"] < 0: enemy_pokemon["current_health"] = 0
        life_bar_battle(enemy_pokemon["name"],enemy_pokemon["current_health"],enemy_pokemon["base_health"])
        life_bar_battle(player_pokemon["name"], player_pokemon["current_health"], player_pokemon["base_health"])
        input("Enter para continuar....\n\n")
        os.system(OS_CLEAN)




#curar pokemon
def cure_pokemon(player_pokemon,player_profile,enemy_pokemon):
    if player_profile["health_potion"]>0:
        if player_pokemon["current_health"]<100:
            print(f"{player_profile['player_name']} ha usado una pocion")
            player_pokemon["current_health"]+=50
            if player_pokemon["current_health"] > 100:player_pokemon["current_health"]=100
            pokemon_health(player_profile["player_name"],player_pokemon["name"],player_pokemon["current_health"])
            player_profile["health_potion"]-= 1
            rest=player_profile["health_potion"]
            act_player_inventory(player_profile["player_name"], 'health_potion',rest)
            print(f"{player_pokemon['name']} se ha recuperado")
            os.system(OS_CLEAN)
            life_bar_battle(enemy_pokemon["name"], enemy_pokemon["current_health"], enemy_pokemon["base_health"])
            life_bar_battle(player_pokemon["name"], player_pokemon["current_health"], player_pokemon["base_health"])
        else:
            print(f"{player_pokemon['name']} ya tiene su salud al maximo")
    else:
        print("No hay pociones disponible ve a la poketienda para comprar algunas\n")

    input("Enter para continuar....\n\n")
    os.system(OS_CLEAN)




#determinar el ganador del encuentro
def who_win_combat(enemy_pokemon,player_pokemon,player_profile,attack_history):
    if enemy_pokemon["current_health"] == 0:
        print(f"{player_pokemon['name']} ha sido el ganador\n")
        assign_experience(attack_history, player_profile)
        player_profile["victories"] += 1
        act_player_inventory(player_profile["player_name"], "victories", player_profile["victories"])
        money = random.randint(20, 1000)
        player_profile["money"] += money
        act_player_inventory(player_profile["player_name"], "money", player_profile["money"])

    else:
        print(f"{enemy_pokemon['name']} enemigo ha sido el ganador\n")
        assign_experience(attack_history, player_profile)
        money = random.randint(10,500)
        player_profile["money"] += money
        act_player_inventory(player_profile["player_name"], "money", player_profile["money"])
        player_profile["defeats"] += 1
        act_player_inventory(player_profile["player_name"], "defeats", player_profile["defeats"])


#empieza el combate
def fight(player_profile,enemy_pokemon,list_pokemon,list_pokemon_enemy,potions):
    print("-----------------NUEVO COMBATE-------------------\n")
    attack_history = []
    player_pokemon = choose_pokemon(player_profile)
    os.system(OS_CLEAN)
    print("Contricantes: {} VS {}\n".format(get_pokemon_info(player_pokemon),
                                          get_pokemon_info(enemy_pokemon)))


    while player_pokemon["current_health"]>0 and enemy_pokemon["current_health"] > 0 :
        action = None

        while action not in ["A", "P", "C"]:
            action = input("¿Que Deseas hacer?: [A]tacar, [P]ocion, [C]ambiar pokemon ")
            if action == "A":
                player_attack(player_pokemon, enemy_pokemon)
                attack_history.append(player_pokemon)
                new_enemy=select_actions_enemy(enemy_pokemon,player_pokemon,player_profile["player_name"],list_pokemon,potions)
                if new_enemy!=None: enemy_pokemon=new_enemy

            elif action == "P":
                cure_pokemon(player_pokemon,player_profile,enemy_pokemon)

            elif action == "C":
                player_pokemon=change_pokemon(player_profile,player_pokemon)



    print("---FIN DEL COMBATE---\n")
    who_win_combat(enemy_pokemon,player_pokemon,player_profile,attack_history)
    player_profile["combats"]+=1
    act_player_inventory(player_profile["player_name"],"combats", player_profile["combats"])





