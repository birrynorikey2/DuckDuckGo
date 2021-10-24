import requests as requests
import pytest


url_ddg = "https://api.duckduckgo.com"


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]

@pytest.mark.parametrize("pres_name", ['Adams', 'Arthur', 'Biden', 'Buchanan', 'Bush', 'Carter', 'Cleveland', 'Clinton', 'Coolidge',
                  'Eisenhower', 'Fillmore', 'Ford', 'Garfield', 'Grant', 'Harding', 'Harrison', 'Hayes', 'Hoover',
                  'Jackson', 'Jefferson', 'Johnson', 'Kennedy', 'Lincoln', 'Madison', 'McKinley', 'Monroe', 'Nixon',
                  'Obama', 'Pierce', 'Polk', 'Reagan', 'Roosevelt', 'Taft', 'Taylor', 'Truman', 'Trump', 'Tyler',
                  'Van Buren', 'Washington', 'Wilson'])
def test_ddg1(pres_name):

    resp = requests.get(url_ddg + "/?q=presidents%20of%20the%20united%20states&format=json")
    rsp_data = resp.json()
    related_topics = rsp_data["RelatedTopics"]
    found = False
    for search in related_topics:
        words = search["Text"]
        if pres_name in words:
            found = True
            break
    assert found is True




