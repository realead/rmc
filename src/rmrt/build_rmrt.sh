#options
#1. option -> object file directory

GOALDIR=$1

#I'm in the rmrt directory
RMRT_PATH=$(dirname $0)

RMRT_SOURCES=$(ls $RMRT_PATH/*.s)

for source in $RMRT_SOURCES
do
  base=$(basename $source ".s")
  as -I$RMRT_PATH $source -o $GOALDIR/$base.o
done


