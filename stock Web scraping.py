import requests
from bs4 import BeautifulSoup


def numbers_to_strings(argument): 
    switcher = { 
        1: "RELIANCE", 
        2: "HDFCBANK",
        3: "ADANIPORTS",
        4: "ITC",
        5: "SBI",
        6: "IOC",
        7: "RBLBANK",
        8: "SBI",
    } 
    return switcher.get(argument,"Sorry Wrong Input") 
    
def stockname(stock_name):
    stockcode = stock_name
    stock_url  = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stockcode)
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    response = requests.get(stock_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_array = soup.find(id='responseDiv').getText().strip().split(":")
    return data_array
  
if __name__ == "__main__":
    print("\n\n1. RELIANCE \n2. HDFCBANK \n3. ADANIPORTS \n4. ITC \n5. SBI \n6. IOC \n7. RBLBANK \n8. SBI  \n\n")
    argument = int(input("Enter the no. you want to check Info "))
    stock_name=(numbers_to_strings(argument))
    data_array=stockname(stock_name)
    #print(data_array)
    for item in data_array:
        if 'closePrice' in item:
            index = data_array.index(item)+1
            close_price=data_array[index].split('"')[1]
            print("\nClose Price: "+close_price)
            
        elif 'open' in item:
            index = data_array.index(item)+1
            open_price=data_array[index].split('"')[1]
            print("\nOpen Price: "+open_price)
            
        elif 'pricebandlower' in item:
            index = data_array.index(item)+1
            priceband_lower=data_array[index].split('"')[1]
            print("\nPrice Band Lower: "+priceband_lower)
            
        elif 'pricebandupper' in item:
            index = data_array.index(item)+1
            priceband_upper=data_array[index].split('"')[1]
            print("\nPrice Band Upper: "+priceband_upper)
            
        elif 'totalTradedVolume' in item:
            index = data_array.index(item)+1
            volume=data_array[index].split('"')[1]
            print("\nVolume: "+volume)
            
        elif 'deliveryQuantity' in item:
            index = data_array.index(item)+1
            delivery_quantity=data_array[index].split('"')[1]
            print("\nDelivery Quantity: "+delivery_quantity)

        elif 'deliveryToTradedQuantity' in item:
            index = data_array.index(item)+1
            deliveryToTradedQuantity=data_array[index].split('"')[1]
            print("\nDelivery Percentage: "+deliveryToTradedQuantity+"%")  


    print("Thank You")            
            
            
        
            
            
    
    

    