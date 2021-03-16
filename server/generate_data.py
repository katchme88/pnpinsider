#from sqlalchemy import create_engine
import pandas as pd
import re

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'noc_list_raw.csv')

draws = pd.read_csv('eoi.csv')
draws['date'] = draws.date.astype('datetime64[ns]')
draws = draws.sort_values(by=['date'], ascending=True).reset_index(drop=True)
draws = draws.reset_index()
draws.columns = ['draw_id', 'date', 'draw_type', 'score', 'invitations', 'nocs']
draws.draw_id = draws.draw_id + 1


nocs_draws_obj = {'noc_id': [], 'draw_id': []}
for i in range (len(draws)):
    nocs_list =  [x.strip() for x in draws.iloc[i].nocs.split(',')]
    draw_id = draws.iloc[i].draw_id
    nocs_draws_obj['noc_id'] = nocs_draws_obj['noc_id'] + nocs_list
    nocs_draws_obj['draw_id'] = nocs_draws_obj['draw_id'] + [draw_id]*len(nocs_list)

df = pd.read_csv(filename)
df['noc'] = df['noc'].astype('str')
df['noc'] = df['noc'].apply(lambda x: '{0:0>4}'.format(x))

nocs = df
nocs.columns = ['noc_id', 'title', 'skill_level', '2019_est_employments', '2019_wage_est', 'job_outlook', 'job_openings', 'soft_skills']
nocs_draws= pd.DataFrame(nocs_draws_obj)

# engine = create_engine('postgresql+psycopg2://postgres:talha@localhost/pnpinsider', echo=False)

# nocs.to_sql('nocs', con=engine, if_exists='replace', index=False)
# draws.to_sql('draws', con=engine, if_exists='replace', index=False)
# nocs_draws.to_sql('nocs_draws', con=engine, if_exists='replace', index=False)

def get_draws_summary():
    return draws.to_dict(orient="records")

def get_draws_details(draw_id=1):
    z = nocs_draws.merge(draws)[['noc_id','date', 'draw_type', 'draw_id']].merge(nocs)
    z = z[(z.draw_id == int(draw_id))]
    return z.to_dict(orient="records")

def get_nocs(noc_id = 'all'):
    if noc_id == 'all':
        return nocs.to_dict(orient="records")
    else:
        return nocs[nocs.noc_id == noc_id].to_dict(orient="records")

def getOverview():
    z = nocs.merge(nocs_draws, on='noc_id', how='left').merge(draws, how='left')[['noc_id','date', 'draw_type']]
    z['draw_date_type'] = z['date'].astype('str')+'_'+z['draw_type']
    z = z.drop_duplicates().sort_values(by='noc_id')
    x=pd.get_dummies(z['draw_date_type'])
    j=pd.concat([z,x], axis=1)
    j = j.drop(['draw_date_type'], axis=1)
    k = j.groupby('noc_id')
    final = nocs.merge(k.sum(), on='noc_id')
    final = final.drop(['soft_skills', '2019_wage_est'], axis=1)
    final['total'] = final.filter(regex='2019-|2020-|2021.*').sum(axis=1)    
    final.update(final.filter(regex='2019-|2020-|2021.*').replace(to_replace=[1,0],value=['YES', 'NO']))
    columns = final.columns.to_list()
    col_1 = columns[0:6]
    col_2 = [columns[-1]]
    col_3 = columns[6:-1]
    col_3.reverse()
    col=col_1+col_2+col_3
    final = final[final.total > 0]
    return final[col].to_dict(orient="records")
