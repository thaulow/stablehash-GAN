import os
import ast

image_folder = '/volumes/1/aligned/'
stablehash_folder =  '/home/ubuntu/trainingfiles/frgc_centers_converted/'
mapping_file =  '/home/ubuntu/trainingfiles/frgc_results_cluster_id_to_subjects.txt'
output_file =  '/home/ubuntu/stablehash-reconstruct/training_data-100percent.csv'

cluster_list = []

o = open(output_file, "w")
o.write("img_dir;stablehash_dir\n")

mapping_file = open(mapping_file, "r")
clusters = mapping_file.readlines()
count = 0

for line in clusters:
    img_var = 0
    if count > 1:
        #Get the first variable and removes spaces and whitespaces.
        x = line.strip().replace(" ","").split(":")
        stablehash_var = x[0]  
        y = ast.literal_eval(x[1])
        cluster_list.append([stablehash_var, y])
    count += 1

for path in os.scandir(image_folder):
    if path.is_file():
        for cluster_data in cluster_list:
            for image_id in cluster_data[1]:
                if image_id in path.name: # and int(cluster_data[0]) < 44:
                    o.write(image_folder+path.name+";"+stablehash_folder+'frgc_cluster_'+cluster_data[0]+".npy\n")
                    
print("Output file generated")
