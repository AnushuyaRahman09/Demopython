#secret number#
alphabet= 'abcdefghijklmnopqrstuvwxyz'
key=3
newMessage=''
message=input('please enter a message:')
for character in message:
    position=alphabet.find(character)
    newPosition=(position+key)
    newCharacter=alphabet[newPosition]
   # print('the new character is:,newCharacter')
    newMessage += newCharacter
print('your new Message is',newMessage)