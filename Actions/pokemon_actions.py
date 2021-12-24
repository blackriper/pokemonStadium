import os
from Database.pokefire import OS_CLEAN

SIZE_BAR_LIFE=20


#estetica para mostrar los pokemon a enfrentarse
def get_pokemon_info(pokemon):
    return " {}  |  lvl {}  |  hp {}/{}".format(pokemon["name"],
                                                pokemon["level"],
                                                pokemon["current_health"],
                                                pokemon["base_health"])


#escoger los pokemon con los que peleara el usuario
def choose_pokemon(player_profile):
    chosen=None
    while not chosen:
        print("Elige con que pokemon lucharas\n")
        print("|***********************************************|")
        for index in range(len(player_profile["pokemon_inventory"])):
            print(" {}.- {}".format(index,get_pokemon_info(player_profile["pokemon_inventory"][index])))
        print("|***********************************************|")
        try:
          ind=int(input("¿Cuál eliges? "))
          if player_profile["pokemon_inventory"][ind]["current_health"]>0:
           return player_profile["pokemon_inventory"][ind]
          else:
            print(f"{player_profile['pokemon_inventory'][ind]['name']} se encuentra debilitado")
            os.system(OS_CLEAN)
        except (ValueError,IndexError):
             print("opcion invalida")



#cambiar pokemon combatiente
def change_pokemon(player_profile,player_pokemon):
    print(f"{player_pokemon['name']} regresa")
    player_pokemon=choose_pokemon(player_profile)
    print("Ve {}".format(player_pokemon["name"]))
    return player_pokemon






#calcular barra de vida del combate
def life_bar_battle(name,current_life,pokemon_life):

    bar_life = int(current_life * SIZE_BAR_LIFE / pokemon_life)
    print("{}:  [{} {}] ({}/{})\n".format(name,"*" * bar_life,
                                               "" * (SIZE_BAR_LIFE - bar_life),
                                               current_life, pokemon_life))




#asignar un nivel a un ataque que no cuenta con un dato de nivel minimo
def get_min_level(level):
    if level=='':
        return 5
    else:
        return int(level)