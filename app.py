from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from gtts import gTTS
from playsound import playsound as p
import os

app = Flask(__name__)
bot = ChatBot("Chatterbot",read_only = True)
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/sample.yml")
@app.route('/')
def index():
      return render_template("index.html")

@app.route("/get")
def get_bot_response():
      userText = request.args.get('msg')
      res = str(bot.get_response(userText))
      if res.startswith('<'):
         return res
      else:
         tts = gTTS(str(bot.get_response(userText)))
         tts.save('bot.mp3')
         p('bot.mp3')
         os.remove('bot.mp3')
         return res

if __name__ == "__main__":
     app.run()