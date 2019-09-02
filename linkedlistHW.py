# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:14:19 2019

@author: Lori
"""

class Node :
    def __init__(self , val= None ):
        self.val = val
        self.link = None
class LinkedList :
    def __init__( self ):
        self.head= None
        
    def printlist(self):
        current_node=self.head
        while current_node !=None:
            print(current_node.val)
            current_node=current_node.link
    def append(self,val ):
        current_node=self.head
        while current_node.link !=None:
            current_node=current_node.link
        current_node.link=Node(val)
    def insert_pos(self,pos,val ):
         if pos > 0:
             current_node=self.head
             for count in range(pos -1):
                 current_node=current_node.link
             next_link=current_node.link
             current_node.link=Node(val)
             current_node.link.link=next_link
         else:
            next_link=self.head
            self.head=Node(val)
            self.head.link=next_link
    def update_pos(self,pos,val):
        current_node=self.head
        for count in range(pos):
            current_node=current_node.link
        current_node.val=val
        
    def delete_pos(self,pos):
        if pos > 0:
            current_node=self.head
            for count in range(pos- 1):
                current_node=current_node.link
                current_node.link=current_node.link.link
        else :
            self.head=self.head.link

    def search(self,search_val):
        if self.head.val == search_val:
            return self.head
        current_node=self.head
        while current_node.link != None:
            current_node=current_node.link
            if current_node.val == search_val:
                return current_node
            return None

my_list = LinkedList ()
my_list . head = Node (5)
my_list . append (10)
my_list . append (13)

search_node = my_list . search (10)
print ( search_node )
my_list=LinkedList()
my_list.head=Node(5)
my_list.append(10)
my_list.append(13)

my_list.insert_pos(1,100)
my_list.delete_pos(1)

my_list.printlist()

my_list=LinkedList()
my_list.head=Node(5)
my_list.append(10)
my_list.append(13)

my_list.update_pos(1,100)

my_list.printlist()       
my_list=LinkedList()
my_list.head=Node(5)
my_list.append(10)
my_list.append(13)

my_list.insert_pos(1,100)

my_list.printlist()
  
my_list=LinkedList()
my_list.head=Node(5)
my_list.append(10)
my_list.append(13)

my_list.printlist()
        
my_list=LinkedList()

my_list.head=Node(5)
n2 =Node(10)
n3 =Node(13)

my_list.head.link=n2
n2.link=n3

print (my_list.head.val, my_list.head.link)
print (n2.val,n2.link)
print (n3.val,n3.link)
print (n2.val)
n2.val=50
print(n2.val)

my_list.printlist()