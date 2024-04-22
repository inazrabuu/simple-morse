d = {
  'A':'.-', 'B':'-...',
  'C':'-.-.', 'D':'-..', 'E':'.',
  'F':'..-.', 'G':'--.', 'H':'....',
  'I':'..', 'J':'.---', 'K':'-.-',
  'L':'.-..', 'M':'--', 'N':'-.',
  'O':'---', 'P':'.--.', 'Q':'--.-',
  'R':'.-.', 'S':'...', 'T':'-',
  'U':'..-', 'V':'...-', 'W':'.--',
  'X':'-..-', 'Y':'-.--', 'Z':'--..',
  '1':'.----', '2':'..---', '3':'...--',
  '4':'....-', '5':'.....', '6':'-....',
  '7':'--...', '8':'---..', '9':'----.',
  '0':'-----', ', ':'--..--', '.':'.-.-.-',
  '?':'..--..', '/':'-..-.', '-':'-....-',
  '(':'-.--.', ')':'-.--.-'
}

class MorseDictionary:
  def __init__(self):
    self.dict = {}
    self.dict_reverse = {}
    self.load_dictionary()

  def load_dictionary(self):
    self.dict = d
    self.dict_reverse = {y: x for x, y in self.dict.items()}

  def get_dictionary(self, is_encode: bool) -> dict:
    return self.dict if is_encode == True else self.dict_reverse