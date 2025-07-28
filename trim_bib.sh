sed -i 's/file =.*//g' pirovc.bib
sed -i 's/keywords =.*//g' pirovc.bib
sed -i 's/urldate =.*//g' pirovc.bib
#awk '{if ($0 ~ /date =/) {print "\tyear = {"substr($0,10,4) "},"}else{print}}' pirovc.bib > tmp && mv tmp pirovc.bib
