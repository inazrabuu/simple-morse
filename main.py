from dict import MorseDictionary
from ui import UI
from translator import Translator

def main():
  dictionary = MorseDictionary()
  gui = UI()
  gui.ask_questions()
  d = dictionary.get_dictionary(gui.is_encode())

  t = Translator(gui.get_input_origin(), gui.is_encode())
  t.translate(d)
  print(t.get_translated())

if __name__ == '__main__':
  main()