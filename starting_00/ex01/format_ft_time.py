import time
from datetime import datetime

def main():
    current_time = time.time()
    print(f"Seconds since January 1, 1970: {current_time:,} or {current_time:.2e} in scientific notation")
    current_time = datetime.now()
    formatted_date = current_time.strftime("%b %d %Y")
    print (formatted_date)

if __name__== "__main__":
    main()
