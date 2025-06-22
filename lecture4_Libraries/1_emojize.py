#  carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.
# emoji module comes with two functions, per
# pypi.org/project/emoji
# one of which is emojize, which takes an optional, named parameter called language. You can install it with:
# pip install emoji

# language='alias' lets you use common shortcodes like :thumbsup:, :heart:, etc.
import emoji
em_txt=input("Input: ")
print(emoji.emojize(em_txt, language="alias"))