import csv

def getDataInput(filename):
    records = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            records.append(row)
    return records

def getMedian(price_list):
    sorted_prices = sorted(price_list)
    n = len(sorted_prices)
    mid = n // 2
    
    if n % 2 == 1:  
        return float(sorted_prices[mid])
    else:  
        return (sorted_prices[mid - 1] + sorted_prices[mid]) / 2.0

def main():
    records = getDataInput('RealEstateData.csv')

    price_list = []
    city_totals = {}
    zip_totals = {}
    property_type_totals = {}

    for record in records:
        city = record[1]  
        property_type = record[6]
        price = float(record[7])  

        price_list.append(price)

        
        if city not in city_totals:
            city_totals[city] = 0
        city_totals[city] += price

        
        zip_code = record[2]  
        if zip_code not in zip_totals:
            zip_totals[zip_code] = 0
        zip_totals[zip_code] += price

        
        if property_type not in property_type_totals:
            property_type_totals[property_type] = 0
        property_type_totals[property_type] += price

    
    price_list.sort()

    
    min_price = min(price_list)
    max_price = max(price_list)
    total_price = sum(price_list)
    average_price = total_price / len(price_list)
    median_price = getMedian(price_list)

    # Outputs
    print(f"Minimum Price: ${min_price:.2f}")
    print(f"Maximum Price: ${max_price:.2f}")
    print(f"Total Price: ${total_price:.2f}")
    print(f"Average Price: ${average_price:.2f}")
    print(f"Median Price: ${median_price:.2f}")

    # Output City
    print("\nSummary by City:")
    for city, total in city_totals.items():
        print(f"{city}: ${total:.2f}")

    # Output Property Type
    print("\nSummary by Property Type:")
    for property_type, total in property_type_totals.items():
        print(f"{property_type}: ${total:.2f}")

if __name__ == "__main__":
    main()
