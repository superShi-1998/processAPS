from collections import defaultdict
import pandas as pd,codecs,json

big_table = []
journals = [j for j in os.listdir('.') if '.' not in j]
for journal in journals:
    volumes = [v for v in os.listdir(journal) if '.' not in v]
    for volume in volumes:
        papers = [p for p in os.listdir(journal+'/'+volume) if '.json' in p]
        for paper in papers:
            filename = journal+'/'+volume+'/'+paper
            pdata = codecs.open(filename,encoding='utf-8').read()
            pdata = json.loads(pdata)
            doi = pdata['identifiers']['doi']
            for a in pdata['authors']:
                a = defaultdict(lambda:'NULL',a)
                affs = dict([(af['id'],af['name']) for af in pdata['affiliations']])
                for af in a[u'affiliationIds']:
                    big_table.append((doi,a['firstname'],a['surname'],a['name'],(a['type'].lower().strip()=='person'),affs[af]))
big_table = pd.DataFrame(big_table,columns=['DOI','firstname','surname','name','person','af_name'])

paper_author = big_table[['DOI','firstname','surname','name','person']].drop_duplicates()
authors = paper_author.drop('DOI',1).drop_duplicates()
authors = authors.reset_index().drop('index',1).reset_index().rename(columns={'index':'AID'})
paper_author = pd.merge(paper_author,authors)[['DOI','AID']].drop_duplicates()
affiliations = pd.merge(big_table,authors)[['DOI','AID','af_name']].drop_duplicates()

authors.to_csv('authors.csv',index=False,encoding='utf-8')
paper_author.to_csv('paper_author.csv',index=False,encoding='utf-8')
affiliations.to_csv('affiliations.csv',index=False,encoding='utf-8')