import discord
import asyncio
from sqlf import load_db

#...just don't ask
blockNut=False
nutCounter=0
#counter of how much minutes bot is online
counter=0

#Friends IDs
class idfnd:
    szefo="<@243142446274445322>"
    v7="<@280843168231063552>"
    nox="<@294905774767865857>"
    adwo="<@372478034147803158>"

#My channels IDs
class chnnl:
    owo="441604832588070933"

def answer(message):

# There is the problem with 'content' attribute so I had to do exception
    try:
        a = message.content 
        if a.startswith("hello V"):
            return 'Witaj {0.author.mention} ^^'.format(message)
        if a.startswith("dobranoc V"):
            return 'Dobrej nocy {0.author.mention}! :heart:'.format(message)
        if a.startswith("V nie ładnie, pożegnaj się"):
            return 'Dobranoc! ^^'
        if a.startswith('szefo where are you'):
            return '%s hunt' % (idfnd.szefo)
        if a.startswith("lumos"):
            return '%s' % (idfnd.nox)

        if message.content.startswith('v!list'):
            msg2=load_db()+"\n For {0.author.mention} :heart:!"
            return msg2.format(message)

    except AttributeError:
        pass
    
    

client = discord.Client()

# while loop
async def alive():
    await client.wait_until_ready()
    global counter
    # Spamming command to one of my channels...he just saying he is alive.
    while not client.is_closed:
        await client.send_message(discord.Object(id=chnnl.owo),'żyje od {}min! :3'.format(str(counter)))
        await asyncio.sleep(60)
        counter += 1


@client.event
async def on_message(message):

    global nutMsg
    global nutCounter
    global blockNut

    if message.author == client.user:
        return
    
    clt = str(message.author)

    if message.content.startswith("bloknij paffła"):
        blockNut=True
        nutMsg = await client.send_message(message.channel, 'Pawełek...przykro mi...')
    if message.content.startswith("uwolnij paffła!"):
        blockNut=False
        nutCounter=0
        await client.send_message(message.channel,'Pawełek jesteś wolny!')
    if blockNut:
        if clt == "Nutplace#0933":
            await client.delete_message(message)
            em = discord.Embed(title="Pawełek punched %d times!" % nutCounter, colour=0xFF0000)
            await client.edit_message(nutMsg, embed=em)
            nutCounter+=1
    if message.content and answer(message):
        await client.send_message(message.channel,answer(message))
    if message.content.startswith('V napisz'):
        msg = 'no siema mordo'.format(message)
        await client.send_message(message.author, msg)

    if message.content.startswith('fajnie'):
        await client.send_message(message.channel, 'Kto jest fajny? Napisz v! -imie-')

        def check(msg):
            return msg.content.startswith('v!')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('v!'):].strip()
        await client.send_message(message.channel, '{} jest fajny(a)!'.format(name))
    answer(message.content)



# I guess this function runs just once
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    # Changing status    
    await client.change_status(discord.Game(name="VVVVVVVVVVVVVVVVVVVVVVVVVVVV"))


client.loop.create_task(alive())
# Taking Secret Token from Secret file :3
filetoken=open("tkn.txt")
token = filetoken.read()
filetoken.close()
# Login & Pass are in Token
client.run(token)