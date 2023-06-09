def generateDocument(characters, document):
    # Write your code here.
    # abhinav_code
    from collections import Counter
    a=Counter(characters)
    b=Counter(document)

    if len(list((b-a).keys()))>0:
        return Falsae
    else:
        return True


