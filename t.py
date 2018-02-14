import requests
import json
import pprint

g = {
    "etf_index_fund_fn":"etf_index_fund",
}

def update_fund_list():
    url = "https://www.jisilu.cn/jisiludata/etf.php?rp=25&page=1"
    response = requests.get(url)
    etf_index_fund_ori = json.loads(response.content)
    try:
        etf_index_fund_native = json.load(open(g["etf_index_fund_fn"],"r"))
    except:
        etf_index_fund_native = []
    for r in etf_index_fund_ori["rows"]:
        if all(map(lambda p: p["id"]!=r["id"], etf_index_fund_native)):
            f = {
                "id": r["id"],
                "name": r["cell"]["fund_nm"],
                "index_id": r["cell"]["index_id"],
            }
            etf_index_fund_native.append(f)
            print("add fund:")
            pprint.pprint(f)
    json.dump(etf_index_fund_native, open(g["etf_index_fund_fn"],"w"))
    
def update_fund(fund_id=None):
    url="https://www.jisilu.cn/data/etf/detail_hists/"
    data = {
        "is_search":1,
        "fund_id":fund_id,
        "rp":50,
        "page":1,
    }
    response = requests.post(url,data=data)
    fund_ori = json.loads(response.content)
    try:
        fund_native = json.load(open(fund_id,"r"))
    except:
        fund_native = []
    for r in fund_ori["rows"]:
        if all(map(lambda p: p["hist_dt"]!=r["cell"]["hist_dt"], fund_native)):
            fund_native.append(r["cell"])
            print(fund_id, "add fund date:")
            pprint.pprint(r["cell"])
    json.dump(fund_native, open(fund_id,"w"))

def main():
    update_fund_list()
    update_fund(fund_id="159901")


if __name__ == '__main__':
    main()