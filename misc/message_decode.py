import base64 

Mess="CUxLTFdaVkJBFBUDUkxfS1FYRxYeExJaHQdUXFVeRlQVEw8ZVQ5LTVFcXlRWFBkZVQ5eX1tLR0IV Ew8ZVQJWWkZcV1hQX1AeXksfWFdRWlREVlhcHB8fGQ4ZFERcX1paGQ5cHhgZFENTUVdQBhgfGQ4Z FEJTVVAeXksfX1tWFBEIExJOGwUZHkk="

key='rk8949312359'

result=[]

for i,c in enumerate(base64.b64decode(Mess)):
    result.append(chr(ord(c)^ord(key[i%len(key)])))

print(''.join(result))
"""
{'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}

! ! ! ! Osm ! ! ! !
"""
