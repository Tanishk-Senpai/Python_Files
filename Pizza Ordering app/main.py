#Pizza toppings

toppings_added = {}
available_toppings = {'pepperoni':5,'paneer':2,'corn':10}

while True:
	disp_available_toppings = []
	
	for i, j in available_toppings.copy().items():
		if j != 0:
			disp_available_toppings.append(i)
		if j == 0:
			del available_toppings[i]
	
	print(disp_available_toppings)
	topping = input("Enter your choice of topping: ")
	quantity = input("Enter the quantity of the topping you want to add: ")
	
	for i in disp_available_toppings:
		if topping.lower() == i.lower():
			print(f"We will be adding {topping} to your pizza")
			toppings_added[topping] = int(quantity)
			available_toppings[i] = (available_toppings[i] - int(quantity))
	
	next = input("Do you want more toppings? (Y/n): ")
	
	try:
		if next.lower() == 'y':
			continue
		elif next.lower() == 'n':

			display_toppings = print("Your choice of toppings are: ")
			for i,j in toppings_added.items():
				print(f"{i} X {j} Servings")
			print("Your Pizza is ready!")
			break
		else:
			raise Exception
	except:
		print("Wrong Input! Please try again")
		next = input("Do you want more toppings? (Y/n): ")
		if next.lower() == 'y':
			continue
		elif next.lower() == 'n':
			for i,j in toppings_added.items():
				print(f"{i} X {j} Servings")
			print("Your Pizza is ready!")
			break


