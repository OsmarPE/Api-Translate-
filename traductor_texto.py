# pip install googletrans==4.0.0-rc1

from googletrans import Translator


def traducir_texto(texto):
  # Crear un objeto Translator
  translator = Translator()

  # Traducir el texto al español
  texto_traducido = translator.translate(texto, dest='en', src='es').text

  return texto_traducido


def mostrar_traduccion(texto, texto_traducido):
  print(f"\n\nTexto en español: {texto}\n\nTexto en ingles: {texto_traducido}\n\n")


def translateText(text):
  texto_traducido = traducir_texto(text)
  return texto_traducido

