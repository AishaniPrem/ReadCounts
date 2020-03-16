#!usr/bin/python3.6
__author__= 'Aishani Prem'
__email__='aishaniprem@gmail.com'
import argparse
import os
import gzip
import re
import glob
import subprocess
import pandas as pd

#---Command Line Arguments----
parser=argparse.ArgumentParser(
      description="This script uses python3. The purpose of this script is to read a sequencing folder (MiSeq and MiniSeq only) and output the read count for the samples in that folder.")

parser.add_argument('-f','--folder', help='Input the path to the sequencing folder',required=True)

args = parser.parse_args()

folder = args.folder

#----Get the type of Sequencer from the name of the folder----
SeqType = folder.split('/')[-1:][0].split('_')[1][:2]

#-----Check if the sequencer is MiSeq or MiniSeq. -----
# For MiSeq
if SeqType.lower() == "m0":
	FastqFiles = glob.glob("%s/Data/Intensities/BaseCalls/*fastq.gz" %folder)
	df = []
	for file in FastqFiles:
		count = os.popen("zcat %s | wc -l" %file).read()
		print(count)		 
		#rows = [file.split('/')[4].split('_')[0],file.split('/')[4].split('_')[3], count.strip('\n')]
		rows = [file.split('/')[4].split('_')[0], file.split('/')[4].split('_')[0][-4:], int(count.strip('\n'))/2]
		df.append(rows)
	#df = pd.DataFrame(df, columns = ["FileName", "Read", "ReadCount"])
	df = pd.DataFrame(df, columns = ["SampleName","SeqType", "ReadCount"])
	df = df.drop_duplicates(subset = ["SampleName","ReadCount"], keep =  "first")
	print(df)
	df.to_csv("%s_Summary.csv"%folder ,index=False)	
	#print(FastqFiles)
	#print("Miseq")
#For MiniSeq
elif SeqType.lower() == "mn":
	FastqFiles = glob.glob("%s/Alignment_1/20*/Fastq/*fastq.gz" %folder)
	df = []
	for file in FastqFiles:
		count = os.popen("zcat %s | wc -l" %file).read()
		#print(count)
		#rows = [file.split('/')[4].split('_')[0],file.split('/')[4].split('_')[3], count.strip('\n')]
		rows = [file.split('/')[4].split('_')[0], int(count.strip('\n'))/2]
		df.append(rows)
	#df = pd.DataFrame(df, columns = ["FileName", "Read", "ReadCount"])
	df = pd.DataFrame(df, columns = ["SampleName","ReadCount"])
	df = df.drop_duplicates(subset = ["SampleName","ReadCount"], keep =  "first")
	print(df)
	df.to_csv("%s_Summary.csv"%folder ,index=False)
	#print(FastqFiles)
	#print("Miseq")
	#print("Miniseq")
else:
	print ("This program is only compatable for sequencing runs from MiSeq or MiniSeq")


