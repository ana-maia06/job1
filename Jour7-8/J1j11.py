def lettre(text):
    if "e" in text:
        return True

    elif "E" in text:
        return True

    else:
        return False

text1 = "Spaghetti"
text2 = "Bonjour"
text3 = "Elle"

print(lettre(text1))
print(lettre(text2))
print(lettre(text3))