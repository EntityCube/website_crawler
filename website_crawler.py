# pip3 install anytree
# pip3 install beautifulsoup4
from anytree import Node, RenderTree
from bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urljoin
import requests
import time
import sys


def main():

    if '-h' in sys.argv or '--help' in sys.argv:
        help_msg()
    elif len(sys.argv) <= 2:
        help_msg()
    else:
        
        url = sys.argv[1]
        url = url_fixer(url)
        data = []
      
        for link in collect_links(url):
            url = link
            data.append(link)
            # for link in collect_links(url):
                # url = link
                # data.append(link)


        data = clean_data(data, url)

        if len(data):
            sitetree = list_to_anytree(data)

            time.sleep(1)
            for pre, fill, node in RenderTree(sitetree):
                print(f"{pre}{node.name}")


def collect_links(url):
        links = []
        page = requests.get(url)    
        page_data = page.text
        soup = BeautifulSoup(page_data, 'html.parser')
        args = sys.argv 
        links = crawl(soup, url, args)


        data = clean_data(data, url)

        if len(data):
            sitetree = list_to_anytree(data)

            time.sleep(1)
            for pre, fill, node in RenderTree(sitetree):
                print(f"{pre}{node.name}")


def collect_links(url):
        links = []
        page = requests.get(url)    
        page_data = page.text
        soup = BeautifulSoup(page_data, 'html.parser')
        args = sys.argv 
        links = crawl(soup, url, args)

        for i, link in enumerate(links):
            if not (links[i][0:8] == 'https://' or links[i][0:7] == 'http://'):
                links[i] = urljoin(url, links[i])

        return links


def help_msg():
        print('Help')
        print('Syntax:')
        print('website_crawler.py <url> <args>')
        print('Arguments:')
        print('-a   find links')
        print('-s   find scripts and links')
        print('-c   find stylesheets')
        print('-m   find medias')


def url_fixer(url):
    """Add https if its not in url input"""
    if not url[0:8].lower() == "https://" or url[0:7].lower() == "http://":
        url = "https://"+url
    return url


def crawl(soup, url, args):
    links = []

    if '-a' in args:
        for link in soup.find_all('a'):
            if ':' in link.get('href') or 'tel:' in link.get('href') or 'javascript:' in link.get('href'):
                links.append(url+link.get('href'))
            else:
                links.append(link.get('href'))

    if '-s' in args:
        for link in soup.find_all('script'):
            links.append(link.get('src'))

    if '-m' in args:
        tags = ['img','src','source','object','iframe']
        for tag in tags:
            for link in soup.find_all(tag):
                links.append(link.get('src'))
                links.append(link.get('data'))

        for link in soup.find_all('audio'):
            links.append(link.get('src'))

        for link in soup.find_all('source'):
            links.append(link.get('src'))

    if '-m' in args:
        for link in soup.find_all('link'):
            links.append(link.get('href'))

    links = list(filter(None, links))
    print(f'Found {len(links)} links on {url}')
    return(links)


def clean_data(data, url):
    data = list(filter(None, data))
    for i, link in enumerate(data):

        data[i] = list(filter(None, data[i].split('/')))
        data[i].insert(0, '^')


    data = list(filter(None, data))
    data.sort(key=len, reverse=True)
    return data


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


main()
