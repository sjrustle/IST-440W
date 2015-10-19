__author__ = 'Scott'
from ebaysdk.finding import Connection as Finding
import SQLConnection
def itemFinder(search_item):
    try:
        api = Finding(appid="",config_file=None,debug=True)
        response = api.execute('findItemsAdvanced', {'keywords': search_item})
        items = response.dict()
        SQLConnection.get_Ebay_data(items['searchResult'])

        ##EbayDbSQL.set_ebay_dict(items['searchResult'])
        ## item in tings['item']:
           ## ebay_info =  "itemId: {}, title: {}, Selling Status: {}".format(item['itemId'],item['title'],item['sellingStatus'])

    except KeyError:
        print KeyError

