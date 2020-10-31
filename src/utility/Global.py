from src.utility.Watcher import Watcher
from src.managers.mysql.SQLManager import SQLManager

from discord import Client

client = Client()

prefix = 'm!'

sql = SQLManager()

watcher = Watcher()
