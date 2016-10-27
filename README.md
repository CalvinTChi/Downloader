# Downloader

Have you ever had to download a list of files from a webpage? A situation similar to this:

<br>
<img height = "280" width = "300" src = "https://github.com/CalvinTChi/Downloader/blob/master/pic1.png" />
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
address=<address>
file_name=<filename>
file_numbers=<numbers>
file_extension=<extension>
```
The `input.txt` in this repository is an example input file for how to download the [lecture notes](http://people.eecs.berkeley.edu/~jordan/prelims/) from Michael I. Jordan on graphical models. Notice that only chapters 2-7, 10-13, 15, and 17 are present. The most succinct way to specify these numbers is:

`file_numbers=2-7,10-13,15,17`

With no space between commas. The rest of the inputs are relatively straightforward. Hopefully this simple script can make the task of downloading multiple files from a site much more efficient!
