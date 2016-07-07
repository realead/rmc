
#parse options:

PROG=$1
ARGS=$2
EXPECTED=$3
NAME=$4

rec=$(./$PROG $ARGS)
if [ "$rec" != "$EXPECTED" ]; then  
   echo "TC $NAME, output is wrong: received [$rec] vs. expected [$EXPECTED]"
   exit 1
fi

