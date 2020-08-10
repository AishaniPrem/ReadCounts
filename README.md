# ReadCounts
The purpose of this script is to output the read count for the each samples in a sequencing run

## To run the code 
1. Git clone this repository.
```
git clone https://github.com/AishaniPrem/ReadCounts.git
```

2. Create docker image 

```
sudo docker build -t readcounts-image readcounts-image/
```
3. Run the script

```
sudo docker run -v `pwd`:`pwd` -w `pwd` -it readcounts-image python3  ReadCounts.py -f #SequencingFolderName
```
