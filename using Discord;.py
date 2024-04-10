import discord
import random
from discord.ext import commands

INTENTS = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=INTENTS)  # 수정된 부분

@bot.event  
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='팀짜기')
async def divide_teams(ctx, team_size: int):
    if team_size <= 0:
        await ctx.send("팀의 인원 수는 1 이상이어야 합니다.")
        return
    
    voice_channel = ctx.author.voice.channel
    members = voice_channel.members

    if len(members) < team_size * 2:
        await ctx.send("팀의 인원 수가 부족합니다.")
        return

    random.shuffle(members)
    num_teams = len(members) // team_size
    teams = [members[i:i+team_size] for i in range(0, len(members), team_size)]

    for i, team in enumerate(teams):
        if len(team) == team_size:  # 인원 수와 동일한 팀만 출력
            team_str = f"Team {i+1}: " + ', '.join([(member.nick or member.display_name) for member in team])
            await ctx.send(team_str)

    remaining_members = len(members) % team_size
    if remaining_members > 0:
        remaining_str = f"남는 사람: " + ', '.join([(member.nick or member.display_name) for member in members[-remaining_members:]])
        await ctx.send(remaining_str)




@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='랜덤뽑기')
async def pick_random_members(ctx, num_winners: int):
    voice_channel = ctx.author.voice.channel

    if not voice_channel:
        await ctx.send("음성 채널에 연결되어 있지 않습니다.")
        return

    members = voice_channel.members

    if not members:
        await ctx.send("음성 채널에 아무도 없습니다.")
        return

    if num_winners < 1 or num_winners > len(members):
        await ctx.send("유효하지 않은 당첨 인원 수입니다. 음성 채널의 참여 인원 수보다 작거나 같아야 합니다.")
        return

    winners = random.sample(members, num_winners)
    winners_names = [winner.nick or winner.name for winner in winners]

    await ctx.send(f"축하합니다! 당첨된 참여자들: {', '.join(winners_names)}")





# 디스코드 봇 토큰을 사용하여 봇 로그인
# 여기에는 본인이 발급받은 디스코드 봇 토큰을 입력해야 합니다.
bot.run('MTIyNzQ1MDgwMjE0MzIzNjE4OA.G3D3tm.tRsOfur0_uXz2hAFxqT1rZMyQwVMnxZD9UIyo4') 
