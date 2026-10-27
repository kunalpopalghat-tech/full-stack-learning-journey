files = ["abc.txt","txt.csv","myfiles.xlxs","file.pdf","csv.json","file.csv"]

def find_valid_file(f):
    chotu_list =[]
    for i in f :

        if ".csv" in i or ".xlxs" in i :

            chotu_list.append(i)
    print(chotu_list)

find_valid_file(files) 