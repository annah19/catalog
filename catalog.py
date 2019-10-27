

class Item:

    def __init__(self, name="", category=""):

        self.__name = name
        self.__category = category

    def get_name(self):
        '''Return the private variable'''
        # Only this class can read the private variable
        # so we return it to use it in another class
        return self.__name

    def set_name(self,new_name):
        '''Change the name''' 

        self.__name = new_name

    def set_category(self,new_category):
        '''Change the category'''

        self.__category = new_category

    def __str__(self):
        return "Name: {}, Category: {}".format(self.__name,self.__category)


class Catalog:

    def __init__(self,name=""):
        self.__name = name
        self.__collection = []

    def add(self,item):
        '''Add each instance into a list'''

        self.__collection.append(item)
        
    def remove(self,remove_item):
        '''Remove requested item'''

        self.__collection.remove(remove_item)

    def set_name(self,new_name):
        '''Set the catalog list name'''

        self.__name = new_name

    def find_item_by_name(self,find_this_name):
        '''Return only the instance with the requested name'''

        for item in self.__collection:
            if item.get_name() == find_this_name:

                return item

    def clear(self):
        '''Remove everything from the Catalog list'''

        self.__collection = []


    def __str__(self):
        '''List the items in the Catalog list along with the Catalogs name'''
        item_str = "Catalog " + self.__name + ":" 

        for item in self.__collection:
            item_str += "\n\t"+ str(item)

        return item_str
        

