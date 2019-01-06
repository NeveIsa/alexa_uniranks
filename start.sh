python3 -B alexarank.py


mdfile="2019-01-06-Alexa-Indian-University-Rankings.markdown"

cat post_template.markdown > $mdfile
cat ranks.yml >> $mdfile

cp $mdfile ../pythonV/JAMPY/_posts/

echo "\n\n ###### Last Updated: `date`" >> $mdfile
