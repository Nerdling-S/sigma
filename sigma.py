while True:
    # prompt indicator
    s = input("\u001b[36mΣ\u001b[0m ")
    # divide into words
    words = s.split()
    #divide into cmd & arguments
    cmd = words[0]
    args = []
    map(lambda w: args.append(w),words[1:])
    # quit by whatever means suitable
    if cmd in ['quit', 'exit', 'q', 'bye', 'voetsak']:
        break
    # echo with common misspellings
    elif cmd[:4] in ['echo', 'ehco', 'echp']:
        print(args)