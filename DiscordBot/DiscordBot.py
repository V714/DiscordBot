import discord
import asyncio
import vninegag
#import pyninegag
from sqlf import load_db
from sqlf import add_db
from sqlf import load_sp

#...just don't ask
block_nut=False
nut_counter=0
#counter of how much minutes bot is online
counter=0

#Friends IDs
idfnd = {
   'szefo':"<@243142446274445322>",
    'v7':"<@280843168231063552>",
    'nox':"<@294905774767865857>",
    'adwo':"<@372478034147803158>",
    }
#My channels IDs
chnl = {
    'owo':"441604832588070933"
    }
def answer(message):
 
# There is the problem with 'content' attribute so I had to do exception
    try:
        a = message.content 
        if a.startswith("hello v"):
            return 'Witaj {0.author.mention} ^^'.format(message)
        if a.startswith("jem"):
            return 'Smacznego {0.author.mention} :3'.format(message)
        if a.startswith("dobranoc v"):
            return 'Dobrej nocy {0.author.mention}! :heart:'.format(message)
        if a.startswith("v nie ładnie, pożegnaj się"):
            return 'Dobranoc! ^^'
        if a.startswith('szefo where are you'):
            return '%s hunt' % (idfnd['szefo'])
        if 'nie spodziewa' in a:
            return 'https://i.ytimg.com/vi/zLj-EAgfFsg/hqdefault.jpg'
        if a.startswith("lumos"):
            return '%s' % (idfnd['nox'])
        if a.startswith("vvvvvvv"):
            return '%s' % (idfnd['v7'])

        ### Taking list of users from database
        if message.content.startswith('v!list'):
            msg2=load_db()+"\n For {0.author.mention} :heart:!"
            return msg2.format(message)
        ### Taking info of only one user by nickname
        if message.content.startswith('v!get'):
            name = message.content[len('v!get'):].strip()
            msg2=load_sp(name).format(message)
            return msg2
        ### Taking new 9gag article
        if message.content.startswith('v!9gag'):
            gag =vninegag.get_gag()
            title = vninegag.get_title(gag)
            url = vninegag.get_url(gag)
            msg=title+"\n\n"+url
            return msg
    except AttributeError:
        pass
    
    

client = discord.Client()

# while loop
#async def alive():
#    await client.wait_until_ready()
#    global counter
#    # Spamming command to one of my channels...he just saying he is alive.
#    while not client.is_closed:
#        await client.send_message(discord.Object(id=chnnl['owo']),'żyje od {}min! :3'.format(str(counter)))
#        await asyncio.sleep(60)
#        counter += 1


@client.event
async def on_message(message):
    message.content = message.content.lower()
    global nut_msg
    global nut_counter
    global block_nut

    # To prevent bot loop - responding to himself
    if message.author == client.user:
        return
    
    print('[%s]: ' % message.author+message.content)
    ### Getting author name
    clt = str(message.author)


    ### Blocking friend (just deleting his messages when he send)
    if message.content.startswith("bloknij paffła"):
        block_nut=True
        nut_msg = await client.send_message(message.channel, 'Pawełek...przykro mi...')
    if message.content.startswith("uwolnij paffła!"):
        block_nut=False
        nut_counter=0
        await client.send_message(message.channel,'Pawełek jesteś wolny!')
    if block_nut:
        if clt == "Nutplace#0933":
            nut_counter+=1
            await client.delete_message(message)
            em = discord.Embed(title="Pawełek punched %d times!" % nut_counter, colour=0xFF0000)
            await client.edit_message(nut_msg, embed=em)
    ####################################################################
    ###
    ### Testing private message sending

    if message.content and answer(message):
        await client.send_message(message.channel,answer(message))
    if message.content.startswith('v napisz'):
        msg = 'no siema mordo'.format(message)
        await client.send_message(message.author, msg)
    ####################################################################
    ###
    ### Testing answer containing user message

    if message.content.startswith('fajnie'):
        await client.send_message(message.channel, 'Kto jest fajny? Napisz v! -imie-')

        def check(msg):
            return msg.content.startswith('v!')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('v!'):].strip()
        await client.send_message(message.channel, '{} jest fajny(a)!'.format(name))
    answer(message.content)
    ####################################################################
    ###
    ### Adding new person to database
    if message.content.startswith('v!add.list'):
        await client.send_message(message.channel, 'Wpisz: v! -nick- -wiek- -imie-')

        def check(msg):
            return msg.content.startswith('v!')

        message = await client.wait_for_message(author=message.author, check=check)
        data = message.content[len('v!'):].strip()
        data = data.split()
        add_db(data[0],int(data[1]),data[2])
        await client.send_message(message.channel, "{0.author.mention} dodał(a) właśnie użytkownika %s do listy! :sunglasses:".format(message) % data[0])
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


######### client.loop.create_task(alive())
# Taking Secret Token from Secret file :3
filetoken=open("tkn.txt")
token = filetoken.read()
filetoken.close()
# Login & Pass are in Token
client.run(token)