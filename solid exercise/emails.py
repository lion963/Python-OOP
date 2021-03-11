from abc import ABC, abstractmethod

class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

class IContent(ABC):

    @abstractmethod
    def format_content(self):
        pass

class MyContent(IContent):
    def __init__(self, content):
        self.content = content

    def format_content(self):
        return ''.join(['<myML>', self.content, '</myML>'])




class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content=content.format_content()

    def __repr__(self):
        template = f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"
        return template


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)







