# TouchDesigner Summit 2019 | External Python Libraries

## Artist Instructors
Matthew Ragan | [matthewragan.com](https://matthewragan.com)  
Zoe Sandoval | [zoesandoval.com](https://zoesandoval.com)  
Materializing Interactive Research | [mir.works](https://mir.works)

## Dependencies
* [TouchDesigner099](https://www.derivative.ca/099/Downloads/)
* [Python 3.5.1](https://www.python.org/downloads/release/python-351/)

## Recommended Tools
Having an external text editor is key to lots of work in Touch. I like VS Code these days, though Sublime is also a solid choice
* [VS Code](https://code.visualstudio.com/)
* [Sublime Text](https://www.sublimetext.com/)

## Schedule
Time | Topic
---- | ----
2:30 pm | Intro - Why Python External Libraries
3:00 pm | Python in TouchDesigner
3:30 pm | Setting up Python on your Machine
4:00 pm | QR Code Example
5:00 pm | Starting from a Template - Tox Buiding
5:30 pm | Dominant Color
6:00 pm | Wrap

## Overview
Python has more and more reach these days - from web services to internet of things objects, scientific and statistical analysis of data, what you can do with Python is ever expanding. While it's possible to do all of this work from the ground up, it's often easier (and faster) to use libraries that other people have published. TouchDesigner already comes with a few extra libraries included like OpenCV and Numpy. Once you have a handle on working with Python the world feels like it's your oyster... but how you work with a magical little external library in TouchDesigner can be very tricksy. Worse yet, if you happen to get it working on your machine, making work on another can be infuriating. Over the course of this workshop we'll take a look at what you can do to make this process as smooth and painless as possible, as well as some considerations and practices that will help you stay sane when you're trouble shooting this wild Python rollercoaster.

## Intro - Why Python External Libraries
External libraries offer huge benefits as an artist-developer. There's a good chance what you want to explore or do will take more hours than there are in a day, or in a lifetime. Using external libraries opens up your possibilities to include all sorts of exciting and interesting integration. From something as banal as sending email or checking weather, to more interesting mechanisms for communicating with web services or IoT devices. Working with these libraries gives you room to focus more deeply on the work you want to do, rather than the lower level mechanics of getting it working. It also means you can make the best use of the limited time we have for complicated projects. 

## Python in TouchDesigner
Python in TouchDesigner is a wild ride. The deep reaches of the integration give you the freedoms to touch nearly any operator, and while that may well be amazing - it also comes with some cautions and considerations. Python in Touch is deeply connected to how TouchDesigner manages time and state. What this means is that anything you're executing in the main thread will bind touch for as long as it takes for the operation to complete. In many cases this is just fine, changing parameters or logic statements are largely straightforward enough, but we can get into some real trouble with very simple seeming things. Let's see a clear example. In a text DAT try this:
```python
import time
time.sleep(5)
```
What you'll see happen next in Touch is that the time-line will freeze, and you might even get a wonderful little spinning icon. `time.sleep(5)` is a Pythonic way of saying "wait 5 seconds, then move on. What that means in Touch, however, is that we stop everything (even updating our rendering) for that 5 seconds. Because Touch is largely single threaded, this can have major performance implications. The last thing any of us want is for everything to freeze suddenly,  or for frames to drop out of nowhere. ALl of this to say that how we use Python in Touch matters, and when we choose to do something in Touch or Outside of Touch often depends on what we're trying to do, and how it connects to our application as a whole. 

### Inside or Outside of Touch...
"How do I know if I should do something in Touch, or with a separate system call?" 
That's a hard question, and to get to an answer there are a few things we can think about:
* Is this in a project that needs a constantly updating output?  
* Is this operation something that happens only during configuration / offline mode, or during a show?
* What's my tolerance for stutters or dropped frames?
* Do I need feedback that this process has completed?

If you've got an expensive Python operation that you have to run doing a live-set, or during performance critical moments you should definitly look at subprocess call or running those pieces in another touch project. If you can't have dropped frames then it's worth thinking hard about whether you need this feature, or how to make it work in a way that won't interrupt your output. 

If the operation happens during calibration or configuration and happens to be slow, then you might be just fine. Web services can be very tricky here. Depending on your network configuration you can easily end up in a situation where touch is waiting for a reply from a remote server, and that can look like a frozen UI. If that's a dealbreaker, then it's time to look at other options for how to handle the operation in question.

### Other options include...
Okay, so what do we do if we end up with one of these deal breakers? Well, there are a few directions we can go.

#### Threads
You can run an operation in another thread - though for this to work you have to be dealing with pure python. If you're working with operators in anyway in threads, you will definitely crash at some point. There are some ways around this, but it's dangerous waters so save often and know that strange things will happen.

#### Subprocess
You can use use a subprocess call - in other words, write a python script in a text file, and then ask your operating system to run that file. There are great ways to pass in arguments in those situations, and if you really need data there are ways to get a response before the process quits. This can be a very flexible solution for a number of situations, and worth looking into if you want something that's non-blocking and can be run outside of TouchDesigner.

Subprocess calls can be infuriating if you're not familiar with them, so let's look at some simple anatomy of making this work from Touch.

If you want to use TouchDesigner's version of Python you'd write something like this:
```python
import subprocess

cmd_python_script   = '{}\\your_python_file.py'.format(project.folder)

subprocess.Popen(['python', cmd_python_script], shell=False)
```

If you want to use a specific version of Python you'd write something like this:
```python
import subprocess

cmd_python_script   = '{}\\your_python_file.py'.format(project.folder)
python_exe          = 'C:\\Program Files\\Python35\\python.exe' #this might be different for you

subprocess.Popen([python_exe, cmd_python_script], shell=False)
```

If you want to call a script with arguments you'd write something like this:

This is our Script in TouchDesigner
```python
import subprocess

cmd_python_script = '{}\\cmd_line_python_args.py'.format(project.folder)
script_args = ['-i', 'Hello', '-i2', 'TouchDesigner']

command_list = ['python', cmd_python_script] + script_args

subprocess.Popen(command_list, shell=False)
```

This is our python script that's being called:
```python
import time
from argparse import ArgumentParser

# a simple method to print out our arguments
def My_python_method(kwargs):

    disp_str = 'key: {} | value: {} | type: {}'
    for each_key, each_value in kwargs.items():
        formatted_str = disp_str.format(each_key, each_value, type(each_value))
        print(formatted_str)

    # keep the shell open so we can debug
    time.sleep(int(kwargs.get('delay')))

# execution order matters -this puppy has to be at the bottom as our functions are defined above
if __name__ == '__main__':
    parser = ArgumentParser(description='Set up a file watcher to stylize files that are added to the specified folder')
    parser.add_argument("-i", "--input", dest="in", help="an input string", required=True)
    parser.add_argument("-i2", "--input2", dest="in2", help="another input", required=True)    
    parser.add_argument("-d", "--delay", dest="delay", help="how long our terminal stays up", required=False, default=10)
    args = parser.parse_args()
    My_python_method(vars(args))
    # My_python_method(args.input, args.intput2, args.delay)
    pass

# example
# python .\cmd_line_python_args.py -i="a string" -i2="another string" -d=15

```

#### Python Stand alones
You can also always write a little python script that just runs in the background. There are plenty of ways for sending data to and from these kinds of applications, so this is a solid option - but it will require some time devoted to developing your Python-fu.

## Setting up Python on your Machine
Install python 3.5.1

### Windows
Update pip  
`python -m pip install --user --upgrade pip`

### Mac
Make sure you have pip  
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
`python3 get-pip.py`

Update pip  
`python3 -m pip install --user --upgrade pip`

Navigate to the folder in Terminal
Set permissions so the file can be execuatable
`chmod +x myfile.sh`

## Installing an External Library
If you're doing some exploration on your own machine it's often very tempting to use the fast and easy process of installing a library with pip's straightforward installation calls. That often looks something like this as a command line operation:  
`pip install numpy`

Boom! Easy, to the point, and fast. Why bother with anything else?

Well, there is a lot going on here... and what our process will look like will actually look like a command string like this:  
Windows  
`py -3.5 pip install -r path_to_our/requirements.txt --target="path_to_an_target_dir/dep/python"`

Mac  
`python3 pip install -r path_to_our/requirements.txt --target="path_to_an_target_dir/dep/python"`

### That Escalated Quickly
Totes. I know. 

But there's some good reasons for all that extra business in there. First we want to make sure that we're targeting a specific version of Python - the version that matches what TouchDesigner is using. Next we want to use a requirements file that lists all of the libraries we want to use, and finally we want to specify where all of those files are going to live when we pull them from the internet. Making sure we're specific and focused here will help ensure that we can replicate our results across machines, and keep us from midnight trouble shooting a silly library installation that got off the rails. 

#### Wait, who is pip?
`pip` is the Python package manger. This handy tool helps use collect all the files we might need for a particular library, install them, and update if necessary. You could certainly do this manually, but it wouldn't be any fun. `pip` comes along with our installation of Python 3.5+ so we shouldn't have to do much extra work to get this up and running - MacOS users we have a little more work to do, but it's only a few extra lines to get us set-up.

#### Why use a requirements.txt
Taking advantage of some built in features for `pip` (the Python package manager) we can even make parts of our process easy to automate and replicate across projects. When using the `-r` flag that you see in the command string above, we can point to a file that lists all of the packages we want to install. Let's say, for example we're doing some fancy and exciting python business and we need to install both `sklearn` and `scipy`. Rather than running two different installation commands, we can instead put both of these packages on their own lines in a text file (`requirements.txt`), and when we pull our packages, pip will gather all of the pieces we need. This not only helps us stay organized, but it will make this whole process easier for us to manage if we need to move our project from a development machine to production hardware. 

#### Why Use a Target Location
The words I dread more than anything when it comes to try to replicate functionality with an external python library are:  
> "It works on my machine" `‾\_(ツ)_/‾`  

Few comments are infuriating as that one.  

No matter what side of that exchange you happen to be on, it's a bummer. If you're the one saying those magic words, it's hard to understand / know what might be different on another person's hardware. Somehow, you managed to get it working, and trouble shooting what's happening on another machine (that you maybe can't even touch) is rough rough business. At the same time, when someone says those magic words to you... well, you're on your own explorer. It's working somewhere out in the universe, but who knows if you'll ever manage to get it working on your stack of hardware. 

In the pure Python universe, folks use things like virtual environments to help with this problem. A virtual environment gives you a cleanly isolated working space where hopefully you can manage to work in a way that's replicable in production. 

"okay, okay... so can't we just use a venv (virtual environment) then?"  

Not really. Malcom has a great reply on the forum about just that challenge:

>I spent a bit of time looking at this, and the issue is that TD doesn't launch a python.exe, TouchDesigner.exe IS python.exe for all intents and purposes. So the venv tools that Python provides don't really help us with this. You'd need a different TD installation for each of your venvs.

>The other issue is that we have some custom changes we do to pythons main .dll to improve speed, so using a different python35.dll that comes from elsewhere won't work with TD.

>All we can really do is provide better tools to manage module search paths, but the actual python compiled code (python35.dll etc.) needs to stay the same in all cases.

[Read the whole thread here](https://www.derivative.ca/Forum/viewtopic.php?f=17&t=12009&p=46692&hilit=virtual+environments#p46692)

So part of what we're after here is a mechanism to better segment our external Python libraries so they're not tangled in our own Python installation (which is usually impossible to reliabaly replicate), and bonus points if we can adapt easily from project to project.

"Okay, easy. Let's just install any externals into the TouchDesigner Python site-packages directory, easy - I even know where it is" `C:\Program Files\Derivative\TouchDesigner099\bin\Lib\site-packages`

That seems like a great idea initially, until you update Touch, and nerf your site-packages. Or have multiple versions of touch installed (experimental and stable), or you're trying to trouble shoot installations that are all on different versions of touch. Take it from someone who has played this game, and gotten burned left and right - seems like a great idea, but this one will bite you for sure. So, what can we do?

That's where using a target installation directory starts to shine. In this case we can set up an external directory alongside our project, and we can keep a tidy record of all the external Python pieces we need here. 

## QR Code Example

## Starting from a Template - Tox Buiding
[Template TOX for Component Dev](https://github.com/raganmd/touchdesigner-template-tox-dev)

## Dominant Color

## Wrap

## Additional Resources
It's always helpful to have additional Resources and learning materials, but where to look. Here's a few places to browse for topics about leanring python in and out of TouchDesigner.

### Learning Python
* [Python in TouchDesigner](https://matthewragan.com/teaching-resources/touchdesigner/python-in-touchdesigner/)  
* [LearnPython.org](https://www.learnpython.org/)  
* [Solo Learn](https://www.sololearn.com/Course/Python/)  
* [Python On Udemy](https://www.udemy.com/pythonforbeginnersintro/?ranMID=39197&ranEAID=JVFxdTr9V80&ranSiteID=JVFxdTr9V80-CZK8xxa.umgByhTZ4voR0g&LSNPUBID=JVFxdTr9V80)  
* [Learn Python the Hard Way](https://www.amazon.com/Learn-Python-Hard-Way-Introduction-ebook/dp/B00FGUS948)  

### Libraries to explore
* [Phue - A library for controlling Phillips Hue Lights](https://github.com/studioimaginaire/phue)
* [Unofficial Instagram API - Python](https://github.com/LevPasha/Instagram-API-python)
* [sklearn - data analysis in Python](https://scikit-learn.org/stable/)
* [spotipy - control spotify with Python](https://github.com/plamere/spotipy)
* [SoCo - control sonos speakers with Python](https://github.com/SoCo/SoCo)
* [Awesome-Python - a list of all sorts of libraries worth exploring](https://github.com/vinta/awesome-python)
