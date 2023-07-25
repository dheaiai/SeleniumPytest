import yaml


# Write data to my_yaml
def writeyaml(dict, filename):
    filename = 'my_yaml/' + filename + '.yaml'
    file = open(filename, "w")
    yaml.dump(dict, file)


# real data from my_yaml file
def readyaml(toFetchTestData, filename):
    filename = 'my_yaml/' + filename + '.yaml'
    with open(filename, 'r') as file:
        TestData = yaml.safe_load(file)
    return TestData[toFetchTestData]
