import lang

while True:
    text = input('> ')
    if text.strip() == "": continue
    result, error = lang.run('program1.lang', text)

    if error: 
        print(error.as_string())
    elif result: 
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))

######EP 12 16:13