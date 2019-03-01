# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 23:56:52 2019

@author: skavy
"""

import re
import statistics
import os
paragraph = "C:\\Users\\skavy\\Desktop\\Bootcamp\\Python-Challenge\\PyParagraph\\paragraph.txt"

num_lines = 0
num_words = 0
num_chars = 0
sentence_count=0

word_count=[]

with open(paragraph, 'r' ,encoding = "UTF-8") as file:
    for para in file:
        #remove " from paragraph
        para1 = re.sub('\"', '', para)
        #get individual sentences split by full stop
        sentences = re.split('(?<=[.!?]) +',para1)
        for sentence in sentences:
            #get words by splitting white spaces
            words=re.split('\s+',sentence)
            #number of words in current sentence
            print("-----words length------")
            print(len(words))
            num_words+=len(words)
            print("-----sentence------")
            print(sentence)
            print("-----words in setence------")
            print(words)
            #for each word get number of letters
            for word in words:
                letter_count=len(word)
                word_count.append(letter_count)
            # increase sentence count by 1for each sentence  
            sentence_count +=1
            

sentence_count -= 1
avg_letter_count = statistics.mean(word_count)
avg_sen_length = int(num_words) / sentence_count
print("Paragraph Analysis")
print("--------------------------------------")
print(f"Approximate Word Count: {num_words}")
print(f"Approximate Sentence Count: {sentence_count}")
print(f"Average Letter Count: {avg_letter_count}")
print(f"Average Sentence Length: {avg_sen_length}")

output_file = os.path.join("para_output.txt")
# Writes output to text file
w = open('para_output.txt','w')
w.write("Paragraph Analysis")
w.write("\n--------------------------------------")
w.write(f"\nApproximate Word Count: {num_words}")
w.write(f"\nApproximate Sentence Count: {sentence_count}")
w.write(f"\nAverage Letter Count: {avg_letter_count}")
w.write(f"\nAverage Sentence Length: {avg_sen_length}")

w.close()

