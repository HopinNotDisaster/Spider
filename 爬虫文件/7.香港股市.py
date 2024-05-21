from lxml import etree

import requests

url = 'https://hk.investing.com/equities/hong-kong'

res = requests.get(url=url)
# print(res.text)
# "/html[@class='html']/body[@class='typography default-theme']/div[@id='__next']/div[@class='desktop:relative desktop:bg-white']/div[@class='relative flex']/div[@class='grid flex-1 grid-cols-1 px-4 pt-5 font-sans-v2 text-[#232526] antialiased xl:container sm:px-6 md:grid-cols-[1fr_72px] md:gap-6 md:px-7 md:pt-10 md2:grid-cols-[1fr_420px] md2:gap-8 md2:px-8 xl:mx-auto']/div[@class='min-w-0']/div[@class='mb-6'][1]/div[@class='relative w-full']/div[@class='relative dynamic-table-v2_dynamic-table-wrapper__fBEvo dynamic-table-v2_scrollbar-x__R96pe']/table[@class='datatable-v2_table__93S4Y dynamic-table-v2_dynamic-table__iz42m datatable-v2_table--mobile-basic__uC0U0 datatable-v2_table--freeze-column__uGXoD undefined']/tbody[@class='datatable-v2_body__8TXQk']/tr[@class='datatable-v2_row__hkEus dynamic-table-v2_row__ILVMx']/td[@class='datatable-v2_cell__IwP1U !h-auto w-full py-2 mdMax:border-r dynamic-table-v2_col-name__Xhsxv !py-2']/div/a[@class='overflow-hidden text-ellipsis whitespace-nowrap font-semibold text-[#181C21] hover:text-[#1256A0]']/h4/span[@class='flex align-middle']/span")

html_tree = etree.HTML(res.text)
# titles = html_tree.xpath(
#     '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[4]/div[2]/div[1]/table/tbody/tr/td[2]/div/a/h4/span/span[2]')
# for title in titles:
#     print(title.text)
# print(len(titles))

# latests = html_tree.xpath(
#     '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[4]/div[2]/div[1]/table/tbody/tr/td[3]/span'
# )
# # print(latests,len(latests))
# for latest in latests:
#     print(latest.text)


links = html_tree.xpath(
    '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[4]/div[2]/div[1]/table/tbody/tr/td[2]/div/a/@href')
for link in links:
    # print(link.attrib.get('href'))
    print(link)
# print(len(links))
# print(links)
