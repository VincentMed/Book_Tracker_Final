# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:09:10 2022

@author: Vincent Medrano
"""
import pprint

class book(object):

    def __init__(self):
        self.key = "key"
        self.author = "author"
        self.length = 0
        self.genre = "genre"
        self.sel = "selection"
        self.library = {}
    
    
    def getChoice(self):
        print("**************************************")
        print("Options")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Edit Book")
        print("4. Display Library")
        print("5. Genre search")
        print("6. Exit")
        print("**************************************\n")

        choice = 0
        
        while choice not in ("1" , "2", "3", "4", "5", "6"):
            choice = input("Enter the number of your choice...\n")
        
        if choice == "1":
            self.add_book()
        elif choice == "2":
            self.delete()
        elif choice == "3":
            self.edit()
        elif choice == "4":
            self.display()
        elif choice == "5":
            self.genre_search()
        else:
            print("You have exited the program!\nGoodbye!")
            exit
    #Add book function   
    def add_book(self):
        for i in range(1):
            self.key = input("Enter Title of Book...\n")
            self.author = input("Enter the name of Author...\n")
            self.length = int(input("Enter number of pages...\n"))
            self.genre = input("Which genre:\n'Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Thriller', 'Unknown'\n")
            self.library[self.key] = {"Author": self.author, "Length": self.length, "Genre": self.genre }        
            print(book.display(self))        
        
        book.getChoice(self)

    #Delete function
    def delete(self):
        print("Which book would you like to delete?\n")
        for key in self.library:
            print(key)

        remove = input("Type name of book you want deleted\n")

        del self.library[remove]

        print("Book has been deleted: Current Library is:")
        book.display(self)

    #edit existing library item
    def edit(self):
        print("Which book would you like to edit?\n")
        for key in self.library:
            print(key)
            #TODO delete key, replace with new key and values
        self.remove = input()
        
        del self.library[self.remove]

        book.add_book(self)
            
    #Display books in library function
    def display(self):
        print("Library items:")

        for key, value in self.library.items():
            print(key, ' - ', value)
            print('----------------------------')
            
        book.getChoice(self)

    def genre_search(self):
        print("Which genre would you like to search?\n")
        self.target = input("'Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Thriller', 'Unknown'\n")
        
        pass  
        
###############################################################################

book_obj = book()
book_obj.getChoice()

