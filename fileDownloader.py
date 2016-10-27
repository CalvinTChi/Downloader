import urllib.request, getopt, sys

def main(argv):
	inputFile = ""
	outputDir = ""
	filename = ""
	location = ""
	numbers = ""
	extension = ""
	try:
		# i.e. "i:" means that argument for i is required
		opts, args = getopt.getopt(argv, "i:o:")
	except getopt.GetoptError:
		print("Usage: fileDownloader.py -i <input-file> -o <output-directory>")
		# Exit status of 2 means command line synax error
		sys.exit(2)
	# opt = input identifier, arg = actual input
	for opt, arg in opts:
		if opt == "-i":
			inputFile = arg
		elif opt == "-o":
			outputDir = arg
	filecontent = [row.strip() for row in open(inputFile)]
	for line in filecontent:
		items = line.split("=")
		try: 
			item1 = items[0]
			item2 = items[1]
			item3 = items[1][0]
		except IndexError:
			print("Input file should have format:\naddress=<address>\nfile_name=<filename>\nfile_numbers=<filenumbers>\nfile_extension=<extension>")
			sys.exit(1)
		if items[0] == "file_name":
			filename = items[1]
		elif items[0] == "address":
			location = items[1]
		elif items[0] == "file_numbers":
			if "," in items[1]:
				numbers = list(items[1].split(","))
			else:
				numbers = [items[1]]
			numbers = numbers_parser(numbers)
		elif items[0] == "file_extension":
			extension = items[1]
		else:
			print("Make sure field names are 'address', 'file_name', 'file_numbers', 'file_extension'")
			sys.exit(1)
	for i in numbers:
		address = location + filename + str(i) + "." + extension
		try:
			response = urllib.request.urlopen(address)
		except:
			print("Invalid address")
			continue
		try:
			f = open(outputDir + filename + str(i) + "." + extension, "wb")
			f.write(response.read())
			f.close()
		except: 
			print("Output directory does not exist")
			sys.exit(1)

def numbers_parser(numbers):
	nums = []
	for num in numbers:
		if "-" in num:
			sf = list(map(int, num.split("-")))
			seq = list(range(sf[0], sf[1]+1))
			nums.extend(seq)
		else:
			nums.append(int(num))
	return nums

if __name__ == "__main__":
	try:
		arg1 = sys.argv[1]
	except IndexError:
		print("Usage: fileDownloader.py -i <input-file> -o <output-directory>")
		sys.exit(2)
	main(sys.argv[1:])
