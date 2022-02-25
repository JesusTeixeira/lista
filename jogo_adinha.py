from unicodedata import digit


secreto = input('Digite uma palavra secreta: ')
digitadas = []


while True:
    letra = input('Digite uma letra: ')
    
    
    if len(letra) < 1:
        print('Isso não vale, digite somente uma letra...')
        continue
    
    digitadas.append(letra)
    
    if letra in secreto:
        print(f'Exite a letra "{letra}" na palavra secreta.')
    else:
        print(f'Não tem essa letra "{letra}" na palavra secreta.')
        digitadas.pop()
        
    
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
            
    if secreto_temporario == secreto:
        print(f'Parabéns, você ganhou!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}.')