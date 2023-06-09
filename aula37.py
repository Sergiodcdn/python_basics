#   JSON em PYTHON - Parte 2
import json

carros_dictionary={
    "marca": "honda",
    "modelo": "HRV",
    "cor": "prata"
}
#dictionary -> objeto json

carros_list=["honda", "volkswagem", "ford", "fiat", "chevrolet"]
#list -> array json

carros_tupla=("honda", "volkswagem", "ford", "fiat", "chevrolet")
#tupla -> array json
""" conversões printadas das listas acima
carros_j=json.dumps(carros_dictionary)
print(carros_j)
print(35 * "*")
carros_j=json.dumps(carros_list)
print(carros_j)
print(35 * "*")
carros_j=json.dumps(carros_tupla)
print(carros_j)
print(35 * "*")
"""
#indent=4 -> 4 é o espaço antes de por as palavras
#separators=(":","=") -> trocou : por =
#sort_keys=True -> ordena os itens em ordem alfabética
carros_j=json.dumps(carros_dictionary, indent=4, separators=(":","="),sort_keys=True) 
print(carros_j)