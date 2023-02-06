#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [BotStatus Telegram bot by TeLe TiPs] (https://github.com/teletips/Powerful_BotStatus-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/Powerful_BotStatus-TeLeTiPs/blob/main/LICENSE

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name = "botstatus_teletips",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

async def main_teletips():
    async with app:
            while True:
                print("Checking...")
                xxx_teletips = f"**✨ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ɴᴏᴏʙ ᴄʀᴇᴀᴛᴏʀ ʙᴏᴛ's sᴛᴀᴛᴜs ᴄʜᴀɴɴᴇʟ\n❄ ʜᴇʀᴇ ɪs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ's ᴡʜɪᴄʜ ᴡᴇ ᴏᴡɴ ᴀɴᴅ ᴛʜᴇɪʀ sᴛᴀᴛᴜs (ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ), ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ᴋᴇᴇᴘ ᴜᴘᴅᴀᴛɪɴɢ ᴏɴ ᴇᴠᴇʀʏ 5 ᴍɪɴᴜᴛᴇs.**"
                for bot in BOT_LIST:
                    try:
                        yyy_teletips = await app.send_message(bot, "/start")
                        aaa = yyy_teletips.id
                        await asyncio.sleep(10)
                        zzz_teletips = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_teletips:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_teletips += f"\n\n╭⎋  @{bot}\n╰⊚  **🔴 sᴛᴀᴛᴜs: ᴅᴇᴀᴅ ❌**"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **ᴀʟᴇʀᴛ! ᴀʟᴇʀᴛ!! @{bot} ɪs ᴅᴇᴀᴅ ᴄᴀʟʟ [ᴘɪʀᴏᴋɪᴅ](t.me/pirokid)** ❌")
                                except Exception:
                                    pass
                            await app.read_chat_history(bot)
                        else:
                            xxx_teletips += f"\n\n╭⎋  @{bot}\n╰⊚  **🟢 sᴛᴀᴛᴜs: ᴡᴏʀᴋɪɴɢ ✅**"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_teletips += f"\n\n✅ ʟᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ: {last_update} ({TIME_ZONE})\n\n<i>♻️ Refreshes automatically</i>\nᴀɴʏ ɪssᴜᴇ ʀᴇᴘᴏʀᴛ [ᴘɪʀᴏᴋɪᴅ](t.me/pirokid)"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
                print(f"✅ ʟᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ: {last_update}")                
                await asyncio.sleep(6300)
                        
app.run(main_teletips())

#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
