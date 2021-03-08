import sys
import numpy as np
from ete3 import Tree
import time

node_dict = dict()

def Next_Joining(A,Node_names,count, N,Node_count):
	tL = list()
	Mat_sum = np.sum(A,0) 
	n = A.shape[0] 
	new_name = Node_count[count]
	i=0
	j = 0
	if n <= 2:
		dist = A[1][0]
		Add_node = node_dict[Node_names[0]]
		if Node_names[1] in Node_count: 
			remove_node=Node_names[1]
			Node_names[1]='(' + node_dict[Node_names[1]]['L'] + node_dict[Node_names[1]]['R'] +')'
			del node_dict[remove_node]   
		Add_node['U'] = "," +str(Node_names[1])+':'+str('%3.5f' %dist)
		
		return None,Node_names


	min_dist = A[i][j]
	for r in range(A.shape[0]):
		
		
		if r == 0:  
			continue
		
		if r==1:c=0

		else:
			
		
			test_col = np.array(((n-2)*A[r][:(r-1)])-Mat_sum[:(r-1)]) 
			test_col=list(np.asarray(test_col)-Mat_sum[r]) 
			c=np.argmin(test_col) 
		    
		dist = A[r][c] 
		Mat_col = Mat_sum[c]
		Mat_row = Mat_sum[r]
		value = (n-2)*dist - Mat_col-Mat_row
		if value <= min_dist: i,j,min_dist = r,c,value
  			
	

	

	dist =  A[i][j]
	 
	dist_i = dist/2 + (Mat_sum[i] - Mat_sum[j])/(2*(n-2))
	dist_j = dist - dist_i
	
	if Node_names[j] in Node_count: 
		remove_node=Node_names[j]
		Node_names[j]='(' + node_dict[Node_names[j]]['L'] + node_dict[Node_names[j]]['R'] +')'
		del node_dict[remove_node]
	if Node_names[i] in Node_count: 
		remove_node=Node_names[i]
		Node_names[i]='(' + node_dict[Node_names[i]]['L'] + node_dict[Node_names[i]]['R'] +')'
		del node_dict[remove_node]      
	Left=str(Node_names[i])+':'+str('%3.5f' %dist_i) +','
	Right=str(Node_names[j])+':'+str('%3.5f' %dist_j)
	node = { 'L': Left,     
			 'R':Right, }
	node_dict[new_name] = node
	
	

	
	ij_dist = A[i][j]
	for k in range(len(A[0])):
		if k == i or k == j:  continue
		
		dist = (A[i][k] + A[j][k] - ij_dist)/2
		
		tL.append(dist)

	
	if i < j:  i,j = j,i
	n_col = np.array(tL)
	n_col.shape = (len(n_col),1)
	n_row = np.array([0] + tL)
	n_row.shape = (1,len(n_row))
	Node_del = list(range(n))     
	Node_del.remove(i)
	if j!=i:Node_del.remove(j)
	A1 = A[Node_del,:]
	A = A1[:,Node_del]     


    
	Node_names = [new_name] + Node_names[:j] + Node_names[j+1:i] + Node_names[i+1:]
	

	A = np.hstack([n_col,A])
	A = np.vstack([n_row,A])
	
	return A,Node_names
	


  

	
def main(argv):
  start=time.time()
  fn = argv[1]
  f = open(fn,'r')
  N=int(f.readline())


  l=[]
  for line in f:
    line = line.strip()
    if len(line) > 1:
       l.append([a for a in line.split()]) 

 
  
  print("size is :", N)
  count = 0
  Node_names = [ row[:1] for row in l]
  data=[ row[1:]for row in l ]

  data_nj = np.array(data, dtype=float)
  data_nj .shape = (N,N)
  Node_count=list(range(N)) 

  

  while True:

    data_nj ,Node_names = Next_Joining(data_nj,Node_names,count,N,Node_count)
    if data_nj is None: 
        break
    count += 1



  Node_List = "" 
 
  for node in node_dict.keys():
      Node_string=""
      for key in ['L','R','U']:
          nD = node_dict[node]
          if not key in nD:
            continue
          v = nD[key]
          Node_string= Node_string+ v + " "
      print()
      Node_List= Node_List  + Node_string
  Node_List='('+ Node_List+ ');'
  Node_List=Node_List.replace("['", "")
  Node_List=Node_List.replace("']", "")
  print(Node_List)
  print(time.time()-start)
  #t1=Tree(Node_List)
  #print(t1)


if __name__ == "__main__":
	main(sys.argv)