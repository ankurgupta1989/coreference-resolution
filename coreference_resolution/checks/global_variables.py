__author__ = 'ankurgupta'

# The global variables.
pronoun_distance = 25
singular_list_personal = ["she", "he", "her", "him", "it", "i", "me"]
plural_list_personal = ["they", "them", "we", "us"]
singular_list_demonstrative = ["this", "that"]
plural_list_demonstrative = ["these", "those"]
singular_list_reflexive = ["myself", "yourself", "himself", "herself", "itself"]
plural_list_reflexive = ["ourselves", "yourselves", "themselves"]
singular_list_possesive = ["my", "its", "mine", "his", "hers"]
plural_list_possesive = ["our", "their", "ours", "yours", "theirs"]

singular_list = singular_list_personal + singular_list_demonstrative + singular_list_possesive + singular_list_reflexive
plural_list = plural_list_personal + plural_list_demonstrative + plural_list_possesive + plural_list_reflexive

singular_set = set(singular_list)
plural_set = set(plural_list)

male_list = ["he", "him", "himself", "his"]
female_list = ["she", "her", "herself", "hers"]
inanimate_list = ["it", "its", "itself", "this", "that", "these", "those"]

male_set = set(male_list)
female_set = set(female_list)
inanimate_set = set(inanimate_list)

additional_list = ["my", "mine"]
third_person_animate_list = male_list + female_list + additional_list
third_person_animate_set = set(third_person_animate_list)

prefix_list = ["ms", "miss", "mr", "mrs", "master", "dr", "prof", "hon", ]
