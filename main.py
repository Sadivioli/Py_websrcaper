from src.justjoinit import *
from src.bulldog import *
from src.nofluff import *
from util.sender import *

#Dla justjoinit:
    #atrybuty możliwe do podania są w pliku readme w sekcji Atrybuty -> justjoinit
    #jeśli chcemy szukać bez miasta lub technologii, podać "all", w przypadku roli akceptujemy też pusty
jj_city = "krakow"
jj_technology = "javascript"
jj_role = "junior"
#podanie 1 wyszuka tylko oferty z widełkami, 0 wyszuka oferty z i bez widełek
jj_salary = 0
# plik do zapisu
jj_file_name = "justjoinit.txt"
jj_offers = unique(search_justjoinit(jj_city, jj_technology, jj_role, jj_salary, keywords))

#Dla bulldogjobs:

bd_city = "Kraków"
bd_technology = "JavaScript"
bd_role = "junior"
#podanie true wyszuka tylko oferty z widełkami, każda inna wartość wyszuka oferty zarówno z i bez widełek
bd_salary="true"
# plik do zapisu
bd_file_name = "bulldog.txt"
bd_offers = search_bulldog(concat(bd_city), concat(bd_technology), concat(bd_role), concat(bd_salary))


#Dla nofluffjobs:

nf_city = "warszawa"
nf_technology = "JavaScript"
nf_role = "junior"
# plik do zapisu
nf_file_name = "nofluff.txt"
nf_offers = search_nofluff(nf_city,nf_technology, nf_role)


save_to_file(nf_offers, nf_file_name)
save_to_file(jj_offers, jj_file_name)
save_to_file(bd_offers, bd_file_name)

output_file = "offers.txt"

concatenate_and_save_files(nf_file_name, jj_file_name, bd_file_name, output_file)

#usuwanie plików tymczasowych
delete_files(nf_file_name, jj_file_name, bd_file_name)

# #wysyłanie maila

# #adres na który ma zostać wysłany email. można użyć np. maila z https://temp-mail.org/
# to = 'ninakeb672@dekaps.com'
# subject = 'Mamy dla Ciebie nowe oferty pracy!'
# file_path = 'offers.txt'
# send_file_contents_if_long(file_path, to, subject, 7)