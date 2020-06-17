# Measuring the Effectiveness of Privacy Policies for Voice Assistant Applications

## Introduction

In this work, we mainly investigate the following three research questions (RQs):

* RQ1: What is the overall quality of privacy policies provided by voice-app developers in different VA platforms? Do they provide informative and meaningful privacy policies as required by VA platforms?

* RQ2: For a seemingly well-written privacy policy that contains vital information regarding the service provided to users, can we trust it or not? Can we detect inconsistent privacy policies of voice-apps?

* RQ3: What are VA users’ perspectives on privacy policies of voice-apps? What is possibly a better usability choice for VA users to make informed privacy decisions?


We conduct the first empirical analysis to measure the effectiveness of privacy policies provided by voice-app developers on both Amazon Alexa and Google Assistant platforms.The major contributions and findings are:

* We analyze 64,720 Amazon Alexa skills and 2,201 Google Assistant actions. 

* For the 17,952 skills and 1,967 actions that have a privacy policy, we find there are many voice-apps in app stores with incorrect privacy policy URLs or broken links. Google and Amazon even have official voice-apps violating their own requirements regarding the privacy policy.

* We analyze the privacy policy content to identify potential inconsistencies between policies and voice-apps. We find there are privacy policies that are inconsistent with the corresponding skill descriptions. We also find skills which are supposed to have a privacy policy but do not provide one.

* We conduct a user study with 91 participants to understand users’ perspectives on VA’s privacy policies and discuss solutions to improve the usability of privacy notices to VA users.

We have reported our findings to both Amazon Alexa and Google Assistant teams, and Federal Trade Commission (FTC) researchers. We had an online meeting with Amazon security team discussing the problems we discovered in May 2020. We have also received acknowledgments from Google Trust & Safety team in June 2020. We are working with the vendors to provide users with effective privacy notices.



## Dataset

We collected 64,720 unique Amazon skills from 21 categories and 2,201 Google actions from 18 categories. 

Among them, 17,952 skills and 1,967 actions provide a privacy policy link. 

The privacy policy and description can be found in folder dataset.

The totally skill number in each category is:

![Skill number of Alexa](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image2/numbers.png)



## Major findings

### short privacy policies

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

Here is the skill link and some other example skills:

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
