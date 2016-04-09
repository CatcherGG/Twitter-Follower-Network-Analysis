import os


# I'll use my followers as a scope for the rest of the assignment [Otherwise, the nodes amount will exceed 200]
def get_users_scope():
    file = open('./TweeterInfo/CatcherGG.txt', 'r')
    follower_scope = []
    for line in file.readlines():
        follower = line.replace('\n', '')
        follower_scope.append(follower)
    file.close()
    return follower_scope


def create_edges_csv():
    edges_file = open('./edges.csv', 'w+')
    edges_file.write("\"From\",\"To\"")
    edges_file.write('\n')
    scope = get_users_scope()

    for follower_file in os.listdir("./TweeterInfo/"):
        follower_name = follower_file.replace(".txt", "")
        follower_file = open('./TweeterInfo/'+follower_file, 'r')
        for follower_of_follwer_line in follower_file.readlines():
            follower_of_follower_name = follower_of_follwer_line.replace('\n', '')
            print(follower_of_follower_name)
            if any(follower_of_follower_name in s for s in scope):
                edges_file.write("\"" + follower_of_follower_name + "\",\"" + follower_name + "\"")
                edges_file.write('\n')
            else:
                print(follower_of_follower_name)

def remove_duplicated_lines(infilename, outfilename):
    lines_seen = set()  # holds lines already seen
    outfile = open(outfilename, "w+")
    for line in open(infilename, "r"):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

create_edges_csv()
remove_duplicated_lines("./edges.csv", "./edges_no_duplicates.csv")