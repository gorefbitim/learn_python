import pandas as pd
raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']                        
            }
pokemon = pd.DataFrame(raw_data)
pokemon.head()
pokemon = pokemon[['name', 'type', 'hp', 'evolution','pokedex']]
pokemon
pokemon['place'] = ['park','street','lake','forest']
pokemon
pokemon.dtypes
