while True:
    # prompt indicator
    cmd = input("\u001b[36mΣ\u001b[0m ")

    # quit by whatever means suitable
    if cmd in ['quit', 'exit', 'q', 'bye', 'voetsak']:
        break
    # echo with common misspellings
    elif cmd[:4] in ['echo', 'ehco', 'echp']:
        print(cmd[5:])