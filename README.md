--------------
Dependecies:
--------------
- Keras - 2.0.2
- Tensorflow = 1.1.0
- Python - 2.7
- Pillow
- Numpy
- Python SkImage

- UI - MacOS Xcode vers 9.2

--------------
Installation Steps:
--------------
Ubuntu - 16.04
```   
make install_ubuntu
```
--------------
Steps to Run Main:
--------------
All of the functionality is found in the "Scripts" folder which can be found
in the NNRunViewer/NNRunViewer/Scripts folder

Make sure that the "data" folder is in the specified working Directory.

To find your working directory, type:
```
pwd
```
while in the folder that you have everything in

main.py requires 6 arguments to run
   1. Working Directory
   2. Number of Epochs
   3. Steps per Epoch
   4. Validation Steps
   5. Validation Percent (100% = 1)
   6. Batch Size

You can replace any/all of the following arguments with -1 to default to the following values:
   2. Number of Epochs = 5
   3. Steps per Epoch = 25
   4. Validation Steps = 25
   5. Validation Percent = .2 (20%)
   6. Batch Size = 35


To run main.py from the working directory /home/example/NeuralNetwork-master
```
python /NNRunViewer/NNRunViewer/Scripts/main.py /home/example/NeuralNetwork-master -1 -1 -1 -1 -1
```

This will create a Neural Network in the workingDirectory/NNRuns/ folder.
The name of the network will be the date and time that is was created.
   Ex: NNRuns/18-05-07-13-34  

--------------
Steps to Run Classification:
--------------
All of the functionality is found in the "Scripts" folder which can be found
in the NNRunViewer/NNRunViewer/Scripts folder

Make sure that the "classify" folder is in the specified working Directory.
Make sure that there are no other folders in the classify folder, just images

To find your working directory, type:
```
pwd
```
while in the folder that you have everything in

classification.py requires 2 arguments to run
   1. Working Directory
   2. Name of the Network to use

to run classification from the working directory /home/example/NeuralNetwork-master on network 18-05-07-13-34
```
python /NNRunViewer/NNRunViewer/Scripts/classification.py /home/example/NeuralNetwork-master 18-05-07-13-34
```
This will create folders and organize them within the "classify" folder


--------------
Steps to Run Visualization:
--------------
All of the functionality is found in the "Scripts" folder which can be found
in the NNRunViewer/NNRunViewer/Scripts folder

To find your working directory, type:
```
pwd
```
while in the folder that you have everything in

visualization.py requires 1 argument to run
   1. Working Directory

to run visualization from the working directory /home/example/NeuralNetwork-master
```
python /NNRunViewer/NNRunViewer/Scripts/visualization.py /home/example/NeuralNetwork-master
```
This will visualize all of the statistics for the networks created in the workindDirectory/NNRuns folder


--------------
Contents:
--------------
Files:
- main.py //Runs all the necessary setup scripts and starts the NN
- setup.py //Holds all of the setup function high level calls
- setupDirectory.py //Sets up the directory structure to support the NN
- setupRecords.py //Currently not being used. Could be used if TFRecord support is added
- run.py //Creates and runs the NN'
- data.py //Works with storing the information about the run.
- visualization.py //Controls the visualization of the NN post run
- parserHelper.py //Controls the helper functions for the parser
- NNRunClass.py //Contains the class definition for an NN run
- classification.py //Controls the classification of the images in a folder

Folders:
- data_test //Used to display the functionality on a super small dataset

Function Hierarchy:
main()
   setupNN()
      setup_dir()
   runNN()


Error Format:
   Error:'[Error Name]':[Description]

Errors:
- 'Data Directory Not Found':Could not find directory named 'data'


Notes:
   1. GUI only works on MacOS using Xcode
   2. The Neural Network used for classification is arbitrary, and can be replaced with a more specific network in run.py
      This project focused on adding accessibility to creating and using networks, not focusing on a unique network design.
   3. Validation Accuracies and Test Accuracies may or may not accurately reflect the accuracy of the network in practice.
      The more data that is used the more accurate these accuracy values will be.
