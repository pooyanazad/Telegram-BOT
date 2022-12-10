import telegram
bot=telegram.Bot(token='9***9587*:**EGbcTK3UzV*****gcIP54Nb25qK*****')
ids=bot.getUpdates()
list_ids=set()
for each in ids:
    list_ids.add(each.message.chat_id)

with open('c://Your_Bot/ids_DB.txt','w') as f:
    for i in list_ids:
        f.write(str(i)+'\n')
with open('c://Your_Bot/ids_DB.txt','w') as f:
    for i in list_ids:
        f.write(str(i)+'\n')
