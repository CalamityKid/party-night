initiation_text = """
Dime a ve tiguerasooo, vamo a ve eta vaina ahora, 
lo que pasa e que uno puede ecribi lo que uno quiera
y la vaina te clacula como un codigo y te dice cuanto
vale tu nombre en el codigo ese, una vaina rarisima
pero me lo pidio ete entonce hay que hacelo, ve?
"""
typo_text= """
 ave tiguere, aqui vamo sin vaina rara, ecribeme plein
 sin simbolo raro, el abecedario normal no me meta vaina 
 rara que asi no vale ok. ecribemelo bn ahora ok?
 """

result_text = """
okey menol, mira.
hice lo calculo y tengo el resultado, ve?
El nombre tuyo e dique {name} y cuando uno hace lo calculo
eso vale {result} puntos en el codigo ese.
Y ya, eso era manin
Quiere otro o ya ta bueno?
"""

end_text = """
Po na menol, acido un plaser
cuidese
"""

value_dict = {' ':0, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

def count_total_value(name):
	name = name.lower()
	total_value = 0
	for letter in name:
		try:
			total_value += value_dict[letter]
		except KeyError:	
			print (typo_text)
			return None
	return total_value

def ask_name():
	result = None
	while result == None:
		print("Mi nombre es:", end="")
		name = input()
		result = count_total_value(name)
	if result != None:
		return result, name

print(initiation_text)
result, name = ask_name()
formatted_string = result_text.format(name=name, result=result)
print (formatted_string)
repeat = True
while repeat == True:
	print ("¿Quiere otro, si o no?", end="")
	otro = input()
	otro = otro.lower()
	if otro == "no":
		print (end_text)
		input()
		exit()
	if otro == "si":
		repeat = True
		result, name = ask_name()
		formatted_string = result_text.format(name=name, result=result)
		print (formatted_string)
	else:
		print ("Que lo que tu me ta diciendo menol, te dije que si o no, quejeso")
