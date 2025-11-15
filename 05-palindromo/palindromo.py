def palindromo(string):
	sentence=string.lower().replace(' ', '')
	return sentence==sentence[::-1]

cadenas=["avion","ala","anita lava la tina"]

for cadena in cadenas:
	if palindromo(cadena):
		print(f"{cadena} es palindromo")
	else:
		print(f"{cadena} no es palindromo")
