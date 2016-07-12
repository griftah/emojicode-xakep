export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

FILENAME="mandel"

rm $FILENAME.py
rm $FILENAME.txt
rm $FILENAME.emo*

python bf-o-compiler.py $FILENAME.b


# ruby xtime.rb python $FILENAME.py
# echo ^^ Python

# ruby xtime.rb python $FILENAME-opt.py
# echo ^^ Optimized Python

echo " "
python emo.py $FILENAME.txt > /dev/null
ruby xtime.rb emojicode $FILENAME.emojib
echo ^^ Emojicode
