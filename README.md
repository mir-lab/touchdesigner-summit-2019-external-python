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

## Before the Workshop
Before we meet there are a few things to make sure you’ve got in place. Here’s a quick run down of the pieces to make sure are in order before the workshop.

**Required**
* Make sure you’ve updated to the most recent stable build of TouchDesigner 099
* Download and install python 3.5.1. There's a link above to make sure you have the right version of Python. This version matches the same version Touch uses and will make sure we don't have any major hiccups while we're working together.
* Download the github repo linked above. We’ll be working with some files that are already set-up so we don’t have to make everything from scratch so it will be important to have these elements in place.
* Make sure you have your laptop charger packed in your bag :)

**Suggested**
* Download and install a text editor - you don’t need this, but it will make a world of difference when working with lots of Python. Our recommendation is to install VS Code as it has a built in terminal. 
* Reflect on the projects you’ve worked on in the past, and bring some questions about the problems you’ve encountered.
* Think about the wobbles you've had when working with Python, and bring some questions for the group to discuss.
* Don’t forget your three button mouse ;)


## Schedule
Time | Topic
---- | ----
2:30 pm | Intro - Why Python External Libraries
3:00 pm | Python in TouchDesigner
3:30 pm | Setting up Python on your Machine
4:00 pm | QR Code Example
5:00 pm | Starting from a Template - Tox Building
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

If you want to learn more [check out Working with Subprocess](https://github.com/raganmd/blog-td-subprocess)

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
There are lots of different kinds of mischief we might get into when working with an external library, and in this workshop we'll first look at how we might do something that's otherwise pretty fussy - creating a [QR code](https://en.wikipedia.org/wiki/QR_code). Quick Response codes have been around for ages. These 2D barcodes are used all over the place these days, from fast reference links to product numbers, to tickets. They can often be handy for generating unique identifiers at installations or events, and if you've done any work in Asia they're often the cornerstone of working with platforms like WeChat. There are lots of ways to make them online, but what if we want to generate them on the fly ourselves? 

Lucky for us there's a python library for this called `qrcode`. We also happen to want / need a library called `Pillow` - which is a friendly Python Imaging Library. The pip command to get both of these is `qrcode[pil]`. During the workshop we'll use this library as our first foray into working with external libraries, keeping our work organized, and working around the fact that we don't have a virtual environment. 

## Dominant Color
So we've managed to get an external library working, but what's an example of something a little more exciting and complicated that we might pick apart? For a project I worked on recently we wanted to pull the dominant color from a source image. That's actually a much more complicated ask than you might initially imagine, and to really get there you really have to dig-in and think deeply about what you're up to. Let's look at an example that required multiple external libraries, and some careful / thoughtful planning to make sure everything worked without a hitch. If you want to see the reference repo you can find it here on the web - [TouchDesigner Dominant Color](https://github.com/raganmd/touchdesigner-dominant-color).

## Starting from a Template - TOX Building
Making deployable and reusable TOXes is it's own adventure, but espeically challenging when it comes to working with non-standard python libraries. If we have time we'll take a look at the process Matthew's started using for making this process as painless as possible. This includes some helper scripts that automatically create all the required directories for your external python bits, and launch terminal windows to do the installation work. An example approach is included in this repo, but if you'd like to learn more, or fork this process for yourself, checkout - [Template TOE for Component Dev](https://github.com/raganmd/touchdesigner-template-tox-dev)

## Wrap
By the end of our workshop you should have walked through the process of integrating an external python library into a TouchDesigner project, and have some ideas about how to make sure this is portable. The hardest part of working with non-standard python libraries is that it's often easy to get working on one machine, but a real hassle to get working out in production. With any luck you should be prepared to tackle this process yourself, and have some ideas about what else you might do with Python in your projects of all sizes.

Happy Programming!

## Additional Resources
It's always helpful to have additional Resources and learning materials, but where to look. Here's a few places to browse for topics about learning python in and out of TouchDesigner.

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
