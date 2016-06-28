

for d in *; do
    if [ -d "$d" ]; then
         cd "$d"
         echo "Test $d:"
         sh test_me.sh
         cd ..
    fi
done


