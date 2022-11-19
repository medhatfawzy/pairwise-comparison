ITEMS = [
"Alignment to Vision and Design",
"Delivery of the Project",
"Integration",
"Cost",
"PROCUREMENT",
"Quality",
"Team",
"Working Hours",
"Location",
"Availability"
]


if __name__ == "__main__":
	comaprisons = set((ITEMS[i],ITEMS[j]) 
			for i in range(len(ITEMS)) 
				for j in range(i+1, len(ITEMS) ))

	try:
		with open("comaprisons.txt", "w") as comparisons_file:
			for comaprison in comaprisons:
				comparisons_file.write(f"{comaprison[0]},  {comaprison[1]}\n")
	except:
		print("An error has ocurred while trying to write the file!")
		print("Check your permissions!")
		exit()

	print( f"File has been written and {len(comaprisons)} comparisons resulted!")
