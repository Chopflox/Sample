import pigSay

newPig = pigSay.main()

def pigConversation(newPig):
    for newPig in range(0,3):
        x = input('Skriv hva grisen skal si')
        pigSay.main(x)