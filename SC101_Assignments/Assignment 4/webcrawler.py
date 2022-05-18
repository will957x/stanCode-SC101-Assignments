"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
    # for year in ['2010s']:  # for tests
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {'class': "t-stripe"})
        clean1 = []
        final_m_ch = ''
        final_f_ch = ''
        final_m = 0
        final_f = 0
        for tag in tags:
            data = tag.tbody.text.split("\n")
            # print(data)
            # print(len(data))
            for i in range(len(data)):
                seg = data[i]
                # print(seg)
                if len(seg) > 3:
                    clean1.append(seg)
            # print(clean1)  # ['Noah 182,993 Emma 194,755', 'Liam 173,717 Olivia 184,291', [...] ]
            for j in range(len(clean1)):
                seg2 = clean1[j]
                # print(seg2)  # Noah 182,993 Emma 194,755
                seg3 = seg2.split(" ")
                # print(seg3)
                # print(seg3[1].replace(',', ''))
                # print(int(seg3[3].split(",")))
                if len(seg3[1]) > 1:
                    # # print(seg3[1])  # 182,993
                    # print(seg3[3])  # 194,755
                    for final1 in range(len(seg3[1])):
                        if seg3[1][final1] != ',':
                        # if seg3[1][final1].isalpha():
                            ch1 = seg3[1][final1]
                            final_m_ch += ch1
                    for final2 in range(len(seg3[3])):
                        if seg3[3][final2] != ',':
                        # if seg3[1][final2].isalpha():
                            ch2 = seg3[3][final2]
                            final_f_ch += ch2
                    final_m += int(final_m_ch)
                    final_m_ch = ''
                    final_f += int(final_f_ch)
                    final_f_ch = ''
                    # final_m += int(seg3[1].replace(',', ''))  # replace method is more succinct
                    # final_f += int(seg3[3].replace(',', ''))  # replace method is more succinct
            print(f'Male Number: {final_m} \nFemale Number: {final_f}')





if __name__ == '__main__':
    main()
