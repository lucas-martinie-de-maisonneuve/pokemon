import json
from files.class_py.pokedex import Pokedex
# import json
pokedex = Pokedex()

class Experience:
    def __init__(self, poke_player, save):
        self.poke_player = poke_player
        self.choose_save = save

        # self.exp_max_poke = 0        
        # self.numero_poke = poke_player["numero"]
        # self.poke_evol = self.numero_poke["numero"]+ 1
        self.exp_poke = 0
        self.level = None
        # self.liste_poke = pokedex.info_pokemon
        self.poke_sherch_name = pokedex.rand_pokemon()
        self.pokemons_name = self.poke_sherch_name['nom']
        self.current_save()
        # self.liste_rencontre_poke = pokedex.pkmn_rencontre
    def current_save(self):
        if self.choose_save == 'save1':
            pokedex.pkmn_rencontre = pokedex.open_save1()
        elif self.choose_save == 'save2':
            self.pkmn_rencontre = pokedex.open_save2()
            print (f"""'self'
                    {self.pkmn_rencontre}""")
            pokedex.pkmn_rencontre = pokedex.open_save2()
            print (f"""pokedex
                   {pokedex.pkmn_rencontre}""")
        elif self.choose_save == 'save3':
            pokedex.pkmn_rencontre = pokedex.open_save3()
        
    def exp_par_combat(self, level):
        if level is not None and level <= 2:
            exp_poke = 15
                        
        elif level is not None and level <= 4:
            exp_poke = 25
            
        elif level is not None and level <= 10:
            exp_poke = 30
            
        elif level is not None and level <= 20:
            exp_poke = 45

        elif level is not None and level <= 35:
            exp_poke = 75
            
        elif level is not None and level <= 50:
            exp_poke = 125

        self.level = level
        self.update_exp(self.poke_player['nom'],exp_poke)

    def exp_max(self, level):
        if level is not None:        
            if level <= 2 :
                self.exp_max_poke = 15            
            elif level <= 4:
                self.exp_max_poke = 25
            elif level <= 10:
                self.exp_max_poke = 30
            elif level <= 20:
                self.exp_max_poke = 60
            elif level <= 35:
                self.exp_max_poke = 140
            elif level <= 50:
                self.exp_max_poke = 290            

        return self.exp_max_poke

    def verif_exp(self, level, exp_poke):
        if exp_poke >= self.exp_max(level):
            self.update_lvl(self.poke_player['nom'],self.exp_max(level))

    def verif_for_evolve(self):
        self.current_save()
        for info_poke_rencontre in pokedex.pkmn_rencontre:
            for position, poke_player in enumerate(pokedex.info_pokemon):
                if self.poke_player["nom"] == poke_player["nom"]:  
                    if info_poke_rencontre["level"] == 16:
                        next_poke = pokedex.info_pokemon[position + 1]
                        if next_poke["evol"] == 2:
                            self.poke_player = next_poke
                    if info_poke_rencontre["level"] == 36:
                        next_poke = pokedex.info_pokemon[position + 1]
                        if next_poke["evol"] == 3:
                            self.poke_player = next_poke
                            
            with open(f'{self.choose_save}.json', 'w') as file:
                json.dump(pokedex.pkmn_rencontre, file, indent=2)    

        # if self.poke_player["level"] == 16:
        #     if self.poke_evol and self.poke_evol["evol"] == 2:
        #         self.poke_player = self.poke_evol
        #         print(self.poke_evol)
        # if self.poke_player["level"] == 36:
        #     if self.poke_evol and self.poke_evol["evol"] == 3:
        #         self.poke_player = self.poke_evol
        #         print(self.poke_evol)             

    def update_lvl(self, poke_name, exps_max):
        self.current_save()
        for pokemon in pokedex.pkmn_rencontre:
            if pokemon['nom'] == poke_name:
                while pokemon['exp'] >= exps_max:
                    pokemon['exp'] = pokemon['exp'] - exps_max
                    pokemon['level'] += 1
        
        with open(f'{self.choose_save}.json', 'w') as file:
                    json.dump(pokedex.pkmn_rencontre, file, indent=2)
        self.verif_for_evolve()
            
    def update_exp(self, poke_name, exp):
        self.current_save()
        for pokemon in pokedex.pkmn_rencontre:
            if pokemon['nom'] == poke_name:
                pokemon['exp'] += exp
                exp_maj = pokemon['exp']
            # Assurez-vous que le fichier est correctement fermé après la modification
        with open(f'{self.choose_save}.json', 'w') as file:
            json.dump(pokedex.pkmn_rencontre, file, indent=2)
        self.verif_exp(self.level, exp_maj)