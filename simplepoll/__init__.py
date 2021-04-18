from .simplepoll import SimplePoll


def setup(bot):
    bot.add_cog(SimplePoll(bot))
