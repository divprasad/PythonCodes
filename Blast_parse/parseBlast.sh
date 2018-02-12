!/bin/bash
date
file=outB_26200428_405

# awk '{print $1}' $file.tsv | sort | uniq > V_${file}_uniq.tsv
# awk '{print $2}' $file.tsv | sort | uniq > B_${file}_uniq.tsv
python transform.py $file
# date
python create_DB.py $file
# python find_lenND.py $file
python fill_DB_2.py $file
date
python create_BigT.py $file
date

#
#file=outB_27654921_405
# #
# # awk '{print $1}' $file.tsv | sort | uniq > V_${file}_uniq.tsv
# # awk '{print $2}' $file.tsv | sort | uniq > B_${file}_uniq.tsv
# # python transform.py $file
#  date
# # python create_DB.py $file
# # python find_lenND.py $file
#python fill_DB_2.py $file
#date
#python create_BigT.py $file
#date
