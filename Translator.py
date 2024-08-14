
import PutToDir
from googletrans import Translator

async def  translator(message):
    #блок перевода
    #await message.send_copy(chat_id=message.chat.id)
    text11 = message.text
    translator = Translator()
    translator_word = translator.translate(text11, src='en', dest='ru').text
    await message.answer(translator_word)
    print(text11, translator_word)
    #блок перевода end
    PutToDir.alfabet(text11)
    print("2")
