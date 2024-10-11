#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title = title
        self.page_count = page_count
        
    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self,value):
        self._title= value

    @property
    def page_count(self):
        return self._page_count
        
    @page_count.setter
    def page_count(self,value):
        if(type(value)is not int):
            print("page_count must be an integer")
        else:
            self._page_count=value

    def turn_page(page):
        print("Flipping the page...wow, you read fast!")