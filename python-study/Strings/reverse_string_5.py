def spin_words(sentence):
  partial = sentence.split()
  print(partial)
  for word in partial:
    if len(word) >= 5:
      print(word)
      new = []
      for l in word:
        new.append(l)
        print(word)
      new.reverse()
      response = ''
      for l in new:
        response += l
  return response