import os
from pyrogram import Client, filters
from os import system as cmd
import shutil

bot = Client(
    "voluemincreaser",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5848326557:AAE00dflZddzH1e9ABLKwReT7ka6qltZHXA"
)


@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا إزالة الضوضاء ورفع مستوى الصوت , فقط أرسل الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/sunnay6626/2 ",disable_web_page_preview=True)

@bot.on_message(filters.private & filters.incoming &  filters.audio | filters.voice  )
def _telegram_file(client, message):
  
  global user_id
  user_id = message.from_user.id 
  file = message
  file_path = message.download(file_name="aud")
  tempmp3 = "mod.mp3"
  tem2pmp3 = "mod2.mp3"
  cmd(f'''ffmpeg -i {file_path} -vf arnndn=m=./rnnoise-models/somnolent-hogwash-2018-09-01/sh.rnnn "{tempmp3}" -y''')
  cmd(f'''ffmpeg -i "{tempmp3}" -vf arnndn=m=./rnnoise-models/somnolent-hogwash-2018-09-01/sh.rnnn "{tem2pmp3}" -y ''')
  cmd(f'''ffmpeg -i "{tem2pmp3}" -vf arnndn=m=./rnnoise-models/beguiling-drafter-2018-08-30/bd.rnnn "{tempmp3}" -y ''')
  cmd(f'''ffmpeg -i "{tempmp3}" -vf arnndn=m=./rnnoise-models/conjoined-burgers-2018-08-28/cb.rnnn "{tem2pmp3}" -y ''')
  cmd(f'''ffmpeg -i "{tem2pmp3}" -vf arnndn=m=./rnnoise-models/leavened-quisling-2018-08-31/lq.rnnn "{tempmp3}" -y ''')
  cmd(f'''ffmpeg -i "{tempmp3}" -vf arnndn=m=./rnnoise-models/marathon-prescription-2018-08-29/mp.rnnn "{tem2pmp3}" -y ''')
  with open(mp3file, 'rb') as f:
         bot.send_audio(user_id, f)
  shutil.rmtree('./downloads/')
  cmd(f'''rm "{file_path}" "{tempmp3}" "{temp2mp3}"''')
  
bot.run()
