#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 01:33:24 2020

@author: oyewunmi oluwaseyi
"""

# importing the necessary packages
from fbchat import Client
from fbchat import log
from fbchat.models import *
import json
import time
from time_of_day import part_of_day
# client = Client('oluwaseyioyewunmi99@gmail.com', 'qwertyu7',session_cookies=cookies)
# cookies = client.getSession()
# with open("session.json", "w") as f:
#     json.dump(cookies, f)
# print(client.uid)

# fetching the list of all users am chatting with
# chat_list = client.fetchAllUsers()
# print(chat_list)
# # print("users' IDs: {}".format([user.uid for user in chat_list]))
# guys_id = {}
# female_id = {}
# for user in chat_list:
#     # print("{} : {}".format(user.name, user.uid))
#     if user.gender == 'male_singular':
#         guys_id.update({user.uid:user.name})
#     elif user.gender == 'female_singular':
#         female_id.update({user.uid:user.name})
#     # print(user.last_message_timestamp)
# #     new_chats = user.last_message_timestamp
# #     new_chats_timestamp.append(new_chats)
# #     print(new_chats)
# print(guys_id)
# print(female_id)

    
# # Fetches a list of the 20 top threads you're currently chatting with
# threads = client.fetchThreadList(limit=5)
# print(threads)
# for user in threads:
#     readable = time.ctime(int(user.last_message_timestamp[:10]))
#     print(user.name,'messaged at {}'.format(readable))
# # Fetches the next 10 threads
# # threads += client.fetchThreadList(offset=20, limit=10)

# messages = client.fetchThreadMessages(thread_id='100005372591917', limit=1)
# # # Since the message come in reversed order, reverse them
# # messages.reverse()

# # Prints the content of all the messages
# for message in messages:
#     print(message.text)
# client.logout()

class Chatbot(Client):

     def name(self, uid):
        threads = Client.fetchThreadList()
        mes_thread = Client.fetchThreadMessages(uid, limit=1)
        for user in threads:
            if uid == user.uid:
                readable = time.ctime(int(user.last_message_timestamp[:10]))
                print(user.name,'messaged at {}'.format(readable))
                for mes in mes_thread:
                    print(user.name,'said {}'.format(mes.text))

     def onBlock(self, author_id, thread_id, thread_type, **kwargs):
         'shows who blocks you and block them back'
         for user in chat_list:
             if user.uid == author_id:
                 print('you have been blocked by {}'.format(user.name))
                 client.blockUser(user.uid)
                 print('you have blocked {}'.format(user.name))

     def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        mes_thread2 = Client.fetchThreadMessages(author_id, limit=20)
        mes_thread2.reverse()
        mes_list = []
        pre_mes = 'Good {}..i\'m Claudia a bot created by seyi to control his social media accounts..it would be nice chatting with you'.format(part_of_day(h))
        if author_id != self.uid:
              self.name(author_id)
              for mes in mes_thread2:
                  mes_list.append(mes.text)
              if pre_mes in mes_list:     
                  pass
                  # self.send(message_object, thread_id=thread_id, thread_type=thread_type)
              else:
                  time.sleep(10)
                  self.send(Message(text=pre_mes), thread_id=author_id, thread_type=thread_type)
        else:
            print('your message has been sent')
            # self.send(message_object, thread_id=thread_id, thread_type=thread_type)
with open("session.json") as f:
    cookies = json.load(f)
client = Chatbot(email, password,session_cookies=cookies)
client.listen()
