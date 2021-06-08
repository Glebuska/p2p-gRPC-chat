import threading

from datetime import datetime
from tkinter import *

import grpc

import chat_pb2 as chat
import chat_pb2_grpc as rpc


class Client:

    def __init__(self, u: str, window, address, port):
        self.window = window
        self.username = u
        channel = grpc.insecure_channel(address + ':' + str(port))
        self.conn = rpc.ServerStub(channel)
        threading.Thread(target=self.__listen_for_messages, daemon=True).start()
        self.__setup_ui()
        self.window.mainloop()

    def __listen_for_messages(self):
        for note in self.conn.ChatStream(chat.MyEmptyMessage()):
            self.chat_list.insert(END, "{}[{}]: {}\n".format(note.name, datetime.now().strftime('%H:%M:%S'),
                                                             note.message))

    def send_message(self, event):
        message = self.entry_message.get()
        if message != '':
            n = chat.MyMessage()
            n.name = self.username
            n.message = message
            self.conn.SendNote(n)
            self.entry_message.delete(0, 'end')

    def __setup_ui(self):
        self.chat_list = Text()
        self.chat_list.pack(side=TOP)
        self.lbl_username = Label(self.window, text=self.username)
        self.lbl_username.pack(side=LEFT)
        self.entry_message = Entry(self.window, bd=5)
        self.entry_message.bind('<Return>', self.send_message)
        self.entry_message.focus()
        self.entry_message.pack(side=BOTTOM)
