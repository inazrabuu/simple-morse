class Translator:
  def __init__(self, code_string:str, is_encode:bool):
    self.is_encode = is_encode
    self.origin = [*code_string.upper()] if self.is_encode else code_string.split(' ')
    self.translated = ''

  def translate(self, dictionary_dict:dict):
    for key in self.origin:
      self.translated += dictionary_dict[key]
      if self.is_encode:
        self.translated += ' '

  def get_translated(self) -> str:
    return self.translated