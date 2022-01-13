from gigadq import gigaid
#import gigadq.gigaid
import pandas as pd

#df1 = pd.read_csv('test_data.csv')
data = [['tom', 10, 2], ['nick', 15, 3], ['juli', 14, 5]]
df = pd.DataFrame(data, columns = ['schoolname', 'schoolid', 'extra'])
#gigaid.gid(df)
print(gigaid.gid(df, v1 = 'schoolname', v2 = 'schoolid', v3 = 'extra'))
