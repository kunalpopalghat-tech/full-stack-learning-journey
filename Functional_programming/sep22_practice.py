Pruducts = ["TV","Laptop","Pencil","Mobile","Chair","Table","Chatrger"]

Category = ["Elecronics","Elecronics","Stationary","Elecronics","Furniture","Furniture","Elecronics"]

def get_products_by_cat(p,c):
    Chotu_list = []

    for i,cat in enumerate(c):
        if cat == "Elecronics" :
            Chotu_list.append(p[i])
    return Chotu_list



Pruduct_list = get_products_by_cat(Pruducts,Category)

print(Pruduct_list)