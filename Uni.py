progress=0
trailing=0
exclude=0
retriever=0

def check(list_name,data_set):
    '''check each data set progression'''
    if (list_name[data_set][0]) == 120:     #to check data set belongs to student is "progress" or not
        print("Progress")
        global progress
        progress += 1
    elif (list_name[data_set][0])==100:      #to check data set belongs to student is "module trailer" or not
        print("Progress (module trailer)")
        global trailing
        trailing+=1
    elif (list_name[data_set][2])==120 or (list_name[data_set][2])==100 or (list_name[data_set][2])==80:    #to check data set belongs to student is "exclude" or not
        print("Exclude")
        global exclude
        exclude+=1
    else:
        print("Do not progress - module retriever")     #to check data set belongs to student is "module retriever" or not
        global retriever
        retriever+=1


data_list=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]



for i in range(len(data_list)):    #iterate every each data lists
    check(data_list,i) #to get progression outcome


progress_stars = progress * "*"         
module_trailer_stars = trailing * "*"
module_retriever_stars = retriever * "*"
exclude_stars = exclude * "*"
outcomes_total = progress + trailing + retriever + exclude  #get total of "progression outcomes"

print(f'''
Progress  {progress}: {progress_stars}
Trailing  {trailing}: {module_trailer_stars}
Retriever {retriever}: {module_retriever_stars}
Excluded  {exclude}: {exclude_stars}
{outcomes_total} outcomes in total.
''')
