import aiohttp
import base64
from pyrogram import enums
from userge import userge, Message
import time, os, math, requests, re, json
import datetime as DT
import requests as req
from pyrogram import Client, filters


header = {"AUTH_KEY":"meki"}

@userge.on_cmd(
    "dns", about={
        'header': "Create DNS Cloudflare",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}dns [ip]:[subdomain]"})
async def trojan(message: Message):
    """DNS Cloudflare"""
    replied = message.input_str 
    if not replied:
        await message.edit("`JGN KOSONG BLOK!`")
        return
    elif ":" not in replied:
        await message.edit("`IP:SUB !`")
        return
    elif ":" and ":" not in replied:
        await message.edit("`IP:SUB !`")
        return
    await message.edit("`Tunggu Blog !`")
    async with aiohttp.ClientSession() as req:
        d = replied.strip().split(':')[0]
        u = replied.strip().split(':')[1]
        param = f"sg1.kmkzteam.me:6969/dns?ip={d}&sub={u}"
        url = ("http://"+param)
        async with req.get(url, headers=header) as resp:
            if resp.status != "error":
              xx = await resp.text()
              x = xx.replace("[","").replace("]","").replace('"','').split(",")
            await message.edit(
        text=(f"**━━━━━━━━━━━━━━━━**\n"
              f"** ⚡️ DNS Cloudflare ⚡️** \n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**🔰 IP:** `{d}`\n"
              f"**🔰 Domain:** `{u}.globalnet.biz.id`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**📆@after_sweet**\n"),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.MARKDOWN
        )
        
        

                  
        

              
