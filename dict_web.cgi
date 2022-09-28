#! /usr/bin/env python3

import csv, cgi

form = cgi.FieldStorage()

print('Content-type: text/html\n')

html = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Dictionary</title>
<link rel="stylesheet" href="css/normalize.css">
<link rel="stylesheet" href="css/styles.css">
<link href="https://fonts.googleapis.com/css?family=Medula+One|;Forum|;Open+Sans" rel="stylesheet">
<link rel="stylesheet" href="//use.fontawesome.com/releases/v5.0.7/css/all.css">

<meta name="viewport" content="initial-scale=1, maximum-scale=1">

</head>
    <body>
		<nav class="topnav" id="myTopnav">
			<div class="nav_links">
			<a href="index.php" class="home_button"><img src="images/logo_white_left.png" alt="taagra logo"></a>
			<a href="index.php" class="dropbtn">Home</a>
			<div class="dropdown active">
				<button class="dropbtn">Dictionary
				</button>
			<div class="dropdown-content">
			<a href="dictionary.php">Dictionary</a>
			<a href="lookup.php">Word Lookup</a>
			<a href="#">Phrases</a>
			<a href="#">Change Log</a>
			</div>
			</div>
			<div class="dropdown">
				<button class="dropbtn">Script
				</button>
			<div class="dropdown-content">
			<a href="alphabet.php">Alphabet</a>
			<a href="script.php">Script &amp; Font</a>
			<a href="#">Numbers</a>
			</div>
			</div>
			<div class="dropdown">
				<button class="dropbtn">Grammar
				</button>
			<div class="dropdown-content">
			<a href="grammar.php">Grammar Rules</a>
			<a href="#">Irregular verbs</a>
			<a href="#">Pronouns</a>
			</div>
			</div>
			<div class="dropdown">
				<button class="dropbtn">Phrases
				</button>
			<div class="dropdown-content">
			<a href="#">Memrise</a>
			<a href="#">Worksheets</a>
			<a href="#">Ta'agra for the Unclawed</a>
			</div>
			</div>
			<div class="dropdown">
				<button class="dropbtn">Documentation
				</button>
			<div class="dropdown-content">
			<a href="#">Source Docs</a>
			<a href="#">Legal</a>
			</div>
			</div>
			</div>

			<div class="social_links">
				<a href="https://www.patreon.com/taagra/creators"><i class="fab fa-patreon"></i></a>
				<a href="https://discord.gg/CkRksCf"><i class="fab fa-discord"></i></a>
				<a href="https://www.youtube.com/channel/UCCplcqENJl555fWl6r_Rycg"><i class="fab fa-youtube"></i></a>
				<a href="https://twitter.com/taagraproject"><i class="fab fa-twitter"></i></a>
			</div>
		<a href="javascript:void(0);" class="icon" onclick="myFunction()">&#9776;</a>
		</nav>
	<main class="content_main">

<div class="search_form">
<form action="dict_web.cgi" method="post">
	<h1 class="content_title">Ta'agra Dictionary</h1>

	<div class="search_tools">

	<div class="search_bar">
	<input type="text" name="search_term" autocomplete="off" placeholder="  What would you like to search..."><br>
    	<button type="submit" class="submit_button"><i class="fas fa-search"></i></button>
	</div>
	<label class="switch">
		<input type="checkbox" id="togBtn" name="language" value="taagra">
		<div class="slider round">
		<span class="tag">TA'AGRA</span><span class="eng">ENGLISH</span>
		</div>
	</label>

	</div>

</form>
</div>
	<div class="content search_result_block">
	<p>{1}</p>
	</div>
</main>
	</body>
</html>"""

parts_of_speech = {"n":"noun", "adj":"adjective", "v":"verb", "adv":"adverb", "cj":"conjunction", "pn":"pronoun"}
dict_entry = """

<div class="search_results">
<p class="planewalker">{tag}</p>

<p class="part_of_speech">{part}</p>
<table>
	<tr>
	<td>English:</td>
	<td>{eng}</td>
	</tr>

	<tr>
	<td>Part of Speech:</td>
	<td>{part}</td>
	</tr>

	<tr>
	<td>Synonyms:</td>
	<td>{syn}</td>
	</tr>

	<tr>
	<td>Notes:</td>
	<td>{note}</td>
	</tr>
</table>
</div>

"""
content = ""
##lang = form.getfirst('language', 'english')
##search = form.getfirst('search_term', ' ').lower()
toggle = ""

###
lang = "english"
search = "accepts"
###s

if lang == "english":
  with open('tadictionary.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', lineterminator="\n")
    found = False
    for line in csv_reader:
      if line[0] == search:
        found = True
        part_of_speech = line[2].split("/")
        pos = ""
        for item in part_of_speech:
          if item in parts_of_speech:
            pos += parts_of_speech[item] + " "
        content += dict_entry.format(eng=line[0], tag=line[1], part=pos, syn=line[3], note=line[4])
        print(line[1])

  if found == False:
    with open('tadictionary.csv', 'r') as csvfile:
      csv_reader = csv.reader(csvfile, delimiter=',', lineterminator="\n")
      for line in csv_reader:
        synonyms = []
        for item in line[3].split():
          synonyms.append(item.strip().replace(',',''))
        if search in synonyms:
          found = True
          part_of_speech = line[2].split("/")
          pos = ""
          for item in part_of_speech:
            if item in parts_of_speech:
              pos += parts_of_speech[item] + " "
          content += dict_entry.format(eng=line[0], tag=line[1], part=pos, syn=line[3], note=line[4])
          print(line[1])
  if found == False:
      content += "Sorry, that word doesn't seem to be in our dictionary."
      with open('failed_searches.csv', mode='a') as search_list:
        word_writer = csv.writer(search_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        word_writer.writerow([search])



elif lang == "taagra":
  toggle = " checked"
  with open('tadictionary.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', lineterminator="\n")
    found = False
    for line in csv_reader:
      if line[1] == search or line[1].replace("'","") == search or line[1].replace("'","-") == search:
        found = True
        part_of_speech = line[2].split("/")
        pos = ""
        for item in part_of_speech:
          if item in parts_of_speech:
            pos += parts_of_speech[item] + " "
        content += dict_entry.format(eng=line[0], tag=line[1], part=pos, syn=line[3], note=line[4])

  if found == False:
      content += "Sorry, that word doesn't seem to be in our dictionary."

#print(html.format(toggle, content))
