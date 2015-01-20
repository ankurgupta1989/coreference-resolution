__author__ = 'ankurgupta'

from global_variables import third_person_animate_set, inanimate_set, prefix_list
from global_variables import pronoun_distance
import string
import re

def is_pronoun(mention):
    if mention[1] == 'PRP' or mention[1] == 'PRP$':
        return True
    return False


def prefix_match(mention, candidate):
    mention_lowercase = string.lower(mention[0])
    candidate_lowercase = string.lower(candidate[0])

    for prefix in prefix_list:
        if mention_lowercase.startswith(prefix):
            reg_ex = re.compile("^" + prefix + "\.? ?")
            result = reg_ex.findall(mention_lowercase)
            length = len(result[0])
            mention_without_prefix = mention_lowercase[length:]
            if candidate_lowercase.find(mention_without_prefix) != -1:
                return True
    return False

def string_match(mention, candidate):
    if is_pronoun(mention):
        return False

    if prefix_match(mention, candidate):
        return True

    candidate_lowercase = string.lower(candidate[0])
    mention_lowercase = string.lower(mention[0])

    if candidate_lowercase.find(mention_lowercase) != -1:
        return True
    return False

# Assumption : mention is a pronoun and candidate is not.
def person_match(mention, candidate):
    mention_match = (string.lower(mention[0]) in third_person_animate_set)
    candidate_match = (candidate[2] == 'B-PERSON')
    return mention_match and candidate_match

# Assumption : mention is a pronoun and candidate is not.
def animacy_match(mention, candidate):
    mention_match = (string.lower(mention[0]) in inanimate_set)
    candidate_match = (candidate[2] == 'B-ORGANIZATION' or candidate[2] == 'I-ORGANIZATION' or candidate[2] == 'B-GPE' or candidate[2] == 'I-GPE')
    return mention_match and candidate_match

def pronoun_match(mention, candidate, distance):
    if not is_pronoun(mention) or is_pronoun(candidate) or distance > pronoun_distance:
        return False
    if person_match(mention, candidate):
        return True
    if animacy_match(mention, candidate):
        return True
    return False