import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
from Models.Pokemon import get_pokemon
from Models.User import getUser,view_profile
import random,os
from dotenv import  load_dotenv

load_dotenv()



#conexion con firebase
cred=credentials.Certificate("Database/pokemonstadium.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':os.environ["FIREBASE_APP"]
})

#modificar texto de acuerdo a tu sistema operativo windows cambiar a cls  linux y mac clear
OS_CLEAN=os.environ["CLEAN"]


#crear perfil de usuario en firebase
def create_user_profile(pokemon_list,name_player):
    ref=db.reference('Users')
    user_ref= ref.child(name_player)
    user=getUser(name_player,[random.choice(pokemon_list) for a in range(3)])
    user_ref.set(user)
    os.system(OS_CLEAN)
    view_profile(user)
    os.system(OS_CLEAN)
    return user


#guardar pokemon en la firestore
def create_pokemon(new_pokemon):
    db= firestore.client()
    doc_ref = db.collection(u'Pokedex').document(u'{}'.format(new_pokemon["name"]))
    doc_ref.set({
        u"name":new_pokemon["name"],
        u"current_health": new_pokemon["current_health"],
        u"base_health":  new_pokemon["base_health"],
        u"level":  new_pokemon["level"],
        u"type":  new_pokemon["type"],
        u"attacks":  new_pokemon["attacks"],
        u"current_exp":  new_pokemon["current_exp"]
    })



#obtener perfil de usuario existente
def get_user_profile(user_name):
    ref=db.reference(f'Users/{user_name}')
    user=ref.get()
    return user


#actualizar la salud del pokemon en el perfil del usuario
def pokemon_health(user_name,pokemon_name,health):
    ref=db.reference(f"Users/{user_name}/pokemon_inventory")
    pokemon_inv=ref.get()
    for key in range(len(pokemon_inv)):
     if pokemon_inv[key]["name"]==pokemon_name:
          ref.child(str(key)).update({"current_health":health})


#actualizar alguna variable del perfil de usuario
def act_player_inventory(user_name,key,value):
    ref=db.reference(f"Users/{user_name}")
    inventory=ref.get()
    ref.update({f"{key}":value})


#actualizar la experiencia del pokemon
def pokemon_exp(user_name,pokemon_name,current_exp):
    ref=db.reference(f"Users/{user_name}/pokemon_inventory")
    pokemon_in=ref.get()
    for key in range(len(pokemon_in)):
        if pokemon_in[key]["name"] == pokemon_name:
            ref.child(str(key)).update({"current_exp": current_exp})



#subir el nivel del pokemon en su perfil de usuario
def set_pokemon_level(user_name,level,current_exp,current_health):
    ref = db.reference(f"Users/{user_name}")
    inventory = ref.get()
    ref.update({
        "current_exp": current_exp,
        "currnt_health": current_health,
        "level":level
      })


#obtener un tipo de la firestore
def get_one_type(ty):
    db=firestore.client()
    ty_ref=db.collection(u"Types")
    types=ty_ref.where(u"name",u"==",u"{}".format(ty)).get()
    for type in types:
       return type.to_dict()

#obtener la lista de todos los pokemon de firestore
def get_all_pokemon():
    db=firestore.client()
    all_pokemon=[]
    print("Cargando pokedex ...")
    pokemons = db.collection(u'Pokedex').get()
    if len(pokemons)>0:
        for pokemon in pokemons:
            all_pokemon.append(pokemon.to_dict())
    else:
        print("¡Pokedex no creada! Creando pokedex de internet...")
        for index in range(151):
            all_pokemon.append(get_pokemon(index))
            create_pokemon(get_pokemon(index))
            print("*", end="")

        print("\nTodos los pokemon han sido descargados")

    print("! Pokedex cargada!\n")
    os.system(OS_CLEAN)
    return all_pokemon


#decorador python para validar si un usuario existe en firebase
def user_exists(func):
    def profile_exists(*args):
        if func(*args) != None:
            return func(*args)
        else:
            print("No se encontro perfil de Entrenador\n")
            return False

    return profile_exists


#retorna el perfil del jugador de la base de datos
@user_exists
def consult_user(name):
    return get_user_profile(name)


#decorador python para validar si un nombre de usuario se repite en la base de datos
def is_create(func):
    def exists(*args):
        if get_user_profile(args[1]) == None:
            return func(*args)
        else:
            print(f"Ya hay un Entranador con el nombre {args[1]}\n")
    return exists

@is_create
def setUser(pokemon_list,name_player):
    return create_user_profile(pokemon_list,name_player)



#retorna un perfil nuevo o existente de un usuario
def get_player_profile(pokemon_list):
   if input("¿Ya tienes un perfil de entrenador? S/N ")=="S":
      profile_user=False

      while profile_user == False:
          name = input("¿Cual es tu nombre entrenador? ")
          profile_user=consult_user(name)

      os.system(OS_CLEAN)
      return profile_user

   else:
       user_profile=None
       while user_profile==None:
           name_player = input("¿Cual es tu nombre? ")
           user_profile=setUser(pokemon_list,name_player)

       return user_profile




