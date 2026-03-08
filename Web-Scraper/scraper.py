import requests
from bs4 import BeautifulSoup

# Η σελίδα που θα "σκανάρουμε" (χρησιμοποιούμε μια στατική σελίδα για δοκιμή)
URL = "https://news.ycombinator.com/" 

def fetch_news():
    print(f"Σύνδεση με το {URL}...")
    
    # Στέλνουμε το αίτημα στην ιστοσελίδα
    response = requests.get(URL)
    
    if response.status_code == 200:
        # Μετατρέπουμε το HTML σε "αναγνώσιμο" κώδικα για την Python
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # βρίσκουμε όλους τους τίτλους (στο Hacker News είναι στην class 'titleline')
        titles = soup.find_all('span', class_='titleline')
        
        print(f"\nΒρέθηκαν {len(titles)} τίτλοι:\n" + "-"*30)
        
        for i, title in enumerate(titles[:10], 1): # Παίρνουμε τους πρώτους 10
            print(f"{i}. {title.text}")
    else:
        print("Αδυναμία σύνδεσης με τη σελίδα.")

if __name__ == "__main__":
    fetch_news()
