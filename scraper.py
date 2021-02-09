"""
proudly created by Radim Kurka
"""

from bs4 import BeautifulSoup as BS
import csv, sys, requests

URL_regions = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"

def choose_region(URL_regions):
    soup = create_soup(URL_regions)
    regions = get_table_data(soup, 0, 4, 1)
    links = extract_links(soup, 3, 4, 0)
    for number, region in enumerate(regions):
        print(number, region)
    print("Please make a selection of region you would like to choose.")
    user_choice = input("Your selection: ")
    try:
        int(user_choice)
    except:
        raise ValueError("You did not enter in numbers, you cheeky bastard.")
    if int(user_choice) not in range(0, len(regions)):
            raise IndexError("Error, index is out of range of regions, please restart the program.")
    chosen_link = f"https://volby.cz/pls/ps2017nss/{links[int(user_choice)]}"
    print("Please wait while I scrape data, this can take up to a minute.")
    return chosen_link

def create_soup(URL):
    try:
        r = requests.get(URL)
        r.raise_for_status()
        soup = BS(r.text, "html.parser")
        return soup
    except requests.exceptions.HTTPError:
        print("Could not retrieve the page")
    except:
        print(sys.exc_info()[:1])

def extract_links(soup, start, step, plus):
    links = list()
    tds = soup.findAll("td")
    for index in range(start, len(tds), step):
        try:
            result = tds[index + plus].a["href"]
            links.append(result)
        except:
            pass
    return links

def get_link_id(link):
    splitted = link.split("&")
    municipal_id = splitted[2].lstrip("xobec=")
    return municipal_id

def extract_data(soup):
    results = []
    try:
        location = soup.select("h3")[2].string.strip("\n")
    except IndexError:
        location = soup.find("h3").string.strip("\n")
    location = location[6:]
    registered = soup.find("td", attrs={"headers": "sa2"}).string
    envelopes = soup.find("td", attrs={"headers": "sa3"}).string
    valid = soup.find("td", attrs={"headers": "sa6"}).string
    results.extend([location, registered, envelopes, valid])
    return results

def get_tables(soup):
    tables = []
    table1 = soup.select("table")[1]
    table2 = soup.select("table")[2]
    tables.extend([table1, table2])
    return tables

def get_table_data(table, start, step, plus):
    table_data = []
    tds = table.findAll("td")
    for index in range(start, len(tds), step):
        try:
            result = tds[index + plus].string
            table_data.extend([result])
        except:
            pass
    return table_data


def fix_output_coding(rows):
    results_fixed = []
    for datapoint in rows:
        results_fixed.append(datapoint.replace(u"\xa0", ""))
    return results_fixed

def write_to_csv(full_data, filename):
    with open(filename, "w", encoding='utf-8', newline="") as file:
        writer = csv.writer(file)
        for row in full_data:
            writer.writerow(row)
    print(f"Written {len(full_data)} lines of data into {filename}")

def get_header(header_extract_link):
    soup = create_soup(f"https://volby.cz/pls/ps2017nss/{header_extract_link}")
    tables = get_tables(soup)
    header = ["Municipality code", "Location", "Number of registered", "Envelopes", "Valid votes"]
    for table in tables:
        parties = get_table_data(table, 1, 5, 0)
        header.extend(parties)
    return header

def format_data(data1, data2, municipal_id):
    lst = []
    full_data = data1 + data2
    lst.extend(full_data)
    lst.insert(0, municipal_id)
    return lst

def main():
    final_output = []
    URL = choose_region(URL_regions)
    soup = create_soup(URL)
    links = extract_links(soup, 0, 3, 0)
    header_extract_link = links[0]
    header = get_header(header_extract_link)

    for link in links:
        soup = create_soup(f"https://volby.cz/pls/ps2017nss/{link}")
        municipal_id = get_link_id(link)
        tables = get_tables(soup)
        data_general = extract_data(soup)
        data_vote1 = get_table_data(tables[0], 1, 5, 1)
        data_vote2 = get_table_data(tables[1], 1, 5, 1)
        data_votes = data_vote1 + data_vote2
        formatted_data = format_data(data_general, data_votes, municipal_id)
        fixed_data = fix_output_coding(formatted_data)
        final_output.append(fixed_data)

    final_output.insert(0, header)
    return final_output

final_output = main()
try:
    choice = input("""
    Would you like to write data to csv? Please type 1.
    Or would you like to print results to terminal? Please type 2.
    """)
    if choice == "1":
        filename = input("Please choose filename ending with .csv ")
        if filename[-4:] != ".csv":
            filename += ".csv"
        write_to_csv(final_output, filename)
    elif choice == "2":
        print(final_output)
except:
    print(sys.exc_info()[:1])



