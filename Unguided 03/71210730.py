nilai2 = input()
while nilai2 != 'Q' :
    if '+' in nilai2 :
        nilai= nilai2.split('+')
        z = int(nilai[0])+int(nilai[1])
        print(z)
    elif '-' in nilai2 :
        nilai= nilai2.split('-')
        z = int(nilai[0])-int(nilai[1])
        print(z)
    elif '/' in nilai2 :
        nilai= nilai2.split('/')
        z = int(nilai[0])/int(nilai[1])
        print(z)
    elif '*' in nilai2 :
        nilai= nilai2.split('-')
        z = int(nilai[0])*int(nilai[1])
        print(z)
    nilai2 = input()
exit()