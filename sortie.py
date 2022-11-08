crossMatches = 0
lastMatch = ''
noteAsk = ''
    
def searchNote(file, matcher):
        banning = 0
        global matchedYet
        matchedYet = 0
        global possBan
        possBan = ''
        global possBan1
        with open(file, 'r') as file1:
            with open('ban.txt', 'r') as banlist:
                contented = file1.read()
                content = contented.split(' ')
                ban = banlist.read()
                for element in content:
                    if matcher == element and matchedYet == 0:
                        print('Match found!')
                        if matcher not in ban:
                            matchedYet = 1
                            if possBan1 == matcher:
                                banning = 1
                            possBan = matcher
                            if banning == 0:
                                    with open(file, 'a') as writer:
                                        writer.write('\n')
                                        writer.write(noteAsk)
                        if matcher in ban:
                            print('Unfortunately the match is banned.')
                        if banning == 1:
                            print('But something got banned.')
                            with open('ban.txt', 'a') as banner:
                                banner.write('\n')
                                banner.write(matcher)

def run():
        allWords = []
        bannedWords = []
        files = []
        global matchedYet
        matchedYet = 0
        global noteAsk
        global possBan1
        possBan1 = ' '
        with open('files.txt', 'r') as fileset:
                read = fileset.read()
                files = read.split(' ')
                for element in files:
                        with open(element, 'r') as banning:
                                content = banning.read()
                                words = content.split(' ')
                                for element in words:
                                        if element in allWords:
                                                bannedWords.append(element)
                                        else:
                                                allWords.append(element)
        noteAsk = input('Enter the text you want to sort.')
        word = noteAsk.split(' ')
        for element in files:
                filetouse = element
                print('Searching' + filetouse + '...')
                matchedYet = 0
                for element in word:
                    if matchedYet == 0:
                        searchNote(filetouse, element)
                        if possBan != '':
                            possBan1 = possBan
        for element in files:
                with open(element, 'r') as reader:
                        content = reader.read()
                        if noteAsk in content:
                                print('The note was taken in' + element)
        print("If the note was taken in more than one place, or if you didn't get any notifications that the note was taken, check all your note files.")

while 1==1:
        run()
                        
                        
                        
                        
        
        
                
                
                
        
                
                
                
                


                

    
