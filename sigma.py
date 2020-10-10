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
    # open a file/folder (run a command)
    elif cmd in ['open', 'opem', 'opne', 'ioen', 'o']:
        path = ''.join(map(lambda c:'\\' if (c=="/") else c,args[0]))
        if os.path.isdir(path):
            os.system("explorer " + path)
        else:
            os.system(path)