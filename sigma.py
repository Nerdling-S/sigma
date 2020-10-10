import os

while True:
    # prompt indicator
    s = input("\u001b[36mΣ\u001b[0m ")
    # divide into words
    words = s.split()
    #divide into cmd & arguments
    cmd = words[0]
    args = words[1:]
    # quit by whatever means suitable
    if cmd in ['quit', 'exit', 'bye', 'voetsak', 'q']:
        break
    # echo with common misspellings
    elif cmd in ['echo', 'ehco', 'echp']:
        print(' '.join(args))
    # open a file/folder
    elif cmd in ['open', 'opem', 'opne', 'ioen', 'o']:
        if args[0][-1] in ['/', '\\']:
            os.system('explorer ' + args[0][:-1] + '\\')