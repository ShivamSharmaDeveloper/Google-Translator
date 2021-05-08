from googletrans import Translator

sentence = input("Type any word or sentece you want to translate: ")

translator = Translator()

translated_sentence = translator.translate(sentence,src='en',dest='fr')

print(translated_sentence.text)