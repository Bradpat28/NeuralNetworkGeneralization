clean:
	rm -r Train/Damaged
	rm -r Validation/Damaged

clean-runs:
	rm -r NNRuns/

visual:
	python src/visualization.py

install_ubuntu:
	sudo apt install python-pip
	sudo pip install --upgrade pip
	sudo pip install pillow
	sudo pip install numpy scipy
	sudo pip install numpy --upgrade
	sudo apt-get install python-skimage
	sudo pip install tensorflow==1.1.0
	sudo pip install keras==2.0.2
