from sqlalchemy import create_engine
import pandas as pd
import re

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'noc_list_raw.csv')
sept_25_2019_express = {'draw_id': 1, 'noc': re.sub('[,\\n ]', ' ', '''0013, 0016, 0111, 0112, 0113, 0114,
0122, 0125, 0131, 0212, 0213, 0421,
0423, 0601, 0621, 0631, 0632, 0651,
0711, 0712, 0714, 0821, 0822, 0912,
1114, 1121, 1211, 1212, 1213, 1215,
1221, 1223, 1224, 1225, 1226, 1241,
1242, 1243, 1251, 1252, 1254, 1311,
1313, 2112, 2131, 2134, 2142, 2148,
2161, 2171, 2172, 2221, 2222, 2242,
2251, 2252, 2253, 2263, 2281, 2282,
3122, 3143, 3211, 3212, 3215, 3234,
4011, 4021, 4033, 4151, 4152, 4161,
4163, 4165, 4166, 4211, 4212, 4214, 4215, 4216, 6221, 6222, 6235,
6331, 6332, 6342, 7201, 7202, 7204,
7231, 7237, 7305, 7311, 7312, 7321,
7322, 7381, 9213, 9241''').split(), 'score': 70, 'ita': 404, 'date': '2019-09-25', 'type': 'express'}

sept_25_2019_oid = {'draw_id': 2, 'noc': re.sub('[,\\n ]', ' ','''0013, 0016, 0111, 0112, 0113, 0114,
0122, 0125, 0131, 0212, 0213, 0421,
0423, 0601, 0621, 0631, 0632, 0651,
0711, 0712, 0714, 0821, 0822, 0912,
1114, 1121, 1211, 1212, 1213, 1215,
1221, 1223, 1224, 1225, 1226, 1241,
1242, 1243, 1251, 1252, 1254, 1311,
1313, 2112, 2131, 2134, 2142, 2148,
2161, 2171, 2172, 2221, 2222, 2242,
2251, 2252, 2253, 2263, 2281, 2282,
3122, 3143, 3211, 3212, 3215, 3234,
4011, 4021, 4033, 4151, 4152, 4161,
4163, 4165, 4166, 4211, 4212, 4214, 4215, 4216, 6221, 6222, 6235,
6331, 6332, 6342, 7201, 7202, 7204,
7231, 7237, 7305, 7311, 7312, 7321,
7322, 7381, 9213, 9241''').split(), 'score': 79, 'ita': 365, 'date': '2019-09-25', 'type': 'oid'}

oct_02_2019_express = {'draw_id': 3, 'noc': re.sub('[,\\n ]', ' ', '''0013, 0014, 0016, 0121, 0125, 0131,
0212, 0421, 0621, 0631, 0632, 0711,
0712, 0714, 0731, 0811, 0912, 1121,
1211, 1212, 1213, 1215, 1222, 1223,
1224, 1225, 1226, 1242, 1243, 1251,
1252, 1254, 1313, 2112, 2172, 2222,
2233, 2234, 2242, 2253, 2262, 2263,
2281, 2282, 3212, 3214, 3219, 3223,
3237, 4033, 4153, 4161, 4163, 4164,
4165, 4166, 4167, 4169, 4211, 4216,
6221, 6222, 6315, 6316, 6321, 6331,
6342, 7232, 7305, 7311, 7315, 7381,
8222, 9212, 9213, 9232, 9241''').split(), 'score': 68, 'ita': 396, 'date': '2019-10-02', 'type': 'express'}

oct_02_2019_oid = {'draw_id': 4, 'noc': re.sub('[,\\n ]', ' ', '''0013, 0014, 0016, 0121, 0125, 0131,
0212, 0421, 0621, 0631, 0632, 0711,
0712, 0714, 0731, 0811, 0912, 1121,
1211, 1212, 1213, 1215, 1222, 1223,
1224, 1225, 1226, 1242, 1243, 1251,
1252, 1254, 1313, 2112, 2172, 2222,
2233, 2234, 2242, 2253, 2262, 2263,
2281, 2282, 3212, 3214, 3219, 3223,
3237, 4033, 4153, 4161, 4163, 4164,
4165, 4166, 4167, 4169, 4211, 4216,
6221, 6222, 6315, 6316, 6321, 6331,
6342, 7232, 7305, 7311, 7315, 7381,
8222, 9212, 9213, 9232, 9241''').split(), 'score': 68, 'ita': 214, 'date': '2019-10-02', 'type': 'oid'}

oct_08_2019_express = {'draw_id': 5, 'noc': re.sub('[,\\n ]', ' ', '''0111, 0112, 0114, 0122, 0821, 1114,
1221, 1241, 1311, 2171, 2174, 2251
6235, 6332, 7321''').split(), 'score': 69, 'ita': 231, 'date': '2019-10-08', 'type': 'express'}

oct_08_2019_oid = {'draw_id': 6, 'noc': re.sub('[,\\n ]', ' ', '''0111, 0112, 0114, 0122, 0821, 1114,
1221, 1241, 1311, 2171, 2174, 2251
6235, 6332, 7321''').split(), 'score': 69, 'ita': 328, 'date': '2019-10-08', 'type': 'oid'}

oct_17_2019_express = {'draw_id': 7, 'noc': re.sub('[,\\n ]', ' ', '''0621, 0631, 0711, 0821, 1114, 1311,
2171, 4212, 4214, 6221, 7312,
7321''').split(), 'score': 67, 'ita': 986, 'date': '2019-10-17', 'type': 'express'}

oct_24_2019_oid = {'draw_id': 8, 'noc': re.sub('[,\\n ]', ' ', '''0013, 0014, 0111, 0112, 0113, 0114,
0121, 0122, 0125, 0131, 0132, 0212,
0213, 0421, 0423, 0601, 0621, 0631,
0632, 0651, 0711, 0714, 0731, 0821,
0912, 1114, 1121, 1211, 1212, 1213,
1215, 1221, 1222, 1223, 1224, 1225,
1226, 1241, 1242, 1243, 1252, 1253,
1311, 1313, 2134, 2142, 2144, 2148,
2171, 2172, 2174, 2221, 2222, 2233,
2234, 2242, 2251, 2252, 2253, 2262,
2263, 2264, 2272, 2281, 2282, 3143,
3211, 3212, 3214, 3215, 3217, 3219,
3223, 3234, 4011, 4021, 4033, 4151,
4152, 4153, 4161, 4163, 4164, 4165,
4166, 4167, 4169, 4211, 4212, 4214,
4214, 4215, 4216, 6221, 6235, 6315,
6316, 6321, 6331, 6332, 6342, 6344,
7201, 7202, 7204, 7231, 7235, 7236,
7237, 7241, 7242, 7243, 7244, 7251,
7271, 7281, 7294, 7305, 7311, 7312,
7313, 7321, 7322, 7381, 7384, 8211,
8222, 9213, 9231, 9232''').split(), 'score': 69, 'ita': 550, 'date': '2019-10-24', 'type': 'oid'}

oct_24_2019_express = {'draw_id': 9, 'noc': re.sub('[,\\n ]', ' ', '''0013, 0014, 0111, 0112, 0113, 0114,
0121, 0122, 0125, 0131, 0132, 0212,
0213, 0421, 0423, 0601, 0621, 0631,
0632, 0651, 0711, 0714, 0731, 0821,
0912, 1114, 1121, 1211, 1212, 1213,
1215, 1221, 1222, 1223, 1224, 1225,
1226, 1241, 1242, 1243, 1252, 1253,
1311, 1313, 2134, 2142, 2144, 2148,
2171, 2172, 2174, 2221, 2222, 2233,
2234, 2242, 2251, 2252, 2253, 2262,
2263, 2264, 2272, 2281, 2282, 3143,
3211, 3212, 3214, 3215, 3217, 3219,
3223, 3234, 4011, 4021, 4033, 4151,
4152, 4153, 4161, 4163, 4164, 4165,
4166, 4167, 4169, 4211, 4212, 4214,
4214, 4215, 4216, 6221, 6235, 6315,
6316, 6321, 6331, 6332, 6342, 6344,
7201, 7202, 7204, 7231, 7235, 7236,
7237, 7241, 7242, 7243, 7244, 7251,
7271, 7281, 7294, 7305, 7311, 7312,
7313, 7321, 7322, 7381, 7384, 8211,
8222, 9213, 9231, 9232''').split(), 'score': 69, 'ita': 372, 'date': '2019-10-24', 'type': 'express'}

data = {
    1: sept_25_2019_express, 
    2: sept_25_2019_oid,
    3: oct_02_2019_express,
    4: oct_02_2019_oid,
    5: oct_08_2019_express,
    6: oct_08_2019_oid,
    7: oct_17_2019_express,
    8: oct_24_2019_oid,
    9: oct_24_2019_express
}

draws_obj = {
    'draw_id': [x for x in data], 
    'date': [x for x in (y['date'] for y in data.values())], 
    'draw_type': [x for x in (y['type'] for y in data.values())], 
    'invitations': [x for x in (y['ita'] for y in data.values())],
    'score': [x for x in (y['score'] for y in data.values())]
}

nocs_draws_obj = {'noc_id': [], 'draw_id': []}
for x in data.values():
    nocs_draws_obj['noc_id'] = nocs_draws_obj['noc_id'] + x['noc']
    nocs_draws_obj['draw_id'] = nocs_draws_obj['draw_id'] + [x['draw_id']]*len(x['noc'])

df = pd.read_csv(filename)
df['noc'] = df['noc'].astype('str')
df['noc'] = df['noc'].apply(lambda x: '{0:0>4}'.format(x))

nocs = df
nocs.columns = ['noc_id', 'title', 'skill_level', '2019_est_employments', '2019_wage_est', 'job_outlook', 'job_openings', 'soft_skills']
draws = pd.DataFrame(draws_obj)
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
    z = nocs.merge(nocs_draws).merge(draws)[['noc_id','date', 'draw_type']]
    z['draw_date_type'] = z['date'].astype('str')+'_'+z['draw_type']
    z = z.drop_duplicates().sort_values(by='noc_id')
    x=pd.get_dummies(z['draw_date_type'])
    j=pd.concat([z,x], axis=1)
    j = j.drop(['draw_date_type'], axis=1)
    k = j.groupby('noc_id')
    final = nocs.merge(k.sum(), on='noc_id')
    final = final.drop(['soft_skills', '2019_wage_est'], axis=1)
    final['total'] = final.filter(regex='2019-.*').sum(axis=1)
    final.update(final.filter(regex='2019-.*').replace(to_replace=[1,0],value=['Yes', 'No']))
    return final.to_dict(orient="records")