import chat_pb2 as chat
import chat_pb2_grpc as rpc


class ChatServer(rpc.ServerServicer):

    def __init__(self):
        self.chats = []

    def ChatStream(self, request_iterator, context):
        lastindex = 0
        while True:
            while len(self.chats) > lastindex:
                n = self.chats[lastindex]
                lastindex += 1
                yield n

    def SendNote(self, request: chat.MyMessage, context):
        self.chats.append(request)
        return chat.MyEmptyMessage()
