# -*- coding: utf-8 -*-

import sys,os,time
import nj


files = os.listdir("unique_distance_matrices")
print(files)
with open("time_consuption.csv", 'w') as f:
#    for i in range(0, len(files)-1):
#        if files[i][0] != ".":
#            start = time.time()
#            os.system("quicktree -in m unique_distance_matrices/" + files[i])
#            end = time.time()
#            finish = end - start
#            num_of_seqs = files[i][0:files[i].index("_")]
#            f.writelines(str(finish)+","+str(num_of_seqs)+ ",quicktree,"+"\n")
#            print(finish, num_of_seqs)
#    
#    print("--------") 
#    for i in range(0, len(files)-1):
#        if files[i][0] != ".":
#            start = time.time()
#            os.system("rapidnj -i pd unique_distance_matrices/"+files[i]+ " -o t -x test_rapid"+str(i)+".newick")
#            end = time.time()
#            finish = end - start
#            num_of_seqs = files[i][0:files[i].index("_")]
#            f.writelines(str(finish)+","+str(num_of_seqs)+",rapidnj,"+"\n")
#            print(finish, num_of_seqs)
    
    print("--------") 
    for i in range(0, len(files)-1):
        if files[i][0] != ".":
            start = time.time()
            #os.system("python nj.py unique_distance_matrices/"+files[len(files)-1])
            nj.main("unique_distance_matrices/"+files[len(files)-6])
            end = time.time()
            finish = end - start
            num_of_seqs = files[i][0:files[i].index("_")]
            f.writelines(str(finish)+","+str(num_of_seqs)+",rapidnj,"+"\n")
            print(finish, num_of_seqs)