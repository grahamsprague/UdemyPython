'''
Translation excersize
'''

from translate import Translator

with open('test.txt') as my_file:
    my_file_content = my_file.read()

print(type(my_file_content))


from translate import Translator
translator= Translator(to_lang="ja")
translation = translator.translate(my_file_content)
print(translation)

with open('test_ja.txt', 'w') as my_tr_file:
    my_tr_file.write(translation)



