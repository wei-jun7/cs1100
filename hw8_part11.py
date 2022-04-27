import json
from BerryField import BerryField
from Bear import Bear
from Tourist import Tourist

if __name__ == '__main__':
    #simulation = 'bears_and_berries_1.json'
    simulation = input('Enter the json file name for the simulation => ')
    print(simulation)

    f = open(simulation)
    data = json.loads(f.read())
    active_bears = []
    for d in data['active_bears']:
        active_bears.append(Bear(d[0], d[1], d[2], True))
    
    reserve_bears = []
    for d in data['reserve_bears']:
        reserve_bears.append(Bear(d[0], d[1], d[2], False))
    
    active_tourists = []
    for d in data['active_tourists']:
        active_tourists.append(Tourist(d[0], d[1]))

    reserve_tourists = []
    for d in data['reserve_tourists']:
        reserve_tourists.append(Tourist(d[0], d[1]))

    berry_field = BerryField(data['berry_field'], active_bears, reserve_bears, active_tourists, reserve_tourists)
    f.close()

    print(berry_field)
