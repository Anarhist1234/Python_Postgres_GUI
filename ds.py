import datetime
import pandas as pd
a = [(1, 2, datetime.time(15, 49, 21, 520587)), (2, 2, datetime.time(15, 49, 22, 982575)), (3, 2, datetime.time(15, 49, 23, 886585)), (4, 2, datetime.time(15, 49, 24, 956346)), (5, 2, datetime.time(15, 49, 25, 916559)), (6, 2, datetime.time(15, 49, 26, 725147)), (7, 1, datetime.time(15, 49, 29, 622526)), (8, 1, datetime.time(15, 49, 30, 551142)), (9, 1, datetime.time(15, 49, 31, 439169)), (10, 1, datetime.time(15, 49, 32, 213920)), (11, 1, datetime.time(15, 49, 32, 950449)), (12, 1, datetime.time(15, 49, 33, 665522)), (13, 1, datetime.time(15, 49, 34, 449839)), (14, 1, datetime.time(15, 49, 35, 458743)), (15, 1, datetime.time(15, 49, 37, 179675)), (16, 3, datetime.time(15, 49, 38, 921298)), (17, 3, datetime.time(15, 49, 39, 679997)), (18, 3, datetime.time(15, 49, 40, 495103)), (19, 3, datetime.time(15, 49, 41, 302693)), (20, 3, datetime.time(15, 49, 42, 186871)), (21, 3, datetime.time(15, 49, 42, 952895)), (22, 3, datetime.time(15, 49, 43, 709114)), (23, 3, datetime.time(15, 49, 44, 445245)), (24, 3, datetime.time(15, 49, 45, 403400))]

k = pd.DataFrame(a, columns=['id', 'calls_id', 'time'])
print(k)