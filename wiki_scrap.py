import wikipedia
import os
import datetime

# Creer un repertoire ou le batch sera sauvegarde
now = datetime.datetime.now()
batch_dir = "./output_dir/batch_cooked_at_" + str(now.year) + "_" + str(now.month) + "_" + str(now.day) + "_" + str(now.hour) + "_" + str(now.minute) + "_" + str(now.second)
os.mkdir(batch_dir, 0755);

# Creer un fichier txt avec un nom "unique"
pseudo_rand_id = str(now.microsecond) + str(now.second) + str(now.hour)
output_file = open(batch_dir + "/" + pseudo_rand_id + ".txt", "w")

wikipedia.set_lang("fr")
while(True):
    # Trouve un nom d'article random
    random_page_title = wikipedia.random(pages=1)
    try:
        # Extrait le resume de l'article et l'ecrit dans le fichier de sortie
        random_page = wikipedia.page(random_page_title)
        output_file.write(random_page.content.encode('utf-8') + "\n")
    except Exception as e:
        print "Unexpected error"

output_file.close()
