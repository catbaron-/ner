#!/usr/bin/env python

import sys
from attr import *

#KnownWikiList Files to read
Knownlists = [
'WikiArtWork',
'WikiArtWorkRedirects',
'WikiCompetitionsBattlesEvents',
'WikiCompetitionsBattlesEventsRedirects',
'WikiFilms',
'WikiFilmsRedirects',
'WikiLocations',
'WikiLocationsRedirects',
'WikiManMadeObjectNames',
'WikiManMadeObjectNamesRedirects',
'WikiOrganizations',
'WikiOrganizationsRedirects',
'WikiPeople',
'WikiPeopleRedirects',
'WikiSongs',
'WikiSongsRedirects',
'cardinalNumber',
'currencyFinal',
'known_corporations',
'known_country',
'known_jobs',
'known_name',
'known_names.big',
'known_nationalities',
'known_place',
'known_state',
'known_title',
'measurments',
'ordinalNumber',
'temporal_words',
]
#features and their RE
fea_regs = {
    'd2':d2,
    'd4':d4,
    'date':date,
    'au':au, 
    'ad':ad,
    'al':al,
    'iu':iu,
    'cd':cd, 
    'da':da,
    'dm':dm,
    'ds':ds,
    'dc':dc, 
    'dd':dd,
    'seq':seq,
    'up':up,
    'ao':ao, 
    'cu':cu,
    'cl':cl,
    'ca':ca,
    'cs':cs, 
    'comma':comma,
    'dot':dot,
    'dollar':dollar,
    'sharp':sharp,
    'quote':quote,
    'dquote':dquote,
    'lp':lp,
    'rp':rp,
    'fin':fin,
    'mid':mid,
}

def readiter(fi, names=('y', 'w', 'pos', 'chk'), sep='\t'):
    seq = []
    for line in fi:
        line = line.strip('\n')
        if not line:
            yield seq
            seq = []
        else:
            fields = line.split(sep)
            if len(fields) != len(names):
                raise ValueError(
                    'Each line must have %d fields: %s\n' % (len(names), line))
            seq.append(dict(zip(names, tuple(fields))))

def apply_template(seq, t, template):
    name = '|'.join(['%s[%d]' % (f, o) for f, o in template])
    values = []
    for field, offset in template:
        p = t + offset
        if p not in range(len(seq)):
            return None
        values.append(seq[p][field])
    return '%s=%s' % (name, '|'.join(values))

def escape(src):
    return src.replace(':', '__COLON__')

def addToTemplates(templates,item):
    templates += [((item, i),) for i in range(-2, 3)]
    templates += [((item, i), (item, i+1)) for i in range(-2, 2)]
    return templates

def readAttr(v, fea_regs, item):
    v[item] = str(isX(fea_regs[item],v['w']))
    return v
    

if __name__ == '__main__':
    fi = sys.stdin
    fo = sys.stdout

    templates = []
    templates += [(('w', i),) for i in range(-2, 3)]
    templates += [(('w', i), ('w', i+1)) for i in range(-2, 2)]
    templates += [(('pos', i),) for i in range(-2, 3)]
    templates += [(('pos', i), ('pos', i+1)) for i in range(-2, 2)]
    templates += [(('chk', i),) for i in range(-2, 3)]
    templates += [(('chk', i), ('chk', i+1)) for i in range(-2, 2)]

    # Add templates for features
    map(lambda x:addToTemplates(templates,x),fea_regs)

    # Add templates for KnownLists
    for item in Knownlists:
        templates += [((item, i),) for i in range(-2, 3)]
        templates += [((item, i), (item, i+1)) for i in range(-2, 2)]

    # Read Knownlist to memery
    kl_dict = readKnownLists(Knownlists)

    for seq in readiter(fi):
        for v in seq:
            # Extract more characteristics of the input sequence
            map(lambda x:readAttr(v,fea_regs,x), fea_regs)
            for item in Knownlists:
                v[item] = str(v['w'] in kl_dict[item])

        for t in range(len(seq)):
            fo.write(seq[t]['y'])
            for template in templates:
                attr = apply_template(seq, t, template)
                if attr is not None:
                    fo.write('\t%s' % escape(attr))
            fo.write('\n')
        fo.write('\n')
