__author__ = 'Scott'
from ebaysdk.finding import Connection as Finding
def get_item():
    return raw_input()
try:
    search_item  = get_item()
    api = Finding(appid="ScottRus-bf7d-437a-a830-3735324dd553",config_file=None,debug=True)
    response = api.execute('findItemsAdvanced', {'keywords': 'iPhone'})
    print(response.dict())
    items = response.dict()
    tings = items['searchResult']
    count = 0
    for item in tings['item']:
        count = count +1
        for a in item:
            ##if item['itemId'] == '201393676152':
                print item
        print count

except:
    print 'Fail'

