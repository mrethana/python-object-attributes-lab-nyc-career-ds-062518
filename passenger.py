class Passenger:
    @property
    def first(self):
        return self._first
    @first.setter
    def first(self, name):
        self._first = name
    @first.deleter
    def first(self):
        del self._first

    @property
    def last(self):
        return self._last
    @last.setter
    def last(self, name):
        self._last = name
    @last.deleter
    def last(self):
        del self._last

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email
    @email.deleter
    def email(self):
        del self._email

    #     #@first.setter
    # def first(self, name):
    #     self._first = name
    # #@last_name.setter
    # def last(self, name):
    #     self._last = name
    #     #@miles.setter
    # def email(self, email):
    #     self._email = email
        #@rating.setter
    def yell_name(self):
        return self._first.upper() + " " + self._last.upper()
