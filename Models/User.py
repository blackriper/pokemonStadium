
#estetica para mostrar los tipos de pokemon
def view_types(pokemon):
    if len(pokemon["type"])>1:
        return f"{pokemon['type'][0]}-{pokemon['type'][1]}"
    else:
        return f"{pokemon['type'][0]}"


# estetica para mostrar el perfil de los pokemon iniciales
def pokemon_inicial(pokemon):
    return f"""    {pokemon["name"]}       {pokemon["level"]}       {view_types(pokemon)}\n"""


#obtener el diccionario usuario para guardarlo en firebase
def getUser(name_player,pokemon_inventory):
   return {
       "player_name": name_player,
       "pokemon_inventory":pokemon_inventory,
       "combats":0,
       "victories":0,
       "defeats":0,
       "pokeballs":0,
       "health_potion":0,
       "money":500
   }


#Mostrar perfil inicial al crearse el usuario
def view_profile(player:dict):

    player_name=player["player_name"]
    money=player["money"]
    pokeballs=player["pokeballs"]
    health_potion=player["health_potion"]
    pokemon_inventory=player["pokemon_inventory"]

    print("***************************************")
    print(f"       Bienvenido {player_name}      ")
    print("***************************************\n")
    print(f"Dinero disponible {money}\n")
    print(f"Pokeballs disponibles {pokeballs}\n")
    print(f"Pociones disponibles {health_potion}\n")
    print("****************************************")
    print("      Tus pokemon Iniciales             ")
    print("****************************************")
    print("  nombre      |    lv   |     Tipo      |\n")
    for index in range(len(pokemon_inventory)):
        print(pokemon_inicial(pokemon_inventory[index]))

    print("*****************************************\n")
    print("Te recomendamos pasar a la poketienda antes de combatir\n")


#Mostrar inventario del jugador
def view_inventory_player(player:dict):
    player_name = player["player_name"]
    money = player["money"]
    pokeballs = player["pokeballs"]
    health_potion = player["health_potion"]
    pokemon_inventory = player["pokemon_inventory"]

    print("***************************************")
    print(f"       Inventario {player_name}       ")
    print("***************************************\n")
    print(f"Dinero:    {money}\n")
    print(f"Pokeballs: {pokeballs}\n")
    print(f"Pociones:  {health_potion}\n")
    print("****************************************")
    print("         Inventario pokemon             ")
    print("****************************************")
    print("  nombre      |    lv   |     Tipo      |\n")
    for index in range(len(pokemon_inventory)):
        print(pokemon_inicial(pokemon_inventory[index]))

    print("*****************************************\n")


