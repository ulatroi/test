import re
from neo4j import GraphDatabase
from Neo4jAPI import add_relation, add_node, make_sense

### Entity type:
# • Organization:
# • Time
# • Product
# • Promotion
# • Regulation
# • Location
# • Price
###

### Relation type
# Affiliation
# Regulation
# Location
# Price
###

URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "1234678@!")

node_1_start = "[E1]"
node_1_end = "[/E1]"

node_2_start = "[E2]"
node_2_end = "[/E2]"

i = 0
test_max = 100


def edgeExtraction(sample, driver):
    # print(sample)
    x = sample.replace('\t', ' ').replace('\n', '')
    tmp = x.split(" ")
    print(tmp)
    node_1 = ''
    node_1_label = ''
    node_2 = ''
    node_2_label = ''
    edge = tmp[0]

    if edge == 'OTHER':
        return

    # print(x.find(node_1_start))
    # print(x.find(node_2_start))

    if x.find(node_1_start) < x.find(node_2_start):
        node_1_label = tmp[5]
        node_2_label = tmp[6]
    else:
        node_1_label = tmp[6]
        node_2_label = tmp[5]

    node_1 = x[x.find(node_1_start) + len(node_1_start):x.find(node_1_end)]
    node_2 = x[x.find(node_2_start) + len(node_2_start):x.find(node_2_end)]

    print("index: " + str(i))
    print("edge: " + edge)
    print("node_1: " + node_1 + "| label: " + node_1_label)
    print("node_2: " + node_2 + "| label: " + node_2_label)

    # Add to neo4j
    add_node(node_1_label, node_1, driver)
    add_node(node_2_label, node_2, driver)
    add_relation(node_1_label, node_1, edge, node_2_label, node_2, driver)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    f = open("/home/lacie/Github/Jellyfish-ChatBot/vlsp2020-relex/VLSP2020_RE_SemEvalFormat_2/Convert_To_Graph.txt", "r")

    try:
        neo4j_driver = GraphDatabase.driver(URI)
        make_sense(neo4j_driver)
        for x in f:
            if len(x) > 0:
                edgeExtraction(x, neo4j_driver)
            i = i + 1

        f.close()

        neo4j_driver.close()
    except Exception as e:
        print(e)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
