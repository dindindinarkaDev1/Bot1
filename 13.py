import sys
import time
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = -166876481
    print(content_type, chat_type, chat_id)

    if content_type == 'test':
        bot.sendMessage(-166876481, 'test')


bot = telepot.Bot('1387631651:AAFLPAGbcNyJDrIRGewZJEc4ADy04zRvSXQ')
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')



while 1:
    time.sleep(10)
