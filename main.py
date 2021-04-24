import spacy

nlp = spacy.load('pt_core_news_lg')

phrases = ['qual o valor', 'quanto custa', 'preço', 'me fala o total']

question = nlp('qual o preço?')
for phrase in phrases:
  print(nlp(phrase).similarity(question))
