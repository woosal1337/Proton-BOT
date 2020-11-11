from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed, File
from datetime import datetime
from discord.ext.commands import CommandNotFound
import time
from selenium import webdriver
import bs4 as bs
from selenium import webdriver  # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import lib.bot.ipresolver as ipresolver

PREFIX = "+"
OWNER_IDS = [618038532665114624]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("BOT has been CONNECTED!")

    async def on_disconnect(self):
        print("BOT has been DISCONNECTED!")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong!")

        else:
            channel = self.get_channel(757016278060761178)
            await channel.send("Dude your code freaking sucks, and error occured right here!")

        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass

        elif hasattr(exc, "original"):
            raise exc.original

        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(746850984701198437)
            print("BOT is ready!")

            channel = self.get_channel(757016278060761178)
            await channel.send("Now online!")

            embed = Embed(title="", url="https://www.protonmail.com/", description="Server Alert",
                                  color=0xe31616)
            embed.add_field(name="Info:",
                            value="In order to protect our customers, the traffic to the servers will be filtered through OVHs mitigation infrastructure. Notes: ICMP (Ping) is dropped during the attack! All open ports will also timeout when mitigation is enabled! Do not flex with those stupid timeouts kids!",
                            inline=False)


            embed.set_author(name="@woosal1337", icon_url=self.guild.icon_url)
            embed.set_footer(text="This is a footer xD?")
            #embed.set_thumbnail(url=self.guild.icon_url)
            #embed.set_image(url="lib/bot/flags/azerbaijan.png")
            # await channel.send(embed=embed)
            # await channel.send(file=File("./data/images/elon.gif"))
            print("Started the Service.")
            print("Scraping ProtonMail")

            with open("lib/bot/warnings.txt", "r") as theWarningFile:
                firstLength = 0  # len(theWarningFile.read())

            while True:
                with open("lib/bot/warnings.txt", "r") as theWarningFile:
                    currentLength = len(theWarningFile.read())
                    print(theWarningFile.read())
                    print("current length is: ", currentLength)
                    print("first length is ", firstLength)
                    if currentLength != firstLength:
                        f = open("lib/bot/warnings.txt", "r")
                        lastLine = f.readlines()[-1]
                        countryName = lastLine.split()[-2]
                        countryFlag = lastLine.split()[-1]
                        countryIp = lastLine.split()[-3]
                        embed.add_field(name="Server location:", value="server.location()", inline=False)
                        embed.add_field(name="IP:", value=f"||{countryIp}||", inline=False)
                        embed.add_field(name="Country:", value=f"{countryName}", inline=True)
                        embed.set_footer(text="Current time")
                        await channel.send(embed=embed)
                        await channel.send(file=File(f"lib/bot/flags/{countryFlag}"))
                        firstLength = currentLength
                        time.sleep(0.5)

        else:
            print("BOT reconnected!")

    async def on_message(self, message):
        pass


bot = Bot()
