from Database.pokefire import get_all_pokemon ,get_player_profile
from Actions.player import menu_player

def main():
    print("Bienvenido a Pokemon Stadium\n")
    pokemon_list=get_all_pokemon()
    player_profile=get_player_profile(pokemon_list)
    menu_player(player_profile,pokemon_list)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
