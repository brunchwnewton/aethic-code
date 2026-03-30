import requests
from bs4 import BeautifulSoup
import re

# Read URLs from the text file
with open("versus_links.txt", "r") as file:
    fight_urls = file.read().splitlines()

with open("duel.csv", "w") as output_file:
    # Iterate through each fight URL and extract information
    for fight_url in fight_urls:
        try:
            fight_response = requests.get(fight_url)
            fight_soup = BeautifulSoup(fight_response.content, "html.parser")

            # Extract species names
            species_names = fight_soup.find("h2").text.strip()
            combatants = species_names.split(" v ")

            # Extract vote percentages
            percent_elements = fight_soup.find_all("div", class_="poll_option_percent")
            rates = [float(re.search(r"\((.*?)\)", element.text).group(1).split('%')[0]) / 100 for element in percent_elements]
            win = rates[0] / (rates[0] + rates[1])

            # Extract total vote count
            total_vote_count = int(fight_soup.find("span", class_="poll_total_vote_cnt").text)

            data = f"{combatants[0]}\t{combatants[1]}\t{win}\t{total_vote_count}\n"
            output_file.write(data)
            print(data, end="")
        except:
            print("A BREAK")
