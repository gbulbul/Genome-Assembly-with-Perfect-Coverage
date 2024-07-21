# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:41:46 2024

@author: gbulb
"""
class Genome_Assembly_with_Perfect_Coverage:
    def find_the_most_frequent(list_of_strings):
        list_of_counts_for_each_base=[]
        for j,string in enumerate(list_of_strings):
            counter_A,counter_C,counter_G,counter_T=0,0,0,0
            for i in range(len(string1)):
                if string[i]=='A':
                   counter_A+=1
                elif string[i]=='C':
                   counter_C+=1
                elif string[i]=='G':
                    counter_G+=1
                elif string[i]=='T':
                    counter_T+=1
            list_of_counts_for_each_base.append((counter_A,counter_C,counter_G,counter_T))
        return list_of_counts_for_each_base
    def determine_the_letters(list_of_counts_for_each_base):
        SUPERSTRING=''
        A_count,C_count,G_count,T_count=0,0,0,0
        for i,idx in enumerate(list_of_counts_for_each_base):
            for j in range(len(list_of_counts_for_each_base[1])):
                if j==0:
                   if A_count<=idx[j]:
                      A_count=idx[j]
                elif j==1:
                    if C_count<=idx[j]:
                       C_count=idx[j]                  
                elif j==2:
                   if G_count<=idx[j]:
                      G_count=idx[j]
                elif j==3:
                   if T_count<idx[j]:
                      T_count=idx[j]
        #print(f'G_count:{G_count},A_count:{A_count},T_count:{T_count},C_count:{C_count}')
        SUPERSTRING=G_count*'G'+''+'A'*A_count+''+'T'*T_count+''+'C'*C_count
        print(SUPERSTRING)
if __name__=="__main__":  
    string1,string2,string3,string4,string5,string6,string7='ATTAC','TACAG','GATTA','ACAGA','CAGAT','TTACA','AGATT'
    list_of_strings=[string1,string2,string3,string4,string5,string6,string7]
    list_of_counts_for_each_base=Genome_Assembly_with_Perfect_Coverage.find_the_most_frequent(list_of_strings)   
    Genome_Assembly_with_Perfect_Coverage.determine_the_letters(list_of_counts_for_each_base)