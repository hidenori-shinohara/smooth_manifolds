for i in 1 2 3 4
do
   echo "Chapter $i"
   echo "  Exercises"
   tr ' ' '\n' < chapter$i.tex | grep "begin{customexer}" | wc -l
   echo "  Problems"
   tr ' ' '\n' < chapter$i.tex | grep "begin{customprob}" | wc -l
   echo ""
done
