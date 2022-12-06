#!/usr/bin/python3
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
	comparisons = set((ITEMS[i],ITEMS[j]) 
										for i in range(len(ITEMS)) 
											for j in range(i+1, len(ITEMS) ))

	try:
		with open("comparisons.txt", "w") as comparisons_file:
			for comparison in comparisons:
				comparisons_file.write(f"{comparison[0]},  {comparison[1]}\n")
	except PermissionError:
		print("An error has ocurred while trying to write the file!")
		print("Check your permissions!")
		exit()
	except:
		exit()

	print( f"File has been written and {len(comparisons)} comparisons resulted!")
