print("Starting script...")

tab = 0
ignore = 0

with open('out.txt', 'w') as f1:
    for line in open('FILE.txt'):
	if '}' in line:
		tab-=1	
	if '/*' in line:
		ignore+=1
		continue
	if '*/' in line: 
		ignore-=1 
		continue
	if tab==3 and ignore==0: f1.write(line)
	if 'in\n' in line: f1.write('in:')
	if 'out\n' in line: f1.write('out:')
	if '{' in line:
		tab+=1
	if 'package' in line: f1.write(line)
	if 'method' in line: 
		f1.write('\n------------------------------------------------------------------------\n')
		f1.write(line)
	if 'broadcast' in line: 
		f1.write('\n------------------------------------------------------------------------\n')
		f1.write(line)


print(tab)
print(ignore)
print("Finished writing data")
print("DONE")