import src.utility.Global as Global
from src.utility.User import User

from random import randrange

def getUserFromId(uid):
    user = Global.sql.get_user(uid)
    return user if user is not None else User(uid)

def getRandomChannel():
    return Global.client.get_channel(Global.sql.get_channels()[randrange(len(Global.sql.get_channels()))])
