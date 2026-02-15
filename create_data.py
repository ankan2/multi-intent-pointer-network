import sys
import pandas as pd
import numpy as np

def count_words_in_a_string(S):
    return len(S.split()) - 1

def float_to_str(num):
    if np.isnan(num) == False:
        return str(int(num))
    else:
        return ""

def createdata(dataset_name, file1, file2, file3, file4, file5):
    df_partitions = pd.read_csv(dataset_name + "/" + dataset_name + "_partition.csv")
    df_partitions['Coarse_dominant'] = df_partitions['Coarse_dominant'].str.replace(' ', '_')
    df_partitions['Coarse_non_dominant'] = df_partitions['Coarse_non_dominant'].str.replace(' ', '_')
    df_partitions['Fine_dominant'] = df_partitions['Fine_dominant'].str.replace(' ', '_')
    df_partitions['Fine_non_dominant'] = df_partitions['Fine_non_dominant'].str.replace(' ', '_')    
    f1 = open(file1,"w")
    f2 = open(file2,"w")
    f3 = open(file3,"w")
    f4 = open(file4,"w")
    f5 = open(file5,"w")
    num_rows = df_partitions.shape[0]
    each_line_of_txt = ""
    for i in range(num_rows):
        each_line_of_txt = df_partitions.iloc[i]["Text"] + "\n"
        f1.write(each_line_of_txt)
    num_rows = df_partitions.shape[0]
    sub_text_coarse_labels = ""
    sub_text_fine_labels = ""
    for i in range(num_rows):
        each_line_of_txt = "0 " + float_to_str(df_partitions.iloc[i]["e1 (words)"]) + " " + float_to_str(df_partitions.iloc[i]["s2 (words)"]) + " " + str(count_words_in_a_string(df_partitions.iloc[i]["Text"]))
        sub_text_coarse_labels = " " + df_partitions.iloc[i]["Coarse_dominant"] + " " + df_partitions.iloc[i]["Coarse_non_dominant"] + "\n"
        sub_text_fine_labels = " " + df_partitions.iloc[i]["Fine_dominant"] + " " + df_partitions.iloc[i]["Fine_non_dominant"] + "\n"
        f2.write(each_line_of_txt + sub_text_coarse_labels)
        f3.write(each_line_of_txt + sub_text_fine_labels)
        # try:
        sub_tup_coarse_labels = df_partitions.iloc[i]["sentence1"] + " ; " + df_partitions.iloc[i]["sentence2"] + " ; " + df_partitions.iloc[i]["Coarse_dominant"] + " ; " + df_partitions.iloc[i]["Coarse_non_dominant"] + "\n"
        sub_tup_fine_labels = df_partitions.iloc[i]["sentence1"] + " ; " + df_partitions.iloc[i]["sentence2"] + " ; " + df_partitions.iloc[i]["Fine_dominant"] + " ; " + df_partitions.iloc[i]["Fine_non_dominant"] + "\n"
        f4.write(sub_tup_coarse_labels)
        f5.write(sub_tup_fine_labels)
        # except TypeError:
        #     print(df_partitions.iloc[i]["sentence1"], df_partitions.iloc[i]["sentence2"])


def split_to_train_test_and_dev(dataset_name, file1, file2, file3, file4, file5):
    df_partitions = pd.read_csv(dataset_name + "/" + dataset_name + "_partition.csv")
    df_partitions['Coarse_dominant'] = df_partitions['Coarse_dominant'].str.replace(' ', '_')
    df_partitions['Coarse_non_dominant'] = df_partitions['Coarse_non_dominant'].str.replace(' ', '_')
    df_partitions['Fine_dominant'] = df_partitions['Fine_dominant'].str.replace(' ', '_')
    df_partitions['Fine_non_dominant'] = df_partitions['Fine_non_dominant'].str.replace(' ', '_')        
    num_rows = df_partitions.shape[0]
    f1 = open(file1,"r")
    f2 = open(file2,"r")
    f3 = open(file3,"r")
    f4 = open(file4,"r")
    f5 = open(file5,"r")

    train_sent = open(dataset_name + "/train.sent", "w")
    dev_sent = open(dataset_name + "/dev.sent", "w")
    test_sent = open(dataset_name + "/test.sent", "w")

    train_coarse_pointer = open(dataset_name + "/coarse_train.pointer", "w")
    dev_coarse_pointer = open(dataset_name + "/coarse_dev.pointer", "w")
    test_coarse_pointer = open(dataset_name + "/coarse_test.pointer", "w")

    train_fine_pointer = open(dataset_name + "/fine_train.pointer", "w")
    dev_fine_pointer = open(dataset_name + "/fine_dev.pointer", "w")
    test_fine_pointer = open(dataset_name + "/fine_test.pointer", "w")

    train_tup_coarse = open(dataset_name + "/coarse_trainb_pt.tup", "w")
    dev_tup_coarse = open(dataset_name + "/coarse_devb_pt.tup", "w")
    test_tup_coarse = open(dataset_name + "/coarse_testb_pt.tup", "w")

    train_tup_fine = open(dataset_name + "/fine_trainb_pt.tup", "w")
    dev_tup_fine = open(dataset_name + "/fine_devb_pt.tup", "w")
    test_tup_fine = open(dataset_name + "/fine_testb_pt.tup", "w")

    for i in range(num_rows):
        sent = f1.readline()
        coarse_triplet = f2.readline()
        fine_triplet = f3.readline()
        coarse_tup = f4.readline()
        fine_tup = f5.readline()
        if i <= (0.8 * num_rows):
            #training set
            train_sent.write(sent)
            train_coarse_pointer.write(coarse_triplet)
            train_fine_pointer.write(fine_triplet)
            train_tup_coarse.write(coarse_tup)
            train_tup_fine.write(fine_tup)
        elif i <= (0.9 * num_rows):
            #dev set
            dev_sent.write(sent)
            dev_coarse_pointer.write(coarse_triplet)
            dev_fine_pointer.write(fine_triplet)
            dev_tup_coarse.write(coarse_tup)
            dev_tup_fine.write(fine_tup)
        else:
            #test set
            test_sent.write(sent)
            test_coarse_pointer.write(coarse_triplet)
            test_fine_pointer.write(fine_triplet)
            test_tup_coarse.write(coarse_tup)
            test_tup_fine.write(fine_tup)

def union_of_two_lists(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    return list(s1.union(s2))

def create_relation_txt_files(dataset_name):
    #coarse
    df_coarse = pd.read_csv(dataset_name + "/" + dataset_name + "_partition.csv")
    df_coarse['Coarse_dominant'] = df_coarse['Coarse_dominant'].str.replace(' ', '_')
    df_coarse['Coarse_non_dominant'] = df_coarse['Coarse_non_dominant'].str.replace(' ', '_')
    df_coarse['Fine_dominant'] = df_coarse['Fine_dominant'].str.replace(' ', '_')
    df_coarse['Fine_non_dominant'] = df_coarse['Fine_non_dominant'].str.replace(' ', '_')        
    l_dom = list(df_coarse["Coarse_dominant"])
    l_non_dom = list(df_coarse["Coarse_non_dominant"])
    l_rel = union_of_two_lists(l_dom, l_non_dom)
    f = open(dataset_name + "/" + "coarse_relation.txt", "w")
    for label in l_rel:
        f.write(label + "\n")
    f.close()

    #fine
    df_coarse = pd.read_csv(dataset_name + "/" + dataset_name + "_partition.csv")
    df_coarse['Coarse_dominant'] = df_coarse['Coarse_dominant'].str.replace(' ', '_')
    df_coarse['Coarse_non_dominant'] = df_coarse['Coarse_non_dominant'].str.replace(' ', '_')
    df_coarse['Fine_dominant'] = df_coarse['Fine_dominant'].str.replace(' ', '_')
    df_coarse['Fine_non_dominant'] = df_coarse['Fine_non_dominant'].str.replace(' ', '_')            
    l_dom = list(df_coarse["Fine_dominant"])
    l_non_dom = list(df_coarse["Fine_non_dominant"])
    l_rel = union_of_two_lists(l_dom, l_non_dom)
    f = open(dataset_name + "/" + "fine_relation.txt", "w")
    for label in l_rel:
        f.write(label + "\n")
    f.close()



def main():
    dataset_name = sys.argv[1]
    createdata(dataset_name, dataset_name + "/triplets.sent", dataset_name + "/coarse.pointer", dataset_name + "/fine.pointer", dataset_name + "/coarseb_pt.tup", dataset_name + "/fineb_pt.tup")
    split_to_train_test_and_dev(dataset_name, dataset_name + "/triplets.sent", dataset_name + "/coarse.pointer", dataset_name + "/fine.pointer", dataset_name + "/coarseb_pt.tup", dataset_name + "/fineb_pt.tup")
    create_relation_txt_files(dataset_name)
    # createdata("train_triplets.txt","train.sent","train.tup","train.pointer")
    # createdata("test_triplets.txt","test.sent","test.tup","test.pointer")
    # createdata("dev_triplets.txt","dev.sent","dev.tup","dev.pointer")


if __name__=="__main__":
    main()
