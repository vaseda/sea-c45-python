# Name: ...
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0

for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
g_count = 0
c_count = 0
a_count = 0
t_count = 0
count_unexpected = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    #total_count = total_count + 1

    if bp == 'C':
        c_count = c_count + 1
        total_count = total_count + 1
        continue

    if bp == 'G':
        g_count = g_count + 1
        total_count = total_count + 1
        continue

    if bp == 'A':
        a_count = a_count + 1
        total_count = total_count + 1
        continue

    if bp == 'T':
        t_count = t_count + 1
        total_count = total_count + 1
        continue

        print("Unexpected char count: ", bp)

atgc_count = (g_count + c_count)/(a_count + c_count + g_count + t_count)

gc_count = g_count + c_count
# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count

at_count = a_count + t_count
# divide the at_count by the total_count
at_content = float(at_count) / total_count

# Print the answer
print('GC-content:', gc_content)
print('AT-content:', at_content)
print('A-number:', a_count)
print('T-number:', t_count)
print('G-number:', g_count)
print('C-number:', c_count)
print('total-number:', total_count)
print("AT/GC ratio:", atgc_count)

# Categorize microorganisms:
if gc_content >= 0.6:
    content = "high GC content"
else:
    if gc_content <= 0.4:
        content = "low GC content"
    else:
        content = "moderate GC content"
print("GC Classification:", content)
