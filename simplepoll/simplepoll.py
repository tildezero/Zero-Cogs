from redbot.core import commands
from redbot.core.utils.menus import start_adding_reactions


# Classname should be CamelCase and the same spelling as the folder
class SimplePoll(commands.Cog):
    """Cog to do polls with simple yes, no, maybe options, and custom options as well!"""

    @commands.command(name='quickpoll', aliases=['vote', 'qpoll'])
    async def quickpoll(self, ctx, *, question):
        """ Makes a simple poll to ask a question """
        await ctx.message.delete()
        embed = discord.Embed(title=question, colour=discord.Colour(ctx.embed_color()))
        embed.set_author(name=f"{ctx.author.name} asks... ")
        msg = await ctx.send(embed=embed)
        start_adding_reactions(msg, ["\U0001f44d", "\U0001f44e", "\U0001f937"])
        
    @commands.command(name='poll')
    async def poll(self, ctx, *, question_and_options):
      """
      Makes a poll that allows custom options. Split the question and each option with a comma (,).
      Example: `[p]poll What is your favorite color?, red, blue, green, other`
      """
      EMOJI = "🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯".split(" ")
      split_args = question_and_options.split(",")
      question = split_args[0].strip()
      answers = [answer.strip() for answer in split_args[1::]]
      desc = ""
      for num, option in enumerate(answers):
        desc += f"{EMOJI[num]} {option}\n"
      embed = discord.Embed(title=question, colour=ctx.embed_color(), description=desc)
      msg = await ctx.send(embed)
      for i in range(len(answers)):
        await msg.add_reaction(EMOJI[i])
        

