python3 -B alexarank.py


mdfile="2019-01-06-Alexa-Internet-Traffic-Rankings-of-Indian-Institutes.markdown"

cat post_template.markdown > $mdfile
cat ranks.yml >> $mdfile


echo "\n\n##### Last Updated: `date`" >> $mdfile


cp $mdfile ../pythonV/JAMPY/_posts/
