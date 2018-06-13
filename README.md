# Communication-for-the-deaf
This local application converts sign language to text. Its purpose is to help the deaf communicate with people who don't understand sign language.
## Getting started
Clone the repository. I have uploaded the trained graph from TensorFlow which can be used for sign language classification. Another option would be to use a Python script to train the neural network on your own hyper-parameters.
## Prerequisites
The program runs using Python3. It can be downloaded at https://www.python.org/
* TensorFlow ( a symbolic math library 
* OpenCV (image processing module)
* NumPy (support for large multi-dimensional arrays and matrices)
* Matplotlib (Plotting library and numerical mathematics extension  of NumPy)

## Installation
You can download the wheel files for the prerequisite Python3 modules at https://www.lfd.uci.edu/~gohlke/pythonlibs/. 

To install run -

`pip install WheelFileName.whl`

Alternative - 

    pip install tensorflow
    pip install opencv-python
    pip install numpy
    pip install matplotlib

To train the neural network, run the following Python script on the terminal with the following hyper-parameters.

    python3 train.py \
    --bottleneck_dir=logs/bottlenecks \
    --how_many_training_steps=2000 \
    --model_dir=inception \
    --summaries_dir=logs/training_summaries/basic \
    --output_graph=logs/trained_graph.pb \
    --output_labels=logs/trained_labels.txt \
    --image_dir=./dataset
  
## Running the algorithm
You can run the following program both at the terminal and with the the Python3 IDE. Use the following command on the terminal.
`Python classify_webcam.py`
## How it works
