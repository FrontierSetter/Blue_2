import openpyxl
import json

def xlsx2obj(wb):
    data = {}
    titles = ["6-3各国年度劳动生产率（美元每人）",
              "6-4各国年度GDP数据（亿美元）",
              "6-5各国年度商品出口单位价值指数（上一年= 100）",
              "6-10主要国家年度GDP" ]
    for sheet in wb:
        if sheet.title not in titles:
            continue
        tab = []
        rowcount = 0
        for rows in sheet.values:
            if(rowcount == 0):
                rowcount = 1
                firstrow = list(rows)
                tmprow = []
                tmprow.append(firstrow[0])
                for i in range(1, len(firstrow)):
                    if(firstrow[i] != None):
                        tmprow.append(firstrow[i])
                    else:
                        break
                tab.append(tmprow)
                continue
            if(rows[0] != None):
                tmprow = []
                for item in rows:
                    if(item != None):
                        tmprow.append(item)
                    else:
                        break
                tab.append(tmprow)
        sheetdata = {sheet.title:tab}
        data.update(sheetdata)
    return data

if __name__=="__main__":
    wb = openpyxl.load_workbook('gdp.xlsx')
    data = {}
    data.update(xlsx2obj(wb))
    jsondata = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    jsondata2 = json.dumps(data, sort_keys=True)
    with open("gdp.json", mode='w+', encoding='utf-8') as f:
        f.write('callback_gdp('+jsondata+')')
    with open("gdp2.json", mode='w+', encoding='utf-8') as f:
        f.write('callback_gdp('+jsondata2+')')