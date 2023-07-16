## Directions  
### For the Model Generator
- Create a virtual environment with the dependencies installed
- Download the repository (unzip if you downloaded the zipped file)
- navigate to model_generator/machine_learning_model/machine_learning_model.py
- open in zsh/bash and run ```python3 machine_learning_model.py```
- this should generate a box in /model_generator/generated_boxes/ titled "generated_box.off"
- this box can be viewed on websites like https://3dviewer.net/
- in model_generator/Datasets/AustensBoxes/ you can find the training and testing datasets. These are filled with boxes, generated from a simpler, box generating algorithm.

### For the Omniverse Plugin
- Sign up to Nvidia's Omniverse programs https://www.nvidia.com/en-us/omniverse/download/
- install Omniverse Code through the Omniverse Launcher
- (In Omniverse Code) click on the extensions tab
- Click on the THIRD PARTY tab
- Find MAKE A RANDOM CUBE by me (Austen Cabret) and toggle the grey switch that activates the plugin.
- a moveable window should pop up that has two buttons.
- click the add button to add random cubes and the delete button the remove them.

## Dependencies
- Python3
- Pytorch
- Numpy

## Features To Come  
* More supported file types (.obj, .usd, .fbx)
* Faster generation speeds
* Plugin to Omniverse UI
* Generate more than just boxes
* Text as input
* Neural network improvements
* Easier execution



<p align="center">
  <img width="750" src="https://github.com/Generlate/model_generator/assets/85384584/93659fd6-ed44-44f0-b9bb-8124e0fe1966">
</p>  