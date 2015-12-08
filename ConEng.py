from wsLogging import error_logging, audit_logging
from ebaysdk.finding import Connection as Finding
import datetime
from datetime import datetime as dt
from scipy import stats
import numpy
import pylab
import math

price_array = []
date_array = []



def itemFinder(search_item):
    items = []
    try:
        api = Finding(appid="ScottRus-bf7d-437a-a830-3735324dd553",config_file=None,debug=True)
        for page_num in range(20):
            # TODO: Change back to range later
            response = api.execute('findCompletedItems', {'keywords': search_item,'paginationInput': {'entriesPerPage': 100, 'pageNumber':page_num}})
            response_dict = response.dict()
            if response_dict['ack'] == 'Failure':
                print "It was a failure"
            else:
                items.append(response.dict())
    except:
        error_logging("ConEng", "Failed")

    for s_item in items:
        # Assign searchResult value to variable
        search_result = s_item['searchResult']
        # Assign item value to item_array
        item_array = search_result['item']

        count = 0
        try:
            for item in item_array:
                count += 1
                print count
                # Get selling status
                selling_status_price = item['sellingStatus']
                selling_status_price = item['sellingStatus']
                #Get current price
                current_price = selling_status_price['currentPrice']
                value = float(current_price['value'])

                # Store price in price_array
                price_array.append(value)

                # Get the listingInfo
                listing_info = item['listingInfo']
                # Get endTime
                end_time = listing_info['endTime']
                sliced_date = end_time[:10]
                a = dt.strptime(sliced_date, '%Y-%m-%d').date()
                # Start date
                star_date = datetime.date(2015,1,1)
                delta = a - star_date
                # Get date number relative to the year
                int_delta = int(delta.days)
                # Store Date in date array
                date_array.append(int_delta)
        except:
            error_logging("ConEng", "Failed")
    return items


# itemFinder("iPhone")
# print len(price_array)
# print len(date_array)