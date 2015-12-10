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
point_array = []



def itemFinder(search_item):
    items = []
    try:
        api = Finding(appid="ScottRus-bf7d-437a-a830-3735324dd553",config_file=None,debug=True)
        for page_num in range(5):
            # TODO: Change back to range later
            response = api.execute('findCompletedItems', {'keywords': search_item,'paginationInput': {'entriesPerPage': 100, 'pageNumber':page_num}})
            response_dict = response.dict()
            if response_dict['ack'] == 'Failure':
                continue
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
                # Y X pair
                point_tuple = (value,int_delta)
                point_array.append(point_tuple)
        except:
            error_logging("ConEng", "Failed")


def compute_error_for_line_give_points(b,m,points):
    try:
        totalError = 0
        for i in range(0,len(points)):
            y,x = points[i]
            totalError += (y - (m * x + b)) ** 2
        return totalError/float(len(points))
    except:
        error_logging("ConEngine", "Error in computer error")

def step_gradient(b_current, m_current, points, learningRate):
    try:
        b_gradient = 0
        m_gradient = 0
        N = float(len(points))
        for i in range(0, len(points)):
            y,x = points[i]
            b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
            m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
        new_b = b_current - (learningRate * b_gradient)
        new_m = m_current - (learningRate * m_gradient)
        return [new_b, new_m]
    except:
        error_logging("webService", "Error in computer error")

def runtest (search_item):
    try:
        std_div_price = numpy.std(price_array)
        std_div_date = stats.stats.tstd(date_array)

        error = None
        new_b, new_m = None, None
        itemFinder(search_item)
        (m,b) = pylab.polyfit(date_array,price_array,1)
        for i in range(100):
            new_b, new_m = step_gradient(b,m,point_array,1)
            error = compute_error_for_line_give_points(new_b,new_m,point_array)
        return ("The new b {0}, the new m {1}, the error {2} this is for {3}\n"
                "Standard Deviations for {3} is {4} for the price".format(new_b,new_m,error,search_item,std_div_price))
    except:
        error_logging("ConEngine", "Error in runtest")


# print len(price_array)
# print len(date_array)