#!/usr/bin/env python
from subprocess import call, check_output
import fnmatch
import os
import sys

clang_format = "clang-format"

def format_dir(folder, extensions):
	"""
		Format directories and all subfolders using clang-format
	"""
	matches = []
	for root, dirnames, filenames in os.walk(folder):
		for ext in extensions:
			for filename in fnmatch.filter(filenames, '*'+ext):
				matches.append(os.path.join(root, filename))

	for filename in matches:
		call([clang_format, "-i", filename])

def detect_clang(max_version = 10, version = 5):
	"""
		Attempt to detect clang by calling "clang-format-3.x" with x an
		increasing version number.
	"""

	if version == max_version + 1:
		print("[ERROR]: You must have clang-format installed to run this script")
		return ""
	else:
		try:
			clang_name = "clang-format-3."+str(version)
			check_output([clang_name, "-help"])
			print("[INFO]: Found "+clang_name)
			return clang_name
		except:
			return detect_clang(max_version, version+1)

# possible extensions
exts = ['.h', '.c', '.hpp', '.cpp', '.hh', '.cc']

if __name__ == "__main__":
	if len(sys.argv) <= 1:
		print "Usage: clean_code.py folder1 [folder2] ..."
		sys.exit()

	# Try to find a version of clang on the system, being either clang-format or
	# of the form clang-format-3.x where x is in [[5, 10]]
	try:
		check_output(["clang-format", "-help"])
		clang_format = "clang-format"
	except:
		clang_format = detect_clang()
		if len(clang_format) == 0:
			sys.exit()

	# config file
	curr_dir = os.getcwd()

	# change if needed to find the config file
	if curr_dir[len(curr_dir)-5:] == 'limbo':
		os.chdir('tools')
		# copy config file
		call(["cp", ".clang-format", curr_dir])
		# change back to old dir
		os.chdir(curr_dir)

	# format directories specified by the user
	for arg in sys.argv[1:]:
		format_dir(arg, exts)

	# remove copied file if needed
	if curr_dir[len(curr_dir)-5:] == 'limbo':
		call(["rm", ".clang-format"])
