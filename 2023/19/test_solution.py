import solution
test_data = [l.strip() for l in '''
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
'''.split('\n') if len(l.strip())]

'''

'''
def test_part_1():
    expected_part_1 = 19114
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 167409079868000
    assert solution.part_2(test_data) == expected_part_2

def test_parse_input():
    rules =         {'px':[{
         'key':'a',
          'op':'<',
          'val':2006,
          'res':'qkq',
         },
         {'key':'m',
          'op':'>',
          'val':2090,
          'res':'A',
          },
         {
          'res':'rfg',
          }]
         ,}
    data = [{'x':2127,'m':1623,'a':2188,'s':1013}]
    assert (rules, [] ) == solution.parse_data(test_data[:1])
    assert ({}, data ) == solution.parse_data(test_data[-1:])

def parse_for():
    rules = {'aaa':[
        {'key':'m',
         'op':'<',
         'val':5,
         'res':'R',
         },
        {'val':'bbb'}
        ],
        'bbb':[
            {'key':'a',
             'op': '>',
             'val':10,
             'res':'R',
             },
            {'res':'A'}
            ]
        }
    data = [
        [{'a' : 9,'x':0,'m':0,'s':0}, False],
        [{'a' : 11,'x':0,'m':5,'s':0}, False],
        [{'a' : 9,'x':0,'m':5,'s':0}, True],
        [{'a' : 11,'x':0,'m':0,'s':0}, False],
        ]

    for d in data:
        assert solution.process_for(rules[0], rules, d[0]) == d[1]

