from Database.pokefire import OS_CLEAN,act_player_inventory
import os, random

#comprar pociones y hacer el descuento en el dinero del usuario en firebase
def buy_potions(user_name,money,helth_potion):
     can=int(input("¿Cuantas pociones deseas comprar? "))
     cost=can*200
     if cost>money:
       print("No cuentas con el suficiente dinero para realizar la compra")
     else:
        money-=cost
        helth_potion+=can
        act_player_inventory(user_name,"money",money)
        act_player_inventory(user_name,"health_potion",helth_potion)
        if can>1:
          print(f"Has comprado {can} pociones\n ")
        else:
          print(f"Has comprado {can} pocion\n ")
     return money

#comprar pokeballas actualizar el perfil del jugador
def buy_pokeballs(user_name, money, pokeballs):
  can = int(input("¿Cuantas pokeballs deseas comprar? "))
  cost = can * 300
  if cost > money:
    print("No cuentas con el suficiente dinero para realizar la compra")
  else:
    money -= cost
    pokeballs += can
    act_player_inventory(user_name, "money", money)
    act_player_inventory(user_name, "pokeballs", pokeballs)
    if can > 1:
      print(f"Has comprado {can} pokeballs\n ")
    else:
      print(f"Has comprado {can} pokeball\n ")
  return money


#loteria al azar para obtener un pokemon al azar
def lotery_pokemon(all_pokemon,name_player,pokemon_inventory:list,money):
  if money<800:
    print("No cuentas con el suficiente dinero para realizar la compra")
  else:
       lotery=random.choice(all_pokemon)
       money-=800
       pokemon_inventory.append(lotery)
       act_player_inventory(name_player,'money',money)
       act_player_inventory(name_player,'pokemon_inventory',pokemon_inventory)
       print("Has obtenido un {} como premio".format(lotery["name"]))

  return money


#acciones disponibles en la tienda
def store_pokemon(player_profile,all_pokemon):
  opcion=None
  while opcion!=4:
    print("\n")
    print("|***********************************************|")
    print("|**|           Poketienda                    |**|")
    print("|***********************************************|")
    print(f"Dinero disponible: ¥ {player_profile['money']}\n")
    print("¿Que desea comprar? : ");
    print("1.- Pociones  ¥200")
    print("2.- Pokeballs ¥300")
    print("3.- Pokerifa obten un pokemon al azar ¥800")
    print("4.- Salir")

    opcion = int(input("Opcion: "))
    os.system(OS_CLEAN)

    if opcion==1:
      player_profile['money']= buy_potions(player_profile["player_name"],player_profile["money"],player_profile['health_potion'])


    elif opcion==2:
       player_profile['money']=buy_pokeballs(player_profile["player_name"],player_profile["money"],player_profile['pokeballs'])


    elif opcion==3:
      player_profile['money']=lotery_pokemon(all_pokemon,player_profile["player_name"],player_profile["pokemon_inventory"]
                      ,player_profile["money"])




