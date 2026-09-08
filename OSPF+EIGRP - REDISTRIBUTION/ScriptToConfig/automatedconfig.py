from netmiko import ConnectHandler, BaseConnection
import json


def load_configs(filename: str) -> list:
    with open(filename, "r") as file:
        commands = []
        for line in file:
            line = line.strip()
            if line:
                commands.append(line)
    return commands

def load_devices_from_json(filename: str) -> dict:
    with open(filename, "r") as file:
        result_dict = json.load(file)
    return  result_dict

def execute_connection(device : dict) -> BaseConnection:
    connection = ConnectHandler(**device)
    return connection

def execute_commands(connection: BaseConnection, commands: list) :
        output = connection.send_config_set(commands)
        print(output)


for i in range(0,6):
    device = load_devices_from_json("devices.json")
    execute_commands(execute_connection(device[i]),load_configs(f"./Instructions/R{i+1}.txt"))



