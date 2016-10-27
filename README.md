# Downloader

Have you ever had to download a list of files from a webpage? A situation similar to this:

<br>
<img height = "300" width = "550" src = "https://github.com/CalvinTChi/Downloader/blob/master/pic1.pngg" />
<br>

Manually downloading each file is time-consuming and inefficient, and `Downloader` is a simple python script that allows you to automate this process. As an overview, `Downloader` requires as input:

1. Web address where files are located
2. Name of file
3. File numbers 
4. File extension
5. Directory to download files to

To clarify points 2, 3, and 4, if the files you want to download are `chapter1.pdf`, `chapter2.pdf`, and `chapter3.pdf`, then name of the file would be `chapter`, file numbers would be `1-3`, and file extension would be `pdf`. Let us delve into the precise usage.

# Usage
A typical usage of `Downloader` looks like this:

`python fileDownloader.py -i <filename> -o <output-directory>`

Where `-o` specifies the output directory to download the files to and `-i` specifies the input file name. The input filename will specify the 1) address, 2) filename 3) file numbers, and 4) file extension in the following format:

```
sdalfsjdlkfasdjf
```
