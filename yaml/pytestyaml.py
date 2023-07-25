import yaml

def writeyaml(dict,filename):
    filename = 'yaml/'+filename+ '.yaml'
    file = open("yaml/search_data.yaml", "w")
    yaml.dump(dict, file)

# real data from yaml file
def readyaml(filename, toFetchTestData):
    filename = 'yaml/'+filename+ '.yaml'
    with open(filename, 'r') as file:
        TestData = yaml.safe_load(file)
    return TestData[toFetchTestData]
