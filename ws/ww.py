# WEB WORM 2.0 [MBG]

import os
import requests
import sys
import re
import urllib.parse
import os
from  .nwf import nwf
# class nwf:
#     def new_file(name,w):
#         with open(name,"w") as f:f.write(w)
#     def at_file(name,w):
#         with open(name,"a+") as f:f.write(w)

#     ### v2.4

class path:
    p1={
        "images": [],
        "system_files": [],
        "other": [],
        "videos":[]
    }
    p2={
        "images": [],
        "system_files": [],
        "other": [],
        "videos":[]
    }
    p3="photo.html"
    p4="video.html"
    p5={
        "images": [],
        "system_files": [],
        "other": [],
        "videos":[]
    }
    p6=5
    p7=10
    p8=f"""[HELP]| python3 {sys.argv[0]} <link> <search service> <?aggressive> \n\n\t SEARCH SERVSEC ->\n\t\t
                      google
                      yandex
                      bing
                      duckduckgo
                      yahoo
                      ecosia
                      ask
                      aol
                      baidu
                      wolfram
                      pubmed
                      shodan
                      arxiv
                      
                      1
[OUT-DEFAULT]| python3 {sys.argv[0]} potato
[OUT-AllSearchService]| python3 {sys.argv[0]} potato 1
[OUT-AggresiveRead/SniffInternetResource]| python3 {sys.argv[0]} potato 1 1
"""
    p9=None # USED FOR LINKS
    p10="links.html"
    p11=['link','video','photo','other'] # USED FOR WANT TYPE
    p12=None

    class search_service:
        google_search_link="https://www.google.com/search?q="
        bing_search_link="https://www.bing.com/search?q="
        yahoo_search_link="https://search.yahoo.com/search?p="
        duckduckgo_search_link="https://duckduckgo.com/?q="
        ecosia_search_link="https://www.ecosia.org/search?q="
        ask_search_link="https://www.ask.com/web?q="
        aol_search_link="https://search.aol.com/search?q="
        yandex_search_link="https://ya.ru/search/?text="
        baidu_search_link="https://www.baidu.com/s?wd="
        wolfram_alpha_search_link="https://www.wolframalpha.com/input/?i="
        pubmed_search_link="https://pubmed.ncbi.nlm.nih.gov/?term="
        arxiv_search_link="https://arxiv.org/search/?query="
        shodan_search_link="https://www.shodan.io/search?query="

    def extract_links(text,tep):
        links = re.findall(r'https?://(?:www\.)?[\w\d\-._]+(?:\.[\w\d\-._]+)+[\w\d\-\._\:\/\?\#\[\]\@\!\$\%\^\&\*\(\)\+\,\;\:\.\~\|\/\?\#]*', text)
        
        for link in links:
            link = link.split('&amp;')[0]           
            link = urllib.parse.unquote(link) 
            extension = os.path.splitext(link)[1].lower()

            if extension in ['.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff', '.svg'] and 'photo' in path.p11: #, '.gif'
                ph_html=f'<img src="{link}" style ="max-width: 200px; height: auto;position:releative;max-height:500px">'
                
                if tep == 1:
                    if link not in path.p1["images"] and link not in path.p2["images"] and link not in path.p5["images"]:
                        path.p1["images"].append(link)
                        nwf.at_file(path.p3,ph_html)
                elif tep == 2:
                    if link not in path.p1["images"] and link not in path.p2["images"] and link not in path.p5["images"]:
                        path.p2["images"].append(link)
                        nwf.at_file(path.p3,ph_html)
                elif tep == 5:
                    if link not in path.p1["images"] and link not in path.p2["images"] and link not in path.p5["images"]:
                        path.p5["images"].append(link)
                        nwf.at_file(path.p3,ph_html)
            elif extension in ['.mp4', '.webm', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.mpg', '.mpeg', '.m4v'] and 'video' in path.p11:
                video_html = f'<video width="320" height="240" controls><source src="{link}" type="video/mp4">Your browser does not support the video tag.</video>'
                
                if tep == 1:
                    if link not in path.p1["videos"] and link not in path.p2["videos"] and link not in path.p5["videos"]:
                        path.p1["videos"].append(link) 
                        nwf.at_file(path.p4, video_html)
                elif tep == 2:
                    if link not in path.p2["videos"] and link not in path.p2["videos"] and link not in path.p5["videos"]:
                        path.p2["videos"].append(link)
                        nwf.at_file(path.p4, video_html)
                elif tep == 5:
                    if link not in path.p5["videos"] and link not in path.p2["videos"] and link not in path.p5["videos"]:
                        path.p5["videos"].append(link)
                        nwf.at_file(path.p4, video_html)
            elif extension in ['.js', '.css', '.json', '.xml', '.html', '.txt', '.csv', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.zip', '.rar', '.gz', '.tar'] and 'sys' in path.p11:
                if tep == 1:
                    if link not in path.p1["system_files"]:
                        path.p1["system_files"].append(link)
                elif tep == 2:
                    if link not in path.p2["system_files"]:
                        path.p2["system_files"].append(link)
                elif tep == 5:
                    if link not in path.p5["system_files"]:
                        path.p5["system_files"].append(link)
            else:
                if 'other' in path.p11:
                    link_html=f"<a href={link}>{link}</a><br><br>"
                    if tep == 1:
                        if link not in path.p1["other"] and link not in path.p2["other"] and link not in path.p5["other"]:
                            path.p1["other"].append(link)
                            nwf.at_file(path.p10, link_html)
                    elif tep == 2:
                        if link not in path.p2["other"]  and link not in path.p2["other"] and link not in path.p5["other"]:
                            path.p2["other"].append(link)
                            nwf.at_file(path.p10, link_html)
                    elif tep == 5:
                        if link not in path.p5["other"]  and link not in path.p2["other"] and link not in path.p5["other"]:
                            path.p5["other"].append(link)
                            nwf.at_file(path.p10, link_html)

            if path.p9!=False:
                text
        if   tep==1:return path.p1
        elif tep==2:return path.p2
        elif tep==5:return path.p5


    def get_search_results(search_engine_url, obj):
        full_url=search_engine_url + obj
        print(f"USE :: {full_url}")
        try:
            response = requests.get(full_url,timeout=path.p7)
            response.raise_for_status() 
            return response.text
        except:
           
            return "" 



def main(obj,ss='google',aggressive=0,want=['photo'],pathss = ['photo.html','video.html','links.html']):
    
    path.p11=want

    path.p3=pathss[0]
    path.p4=pathss[1]
    path.p10=pathss[2]
    
    nwf.new_file(path.p3, '<style>body{background:rgb(33,33,33);}</style>')
    nwf.new_file(path.p4, '<style>body{background:rgb(33,33,33);}</style>')
    nwf.new_file(path.p10,'<style>body{background:rgb(33,33,33);a{color:white;}}</style>')
    
    print(f"SearchText == {obj} | SearchService == {ss} |  Aggressive == {aggressive}")
    
    if "http" in obj or "https" in obj: 
        try:
            text_restText=requests.get(f'{obj}',timeout=path.p7).text
            print(f'USE :: {obj}')
            path.p9=obj
        except:
            print(f'ERR :: {obj}')
            sys.exit()
    elif ss=='google':
        try:
            text_restText=requests.get(f'{path.search_service.google_search_link}{obj}',timeout=path.p7).text
            print(f'USE :: {path.search_service.google_search_link}{obj}')
        except:text_restText=""
    elif  ss=='bing':
        try:
            text_restText=requests.get(f'{path.search_service.bing_search_link}{obj}',timeout=path.p7).text
            print(f'USE :: {path.search_service.bing_search_link}{obj}')
        except:text_restText=""
    elif ss=='yahoo':
        try:
            text_restText=requests.get(f'{path.search_service.yahoo_search_link}{obj}',timeout=path.p7).text
            print(f'USE :: {path.search_service.yahoo_search_link}{obj}')
        except:text_restText=""
    elif ss=='duckduckgo':
        try:
            text_restText=requests.get(f'{path.search_service.duckduckgo_search_link}{obj}',timeout=path.p7).text
            print(f'USE :: {path.search_service.duckduckgo_search_link}{obj}')
        except:text_restText=""
    elif ss=='ecosia':
        try:
            text_restText=requests.get(f'{path.search_service.ecosia_search_link}{obj}',timeout=path.p7).text
            print(f'USE :: {path.search_service.ecosia_search_link}{obj}')
        except:text_restText=""
    elif ss=='ask':
        try:
            text_restText=requests.get(f'{path.search_service.ask_search_link}{obj}',timeout=path.p7).text
            print(f'USE :: {path.search_service.ask_search_link}{obj}')
        except:text_restText=""
    elif ss=='aol':
        try:
            text_restText=requests.get(f'{path.search_service.aol_search_link}{obj}',timeout=path.p7).text
            print(f'USE :: {path.search_service.aol_search_link}{obj}')
        except:text_restText=""
    elif ss=='yandex':
        try:
            text_restText=requests.get(f'{path.search_service.yandex_search_link}{obj}',timeout=path.p7).text
            print(f'USE :: {path.search_service.yandex_search_link}{obj}')
        except:text_restText=""
    elif ss=='baidu':
        try:
            text_restText=requests.get(f'{path.search_service.baidu_search_link}{obj}',timeout=path.p7).text
            print(f'USE :: {path.search_service.baidu_search_link}{obj}')
        except:text_restText=""
    elif ss=='wolfram':
        try:
            text_restText=requests.get(f'{path.search_service.wolfram_alpha_search_link}{obj}',timeout=path.p7).text
            print(f'USE :: {path.search_service.wolfram_alpha_search_link}{obj}')
        except:text_restText=""
    elif ss=='pubmed':
        try:
            text_restText=requests.get(f'{path.search_service.pubmed_search_link}{obj}',timeout=path.p7).text
            print(f'USE :: {path.search_service.pubmed_search_link}{obj}')
        except:text_restText=""
    elif ss=='arxiv':
        try:
            text_restText=requests.get(f'{path.search_service.arxiv_search_link}{obj}',timeout=path.p7).text
            print(f'USE :: {path.search_service.arxiv_search_link}{obj}')
        except:text_restText=""
    elif ss=='shodan':
        try:
            text_restText=requests.get(f'{path.search_service.shodan_search_link}{obj}',timeout=path.p7).text
            print(f'USE :: {path.search_service.shodan_search_link}{obj}')
        except:text_restText=""
    
    else:
        if ss=='1':
            print('\n\n************************* ALL SS [BERSERK] *************************\n')
            text_restText = f"""
            {path.get_search_results(path.search_service.google_search_link, obj)}
            {path.get_search_results(path.search_service.bing_search_link, obj)}
            {path.get_search_results(path.search_service.yahoo_search_link, obj)}
            {path.get_search_results(path.search_service.duckduckgo_search_link, obj)}
            {path.get_search_results(path.search_service.ecosia_search_link, obj)}
            {path.get_search_results(path.search_service.ask_search_link, obj)}
            {path.get_search_results(path.search_service.aol_search_link, obj)}
            {path.get_search_results(path.search_service.yandex_search_link, obj)}
            {path.get_search_results(path.search_service.wolfram_alpha_search_link, obj)}
            {path.get_search_results(path.search_service.pubmed_search_link, obj)}
            {path.get_search_results(path.search_service.arxiv_search_link, obj)}
            {path.get_search_results(path.search_service.shodan_search_link, obj)}
            """
       
        else:print('ERR __ ARG')
    
    start_links=path.extract_links(text_restText,1)

    
    print(f"\n************ START LINKS ************ LINKS {len(path.p1['other'])} | PHOTO {len(path.p1['images'])} | \n\n{start_links}\n\n")
    
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------

    for link_other in  path.p1["other"]:
        
        try:
            response = requests.get(link_other,timeout=path.p6)
            response.raise_for_status() 
            
            if response.status_code == 200:
                print(f"USE == {link_other}")
                link_other=path.extract_links(response.text,2)
            

        except requests.exceptions.RequestException as e:
            print(f"ERR -- {link_other} => {e}")
    
    print(f"\n\n\n************ OTHER LINKS ************ LINKS {len(path.p2['other'])} | PHOTO {len(path.p2['images'])} | \n\n{path.extract_links('',tep=2)}\n\n\n")
    
    if aggressive=='1':
        for link_other5 in  path.p2["other"]:
            try:
                response = requests.get(link_other5,timeout=path.p6)
                response.raise_for_status() 
                
                if response.status_code == 200:
                    print(f"USE *== {link_other5}")
                    link_other5=path.extract_links(response.text,5)
                

            except requests.exceptions.RequestException as e:
                print(f"ERR *-- {link_other5} => {e}")
   
        print(f"\n\n\n************ OTHER LINKS 5 ************ LINKS {len(path.p5['other'])} | PHOTO {len(path.p5['images'])} | \n\n{link_other5}\n\n\n")

try:
    if __name__ == '__main__':
        if  len(sys.argv)==1:print(path.p8)
        elif  len(sys.argv)==2:
            if  sys.argv[1] in ['--help','-h']:print(path.p8)
            else:main(str(sys.argv[1]))
        elif len(sys.argv)==3:main(str(sys.argv[1]),ss=str(sys.argv[2]))
        elif len(sys.argv)==4:main(str(sys.argv[1]),ss=str(sys.argv[2]) ,aggressive=sys.argv[3])
            
        else: print("[ERROR]|['ARGUMENTS']")
except:print('[EXT STOPED]')
