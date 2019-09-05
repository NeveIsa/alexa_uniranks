import yaml
from multiprocessing.dummy import Pool

import requests
from bs4 import BeautifulSoup
import re


def fetchrank(site,name=None):
    try:
        #print("site",site)
        #print("name",name)
        if name:
            print("Started... ",name)
        url = "https://www.alexa.com/siteinfo/%s" % site
        r=requests.get(url)
        soup=BeautifulSoup(r.text,'html.parser')
        Irank = soup.find_all("span",class_="countryRank")[0].find_all("strong",class_="metrics-data")[0].text
        Irank = re.search("\d+.*\d+",Irank).group()
        Irank=Irank.replace(",","")
        Irank=int(Irank)
        if name:
            print("           ",name,"... Finished")
        return name,Irank
    except Exception as e:
        print("Exception ->",name,":",e)


if __name__=="__main__":

    pool = Pool(20)

    unilist=yaml.safe_load(open("unilist.yml").read())

    univs = []

    for uni in unilist:
        uname = list(uni.keys())[0]
        usite=uni[uname]
        univs.append((usite,uname))
    
    #print(univs)

    results=pool.map(lambda x:fetchrank(x[0],x[1]),univs)
    
    
    uranks=[]

    print("\n-------------------------")
    
    for r in sorted(results,key=lambda x: x[1]):
        print (r[0],"->",r[1])
        uranks.append({r[0]:r[1]})
    
    print("-------------------------")

    #print(uranks)
    
    with open('ranks.yml', 'w') as outfile:
        yaml.dump(uranks, outfile, default_flow_style=False)
     
