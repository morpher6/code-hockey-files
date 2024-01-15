from bs4 import BeautifulSoup as Soup

table_html = """
<html>
  <table>
    <tr>
     <th>Name</th>
     <th>Date</th>
     <th>Team</th>
     <th>Opp</th>
     <th>Shots</th>
     <th>Goals</th>
    </tr>
    <tr>
     <td>Sidney Crosby</td>
     <td>2019-10-03</td>
     <td>PIT</td>
     <td>BUF</td>
     <td>4</td>
     <td>1</td>
    </tr>
    <tr>
     <td>Alexander Ovechkin</td>
     <td>2019-10-05</td>
     <td>WAS</td>
     <td>CAR</td>
     <td>9</td>
     <td>2</td>
    </tr>
  </table>
<html>
"""

html_soup = Soup(table_html)

tr_tag = html_soup.find('tr')
tr_tag
type(tr_tag)

table_tag = html_soup.find('table')
table_tag
type(table_tag)

td_tag = html_soup.find('td')
td_tag
type(td_tag)

# simple tags
td_tag
td_tag.string
str(td_tag.string)

# nested tags
tr_tag.find_all('th')

[str(x.string) for x in tr_tag.find_all('th')]

# other notes on find_all and nested tags
all_td_tags = table_tag.find_all('td')
all_td_tags

all_rows = table_tag.find_all('tr')
first_data_row = all_rows[1]  # 0 is header
first_data_row.find_all('td')

all_td_and_th_tags = table_tag.find_all(('td', 'th'))
all_td_and_th_tags

[str(x.string) for x in all_td_tags]

all_rows = table_tag.find_all('tr')
list_of_td_lists = [x.find_all('td') for x in all_rows[1:]]
list_of_td_lists
