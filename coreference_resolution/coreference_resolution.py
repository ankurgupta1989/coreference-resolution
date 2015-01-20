__author__ = 'ankurgupta'

from mention_extraction import extract_mentions
from checks.used_checks import string_match
from checks.used_checks import pronoun_match


def match(mention, candidate, distance, coref_list):
    if string_match(mention, candidate):
        coref_list.append((mention, candidate))
        return True
    if pronoun_match(mention, candidate, distance):
        coref_list.append((mention, candidate))
        return True
    return False

def get_data(input_file):
    fh = open(input_file, 'rt')

    line = fh.readline()
    data = []
    while line:
        data.append(line.decode('utf-8'))
        line = fh.readline()

    return data


def coreference_resolution():
    coref_list = []
    data = get_data('input.txt')
    mentions = extract_mentions(data)

    for i in range(len(mentions)):
        j = i - 1
        mention = mentions[i]
        mention_sentence_number = mention[3]
        found = False
        while j >= 0:
            cand = mentions[j]
            cand_sentence_number = cand[3]
            if mention_sentence_number != cand_sentence_number:
                break
            if match(mention, cand, i - j, coref_list):
                found = True
                break
            j -= 1

        if found:
            continue

        while j >= 0:
            cur_sentence_number = mentions[j][3]
            thisList = []
            while j >= 0 and mentions[j][3] == cur_sentence_number:
                thisList.append(mentions[j])
                j -= 1
            k = len(thisList) - 1
            while k >= 0:
                if match(mentions[i], thisList[k], i - j, coref_list):
                    found = True
                    break
                k -= 1
            if found:
                break


    print "\nCo-references"
    for coref in coref_list:
        print coref[0][0],coref[0][3], "corefers", coref[1][0], coref[1][3]

# print 'Running coreference resolution\n\n'
coreference_resolution()
