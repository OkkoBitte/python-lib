# NEW WRITE FILE 3.0 [MBG]

import os
import shutil
import json
class nwf:
	def new_file(name,w):
		with open(name,"w") as f:
			f.write(w)
	def new_dir(name):
		os.mkdir(name)
	def at_file(name,w):
		with open(name,"a+") as f:
			f.write(w)
	def read_file(name):
		with open(name,"r") as f:
			ret = f.read()
			return ret
	def del_file_all(name):
		shutil.rmtree(name)
	def del_file(name):
		os.remove(name)
	def is_file(name):
		return os.path.isfile(name)
	def is_dir(name):
		return os.path.isdir(name)
	def js_input(name,w):
		with open(name,"w")as f:
			json.dump(w,f, indent=4)
	def js_output(name):
		with open(name,"r")as f:
			return json.load(f)
