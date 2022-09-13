# jabber = open('Jabberwocky.txt', 'r')
#
# for line in jabber:
#     print(line.rstrip())
#     # print(len(line))
#
# jabber.close()

# with open('Jabberwocky.txt', 'r') as jabber:
#     for line in jabber:
#         print(line.rstrip())
#     # lines = jabber.readlines() # returns the output as list

with open('Jabberwocky.txt', encoding='utf-8') as jabber:
    for line in jabber:
        print(line.rstrip())
#
# print(lines)
# print(lines[-1:])
#
# for lines in reversed(lines):
#     print(lines, end='') # do some processing in reversed order

# with open('Jabberwocky.txt', 'r') as jabber:
#     text = jabber.read()
#
# # print(text)
# for character in reversed(text):
#     print(character, end='')

def removeprefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:] # return copy of the string


def removesuffix(string: str, suffix: str) -> str:
    if string and string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:] # return copy of the string

# with open('Jabberwocky.txt') as jabber:
#     while True:
#         line = jabber.readline().rstrip()
#         print(line)
#         # alternate way
#         # for line in jabber:
#         #     print(line.rstrip())
#         if 'jubjub' in line.casefold():
#             break


