# Python Challenge Implementation: Fulfillment for GSOC 2025 Mentorship Application

## How to run the code
> **To run code on GNU Linux / Unix**
```shell
 ./matplotlib.sh
```

> **To run code on Windows**
```shell
 .\matplotlib_for_windows.ps1
```
<a id="how-to-make-it-more-fun"></a>
## How to make it more fun
> To make the code a bit interactive I added the possibility to pass arguments
> that will make the code run in different 
> * arena size, 
> * steps per frame and 
> * interval
> 
> For example :
```shell
 ./matplotlib.sh --arena-size 15.0 --steps-per-frame 3 --interval 30
```
```shell
.\matplotlib_for_windows.ps1 --arena-size 15.0 --steps-per-frame 3 --interval 30
```

## Program Explanation
The code has been implemented as a module as instructed to.

### File structure 
```shell
├── app
│   ├── brownian_motion.py
│   ├── implementation_with_matplotlib.py
│   ├── __init__.py
│   └── __pycache__
├── main.py
├── matplotlib.sh
```

### File functions
* [matplotlib.sh](./matplotlib.sh) : This is the shell file that helps run the code in a GNU Linux/ Unix environment
* [main.py](./main.py) : The main.py is the entry point of the program, it also receives argument
while running the program from [matplotlib.sh](./matplotlib.sh)  for add on configurations, see [How to make it more fun](#how-to-make-it-more-fun).
* app: This is the directory that house the brownian motion implementation(module), and it's use in matplotlib(module).
* [app/brownian_motion.py](./app/brownian_motion.py) : This is the module with brownian motion implementation
* [implementation_with_matplotlib.py](app/implementation_with_matplotlib.py) : This is the module that utilise the [app/brownian_motion.py](./app/brownian_motion.py) module 
to create a brownian motion movement/behaviour for a robot like dot in a square 2d container.


### Logic

#### **brownian_motion()**

>simulates a robot that:
* Starts in the center of a square arena 
* Moves in straight lines 
* Changes direction only when it hits a wall 
* Returns initialization and update functions for animation

#### **brownian_motion_matplotlib()** 
* Creates an animated visualization of the modified 
Brownian motion algorithm defined in the previous code. <br>
* It shows a robot (blue circle) moving around a square arena with 
its direction (red arrow) and path history.