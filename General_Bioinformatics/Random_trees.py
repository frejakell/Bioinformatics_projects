import itertools
from itertools import combinations
from itertools import combinations, permutations, product
import random
import string
import time
import sys

def Random_possible_trees(n):
    if n == 1:
        yield 'l'
    else:
        split=random.randint(1,n-1)
        
        left = Random_possible_trees(split)
        right = Random_possible_trees(n-split)
        for left, right in itertools.product(left, right):
            yield [left,right]
        
            
                
                
def main( arg1,arg2,arg3):
 
    leaves=list(string.ascii_lowercase)
    leaf_list=[]
    for i,j in product(leaves,leaves):
        leaf_list.append(i+j)
    leaves=leaf_list[0:arg2]
    trees=[]
    n = arg2
    number_trees= arg1
    if(arg3.upper()=="R"):
        for i in range(number_trees):
            leaf_list=leaves.copy()
            tree_temp=''
            for s in Random_possible_trees(n):
                tree=str(s)
           
            for c in tree:    
                if c is 'l':
                    new_leaf=random.choice(leaf_list)
                    tree_temp+=new_leaf
                    leaf_list.remove(new_leaf)
                else:
                    tree_temp+=c
            tree_temp=str(tree_temp).replace("'", "")        
            tree_temp=str(tree_temp).replace("[", "(")   
            tree_temp=str(tree_temp).replace("]", ")") 
            tree_temp=str(tree_temp)+';'  
            trees.append(tree_temp)
    elif(arg3.upper()=="U"):
            out_g=leaves.pop()
            for i in range(number_trees):
                leaf_list=leaves.copy()
                
                tree_temp=''
                for s in Random_possible_trees(n-1):
                    tree=str(s)
               
                for c in tree:    
                    if c is 'l':
                        new_leaf=random.choice(leaf_list)
                        tree_temp+=new_leaf
                        
                        leaf_list.remove(new_leaf)
                        
                    else:
                        tree_temp+=c
                tree_temp=str(tree_temp).replace("'", "")        
                tree_temp=str(tree_temp).replace("[", "(")   
                tree_temp=str(tree_temp).replace("]", ")") 
               
                tree_temp='('+tree_temp+ ','+out_g +');'
                trees.append(tree_temp)
    
    return(trees)           
    
if __name__ == '__main__':
    arg1=4
    arg2=4
    arg3="U"
    main(arg1,arg2,arg3)