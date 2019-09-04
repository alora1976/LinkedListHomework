# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:42:28 2019

@author: Lori
"""
#Linked Lists

class Node:
    
    def __init__(self, val=None):
        self.val = val
        self.link = None
class LinkedList:
    
    def __init__ (self):
        self.head = None
        
    def printlist(self):

        current_node=self.head

        while current_node !=None:

            print(current_node.val)

            current_node=current_node.link
    def append(self,val):
        current_node=self.head
        while current_node.link != None:
            current_node = current_node.link
        current_node.link =Node(val)
        
    def insert_pos(self,pos,val):
        if pos> 0:
            current_node = self.head
            for count in range (pos -1):
                current_node = current_node.link
            next_link = current_node.link
            current_node.link = Node (val)
            current_node.link.link = next_link
    def update_pos(self,pos,val):
        current_node = self.head
        for count in range (pos):
            current_node.val = val
            
    def delete_pos(self,pos):
        if pos > 0:
            current_node = self.head
            for count in range (pos - 1):
                current_node = current_node.link
            current_node.link = current_node.link.link
        else:
            self.head = self.head.link
            
    def search(self,search_val):
        if self.head.val == search_val :
            return self.head
        current_node = self.head
        while current_node.link != None:
            current_node = current_node.link
            if current_node.val == search_val:
                return current_node
        return None
    
        
n1=Node(5)#assign value inside node1
n2=Node(10)#assign value inside node2
n3=Node(13)#assign value inside node3

print(n1.val)#prints value inside node
print(n2.val)
print(n3.val)
print("\n")#creates a space between lines of code so this is easier to follow


my_list=LinkedList()
my_list.head =Node(5)
n2 =Node(10)
n3=Node(13)

my_list.head.link =n2
n2.link=n3

print(my_list.head.val,my_list.head.link)#prints value in node and memory location to next node
print(n2.val,n2.link)#prints value in node and memory location to next node
print(n3.val,n3.link)#prints value in node and memory location to next node(there is not a link to another node, so it returns none)
print("\n")#creates a space between lines of code so this is easier to follow

#updating the nodes
print(n2.val)#prints current value inside node2
n2.val=50#assigns new value inside node2
print(n2.val)#prints new value inside node2
print("\n")#creates a space between lines of code so this is easier to follow

#traversing a Linked List

my_list.printlist()

print("\n")#creates a space between lines of code so this is easier to follow
#appending to Linked List
my_list.append (10)
my_list.append(13)
my_list.printlist()

print("\n")#creates a space between lines of code so this is easier to follow
#inserting into a linked list
my_list.insert_pos(1,100)
my_list.printlist()
print("\n")#creates a space between lines of code so this is easier to follow

#updating Node

my_list.update_pos(2,100)
my_list.printlist()
print("\n")#creates a space between lines of code so this is easier to follow

#deleting from a linked list
my_list.delete_pos(1)
my_list.printlist()
print("\n")#creates a space between lines of code so this is easier to follow

#searching a Linked List

search_node = my_list.search(10)
print(search_node)
print("\n")#creates a space between lines of code so this is easier to follow
    
