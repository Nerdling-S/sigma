import os
import json

js = json.load(open("C:\\Users\\seblf\\Documents\\Python\\Sigma\\cmds.json"))

while True:
    # prompt indicator
    s = input("\u001b[36mΣ\u001b[0m ")
    # divide into words
    words = s.split()
    #divide into cmd & arguments
    cmd = words[0]
    args = words[1:]
    argstr = ' '.join(args)
    # quit by whatever means suitable
    if cmd in ['quit', 'exit', 'bye', 'voetsak', 'q']:
        break
    # echo with common misspellings
    elif cmd in ['echo', 'ehco', 'echp']:
        print(' '.join(args))
    # open a file/folder (run a command)
    elif cmd in ['open', 'opem', 'opne', 'ioen', 'o']:
        path = ''.join(map(lambda c:'\\' if (c=="/") else c,args[0])) + ' ' + ' '.join(args[1:])
        if os.path.isdir(path):
            os.system('explorer "%s"' % path)
        else:
            os.system("'%s'" % path)
    elif cmd in js:
        os.system("%s" % js[cmd][argstr])