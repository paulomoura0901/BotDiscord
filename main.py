import discord
from discord.ext import commands

# Importa a função que configura os comandos
from functions import setup_comandos

# Ativa todos os intents (necessário para o bot reagir a eventos como mensagens, reações, etc.)
intents = discord.Intents.all()

# Cria uma instância do bot com o prefixo "!" e os intents ativados
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento chamado automaticamente quando o bot estiver pronto para uso
@bot.event
async def on_ready():
    print("Gaibu foi inicializado com sucesso!")

# Configura os comandos ao carregar o bot
setup_comandos(bot)

# Inicia o bot (substitua "SEU_TOKEN_AQUI" pelo seu token real do bot)
bot.run("SEU_TOKEN_AQUI")
