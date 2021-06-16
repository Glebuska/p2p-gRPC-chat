import resources.chat_pb2 as chat
import resources.chat_pb2_grpc as rpc


class ChatServer(rpc.ServerServicer):

    def __init__(self):
        """Initialize a chat content as a list of messages."""
        self.chats = []

    def ChatStream(self, request_iterator, context):
        """Return a last message index."""
        lastindex = 0
        while True:
            if len(self.chats) > lastindex:
                n = self.chats[lastindex]
                lastindex += 1
                yield n

    def SendNote(self, request: chat.MyMessage, context):
        """Handle a sent message."""
        self.chats.append(request)
        return chat.MyEmptyMessage()
