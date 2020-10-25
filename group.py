# - Jill is 26, a biologist and she is Zalika's friend and John's partner.
# - Zalika is 28, an artist, and Jill's friend
# - John is 27, a writer, and Jill's partner.
# - Nash is 34, a chef, John's cousin and Zalika's landlord.

group_dict={'Jill': {'age':26,'job':'biologist','connection':{'Zalika':'friend','John':'partner'}},
            'Zalika':{'age':28,'job':'artist','connection':{'Jill':'friend'}},
            'John':{'age':27,'job':'writer','connection':{'Jill':'partner'}},
            'Nash':{'age':34,'job':'chef','connection':{'John':'cousin','Zalika':'landlord'}}}


def load_yaml(filepath):
    # Prints yaml data from file provided
    import yaml

    with open(filepath, 'r') as myfile:
        data = yaml.safe_load(myfile)
        print(data)   


def save_yaml(mydict, filepath):
    # Saves dictionary data to yaml file in location specified
    import yaml 

    with open(filepath, 'w') as myfile:
        yaml.dump(mydict, myfile)

def main():
    # Collect data
    data = group_dict.values()

    # 1. Calculate maximum age in the group
    maximum_age = max([x['age'] for x in data])
    print('The maximum age in group_dict is :', maximum_age)

    # 2. Average number of relations in the group
    import numpy as np
    av_connections = np.mean([len(x['connection']) for x in data])
    print('The average number of connections in group_dict is :', av_connections)

    #3. The maximum age of people with at least one relation
    maximum_age = max([x['age'] for x in data if len(x['connection']) >= 1])
    print('The maximum age of people in group_dict with at least one connection is :', maximum_age)

    #4. The maximum age of people in the group that have at least one friend
    maximum_age = max([x['age'] for x in data if len([connection for connection in x['connection'].values() if connection=='friend']) >=1 ])
    print('The maximum age of people in group_dict with at least one friend is :', maximum_age)



if __name__ == "__main__":
    print(group_dict)
    save_yaml(group_dict, './groupdict.yaml')
    print('Saving dictionary data ... ')
    print('Loading dictionary data ..')
    load_yaml('./groupdict.yaml')