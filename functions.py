from discord.ext import commands

def setup_comandos(bot):
    @bot.command()
    async def jogos(ctx):
        mensagem = """
🎮 *Olá, gamer! Pronto para novidades?*
Estou aqui pra te manter por dentro do mundo dos jogos!

1️⃣ *Lançamentos de jogos famosos*  
2️⃣ *Promoções imperdíveis em lojas oficiais*

Responda com o número da opção que você quer, ou digite cancelar pra sair. 🚀
"""
        await ctx.reply(mensagem)
        print("Mensagem enviada!")

        # Função 'checar' indentada corretamente dentro de 'jogos'
        def checar(mensagem):
            print(f"Verificando mensagem: {mensagem.content}")
            return (
                mensagem.author == ctx.author and  # 'ctx' é acessível aqui
                mensagem.channel == ctx.channel and
                mensagem.content in ['1', '2', 'cancelar']
            )

        try:
            resposta = await bot.wait_for("message", check=checar, timeout=30.0)
            print(f"Resposta recebida: {resposta.content}")

            if resposta.content == '1':
                await ctx.send("🆕 Aqui estão os últimos lançamentos de jogos!")
            elif resposta.content == '2':
                await ctx.send("💸 Essas são as promoções atuais nas lojas oficiais!")
            elif resposta.content.lower() == 'cancelar':
                await ctx.send("❌ Operação cancelada com sucesso.")
        except Exception as e:
            print(f"Erro: {e}")
            await ctx.send("⏰ Tempo esgotado! Por favor, tente novamente usando !jogos.")
