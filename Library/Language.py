from translate import Translator

def deutsch_englisch(text):
    translator = Translator(from_lang="de", to_lang="en")
    translation = translator.translate(text)
    return translation

def englisch_deutsch(text):
    translator = Translator(from_lang="en", to_lang="de")
    translation = translator.translate(text)
    return translation

def deutsch_italienisch(text):
    translator = Translator(from_lang="de", to_lang="it")
    translation = translator.translate(text)
    return translation

def italienisch_deutsch(text):
    translator = Translator(from_lang="it", to_lang="de")
    translation = translator.translate(text)
    return translation

def deutsch_spanisch(text):
    translator = Translator(from_lang="de", to_lang="es")
    translation = translator.translate(text)
    return translation

def spanisch_deutsch(text):
    translator = Translator(from_lang="es", to_lang="de")
    translation = translator.translate(text)
    return translation

def deutsch_franzoesisch(text):
    translator = Translator(from_lang="de", to_lang="fr")
    translation = translator.translate(text)
    return translation

def franzoesisch_deutsch(text):
    translator = Translator(from_lang="fr", to_lang="de")
    translation = translator.translate(text)
    return translation