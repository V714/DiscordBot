import discord

class idfnd:
    szefo="<@243142446274445322>"
    v7="<@280843168231063552>"
    nox="<@294905774767865857>"
class chnnl:
    owo="441604832588070933"


client = discord.Client()


@client.event
async def on_message(message):
    content = message.content.split(" ")
    print(content)
    clt = str(message.author)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('hello V'):
        msg = 'Witaj {0.author.mention} ^^'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('szefo where are you'):
        msg = '%s hunt'.format(message)
        await client.send_message(message.channel, msg % idfnd.szefo)
    if message.content.startswith('lumos'):
        msg = '%s'.format(message)
        await client.send_message(message.channel, msg % idfnd.nox)

    #if clt == "kane#0214":
    #    await client.delete_message(message)




       
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.send_message(discord.Object(id=chnnl.owo),'owo hunt')

filetoken=open("tkn.txt")
token = filetoken.read()
filetoken.close()
client.run(token)