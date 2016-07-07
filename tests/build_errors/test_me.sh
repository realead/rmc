############# SET UP ################################################
#load functions:

. $TOOLS/utils.sh

############### COMPILE ##############################################

only_compile "unknown_instruction" "unknown instruction STRE"



########### CLEAN UP #################################################

rm *.s

############ REPORT ################################################## 
report

exit $failed_cnt


