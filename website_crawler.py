# pip3 install anytree
# pip3 install beautifulsoup4

from anytree import Node, RenderTree
from bs4 import BeautifulSoup, SoupStrainer
import requests
import time

url = input("url: ")
deep = 1

# Add https if its not in url input
if not url[0:8].lower() == "https://" or url[0:7].lower() == "http://":
    url = "https://"+url

page = requests.get(url)    
page_data = page.text
soup = BeautifulSoup(page_data, 'html.parser')

links = []

for link in soup.find_all('a'):
    links.append(link.get('href'))


print(f'Found {len(links)} links on {url}')

time.sleep(1)

def clean_data(data):
    data = list(filter(None, data))
    for i, link in enumerate(data):
        data[i] = list(filter(None, link.split('/')))
        data[i].insert(0, '^')

        if not (data[i][1] == 'https:' or data[i][1] == 'http:'):
            data[i].insert(1, url)
    data = list(filter(None, data))
    data.sort(key=len, reverse=True)
    return data

data = links
data = clean_data(data)


def list_to_anytree(lst):
    root_name = lst[0][0]
    root_node = Node(root_name)
    nodes = {root_name: root_node}  # keeping a dict of the nodes
    for branch in lst:
        for parent_name, node_name in zip(branch, branch[1:]):
            node = nodes.setdefault(node_name, Node(node_name))
            parent_node = nodes[parent_name]
            if node.parent is not None:
                pass
            else:
                node.parent = parent_node
    return root_node


if len(data):
    sitetree = list_to_anytree(data)

    for pre, fill, node in RenderTree(sitetree):
        print(f"{pre}{node.name}")
    print(data)
