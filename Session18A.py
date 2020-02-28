import requests
from bs4 import BeautifulSoup


class Team:

    def __init__(self, teamName, total, won, lost,
                 tied, abandoned, points, netRunRate, scoreFor, scoreAgainst):
        self.teamName = teamName
        self.total = total
        self.won = won
        self.lost = lost
        self.tied = tied
        self.abandoned = abandoned
        self.points = points
        self.netRunRate = netRunRate
        self.scoreFor = scoreFor
        self.scoreAgainst = scoreAgainst

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{}\n".format(
            self.teamName, self.total, self.won, self.lost,
            self.tied, self.abandoned, self.points, self.netRunRate, self.scoreFor, self.scoreAgainst                                          )

url = "https://www.espncricinfo.com/table/sort/matchesplayed/series/8048/season/2019/ipl"
response = requests.get(url)
# print(response.text)

# Extract Meaningful Data from Web Page HTML Response
# HTML Parsing :)

soup = BeautifulSoup(response.text, "html.parser")

spanTags = soup.find_all("span", class_="team-names")
tdTags = soup.find_all("td", class_="")

for tag in spanTags:
    print(tag.text)

print("~~~~~~~~~~~")

for tag in tdTags:
    print(tag.text)


# Task1: Organise Data for Teams as in every team is 1 Single Object
# Task2: Organize Team Objects in a List(Python Inbuilt List)
# Task3: Organize Team Objects as a HashTable, where Team Name must be used as key for hash code
#
