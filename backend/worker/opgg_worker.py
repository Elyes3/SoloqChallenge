import functools
from requests_html import HTMLSession
from bs4 import *
from tabulate import tabulate
import sys


def run(arg):
	server = "euw"
	player = arg

	################################################################################
	ranks = ["challenger","grandmaster","master","diamond 1","diamond 2","diamond 3","diamond 4","platinum 1","platinum 2","platinum 3","platinum 4","gold 1","gold 2","gold 3","gold 4","silver 1","silver 2","silver 3","silver 4","bronze 1","bronze 2","bronze 3","bronze 4","iron 1","iron 2","iron 3", "iron 4","unranked"]


	session = HTMLSession()


	page = 'https://' + server + '.op.gg/summoner/userName=' + player.replace(" ","+")
	html = session.get(page)
	soup = BeautifulSoup(html.content, 'html.parser')

	output = {}
	try:
		rank = soup.find("div", {"class": "tier"}).text
		LP = soup.find("div", {"class": "lp"})
	except Exception:
		print("Summoner not found")
		output['summoner'] = player
		output['status'] = "NOT_FOUND"
		return output

	if LP is not None:
		LP = LP.text
	else:
		LP = "0 LP"

	win_lose = soup.find("div", {"class": "win-lose"})
	if win_lose is not None:
		wins = int(win_lose.text[:win_lose.text.index("W")])
		losses = int(win_lose.text[win_lose.text.index("W")+2:win_lose.text.index("L")])
	else:
		wins = 0
		losses = 0

	winrate = 0
	winratio = soup.find("div", {"class": "ratio"})
	if winratio is not None:
		temp = winratio.text.replace("Win Rate ", "")
		temp = temp.replace("%", "")
		winrate = int(temp)

	if LP is not None:
		league = rank
	else:
		league = "Unranked"

	if wins is not None:
		games = wins+losses

	output['summoner'] = player
	output['tier'] = league
	output['wins'] = wins
	output['losses'] = losses
	output['games'] = games
	output['lp'] = LP
	output['winrate'] = winrate
	output['status'] = "OK"
	return output


if __name__ == '__main__':
	run(sys.argv[1])


