#!/bin/bash
x=80
if [ $x -ge 90 -a $x -le 100 ]
then
y=优秀
echo $y
elif [ $x -lt 90 -a $x -ge 80 ]
then
y=良好
echo $y
elif [ $x -lt 80 -a $x -ge 70 ]
then
y=中等
echo $y
elif [ $x -lt 70 -a $x -ge 60 ]
then
y=及格
echo $y
else
y=不及格
echo $y
fi
