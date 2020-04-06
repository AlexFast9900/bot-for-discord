import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready.') # Бот загружен.

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            return

@client.command()
async def ping(ctx):
    await ctx.send('pong!')

@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@client.command()
async def help(message):
        helpp = discord.Embed(title='Помощь:', color=0xfb0000, url='https://sun9-3.userapi.com/c854020/v854020950/a4159/mf4TYuKp2T0.jpg')
        helpp.set_thumbnail(url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d579df4f-771f-4eab-9fa2-b00a265ef177/d6icujy-1685e8e7-67fb-437e-ad6c-b3e28c5e314b.png/v1/fill/w_793,h_1008,strp/rainbow_stalin_by_lelouche1711_d6icujy-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjAzNSIsInBhdGgiOiJcL2ZcL2Q1NzlkZjRmLTc3MWYtNGVhYi05ZmEyLWIwMGEyNjVlZjE3N1wvZDZpY3VqeS0xNjg1ZThlNy02N2ZiLTQzN2UtYWQ2Yy1iM2UyOGM1ZTMxNGIucG5nIiwid2lkdGgiOiI8PTE2MDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.z6kIutfI_RchUci7QVqrRa-ciGMIj4fVdvR1zIcoMMQ')
        helpp.add_field(name='!help', value='Помощь (красивая, как я)', inline=False)
        helpp.add_field(name='!ping', value='Пингануть Сталина (это платная услуга)', inline=False)
        helpp.add_field(name='!kick @nick', value='Изгнать его к чёртовой бабушке!', inline=False)
        helpp.add_field(name='!ban @nick', value='Приговорён к расстрелу!', inline=False)
        helpp.add_field(name='!clear (int)', value='Вызвать уборщицу', inline=False)
        helpp.set_footer(text='Ну вобщем, я больше ничего не добавил.')
        await message.send(embed=helpp)


client.run('Ваш токен')
