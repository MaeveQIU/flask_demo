def search_for_letter(phrase, letter = 'aeiou'):
  return set(phrase).intersection(set(letter))