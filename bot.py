import requests
import json
import configparser as cfg
import os

class telegram_chatbot():

    def __init__(self, config):
        self.token = self.read_token_from_config_file(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)

    def read_token_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')

    def execute_command(self, commands):
        print(commands)
        command = commandCreator(commands)
        command.execute_command()
        

class commandCreator():
    def __init__(self, commands):
        comandos = commands.split()
        self.comando= None
        if comandos[0] == 'Python':
            self.comando = pythonCommand(comandos[1:])
        if comandos[0] == 'Sys':
            self.comando = sysCommand(comandos[1:])

    def execute_command(self):
        self.comando.execute_command()


class sysCommand():
    def __init__(self, commands):
        comando = ''
        for x in commands:
            comando = comando + x + ' '
        comando = comando + ' > results.txt'
        self.syscommand = comando

    def command_to_execute(self):
        return self.syscommand

    def execute_command(self):
        os.system(self.command_to_execute())


class pythonCommand():
    def __init__(self, commands):
        comando = './'
        for x in commands:
            comando = comando + x + ' '
        self.pythoncommand = comando

    def command_to_execute(self):
        return self.pythoncommand

    def execute_command(self):
        os.system(self.command_to_execute())
