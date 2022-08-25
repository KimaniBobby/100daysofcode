import random
from affirmationslist import affirmations
# lst = [
#     "You are fearfully and wonderfully made in the image of God.",
#     "You are loved more than you can fathom.",
#     "You are chosen and wanted.",
#     "Thank you for being a friend to me.",
#     "I miss you!",
#     "You are important and valued.",
#     "You are not alone even when you feel lonely.",
#     "I admire how strong you are!"
# ]

lst_without_dups = list(set(affirmations))

print(','.join(random.choices(lst_without_dups, k=1)))

# print(','.join(lst)) removes the square brackets when printing items from a list
