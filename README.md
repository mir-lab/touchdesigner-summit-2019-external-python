# TouchDesigner Summit 2019 | External Python Modules

## Artist Instructors
Matthew Ragan | [matthewragan.com](https://matthewragan.com)  
Zoe Sandoval | [zoesandoval.com](https://zoesandoval.com)  
Materializing Interactive Research | [mir.works](https://mir.works)

## Dependencies
* [TouchDesigner099](https://www.derivative.ca/099/Downloads/)
* [Python 3.5.1](https://www.python.org/downloads/release/python-351/)

## Schedule
Time | Topic
---- | ----
2:30 pm | Intro - Why Python External Libraries
3:00 pm | Python in TouchDesigner
3:30 pm | Setting up Python on your Machine
4:00 pm | Instagram Example
5:00 pm | Packaging your Python
5:30 pm | Starting Points - an example for Tox Buiding
6:00 pm | Wrap

## Overview


## Intro - Why Python External Libraries


## Python in TouchDesigner


### Inside or Outside of Touch...


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

In in the pure Python universe, folks use things like virtual environments to help with this problem. A virtual environment gives you a cleanly isolated working space where hopefully you can manage to work in a way that's replicable in production. 

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

## Instagram Example


## Packaging your Python


## Starting Points - Example Reusable Approach
[Template TOX for Component Dev](https://github.com/raganmd/touchdesigner-template-tox-dev)

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