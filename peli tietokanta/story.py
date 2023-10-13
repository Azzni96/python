import textwrap

story = ("Huomio!\nSinut on kidnapattu ja heräät Suomesta. Kaivat taskujasi ja löydät sieltä kolikoita.\nTavoitteenasi on päästä takaisin kotimaahasi Ranskaan, mutta sinne matkustaminen on kalleinta ja se maksaa 60 kolikkoa.\nVoit kerätä kolikkoja matkustamalla maihin, joissa kohtaat kysymyksen, johon oikein vastaamalla ansaitset kolikkoja.\nHuomaa, että myös toiseen maahan lentäminen kuluttaa kolikkojasi. Vastaamalla väärin kolikot jää sinulta saamatta.")

print("Huomio!\nSinut on kidnapattu ja heräät Suomesta. Kaivat taskujasi ja löydät sieltä kolikoita.\nTavoitteenasi on päästä takaisin kotimaahasi Ranskaan, mutta sinne matkustaminen on kalleinta ja se maksaa 60 kolikkoa.\nVoit kerätä kolikkoja matkustamalla maihin, joissa kohtaat kysymyksen, johon oikein vastaamalla ansaitset kolikkoja.\nHuomaa, että myös toiseen maahan lentäminen kuluttaa kolikkojasi. Vastaamalla väärin kolikot jää sinulta saamatta.")




# Set column width to 80 characters
wrapper = textwrap.TextWrapper(width=80, break_long_words=False, replace_whitespace=False)
# Wrap text
word_list = wrapper.wrap(text=story)


def getStory():
    return word_list