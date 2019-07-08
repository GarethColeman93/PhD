import re


file_used = sys.argv[1]

s = open (file_used, 'r')


text= s.read()

text2 = re.sub('_____[^:]+:', ':', text)


#file.write('test.txt')

print (text2)