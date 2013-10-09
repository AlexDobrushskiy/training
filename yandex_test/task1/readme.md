This module eliminates begining and ending empty strings, and compresses internal sequences of empty string to one empty string.

Usage:
root@alex-VirtualBox:/home/alex/TESTS/training/yandex_test/task1# cat input.dat | python raws.py > ouput.dat

Running tests:
root@alex-VirtualBox:/home/alex/TESTS/training/yandex_test/task1# python tests.py -v
test_generator_input (__main__.Task1Test) ... ok
test_long_list_input (__main__.Task1Test) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.022s

OK

Example of usage:
root@alex-VirtualBox:/home/alex/TESTS/training/yandex_test/task1# cat input.dat | python raws.py > ouput.dat
root@alex-VirtualBox:/home/alex/TESTS/training/yandex_test/task1# cat ouput.dat
a

d

v

asd
aa
qqq

wwww

sdf
root@alex-VirtualBox:/home/alex/TESTS/training/yandex_test/task1# cat input.dat



#lots of empty strings here
a

d

v

#lots of empty strings here
asd
aa
qqq


#lots of empty strings here
wwww

sdf


#<lots of empty strings here>



root@alex-VirtualBox:/home/alex/TESTS/training/yandex_test/task1#
