from invoker import MealInvoker as mi

from receivers import Salad, Sandwich, Taco

from command_impl import SaladCommand as sdc
from command_impl import SandwichCommand as swc
from command_impl import TacoCommand as tc

salad = Salad()
sandwich = Sandwich()
taco = Taco()

salad_com = sdc(salad)
sandw_com = swc(sandwich)
taco_com = tc(taco)
meal = mi(sandw_com)

def test1():

	meal.invoke() # makes a sandwich meal
	meal.execute_commands()

def test2():
	
	sandwich = Sandwich()  # receiver
	command_sandwich = swc(sandwich)  # concrete command

	salad = Salad()  # receiver
	command_salad = sdc(salad)  # concrete command

	taco = Taco()  # receiver
	command_taco = tc(taco)  # concrete command

	meal_invoker = mi(command_sandwich)  # invoker
	meal_invoker.invoke() # Starting the method calls

	meal_invoker.add_command_to_list(command_salad)
	meal_invoker.add_command_to_list(command_taco)
	meal_invoker.execute_commands()

if __name__ == '__main__':
	test2()
