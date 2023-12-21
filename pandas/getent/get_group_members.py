#!/usr/bin/env python
import grp
import pandas as pd

groupnames = ('davatzic', 'fanyo', 'sattertt')
grouppis = ('Christos Davatzikos', 'Yong Fan', 'Ted Satterthwaite')

df = pd.DataFrame({'group': groupnames, 'pi': grouppis})

print(df['group'].apply(grp.getgrnam))
