#!/usr/bin/env python
from itertools import count
import os.path
import time
import sys



class Tree:
    def __init__(self, Text):
        self.root = Node(0, None)
        self.text = Text + "$"
        self._BulidSuffixTree(len(self.text))
    def traverse(self, fn):
        self._traverse(self.root, fn)

    def _traverse(self, aNode, fn):
        if len(aNode.children) == 0:
            fn(aNode)
        else:
            fn(aNode)
            for child in aNode.children:
                self._traverse(child, fn)
    def _findNode(self, Node, String):
        for child in Node.children:
            current_IN_Edge = child.IN_Edge
            CommonPrefix=os.path.commonprefix([current_IN_Edge, String])

            if  CommonPrefix:
                return child,  CommonPrefix
        return None, ''

    def _BulidSuffixTree(self, last_id):
        new_id=0
        
        for i in range(last_id):
            current_node = self.root
            current_suffix = self.text[i:last_id]
            

            child, shared_prefix = self._findNode(current_node,current_suffix)
            temp_path = shared_prefix

            while shared_prefix:
                if (shared_prefix == child.IN_Edge):
                    current_suffix = current_suffix[len(shared_prefix):]
                    current_node = child
                    child, shared_prefix = self._findNode(child,current_suffix)
                    temp_path  =temp_path + shared_prefix
                else: 
                    break

            if  shared_prefix:
                new_id=0          
                new_node = Node(new_id, current_node, shared_prefix, temp_path)
                current_node.children.append(new_node)
                current_node.children.remove(child)
                new_node.children.append(child)

                
                child.parent = new_node
                child.IN_Edge = child.IN_Edge[len(shared_prefix):]
                new_path = temp_path + child.IN_Edge 
                child.path=new_path
                new_id=i+1
                new_leaf = Node(new_id,new_node,current_suffix[len(shared_prefix):],temp_path + current_suffix[len(shared_prefix):])
                new_node.children.append(new_leaf)
                
            else:
               new_id=i+1
               new_child = Node(new_id,current_node,current_suffix,current_suffix)
               current_node.children.append(new_child)
                

    def find_nodelist(self, Node):
        node_list = []
        leaf_list = []
        if  Node.children:
            for c in Node.children:
                recursive_nodes_list = self.find_nodelist(c)
                node_list.append(recursive_nodes_list)

            for Temp_list in node_list:
                for i in Temp_list:
                    leaf_list.append(i)
            return  leaf_list
           
        else:
            return [Node]

 
    def traversal(self, Node, Pattern):
        for child in Node.children:
            shared_prefix = os.path.commonprefix([Pattern, child.IN_Edge])
            
            if Pattern is shared_prefix:
                node_indices=[]
                for node in self.find_nodelist(child):
                    node_indices.append(node.id) 
                return node_indices

            elif len(shared_prefix) < len(Pattern) and len(shared_prefix) > 0:
              
                remaining_pattern = Pattern[len(shared_prefix):]
                nodes_indices = self.traversal(child, remaining_pattern)
                return nodes_indices
       
        return []
        
    def search_pattern(self, Pattern):
 
        result = self.traversal(self.root, Pattern)
        result.sort()
       
        return result




class Node:
    
    def __init__(self, Id, Parent, Edge='', Path=''):
        
        self.id = Id
        self.path = Path
        self.children = []
        self.parent = Parent
        self.IN_Edge = Edge
        

def main(aFile, aPattern):
  
    file=aFile 
    with open(file, 'r') as myfile:
        text=myfile.read()
    start_time = time.time()
    tree = Tree(text)
    end_time=time.time() - start_time
    print('Suffix tree construction time: %s' % end_time )
    start_time = time.time()
    search_result = tree.search_pattern(aPattern)
    end_time=time.time() - start_time
    print('Pattern searching time: %s' % end_time)
    
    if search_result==[]:
        print("---------------Pattern not found in text--------------")
    else:
        print("Pattern found at indices:")
        print(' '.join(map(str, search_result)))
if __name__ == '__main__':

    main(sys.argv[1], sys.argv[2])
