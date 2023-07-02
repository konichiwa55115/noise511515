import os
from pyrogram import Client, filters
from pyrogram.types import ForceReply
import subprocess
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery

bot = Client(
    "voluemincreaser",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6280972722:AAG3GrropPJhZvfjljtgppKeeXpfpBVZG4Y"
)

CHOOSE_UR_LANG = " اختر النمط الخاص بإزالة الضوضاء "
CHOOSE_UR_LANG_BUTTONS = [
    [InlineKeyboardButton("mod1",callback_data="mod1")],
     [InlineKeyboardButton("mod2",callback_data="mod2")],
     [InlineKeyboardButton("mod3",callback_data="mod3")],
     [InlineKeyboardButton("mod4",callback_data="mod4")],
     [InlineKeyboardButton("mod5",callback_data="mod5")]
]


@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا إزالة الضوضاء ورفع مستوى الصوت , فقط أرسل الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)

@bot.on_message(filters.private & filters.incoming &  filters.audio | filters.voice  )
def _telegram_file(client, message):
  
  global user_id
  user_id = message.from_user.id 
  file = message
  global file_path
  file_path = message.download(file_name="./downloads/")
  filename = os.path.basename(file_path)
  realname, ext = os.path.splitext(filename)
  global mp3file
  mp3file = realname+".mp3"
  message.reply(
             text = CHOOSE_UR_LANG,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_LANG_BUTTONS)

        )
@bot.on_callback_query()
def callback_query(CLIENT,CallbackQuery):
  global langtoken
  if CallbackQuery.data == "mod1":
      langtoken = "./rnnoise-models/somnolent-hogwash-2018-09-01/sh.rnnn"
  elif CallbackQuery.data == "mod2":
      langtoken = "./rnnoise-models/marathon-prescription-2018-08-29/mp.rnnn"
  elif CallbackQuery.data == "mod3":
      langtoken = "./rnnoise-models/leavened-quisling-2018-08-31/lq.rnnn"
  elif CallbackQuery.data == "mod4" :
      langtoken = './rnnoise-models/conjoined-burgers-2018-08-28/cb.rnnn'
  elif CallbackQuery.data == "mod5":
      langtoken = "./rnnoise-models/beguiling-drafter-2018-08-30/bd.rnnn"
  
  CallbackQuery.edit_message_text(
      
      "جار إزالة الضوضاء"
  )   
  subprocess.call(['ffmpeg','-i',file_path,'-af','arnndn=m=./rnnoise-models/beguiling-drafter-2018-08-30/bd.rnnn',"mod"+mp3file,'-y']) 
  subprocess.call(['ffmpeg','-i',"mod"+mp3file,'-af', "volume=4",mp3file,'-y']) 
  with open(mp3file, 'rb') as f:
         bot.send_audio(user_id, f)
  subprocess.call(['unlink',mp3file]) 
  subprocess.call(['unlink',"mod"+mp3file])
  subprocess.call(['unlink',file_path]) 


       

bot.run()
