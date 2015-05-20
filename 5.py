# 5.1 Using a Tagger
import nltk
text = nltk.word_tokenize("And now for something completely different")
nltk.pos_tag(text)

text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
nltk.pos_tag(text)

text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
text.similar('woman')

text.similar('bought')
text.similar('over')

text.similar('the')


