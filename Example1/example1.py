from receiver import Receiver
from command_impl import ConcreteCommand
from invoker import Invoker

def main():
    receiver = Receiver()
    concrete_command = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.store_command(concrete_command)
    invoker.execute_commands()


if __name__ == "__main__":
    
    main()
