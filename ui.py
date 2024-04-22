questions = [
  'Do you want to encode (e) or decode (d)? \n',
  'Please input the morse code to decode, separate by a space between each word character: \n',
  'Please input the word to encode: \n'
]

class UI:
  def __init__(self):
    self.questions = questions
    self.answers = []

  def ask_questions(self):
    q = self.questions
    correct = False
    while not correct:
      a = input(q[0])
      if a == 'e' or a == 'd':
        correct = True
    
    self.answers.append(a)

    next = q[1] if self.answers[0] == 'd' else q[2]

    self.answers.append(input(next))

  def is_encode(self):
    return self.answers[0] == 'e'
  
  def get_input_origin(self):
    return self.answers[1]