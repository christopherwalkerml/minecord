import src.utility.Global as Global

async def reactionManager(reaction, user):
    message = reaction.message

    for p in Global.pages:
        if p.message == message and p.user.userId == user.id:
            print('yeah')
