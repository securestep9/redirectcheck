import requests
import csv
import sys
import socket

if __name__ == "__main__":
    if len(sys.argv) != 2:
         print("Bulk URL redirect checker - read a list of sites from file and output CSV")
         print ("with response code and redirection location in CSV format")
         print("Usage: python redirectcheck.py inputlist.csv")
         sys.exit()
    else:    
        target=sys.argv[1]


with open(target, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        theitem = row[0].strip().replace("http://","")
        url = 'http://' + theitem
        try:            
            socket.setdefaulttimeout(5)
            ip = socket.gethostbyname(theitem).strip()      
            headers = requests.utils.default_headers()
            headers.update(
                {
                    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)'
                }
            )
            r = requests.get(url, allow_redirects=False, timeout=3,)
            
            status_code = str(r.status_code)
            location = r.headers.get('location',''.join(''))

            print(theitem + ', ' + ip + ', ' + status_code + ', ' + location)
            
        except Exception as e:
            print(theitem + ', NOIP, ' +'NULL,')
