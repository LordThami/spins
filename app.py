import json

import requests
from flask import Flask
from bs4 import BeautifulSoup


app = Flask(__name__)


@app.route('/get_spins')
def get_spins():
    res = requests.get("https://www.pockettactics.com/coin-master/free-spins")
    soup = BeautifulSoup(res.text, 'html.parser')
    search_result = {}
    results = []
    for code in soup.select(".single .entry-content"):
        for d in code.find_all("a", href=True, target="_blank"):
            manga = {'title': d.text, 'link': d['href']}
            results.append(manga)
    search_result['result'] = results
    return search_result
