## Voice-assistant-research

This project is about the research of voice assistant.

Two platforms are mainly analyzed, Amazon skills and Google actions. 

Here are dataset of privacy policy and description as well as our analysis result


## Dataset

Totally, we collected 19141 Amazon skills from 21 categories and 2201 Google actions from 18 categories. 

Among them, 6439 skills and 1967 actions provide a privacy policy link. 

The privacy policy and description can be found in folder dataset.

The totally skill number in each category is:

![Skill number of Alexa](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/skill_number.png)

The number of privacy policy is:


![Number of privacy policy](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/goodpolicy.png)

The number of duplicated privacy policy is:

![Number of duplicated privacy policy](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/samepolicy.png)


## Data collection

Here is how Amazon define the personal data and permission:

![Permission](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/permerssion.png)

## Data practice
Here are some privacy policy with low or zero data practice:

![Types of good privacy policy page](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/example2.png)

![Types of good privacy policy page](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/example3.png)

![Types of good privacy policy page](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/example4.png)

![Types of good privacy policy page](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/example5.jpg)

![Types of good privacy policy page](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/example6.jpg)

![Types of good privacy policy page](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/example7.png)

![Types of good privacy policy page](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/example8.png)

## Result


Here are some result about problematic skills:

(1) Some skills have imcomplate policy:

![Types of inomplete skills](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/incomplete.png)

And here is an example of them. It asks for device location but not mentions in privacy policy.

![Example of incomplete skill](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/example1.png)

And is the skill link and some other example skills:
[Record-Journal - Things to Do Calendar](https://www.amazon.com/Record-Journal-Things-to-Do-Calendar/dp/B07NC478M9/ref=sr_1_1?keywords=record+journal&qid=1582232641&s=digital-skills&sr=1-1)

[FortiRecorder](https://www.amazon.com/Fortinet-FortiRecorder/dp/B079P35CGQ/ref=sr_1_1?keywords=fortirecorder&qid=1582232693&s=digital-skills&sr=1-1)

[Running Outfit Advisor](https://www.amazon.com/CraftyC-Running-Outfit-Advisor/dp/B0735XW8LM/ref=sr_1_1?crid=24ZNWXDR4FZKZ&keywords=running+outfit+advisor&qid=1582232728&s=digital-skills&sprefix=Running+outfit+%2Calexa-skills%2C143&sr=1-1)



(2) Some skills should provide a privacy policy but not:

![Types of no_policy skills](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/example10.jpg)

And here is an example:

![Example of no_policy skill](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image/example9.png)

Here is skill link and andother example skills:

[Heritage Flag Color](https://www.amazon.com/Thomas-Anderson-Heritage-Flag-Color/dp/B01MR9JBWU/ref=sr_1_1?keywords=heritage+flag+color&qid=1582233183&s=digital-skills&sr=1-1)

[Name My Grandkids](https://www.amazon.com/Cooper-Name-My-Grandkids/dp/B01EW3KUXC/ref=sr_1_1?keywords=name+my+grandkids&qid=1582233215&s=digital-skills&sr=1-1)
