
import nltk
from nltk.chat.util import Chat,reflections

reflections_pt = {
    'eu': 'você',
    'eu sou ':'você é',
    'eu era ':'você era',
    'eu iria ': 'você iria',
    'eu irei': 'você irá',
    'meu': 'seu',
    'meus': 'seus',
    'você': 'eu',
    'você é':'eu sou',
    'vocÊ era ': 'eu era',
    'você iria ': 'eu iria',
    'você irá': 'eu irei',
    'seu ': 'meu',
    'seus': 'meus',
}
pares = [
    [
        r'olá|Opa|Oi|Iae (.*)',
        ['Olá','Como Vai ','tudo bem']
    ],
    [r'(.*)idade', # r - expressão regular  e (.*) permite identificar qauqleur caracter
     ['Não tenho uma idade definida']
    ],
    [r'(.*)bem',  # r - expressão regular  e (.*) permite identificar qauqleur caracter
     ['Sim e vc? ']
    ],
    [r'meu nome é (.*)',
     ['Olá %1 como vc está ?O que você faz? ']
    ],
    [r'eu (.*)',
     ['Que legal! Como é %1']
    ],
    [r'quit',
        ['Até Logo']
    ],
    [r'quit',
     ['Até a próxima']
     ]
]
print('Olá sou chatIn')
chat = Chat(pares, reflections_pt)
chat.converse()



