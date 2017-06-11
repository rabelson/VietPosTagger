# VietPosTagger
Vietnamese part of speech tagger based on the Vietnamese corpus found [here](http://viet.jnlp.org/download-du-lieu-tu-vung-corpus).

## Tagset
The tagset in use contains 17 main lexical tags:  

**Np** - Proper noun  
**Nc** - Classifier  
**Nu** - Unit noun  
**N** - Common noun  
**V** - Verb  
**A** - Adjective  
**P** - Pronoun  
**R** - Adverb  
**L** - Determiner  
**M** - Numeral  
**E** - Preposition  
**C** - Subordinating conjunction  
**CC** - Coordinating conjunction  
**I** - Interjection  
**T** - Auxiliary, modal words  
**Y** - Abbreviation  
**Z** - Bound morphemes  
**X** - Unknown  
  
## Feature Set
**Probability Array**

A probability array of possible part of speeches for words. For example, consider [tránh: “N”, “N”, “V”, “N], read as “tránh” maps to the parts of speeches “N” three times and “V” once. Clearly, the probability of “tránh” being a noun later on in the testing dataset is more likely than not. This was the most important feature in our classifier.


**Bigram Part of Speech Frequency**

This feature was mainly taken into account for when we encounter a word we have never seen before. To figure out this new word’s part of speech, we looked at the part of speech of the word before it and ruled out which part of speech was the least likely to appear in this new word.


**Word Position in Sentence**

Usually sentence position determines the probability that a word will be a certain part of speech. Like English, Vietnamese sentence structure follows a Subject-Verb-Object order. Therefore, there is a tendency for nouns to appear on the ends, and verbs tend to be in the middle. 


** Capitalization**

This feature made us of the fact that proper nouns contain capital letters in the corpora.

### Tools  
Vietnamese Tokenizer:  
https://github.com/manhtai/vietseg  
