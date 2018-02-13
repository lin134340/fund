import requests
import json
import pprint

def pull_fund():
    url="https://www.jisilu.cn/jisiludata/etf.php?rp=25&page=1"
    response = requests.get(url)
    etf_index = json.loads(response.content)
    pprint.pprint(etf_index)
    url="https://www.jisilu.cn/data/lof/index_lof_list/?rp=25&page=1"
    response = requests.get(url)
    lof_index = json.loads(response.content)
    pprint.pprint(lof_index)
    
if __name__ == '__main__':
    pull_fund()