import src.utility.Global as Global

from random import randrange

def getUserFromId(uid):
    user = Global.client.get_user(uid)
    return user

def getRandomChannel():
    return Global.client.get_channel(Global.sql.get_channels()[randrange(len(Global.sql.get_channels()))])
