import requests
import json
import pprint

def update_fund_list():
    url = "https://www.jisilu.cn/jisiludata/etf.php?rp=25&page=1"
    response = requests.get(url)
    etf_index = json.loads(response.content)
    pprint.pprint(etf_index)
    url = "https://www.jisilu.cn/data/lof/index_lof_list/?rp=25&page=1"
    response = requests.get(url)
    lof_index = json.loads(response.content)
    pprint.pprint(lof_index)
    
def update_fund(fund_id=None):
    url="https://www.jisilu.cn/data/etf/detail_hists/"
    data = {
        "is_search":1,
        "fund_id":fund_id,
        "rp":50,
        "page":1,
    }
    response = requests.post(url,data=data)
    fund = json.loads(response.content)
    pprint.pprint(fund)

if __name__ == '__main__':
    # update_fund_list()
    update_fund(fund_id=159901)