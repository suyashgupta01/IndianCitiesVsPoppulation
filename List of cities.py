import requests as rq
import bs4


def main():
    r = rq.get("https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population")
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    table = soup.findAll('table')[0].find_all('tr') # This is a list, with one tr=table row at each index
    f = open("list_of_cities_by_poppulation.txt", 'w+')
    for item in table[1:]: # excluding the first item.. which is just table heading....
        one_row = item.get_text().split("\n")
        data = one_row[1] + "   ->   " + one_row[2] + ", " + one_row[5] + ": " + one_row[3] + "\n"
        f.write(data)
    f.close()

if __name__ == main():
    main()