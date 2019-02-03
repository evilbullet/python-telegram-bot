"""This example shows how to retrieve the full message history of a chat"""

import time

from pyrogram import Client
from pyrogram import Message
from pyrogram.api.errors import FloodWait

from PIL import Image


app = Client(
"my_account", api_id=668604, api_hash="691dfb6e3825de315413c995ee3dd558"
)
target = "memlrd"  # "me" refers to your own chat (Saved Messages)
messages = []  # List that will contain all the messages of the target chat
offset_id = 10  # ID of the last message of the chunk

with app:
    while True:
        try:
            m = app.get_history(target, offset_id=offset_id)

        except FloodWait as e:  # For very large chats the method call can raise a FloodWait
            print("waiting {}".format(e.x))
            time.sleep(e.x)  # Sleep X seconds before continuing
            continue

        if not m.messages:
            break

        messages += m.messages
        offset_id = m.messages[-1].message_id

        # print("Messages: {}".format(len(messages)))
        # [print(i) for i in messages]
        # print(type(messages[1].__str__()))
        # for mm in messages:
        #     print(mm)
        # img = ''
        for i in range(len(messages)):
            try:
                print(messages[i].views)
                print(messages[i].photo.sizes.dir())
                # print(messages[i].photo.sizes{file_id})
                # 'https://api.telegram.org/file/bot<token>/<file_path>'
                # img = Image.open(messages[i].photo)
                # img.show()

            except:
                print('no view')
            i += 1
        print(dir(messages[1].photo.sizes))

# Now the "messages" list contains all the messages sorted by date in
# descending order (from the most recent to the oldest one)
