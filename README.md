# DotMatrix_LED_RPi_Stand

This repo was thrown together, as was the code. The stand was a gift I made for someone and I wasn't planning on uploading which is why its not really a well documented project.

The stand uses an Embedded Adventures 80x8 Dotmatrix LED screen which is found here: http://www.embeddedadventures.com/LED_matrix_display_LDP-8008.html
It runs off of the RPi power but its not recommended. Its much brighter if you give it a bettetr source of 5V and is probably stressing my Pi as we speak. I used resources from all over, this is a good one to get the screen working with the Pi: http://kimondo.co.uk/raspberry-pi-led-scrolling-sign/

There is a DXF file located in the stand folder, which you can take to your local laser cutter place, or online to get the pieces needed to put it together. 

Required libraries: urllib2, json, and the included fontv and ldp(for the LED display).

There are three demos, two which were not modified by me, the third being the upvote program, was just cobbled together with random snippets of code and is in no way effecient or well though out(think two minutes of play out of my day).

static_demo.py and scroll_demo.py both operate in the same way using "python2 ######_demo.py "Your Text" 1" - Using either 1 or 2 will determine what colour the LEDs will be lit up, Red or Green. Only one colour for the whole screen at a time. 

upvote_scroll_demo.py is a program that will notify you when a Reddit thread has been upvoted. Its not "live" per-say, as it only checks every ten seconds whether there are more upvotes than last time. It will display the total number of upvotes until it checks for more then will display "UpVote!" 3 times. To use this program simply "python2 upvote_scroll_demo.py "http://www.reddit.com/r/YOURSUBREDDIT/YOUR-CHOSEN-REDDIT-THREAD-HERE/" make sure to use http and not https. Also since its using urllib2 you may receive a "Too many requests" error, I have not taken the time to debug, sometimes you just have to run it a couple times then it starts. 

Enjoy! Probably missing lots of stuff here, but its a cool screen that you can do lots of stuff with. I also have a twitter that displays when people tweet certain words. I will work on submitting that here as well.
