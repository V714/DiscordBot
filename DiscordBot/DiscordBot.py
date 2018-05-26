import discord
import asyncio
blockKane=False
blockNut=False
class idfnd:
    szefo="<@243142446274445322>"
    v7="<@280843168231063552>"
    nox="<@294905774767865857>"
    adwo="<@372478034147803158>"
class chnnl:
    owo="441604832588070933"



def load_db():
    db_file = open("database2.txt")
    db=db_file.readlines()
    nick,age,name=[''],[''],['']
    for i in range(0,len(db)):
        counter=0
        data=''
        for i2 in range(0,len(db[i])):
            if db[i][i2] != "|":
                data+=db[i][i2]
            else:
            
                if counter==0:
                    nick.append(data)
                elif counter==1:
                    age.append(data)
                counter+=1
                data=''
            if i2 == len(db[i])-2:
                name.append(data) 
                data=''
        

    db_file.close()
    database=''
    for i in range(0,len(nick)):
       database+=str('{:-<15}{:-^15}{:->15}'.format(nick[i],age[i],name[i]))
       database+="\n"
    return database 


client = discord.Client()
blockKane=False
@client.event
async def on_message(message):
    global blockKane
    global blockNut
    clt = str(message.author)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('hello V'):
        msg = 'Witaj {0.author.mention} ^^'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('bloknij kane'):
        msg = 'Oczywiście {0.author.mention}!'.format(message)
        blockKane=True
        await client.send_message(message.channel, msg)
    if message.content.startswith('uwolnić kane!'):
        msg = 'No ok {0.author.mention}!'.format(message)
        blockKane=False
        await client.send_message(message.channel, msg)
    if message.content.startswith('bloknij paffła'):
        msg = 'Pawełek...przykro mi...'.format(message)
        blockNut=True
        await client.send_message(message.channel, msg)
    if message.content.startswith('uwolnij paffła!'):
        msg = 'Pawełek jesteś wolny!'.format(message)
        blockNut=False
        await client.send_message(message.channel, msg)
    if message.content.startswith('szefo where are you'):
        msg = '%s hunt'.format(message)
        await client.send_message(message.channel, msg % idfnd.szefo)
    if message.content.startswith('lumos'):
        msg = '%s'.format(message)
        await client.send_message(message.channel, msg % idfnd.nox)
    if message.content.startswith('adwo chcesz bota?'):
        msg = 'Nie oddawaj mje dla %s!'.format(message)
        await client.send_message(message.channel, msg % idfnd.adwo)
    if blockKane:
        if clt == "kane#0214":
            await client.delete_message(message)
    if blockNut:
        if clt == "Nutplace#0933":
            await client.delete_message(message)
    if message.content.startswith('v!list'):
        msg2=load_db()+"\n For {0.author.mention} :heart:!"
        msg = msg2.format(message)
        await client.send_message(message.channel,msg)



       
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_status(discord.Game(name="VVVVVVVVVVVVVVVVVVVVVVVVVVVV"))

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    while not client.is_closed:
        counter += 1
        await client.send_message(discord.Object(id=chnnl.owo),'żyje! ' +str(counter))
        await asyncio.sleep(60)
filetoken=open("tkn.txt")
token = filetoken.read()
filetoken.close()
client.run(token)