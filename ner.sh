echo "########extract features for train...########"
./feature.py < train > train.f
echo "########extract features for dev ...########"
./feature.py < dev > dev.f
echo "########extract features for test...########"
./feature.py < test> test.f
echo "########learning...########"
crfsuite learn -a ap -p max_iterations=120 -m ner.model train.f
echo "########add tags...########"
crfsuite tag -m ner.model < dev.f > dev.tagged
crfsuite tag -m ner.model < test.f > test.tagged
echo "########predicting test...########"
crfsuite tag -r -m ner.model < test.f > test.eval
echo "########predicting dev...########"
crfsuite tag -r -m ner.model < dev.f > dev.eval
echo "########performance:########"
echo "======test:======="
conlleval.py < test.eval
echo "======dev:======="
conlleval.py < dev.eval
