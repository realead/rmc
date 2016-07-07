

for d in *; do
    if [ -d "$d" ] && [ $d != "tools" ]; then
         cd "$d"
         echo "Test $d:"
         sh test_me.sh
         cd ..
    fi
done


