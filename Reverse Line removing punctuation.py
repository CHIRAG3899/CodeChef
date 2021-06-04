#In this problem the input will consist of a number of lines of English
#text consisting of the letters of the English alphabet, the punctuation
#marks ' (apostrophe), . (full stop), , (comma), ; (semicolon), :(colon)
#and white space characters (blank, newline). Your task is print the words
#in the text in reverse order without any punctuation marks.
#For example consider the following candidate for the input text:

#  This is a sample piece of text to illustrate this 
#  problem.  If you are smart you will solve this right.
#The corresponding output would read as:
#  right this solve will you smart are you If problem
#  this illustrate to text of piece sample a is This
#That is, the lines are printed in reverse order and in each line the words
#are printed in reverse order.

#Input:
#The first line of input contains a single integer N, indicating the number
#of lines in the input. This is followed by N lines of input text.

#Output:
#N lines of output text containing the input lines in reverse order and where
#each line contains the words in reverse order as illustrated above.


n=int(input())
l=[]
for i in range(n):
    s=input()
    l.insert(0,list(s))
for i in l:
    str1=""
    str2=""
    for j in i:
        if j in ["'",".",",",";",":"]:
            continue
        else:
            if j==" ":
                str1=str2+j+str1
                str2=""
            else:
                str2=str2+j
    print(str1)
