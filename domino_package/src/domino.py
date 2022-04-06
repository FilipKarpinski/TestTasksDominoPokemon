def iteration(text):
    new_text = ''

    for x in range(1, len(text) - 1):
        if text[x] == '|':
            if text[x-1] == '/' and text [x+1] != '\\':
                new_text += '/'
            elif text[x+1] == '\\' and text [x-1] != '/':
                new_text += '\\'
            else:
                new_text += '|'
        else: 
            new_text += text[x]

    if text[0] == '|' and text[1] == '\\':
        new_text = '\\' + new_text
    else:
        new_text = text[0] + new_text

    if text[-1] == '|' and text[-2] == '/':
        new_text = new_text + '/'
    else:
        new_text = new_text + text[-1]

    return new_text

def run_domino(text, n):
    if not all(x in "/|\\" for x in text) or n < 1:
        raise ValueError('Incorrect input')

    if len(text) < 2:
        return text

    new_text = text
    for x in range (n):
        new_text = iteration(new_text)
    
    return new_text

def reverse_iteration(text):
    if len(text) == 2:
        if text[0] != text[1] or (text[0] == text[1] and text[0] == '|'):
            return '||'
        elif text[0] == '/':
            return '/|'
        else:
            return '|\\'

    new_text = ''

    for x in range(1, len(text) - 1):
        if (text[x] == '|') or (text[x] == '/' and text[x+1] != '/') or (text[x] == '\\' and text[x-1] != '\\'):
            new_text += '|'
        else:
            new_text += text[x]
            
    if text[0] == text[1]:
        new_text = text[0] + new_text
    else:
        new_text = '|' + new_text

    if text[-1] == text[-2]:
        new_text = new_text + text[-1]
    else:
        new_text = new_text + '|'
    
    return new_text

def reverse_run_domino(text, n):
    if not all(x in "/|\\" for x in text) or n < 1:
        raise ValueError('Incorrect input')

    if len(text) < 2:
        return text

    new_text = text
    for x in range (n):
        new_text = reverse_iteration(new_text)
    
    return new_text