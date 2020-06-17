# Measuring the Effectiveness of Privacy Policies for Voice Assistant Applications

## Introduction

We conduct the first empirical analysis to measure the effectiveness of privacy policies provided by voice-app developers on both Amazon Alexa and Google Assistant platforms. The major contributions and findings are:

* We analyze 64,720 Amazon Alexa skills and 2,201 Google Assistant actions about privacy policy. 

* For the 17,952 skills and 1,967 actions that have a privacy policy, we find there are many voice-apps in app stores with incorrect privacy policy URLs or broken links. Google and Amazon even have official voice-apps violating their own requirements regarding the privacy policy.

* We analyze the privacy policy content to identify potential inconsistencies between policies and voice-apps. We find there are privacy policies that are inconsistent with the corresponding skill descriptions. We also find skills which are supposed to have a privacy policy but do not provide one.

* We conduct a user study with 91 participants to understand users’ perspectives on VA’s privacy policies and discuss solutions to improve the usability of privacy notices to VA users.

We have reported our findings to both Amazon Alexa and Google Assistant teams, and Federal Trade Commission (FTC) researchers.



## Dataset

We collected 64,720 unique Amazon skills from 21 categories and 2,201 Google actions from 18 categories. 

Among them, 17,952 skills and 1,967 actions provide a privacy policy link. 

The privacy policy and description can be found in folder dataset.

![Skill and actions in categories](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image2/numbers.png)



## Major findings

### Short privacy policies:

There are many very short privacy policies which are not informative.

![Short privacy policy](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image2/short_policy.png)

### Broken links and incorrect URLs:

Not all voice-apps have a privacy policy URL. For those voice-apps that have provided a privacy policy URL, not every URL leads to the page containing a privacy policy.

![Broken_link](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image2/broken_link.png)

![Incorrect_link](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image2/promotionpage.png)

### Duplicate URLs:

A substantial portion of privacy policies share same URLs. For the top 5 developers who published the most skills with a privacy policy, 99.8% of their skills use duplicate URLs.

![Duplicate_link](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image2/duplicate.png)

### Official voice-apps:

There are Google and Amazon’s official voice-apps violating their own requirements.

![Official_apps](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image2/official.png)

### Privacy with zero data practice:

![zero_data_pracatice](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image2/zero_data_practice.png)

### Inconsistency between privacy policy and description:

Some voice-apps describe data collection in the description but not mentione in privacy policy.

![Incomplete_privacy_policy](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image2/incomplete.png)


Here are some example skills link:

[Record-Journal - Things to Do Calendar](https://www.amazon.com/Record-Journal-Things-to-Do-Calendar/dp/B07NC478M9/ref=sr_1_1?keywords=record+journal&qid=1582232641&s=digital-skills&sr=1-1)

[FortiRecorder](https://www.amazon.com/Fortinet-FortiRecorder/dp/B079P35CGQ/ref=sr_1_1?keywords=fortirecorder&qid=1582232693&s=digital-skills&sr=1-1)

[Running Outfit Advisor](https://www.amazon.com/CraftyC-Running-Outfit-Advisor/dp/B0735XW8LM/ref=sr_1_1?crid=24ZNWXDR4FZKZ&keywords=running+outfit+advisor&qid=1582232728&s=digital-skills&sprefix=Running+outfit+%2Calexa-skills%2C143&sr=1-1)

### Lacking privacy policy:

![Lacking_privacy_policy](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image2/lack_policy.png)

Here are some example skills link:

[Heritage Flag Color](https://www.amazon.com/Thomas-Anderson-Heritage-Flag-Color/dp/B01MR9JBWU/ref=sr_1_1?keywords=heritage+flag+color&qid=1582233183&s=digital-skills&sr=1-1)

[Name My Grandkids](https://www.amazon.com/Cooper-Name-My-Grandkids/dp/B01EW3KUXC/ref=sr_1_1?keywords=name+my+grandkids&qid=1582233215&s=digital-skills&sr=1-1)

### User study:

![User_study](https://github.com/voice-assistant-research/voice-assistant/blob/master/dataset/image2/user_study.png)



