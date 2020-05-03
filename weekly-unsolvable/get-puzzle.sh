output_file=sudokuwiki-weekly-unsolvable.txt
rm $output_file
for i in {1..398}
do
    echo $i out of 398
    curl https://www.sudokuwiki.org/feed/scanraid/ASSudokuWeekly.asp?wp=$i | sed -n 23p | cut -c216-296 >> $output_file
done
