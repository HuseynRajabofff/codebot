import discord
from discord.ext import commands
from settings import BOT_TOKEN
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))
    
eco_tips = [
    "Сократите использование пластика, носите с собой многоразовую бутылку для воды.",
    "Выключайте электронику, когда не используете её, чтобы экономить энергию.",
    "Перейдите на энергосберегающие лампочки.",
    "Компостируйте пищевые отходы вместо того, чтобы выбрасывать их.",
    "Покупайте оптом, чтобы сократить количество упаковочных отходов.",
    "Используйте многоразовые сумки для покупок вместо пластиковых пакетов.",
    "Ходите пешком или ездите на велосипеде, когда это возможно, вместо использования машины.",
]


eco_challenges = [
    "Никаких пластиковых пакетов в течение недели!",
    "Компостируйте все органические отходы в течение 5 дней.",
    "Используйте общественный транспорт или велосипед для поездок на работу в течение недели.",
    "Сократите потребление энергии на 10% в этом месяце.",
    "Не покупайте одноразовый пластик в течение недели.",
    "Начните использовать многоразовую кружку для кофе в течение месяца.",
]


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True


bot = commands.Bot(command_prefix="/", intents=intents)

@bot.command()
async def tip(ctx):
    tip = random.choice(eco_tips)
    await ctx.send(f"🌍 Экологичный совет: {tip}")


@bot.command()
async def challenge(ctx):
    challenge = random.choice(eco_challenges)
    await ctx.send(f"🌱 Ваш вызов: {challenge}")


bot.run(BOT_TOKEN)
