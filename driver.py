class Driver:
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
    def miles_driven(self):
        return self._miles_driven
    @miles_driven.setter
    def miles_driven(self, miles):
        self._miles_driven = miles
    @miles_driven.deleter
    def miles_driven(self):
        del self._miles_driven

    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, rating):
        self._rating = rating
    @rating.deleter
    def rating(self):
        del self._rating


    #@rating.setter

    # def __init__(self, _first_name, _last_name, _miles_driven, _rating):
    #     self.first = _first_name
    #     self.last = _last_name
    #     self.miles_driven = _miles_driven
    #     self.rating = _rating
    def greet_passenger(self):
        return "Hello! I'll be your driver today. My name is " + self._first + ' ' + self._last
