import collections
import datetime

class RecentMessages:
    def __init__(self, save_time_mins=2, max_word_count=8):
        self.save_time_mins = save_time_mins
        self.max_word_count = max_word_count
        self.message_history = collections.defaultdict(list)
        self.first_message_time = {}

    def add_message(self, message):
        if message.author not in self.first_message_time:
            self.first_message_time[message.author] = datetime.datetime.now()
        self.message_history[message.author].append(message)

    def messages_word_count(self, user):
        return sum([len(message.content.split()) for message in self.message_history[user]])

    def is_time_for_reset(self,user):
        if user not in self.first_message_time:
            return False
        return (datetime.datetime.now() - self.first_message_time[user]).seconds >= self.save_time_mins * 60

    def get_concatenated_messages(self, user):
        return ". ".join([message.content for message in self.message_history[user]])

    def reset(self, user):
        self.message_history[user] = []
        del self.first_message_time[user]

    def get_response(self, message):
        author = message.author
        if self.is_time_for_reset(author):
            self.reset(author)
        self.add_message(message)
        if self.messages_word_count(author) > self.max_word_count:
            concatenated_messages = self.get_concatenated_messages(author)
            self.reset(author)
            return concatenated_messages

class MessageCounts:
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