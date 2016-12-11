
all: build test

# into package folder
build: *.pyx
	python setup.py build_ext --inplace
test:

	#python -c "from hello import *;say_tree();say_hello_c('smile')"
	python test.py
	# python planarLinkage.py
