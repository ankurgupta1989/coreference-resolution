__author__ = 'ankurgupta'

from global_variables import singular_set
from global_variables import plural_set
from global_variables import male_set
from global_variables import female_set
from global_variables import inanimate_set
import string
from used_checks import is_pronoun

# Returns
#   2  -- for plural
#   1  -- for singular
#   0  -- for unknown
def number(mention):
    if is_pronoun(mention):
        if string.lower(mention[0]) in singular_set:
            return 1
        elif string.lower(mention[0]) in plural_set:
            return 2
        else:
            return 0
    else:
        if mention[1] == 'NN' or mention[1] == 'NNP':
            return 1
        elif mention[1] == 'NNS' or mention[1] == 'NNPS':
            return 2
        else:
            return 0

# Returns
#   3  -- for male
#   2  -- for female
#   1  -- for non-living.
#   0  -- for unknown.
def gender(mention):
    if is_pronoun(mention):
        if string.lower(mention[0]) in male_set:
            return 3
        elif string.lower(mention[0]) in female_set:
            return 2
        elif string.lower(mention[0]) in inanimate_set:
            return 1
        else:
            return 0
    else:
        if mention[2] == 'O':
            return 0
        elif not mention[2] == 'B-PERSON' and not mention[2] == 'I-PERSON':
            return 1
        else:
            return 0

# Returns
#   1   --  for inanimate
#   0   --  otherwise
def animacy(mention):
    if is_pronoun(mention):
        if string.lower(mention[0]) in inanimate_set:
            return 1
        else:
            return 0
    else:
        if mention[2] == 'B-ORGANIZATION' or mention[2] == 'I-ORGANIZATION' or mention[2] == 'B-GPE' or mention[2] == 'I-GPE':
            return 1
        else:
            return 0

def animacy_match(mention, candidate):
    if animacy(mention) == animacy(candidate):
        return True
    return False


def gender_match(mention, candidate):
    mention_gender = gender(mention)
    candidate_gender = gender(candidate)
    if mention_gender == 0 or candidate_gender == 0 or mention_gender == candidate_gender:
        return True
    return False

def number_match(mention, candidate):
    mention_number = number(mention)
    candidate_number = number(candidate)
    if mention_number == candidate_number:
        return True
    return False

