import suffix_tree as suffix
import time
import sys


def tandem_repeat(aTree,branching, nonbranching,treenodes):    
    S = aTree.text
    for t in treenodes:
        v_leaflist = aTree.find_nodelist(t)
 
        Dv = len( t.path )  
        for i in v_leaflist:
            j = i.id + Dv

            for n in v_leaflist:
                if n.id == j:
                    test1 = True
                    break
                test1=False
            s_index = i.id - 1
            if test1 is True:
                if S[s_index] != S[s_index + (2 * Dv)]:
                    test2 = True 
                else:
                    test2=False

                if test1 is True and test2 is True:
                   
                    
                    t_len = 2 * Dv
                    branching.add((s_index,S[s_index: s_index+ t_len]))
                    k = i.id - 1
                    
                    for i in range(k, 0, -1):
                        s_index = i - 1
                        if S[s_index] != S[s_index + t_len ]: 
                            break
                        nonbranchingtandem = S[s_index: s_index + t_len]
                        nonbranching.add((i, nonbranchingtandem))
                        

    return branching, nonbranching, len(branching), len(nonbranching)

def dfs_tr(aNode, dfs):
    pos=len(dfs)
    if len(aNode.children) > 0:
        aNode.leaflist_start = pos
        for child in aNode.children:
            dfs=dfs_tr(child,dfs)
        pos=len(dfs)-1
        aNode.leaflist_end = pos    
    else:
        aNode.leaflist_end = pos
        aNode.leaflist_start = pos
        dfs.append(aNode)
    return dfs




def tandem_repeat_SpeedUp(aTree, branching, nonbranching,treenodes):

    dfs_temp = []
    dfs_order=dfs_tr(aTree.root,dfs_temp)
    
    for v in treenodes:
        
        if v.children:
            v_leaf_start=v.leaflist_start
            v_leaf_End=v.leaflist_end
            LLvm=[]
            for c in v.children:
                leaf_start=c.leaflist_start
                leaf_End=c.leaflist_end
                LLvm = LLvm+[(leaf_start,leaf_End, leaf_End - leaf_start + 1)]
           
            LLvm = max(LLvm, key=lambda x: x[2])
            LLvm = LLvm[0:2]
            LLmv = list(set(range(v_leaf_start, v_leaf_End + 1)) -
                        set(range(LLvm[0], LLvm[1] + 1)))
          
            LLmv_temp = []
            for i in LLmv:
                LLmv_temp.append(dfs_order[i] )
            LLmv=LLmv_temp
            Dv = len(v.path)
            S = aTree.text
            LLv_actual = dfs_order[v_leaf_start:v_leaf_End + 1]  
            for i in LLmv:
                
                j = i.id + Dv
                
                for n in LLv_actual :
                    if n.id == j:
                        test1 = True
                        break
                    test1=False
                if test1 is True:
                    comp1=i.id - 1
                    comp2= i.id + (2 * Dv) - 1
                    test2=False
                    if S[comp1] != S[comp2]:
                        test2 = True 
                 
                    if test1 is True and test2 is True:
                        branching.add((i.id, S[comp1: comp2]))

                        k = i.id - 1
                        
                        for i in range(k, 0, -1):
                            comp1=i - 1
                            comp2= i + (2 * Dv) - 1
                            if S[comp1] != S[comp2]:
                                break
                        
                            nonbranching.add((i, S[comp1: comp2]))
                            
            for j in LLmv:
                
                i = j.id - Dv
                
                for n in LLv_actual :
                   if n.id ==i:
                       test1 = True
                       break
                   test1=False
                if test1:
                    comp1=i-1
                    comp2= i + (2 * Dv) - 1

                test2=False  
                if test1 is True:
                    if  S[comp1] != S[comp2]:
                        test2 = True 
                                        
                    
                    if test1 is True and test2 is True:
                        branching.add((i, S[comp1:comp2]))

                        k = i - 1
                        for i in range(k, 0, -1):
                            if S[i - 1] != S[i + (2 * Dv) - 1]:
                                break
                           
                            
                            nonbranching.add((i, S[i - 1: i + (2 * Dv) - 1]))
                           

  

    return branching, nonbranching, len(branching), len(nonbranching)



def main(aFile):


    branching = set()
    nonbranching = set()
    alg_choice = False
    file=aFile
    
    with open(file, 'r') as myfile:
        
        text=myfile.read()

    tree = suffix.Tree(text)
    treenodes = []
    tree.traverse(lambda x: treenodes.append(x))
    branching = set()
    nonbranching = set()
    if alg_choice:
        branching_list, nonbranching_list,branching_count, nonbranching_count = tandem_repeat(tree,branching, nonbranching,treenodes)
        print('%i %i' % (branching_count, nonbranching_count))
        return branching_count,nonbranching_count
    else:
        branching_list, nonbranching_list,branching_count, nonbranching_count= tandem_repeat_SpeedUp(tree,branching, nonbranching,treenodes)
        print('%i %i' % (branching_count, nonbranching_count))
        return branching_count,nonbranching_count

   

if __name__ == '__main__':

    main(sys.argv[1])
