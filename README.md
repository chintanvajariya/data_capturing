# Double Screen Grabber

## Purpose
In this day and age, any data-collecting hardware will come with packaged software assistance, without which the hardware is moot. Unfortunately, one of these products, the specifics of which I won't mention, allows for the collection of data but requests thousands of dollars to pay for its recording. In other words, if we want to analyze the 2e- ARPES' pressure values, we must waste precious grant money. Without going into too much detail, I brought up the idea of scraping the screen on which the app displays this pressure information, and that's how this program was born.

## How do we use it?
Because both of the time of flight chambers have different pressures, we needed to be able to collect both readings at the same time; hence the *double* screen grabber. As outlined in the following video, you just select the parts of the screen that must be read and the program does the rest. This gets us approximately 1.5 FPS per selection, which is more than enough for our long data collection periods (getting the perfect Cooper pair to emit is harder than you might think). Both sections of the screen get their own .csv file, which can be easily analyzed and visualized.

## Double Screen Grabber Demo
<img width="500" alt="Double Screen Grabber Demo" src="https://github.com/chintanvajariya/double_grabber/assets/49341214/016870be-9e63-4371-b729-512a133b3a0f">

I decided to collect time zone values as opposed to our data presented by the collecting app, as I don't plan to show the software I have thus far slandered.
