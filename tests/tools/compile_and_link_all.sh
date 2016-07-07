#options:
# 1. parameter - target name 
# 2. parameter - file extension to compile, defaults to "s"
# 3. parameter - source dir, defaults to "."
# 4. parameter - object dir, defaults to "."

TARGET=$1
EXT=${2:-"s"}
SOURCE_DIR=${3:-"."}
OBJECT_DIR=${4:-"."}

SOURCES=$(ls $SOURCE_DIR/*.$EXT)
for source in $SOURCES 
do
    base=$(basename $source ".$EXT")
    as $source -o $OBJECT_DIR/$base.o
done

OBJECTS=$(ls $OBJECT_DIR/*.o)

ld $OBJECTS -o $TARGET
