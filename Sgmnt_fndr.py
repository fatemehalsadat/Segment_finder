import numpy as np 
import pandas as pd 

#HH2: The hours in which the network topology is constant {i:t_i,t_i+1,...,t_j}
#dict_L: dictionary of lines: segment numbers as key   
#M: Dictionary of lines that their segment should be found {t:lines}
  
seg = {} # the resultant segments
for n, v in dict_L.items():
	seg.setdefault(n, [])

#all indices: the aaa containts t,m,a:segment number by time,key: segment number
aaa = np.zeros((1000000,4)).astype(int)
a0 = 0
#find segments of each (m,t)
for t in M.keys():
	for a, b in HH2.items():  
		if t in b: #if any(b == t):
			t_h = a 
			aaa[a0,2] = a
	for m in M[t]:#for m,t in M.items():
		aaa[a0,0:2] = t,m            
		for key, val in dict_L.items():
			if str(t_h)+str(',') in key:                    
				if m+1 in (val[:,0]).astype(int): 
					aaa[a0,3] =  list(dict_L).index(key)
		a0 += 1

aaa = aaa[:a0,:]
aac = np.delete(aaa,2,1).astype(int) # if just instances are to be used
#unique_rows_02 = np.unique(aac[:,(0,2)], axis=0) 
unique_rows_12 = np.unique(aac[:,(1,2)], axis=0)
unique_seg = np.unique(aac[:,-1]).astype(int)

M2 = {}       
#seg: each dictionary key is the segment name and values are the time index and line index
for i in unique_seg: 
	ind_l = unique_rows_12[np.where(unique_rows_12[:,1]==i)[0],0]
	M2.setdefault(list(dict_L)[i], [])    
	M3 = {}        
	for i1 in ind_l:
		M3.setdefault(i1,[])
		M3[i1]=aac[np.where((aac[:,1]==i1)&(aac[:,2]==i))[0],0]
	M2[list(dict_L)[i]] = M3
M2 = dict((k, v) for k, v in M2.items() if len(v) > 0) #seg name:{t:m s}
