input1 = [False,True,True,None,True,None,None,False,False,None,True,False]
function = ["or","or","or","==","!=","==","and","==","!=","and","==","or"]
input2 = [False,False,None,None,True,True,False,True,None,False,True,None]

for i in range(len(function)):
	arg = (input1[i], function[i], input2[i])
	print(arg)
	#print(' '.join(argument, '=>', eval(argument))