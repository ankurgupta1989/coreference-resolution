import BigramChunker
__author__ = 'ankurgupta'

import nltk
from nltk.corpus import conll2000

def get_noun_phrases_and_named_entities(file_name, start_index, end_index):

    sentences = conll2000.sents(file_name)
    noun_phrase_sentences = conll2000.chunked_sents(file_name, chunk_types=['NP'])
    pos_tagged_sentences = conll2000.tagged_sents(file_name)

    sentences = sentences[start_index:end_index]
    pos_tagged_sentences = pos_tagged_sentences[start_index:end_index]
    noun_phrase_sentences = noun_phrase_sentences[start_index:end_index]

    # Extacting mentions.
    words = []
    cnt = 0
    for sent in sentences:
        cnt += 1
        for word in sent:
            words.append((word, cnt))

    noun_phrases = []
    for sent in noun_phrase_sentences:
        noun_phrases += nltk.chunk.tree2conlltags(sent)

    named_entities = []
    for tagged_sent in pos_tagged_sentences:
        tree = nltk.chunk.ne_chunk(tagged_sent)
        named_entities += nltk.chunk.tree2conlltags(tree)

    return (words, noun_phrases, named_entities)



def get_noun_phrases_and_named_entities_data(data):
    # print data
    train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
    chunker = BigramChunker.BigramChunker(train_sents + test_sents)

    tagged_data = []
    for sent in data:
        tokens = nltk.word_tokenize(sent)
        tagged = nltk.pos_tag(tokens)
        tagged_data.append(tagged)

    noun_phrases = []
    for tagged_sent in tagged_data:
        tree = chunker.parse(tagged_sent)
        noun_phrases += nltk.chunk.tree2conlltags(tree)

    named_entities = []
    for tagged_sent in tagged_data:
        tree = nltk.chunk.ne_chunk(tagged_sent)
        named_entities += nltk.chunk.tree2conlltags(tree)

    words = []
    cnt = 0
    for sent in data:
        cnt += 1
        tokens = nltk.word_tokenize(sent)
        for token in tokens:
            words.append((token, cnt))

    # print words
    # print noun_phrases
    # print named_entities

    return (words, noun_phrases, named_entities)



def extract_mentions(data=None):
    if data == None:
        (words, noun_phrases, named_entities) = get_noun_phrases_and_named_entities('test.txt', 155, 160)
    else:
        (words, noun_phrases, named_entities) = get_noun_phrases_and_named_entities_data(data)

    mentions = []
    running_word = ''
    running_entity = ''
    running_pos = ''
    running_sent_number = 0
    for i in range(len(words)):
        if noun_phrases[i][0] == 'PRP' or noun_phrases[i][1] == 'PRP$':
            if running_word != '':
                mentions.append((running_word, running_pos, running_entity, running_sent_number))
            mentions.append((words[i][0], noun_phrases[i][1], named_entities[i][2], words[i][1]))
            running_word = ''
        elif noun_phrases[i][2] == 'B-NP':
            if running_word != '':
                mentions.append((running_word, running_pos, running_entity, running_sent_number))
            running_word = words[i][0]
            running_sent_number = words[i][1]
            running_entity = named_entities[i][2]
            running_pos = noun_phrases[i][1]
        elif noun_phrases[i][2] == 'I-NP':
            running_word += ' ' + words[i][0]
            if running_entity == 'O' and named_entities[i][2] != 'O':
                running_entity= named_entities[i][2]
            if noun_phrases[i][1] == 'NN' or noun_phrases[i][1] == 'NNS' or noun_phrases[i][1] == 'NNP' or noun_phrases[i][1] == 'NNPS':
                running_pos = noun_phrases[i][1]
        else:
            if running_word != '':
                mentions.append((running_word, running_pos, running_entity, running_sent_number))
            running_word = ''

    if running_word != '':
        mentions.append((running_word, running_pos, running_entity, running_sent_number))

    # Print the results for debugging.
    text = ''
    for word in words:
        text += word[0] + ' '


    print text
    # print noun_phrases
    # print named_entities
    print '\nMentions'
    for mention in mentions:
        print mention

    # Return the mentions found.
    return mentions