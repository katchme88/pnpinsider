from sqlalchemy import create_engine
import pandas as pd
import re

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'noc_list_raw.csv')
print (filename)
sept_25_2019_express = {'noc': re.sub('[,\\n ]', ' ', '''0013, 0016, 0111, 0112, 0113, 0114,
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
7322, 7381, 9213, 9241''').split(), 'score': 70, 'ita': 404}

sept_25_2019_oid = {'noc': re.sub('[,\\n ]', ' ','''0013, 0016, 0111, 0112, 0113, 0114,
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
7322, 7381, 9213, 9241''').split(), 'score': 79, 'ita': 365}

oct_02_2019_express = {'noc': re.sub('[,\\n ]', ' ', '''0013, 0014, 0016, 0121, 0125, 0131,
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
8222, 9212, 9213, 9232, 9241''').split(), 'score': 68, 'ita': 396}

oct_02_2019_oid = {'noc': re.sub('[,\\n ]', ' ', '''0013, 0014, 0016, 0121, 0125, 0131,
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
8222, 9212, 9213, 9232, 9241''').split(), 'score': 68, 'ita': 214}

oct_08_2019_express = {'noc': re.sub('[,\\n ]', ' ', '''0111, 0112, 0114, 0122, 0821, 1114,
1221, 1241, 1311, 2171, 2174, 2251
6235, 6332, 7321''').split(), 'score': 69, 'ita': 231}

oct_08_2019_oid = {'noc': re.sub('[,\\n ]', ' ', '''0111, 0112, 0114, 0122, 0821, 1114,
1221, 1241, 1311, 2171, 2174, 2251
6235, 6332, 7321''').split(), 'score': 69, 'ita': 328}

oct_17_2019_express = {'noc': re.sub('[,\\n ]', ' ', '''0621, 0631, 0711, 0821, 1114, 1311,
2171, 4212, 4214, 4214, 6221, 7312,
7321''').split(), 'score': 67, 'ita': 986}

df = pd.read_csv(filename)
df['noc'] = df['noc'].astype('str')
df['noc'] = df['noc'].apply(lambda x: '{0:0>4}'.format(x))
df['statscan_link'] = df['noc'].apply(lambda x: f'https://www120.statcan.gc.ca/stcsr/en/cm1/cls?fq=ds%3A102noc2016&start=0&showSum=show&q={x}')

nocs = df
nocs.columns = ['noc_id', 'title', 'skill_level', '2019_est_employments', '2019_wage_est', 'job_outlook', 'job_openings', 'soft_skills', 'statscan_link']
draws = pd.DataFrame({'draw_id':[1,2,3,4,5,6,7], 'date': ['2019-09-25','2019-09-25','2019-10-02','2019-10-02','2019-10-08','2019-10-08','2019-10-17'], 'draw_type':['express','oid','express','oid','express','oid','express'], 'invitations': [404,365,396,214,231,328,986], 'score': [70,79,68,68,69,69,67]})

nocs_draws = pd.DataFrame({'draw_id': [1]*len(sept_25_2019_express['noc']), 'noc_id': sept_25_2019_express['noc']})
nocs_draws = nocs_draws.append(pd.DataFrame({'draw_id': [2]*len(sept_25_2019_oid['noc']), 'noc_id': sept_25_2019_oid['noc']}))
nocs_draws = nocs_draws.append(pd.DataFrame({'draw_id': [3]*len(oct_02_2019_express['noc']), 'noc_id': oct_02_2019_express['noc']}))
nocs_draws = nocs_draws.append(pd.DataFrame({'draw_id': [4]*len(oct_02_2019_oid['noc']), 'noc_id': oct_02_2019_oid['noc']}))
nocs_draws = nocs_draws.append(pd.DataFrame({'draw_id': [5]*len(oct_08_2019_express['noc']), 'noc_id': oct_08_2019_express['noc']}))
nocs_draws = nocs_draws.append(pd.DataFrame({'draw_id': [6]*len(oct_08_2019_oid['noc']), 'noc_id': oct_08_2019_oid['noc']}))
nocs_draws = nocs_draws.append(pd.DataFrame({'draw_id': [7]*len(oct_17_2019_express['noc']), 'noc_id': oct_17_2019_express['noc']}))


# engine = create_engine('postgresql+psycopg2://postgres:talha@localhost/pnpinsider', echo=False)

# nocs.to_sql('nocs', con=engine, if_exists='replace', index=False)
# draws.to_sql('draws', con=engine, if_exists='replace', index=False)
# nocs_draws.to_sql('nocs_draws', con=engine, if_exists='replace', index=False)

def get_draws():
    return draws.to_dict(orient="records")

def get_nocs(noc_id = 'all'):
    if noc_id == 'all':
        return nocs.to_dict(orient="records")
    else:
        return nocs[nocs.noc_id == noc_id].to_dict(orient="records")