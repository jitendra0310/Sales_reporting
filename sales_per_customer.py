import csv
import sys
import unittest

def read_csv(filename):
    # Read CSV file
    kwargs = {'newline': ''}
    mode = 'r'
    
    with open(filename, mode, **kwargs) as fp:
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        # next(reader, None)  # skip the headers
        data_read = [row for row in reader]
    
    return data_read
        
def write_csv(filename, data):
    # Write CSV file
    kwargs = {'newline': ''}
    mode = 'w'
    
    with open(filename, mode, **kwargs) as fp:
        writer = csv.writer(fp, delimiter=',')
        # writer.writerow(["your", "header", "foo"])  # write header
        writer.writerows(data)

def calculate_sales_per_customer(customers, sales):
    sales_per_customers = [['name', 'email', 'address', 'sum(quantity)']]
    
    # Loop through customers
    for customer in customers:
        sales_per_customer = []
        
        # Calculate the total sum
        total = 0
        for sale in sales:
            if customer[0] == sale[0]:
                total = total + int(sale[3])
        
        # Add new sales per customer
        sales_per_customer.append(customer[1])
        sales_per_customer.append(customer[2])
        sales_per_customer.append(customer[3])
        sales_per_customer.append(total)
        
        sales_per_customers.append(sales_per_customer)
    
    return sales_per_customers
        
def run():
    # Read sales and customers
    sales = read_csv('sales.csv')
    customers = read_csv('customers.csv')
    
    # Remove header row
    customers.pop(0)
    sales.pop(0)
    
    # Calculate the sales per customer
    sales_per_customers = calculate_sales_per_customer(customers, sales)
    write_csv('sales_per_customer.csv', sales_per_customers)
    
    print(sales)
    print(customers)

class CSVReadWriteMethods(unittest.TestCase):
    def test_read_csv(self):
        sales = read_csv('sales.csv')
        self.assertEqual(len(sales), 7)
        self.assertEqual(len(sales[0]), 4)
        
    def test_write_csv(self):
        sales = read_csv('sales.csv')
        write_csv('sales_test.csv', sales)
        sales_test = read_csv('sales_test.csv')
        self.assertEqual(len(sales_test), 7)
        self.assertEqual(len(sales_test[0]), 4)
        
if __name__ == '__main__':
    run()
    unittest.main()