##-------------##
##--Variables--##
##-------------##

letters = ["a","ai","ay","b","ch","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","rr","s","ss","sh","t","th","u","v","w","y","z","gs"]
vowels = ["e","i","o"]

letter_names = {"a":"aho","ai":"aito","ay":"ayto","b":"beh","ch":"cho","d":"doh","e":"eho",
                "f":"fih","g":"geh","h":"hih","i":"iho","j":"joja","k":"kehi","l":"loh",
                "m":"min","n":"nin","o":"ohi","p":"peh","q":"qehi","r":"roh","rr":"arroh",
                "s":"sih","ss":"assih","sh":"shih","t":"toh","th":"thes","u":"uho","v":"vehi",
                "w":"wehu","y":"yehi","z":"zehi","gs":"glottal"}


html_format = '<td><img src="images/letters/{0}{1}.png"></td>'
table_data = '<td>{}</td>'

html = ""

positions = ["_init","_med","_fin"]

notes = {"a":"ah","ai":"eye","ay":"ay","e":"eh","g":'"guh", never makes "jay" sound',
         "i":'"ee", never make souns like "hit" or "hike"',
         "j":'Sounds like "<em>j</em>ob" when starting a word, but sounds like "vi<em>s</em>ion" otherwise',
         "o":'"oh", never sounds like in "hot"', "q":"similar to a K, but deeper in the throat",
         "r":"r's in Ta'agra are all trilled (rolled)", "s":'"s", never sounds like "z"',
         "ss":'a drown-out for of the single "s"', "th":'"th", always unvoiced like "bath", never voiced like "bathe"',
         "o":'"ooh", never sounds like "uh"', "gt":"glottal stop"}

all_positions = ["_isol","_init","_med","_fin"]

position_labels = "<tr><td>English</td><td>IPA</td><td>Isolated</td><td>Initial</td><td>Medial</td><td>Terminal</td><td>Character Name</td><td>Notes</td></tr>\n"

##-------------------##
##---Mobile Format---##
##-------------------##

##for letter in letters:
##    if letter in vowels:
##        html += "<tr>"
##        html += html_format.format(letter, "")
##        html += html_format.format(letter, positions[1])
##        html += html_format.format(letter, "")
##        html += "</tr>\n"
##        if letter in notes:
##            html += '<tr><td colspan="3">' + notes[letter] + "</td></tr>"
##    else:
##        html += "<tr>"
##        for position in positions:
##            html += html_format.format(letter, position)
##        html += "</tr>\n"
##        if letter in notes:
##            html += '<tr><td colspan="3">' + notes[letter] + "</td></tr>"

##-----------------------##
##---Fullscreen Format---##
##-----------------------##

html += position_labels
for letter in letters:
    html += "<tr>"
    html += table_data.format(letter.lower())
    html += table_data.format(letter.upper())
    
    if letter in vowels:
        html += html_format.format(letter, "")
        html += html_format.format(letter, "")
        html += html_format.format(letter, positions[1])
        html += html_format.format(letter, "")
        html += table_data.format(letter_names[letter])
        if letter in notes:
            html += table_data.format(notes[letter])
        html += "</tr>\n"

    elif letter == "gs":
        html += html_format.format(letter, "")
        html += html_format.format(letter, "")
        html += html_format.format(letter, "")
        html += html_format.format(letter, "")
        html += table_data.format(letter_names[letter])
        if letter in notes:
            html += table_data.format(notes[letter])
        html += "</tr>\n"

    else:
        for position in all_positions:
            html += html_format.format(letter, position)
        html += table_data.format(letter_names[letter])
        if letter in notes:
            html += table_data.format(notes[letter])
        html += "</tr>\n"

    

print(html)
