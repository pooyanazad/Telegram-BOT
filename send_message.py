import telegram
print('++Start connecting...\n')
bot=telegram.Bot(token='9***9587*:**EGbcTK3UzV*****gcIP54Nb25qK*****')
print('++Connecting complete.\n','*'*30)


print('++Start sending...\n')
message=open('c://Your_Bot/Message.txt','r',encoding='UTF-8')
DB=open('c://Your_Bot/ids_DB.txt','r')

for i in DB:
    print('++Start sending for ',i)
    while True:
        text=message.read(1024)
        if not text:
            break
        try:
            bot.sendMessage(chat_id=i,text=text)
        except:
            print(i,'Error')
    message.seek(0)
    print('++Proccess complete for ',i)
message.close()
DB.close()

print('********Proccess finished********')
