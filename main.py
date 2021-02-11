#!/usr/bin/env python3
from steam.client import SteamClient
from dota2.client import Dota2Client

import dota2
import click

client = SteamClient()
dota = Dota2Client(client)

@client.on('logged_on')
def on_logged_on():
    dota.launch()

@click.command('create-lobby')
@click.option('--name', default='lobby-teste', prompt='Lobby name')
@dota.on('ready')
def create_lobby(name = 'meulobby'):
    lobby = dota.create_practice_lobby(options = {'game_name': name})

if __name__ == '__main__':
    client.cli_login()
    client.run_forever()
