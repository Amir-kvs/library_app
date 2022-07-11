class Book:
    def __int__(self, title, wname, tname, translate, avalable):
        self.title = title
        self.wname = wname
        self.tname = tname
        self.translate = translate
        self.is_avalable = is_avalable
    def display(self):
        print('Name: ' + self.title)
        print('Writer: ' + self.wname)
        if self.translate:
            print('Translator: ' + self.tname)
        print('Avalable? ' + str(self.avalable))