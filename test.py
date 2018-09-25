import wikipedia
import os

wikipedia.set_lang("fr")
output_path =  './output_dir'
already_scraped_pages = []

# Charge les fichiers qui ont deja ete enregistre dans une liste
for filename in os.listdir(output_path):
    already_scraped_pages.append(filename)


while(True):
    # Trouve un article random
    random_page_title = wikipedia.random(pages=1)
    # Si l'article n'a pas deja ete enregistre
    if(random_page_title + ".txt" not in already_scraped_pages):
        try:
            # On sauvegarde un fichier txt, son nom est le nom de l'article + ".txt"
            random_page = wikipedia.page(random_page_title)
            output_file = open("./output_dir/" + random_page_title + ".txt", "w")
            output_file.write(random_page.summary)
            already_scraped_pages.append(random_page_title + ".txt")
            output_file.close()
        except Exception as e:
            print "Unexpected error"
