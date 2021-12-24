from Database.pokefire import OS_CLEAN
from Models.User import view_inventory_player
from Actions.battle import fight
from Actions.store import store_pokemon
import os,random

#inicia una batalla pokemon
def confrontation(player_profile, pokemon_list):
    con=None
    while con!="N" :
        list_pokemon_enemy = [random.choice(pokemon_list) for p in range(4)]
        potions = random.randint(0, 5)
        enemy_pokemon = random.choice(list_pokemon_enemy)
        fight(player_profile, enemy_pokemon,pokemon_list,list_pokemon_enemy,potions)
        con = input("Deseas seguir combatiendo S/N \n")


#muestra menu de la tienda
def poketienda(player_profile,pokemon_list):
    store_pokemon(player_profile,pokemon_list)



#muestra  el historial de batallas del usuario
def record_user(player_profile):
    print("Combates: {} ----Victorias: {} ---- Derrotas: {} ".format(player_profile["combats"],
                                                                     player_profile["victories"],
                                                                     player_profile["defeats"]))


#cierra la sesion del usuario y la aplicacion
def close_session():
    print("Cerrando sesion ....")
    exit()



#menu principal de acciones del usuario
def menu_player(player_profile,pokemon_list):
    os.system(OS_CLEAN)
    while True:
        print("\n")
        print("|***********************************************|")
        print("|**|           Bienvenido                    |**|")
        print("|**|              Menu                       |**|")
        print("|***********************************************|")
        print("Seleccione una de las siguientes opciones:");
        print("1.- Batalla en Stadium")
        print("2.- Historial de combates")
        print("3.- Inventario")
        print("4.- Poketienda")
        print("5.- Cerrar sesion\n")

        opcion = int(input("Opcion: "))

        if opcion==1:
            os.system(OS_CLEAN)
            confrontation(player_profile,pokemon_list)
        elif opcion==2:
            os.system(OS_CLEAN)
            record_user(player_profile)
        elif opcion==3:
            os.system(OS_CLEAN)
            view_inventory_player(player_profile)
        elif opcion==4:
            os.system(OS_CLEAN)
            poketienda(player_profile,pokemon_list)
        elif opcion==5:
            os.system(OS_CLEAN)
            close_session()