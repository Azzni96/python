import textwrap

story = ("olet ranskalainen henkilö joka on kidnapattu ranskasta suomeen. Pääset kidnaappajia karkuun ja sinun tavoite on päästä takas ranskaan sinun kotimaahan"
         "miten tämä tapahtuu on että sinulla on 10 coinsia taskussa ja sun tavoite on kerätä 50 coinsia, jotta voit ostaa liput ranskaan ja voittaa pelin mutta sinä joudut ansaita sinun coinsit vastaa malla kysymyksiin joka kerta kuin vastaat okein saat jonkun verran koinsseja")

print("Huomio!\nSinut on kidnapattu ja heräät Suomesta. Kaivat taskujasi ja löydät sieltä kolikoita.\nTavoitteenasi on päästä takaisin kotimaahasi Ranskaan, mutta sinne matkustaminen on kalleinta ja se maksaa 60 kolikkoa.\nVoit kerätä kolikkoja matkustamalla maihin, joissa kohtaat kysymyksen, johon oikein vastaamalla ansaitset kolikkoja.\nHuomaa, että myös toiseen maahan lentäminen kuluttaa kolikkojasi. Vastaamalla väärin kolikot jää sinulta saamatta.")




# Set column width to 80 characters
wrapper = textwrap.TextWrapper(width=80, break_long_words=False, replace_whitespace=False)
# Wrap text
word_list = wrapper.wrap(text=story)


def getStory():
    return word_list