import collections
import datetime

class Messages:
    def __init__(self):
        self.messages_sent_today = collections.defaultdict(int)
        self.last_reset = datetime.datetime.now()
    
    def reset(self):
        self.messages_sent_today = collections.defaultdict(int)
        self.last_reset = datetime.datetime.now()

    def is_time_for_reset(self):
        return (datetime.datetime.now() - self.last_reset).days >= 1

    def get_author_message_count(self, author):
        if self.is_time_for_reset():
            self.reset()
        return self.messages_sent_today[author]

    def increment_author_message_count(self, author):
        self.messages_sent_today[author] += 1