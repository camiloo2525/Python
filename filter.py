# La función filter(), 
#devuelve un valor que esta siendo iterado de la cual su resultado será el valor que se esta buscando en el filter

numeros = [1,2,3,4,5]
nuevos_numeros = list(filter( lambda x: x % 2 == 0 , numeros))
print (numeros)
print (nuevos_numeros)

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(matches)

# cantidad de elementos
print(len(matches))

new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

print(new_list)
print(len(new_list))

print(matches)
print(len(matches))