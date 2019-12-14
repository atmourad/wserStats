# wserStats
_DISCLAIMER: I am not a data scientist of any kind. I am not advocating for anything one way or another. I am just a programmer who loves ultrarunning who was fortunate enough to get his kids to bed early so he could play around with this data. Please feel free to copy and modify the script as you wish and please do reach out if you see any glaring errors._

After listening to the epsiode of KoopCast (https://twitter.com/jasonkoop/status/1205550084970045440) where they discussed the WSER lottery, one thing that stood out to me was the point about the gender disparity. I was curious what the numbers looked like. Luckily the folks over at WSER provide all sorts of neat data on their website.

I pulled the lottery numbers for 2013-2020 from the various https://www.wser.org/lottery20XX.html pages.
I pulled the runners numbers for 2013-2020 from the various https://www.wser.org/20XX-entrants-list/ pages.

## Findings
The ratio of men to women stands at approximately 80/20 across the board pretty consistenly (plus or minus a few points). There are a few data points I looked for:
* number of people that enter the lottery broken down by M/F.
* the number of tickets in the lottery broken down by M/F.
* the number of runners in the race broken down by M/F.
  * one thing to note about this stat is that it includes ALL runners represented in the race, not just those chosen by lottery. I figured that this was ok since the argument presented in the podcast was that the breakdown of runners at the start line may be a deterrent for people choosing to run the race.

One interesting thing is that while the total number of people entering the lottery has approximately tripled from 2295 to 6664, the ratio has remained the same, suggesting that the interest in the race is rising at the same rate among both genders.

I did a quick search of ultrarunning finishes by gender and found this study on ultrarunning.com: https://ultrarunning.com/featured/ultrarunning-finishes-by-gender/

The 100 miler finishes by gender for the data provided that overlaps with the below data is as follows:
* 2013 **78.95/21.05**
* 2014 **77.38/22.62**
* 2015 **75.99/24.01**
* 2016 **78.54/21.46**

Interestingly enough, we see this approximate 80/20 split consistently here as well (closer to 76/24 probably), which suggests that WSER is pretty representative of 100milers (unless more recent data varies dramatically). When you factor in other ultras (50k, 50mi, 100k) the ratios start drifting more toward **67/33** (again with data through 2016). This may or may not be a valid comparison, depending on what you are looking to compare to.

Lastly, with regards to WSER the ratio of the runners remains approximately the same as the ratio of the lottery, which is precisely what we would expect from a random lottery.

### 2013 LOTTERY
* RUNNERS (M/F): 1876/419 **(81.7%/18.3%)** TOTAL: 2295
* TICKETS (M/F): 2954/601 **(83.1%/16.9%)** TOTAL: 3555

### 2013 RUNNERS
* RUNNERS (M/F): 325/83 **(79.7%/20.3%)** TOTAL: 408

### 2014 LOTTERY
* RUNNERS (M/F): 2189/515 **(81.0%/19.0%)** TOTAL: 2704
* TICKETS (M/F): 3548/759 **(82.4%/17.6%)** TOTAL: 4307

### 2014 RUNNERS
* RUNNERS (M/F): 316/83 **(79.2%/20.8%)** TOTAL: 399

### 2015 LOTTERY
* RUNNERS (M/F): 2072/494 **(80.7%/19.3%)** TOTAL: 2566
* TICKETS (M/F): 5547/1054 **(84.0%/16.0%)** TOTAL: 6601

### 2015 RUNNERS
* RUNNERS (M/F): 305/83 **(78.6%/21.4%)** TOTAL: 388

### 2016 LOTTERY
* RUNNERS (M/F): 2806/704 **(79.9%/20.1%)** TOTAL: 3510
* TICKETS (M/F): 6847/1444 **(82.6%/17.4%)** TOTAL: 8291

### 2016 RUNNERS
* RUNNERS (M/F): 291/90 **(76.4%/23.6%)** TOTAL: 381

### 2017 LOTTERY
* RUNNERS (M/F): 3429/819 **(80.7%/19.3%)** TOTAL: 4248
* TICKETS (M/F): 9106/1915 **(82.6%/17.4%)** TOTAL: 11021

### 2017 RUNNERS
* RUNNERS (M/F): 284/85 **(77.0%/23.0%)** TOTAL: 369

### 2018 LOTTERY
* RUNNERS (M/F): 3942/967 **(80.3%/19.7%)** TOTAL: 4909
* TICKETS (M/F): 12442/2632 **(82.5%/17.5%)** TOTAL: 15074

### 2018 RUNNERS
* RUNNERS (M/F): 292/77 **(79.1%/20.9%)** TOTAL: 369

### 2019 LOTTERY
* RUNNERS (M/F): 4689/1173 **(80.0%/20.0%)** TOTAL: 5862
* TICKETS (M/F): 16680/3439 **(82.9%/17.1%)** TOTAL: 20119

### 2019 RUNNERS
* RUNNERS (M/F): 282/87 **(76.4%/23.6%)** TOTAL: 369

### 2020 LOTTERY
* RUNNERS (M/F): 5288/1376 **(79.4%/20.6%)** TOTAL: 6664
* TICKETS (M/F): 23098/4774 **(82.9%/17.1%)** TOTAL: 27872

### 2020 RUNNERS (data not yet complete)
* RUNNERS (M/F): 275/63 **(81.4%/18.6%)** TOTAL: 338

Raw script output:
```
data/2013_entrants.csv: RUNNERS (M/F): 1876/419 (81.7%/18.3%) TOTAL: 2295 
data/2013_entrants.csv: TICKETS (M/F): 2954/601 (83.1%/16.9%) TOTAL: 3555 
data/2013_runners.csv: RUNNERS (M/F): 325/83 (79.7%/20.3%) TOTAL: 408 
data/2014_entrants.csv: RUNNERS (M/F): 2189/515 (81.0%/19.0%) TOTAL: 2704 
data/2014_entrants.csv: TICKETS (M/F): 3548/759 (82.4%/17.6%) TOTAL: 4307 
data/2014_runners.csv: RUNNERS (M/F): 316/83 (79.2%/20.8%) TOTAL: 399 
data/2015_entrants.csv: RUNNERS (M/F): 2072/494 (80.7%/19.3%) TOTAL: 2566 
data/2015_entrants.csv: TICKETS (M/F): 5547/1054 (84.0%/16.0%) TOTAL: 6601 
data/2015_runners.csv: RUNNERS (M/F): 305/83 (78.6%/21.4%) TOTAL: 388 
data/2016_entrants.csv: RUNNERS (M/F): 2806/704 (79.9%/20.1%) TOTAL: 3510 
data/2016_entrants.csv: TICKETS (M/F): 6847/1444 (82.6%/17.4%) TOTAL: 8291 
data/2016_runners.csv: RUNNERS (M/F): 291/90 (76.4%/23.6%) TOTAL: 381 
data/2017_entrants.csv: RUNNERS (M/F): 3429/819 (80.7%/19.3%) TOTAL: 4248 
data/2017_entrants.csv: TICKETS (M/F): 9106/1915 (82.6%/17.4%) TOTAL: 11021 
data/2017_runners.csv: RUNNERS (M/F): 284/85 (77.0%/23.0%) TOTAL: 369 
data/2018_entrants.csv: RUNNERS (M/F): 3942/967 (80.3%/19.7%) TOTAL: 4909 
data/2018_entrants.csv: TICKETS (M/F): 12442/2632 (82.5%/17.5%) TOTAL: 15074 
data/2018_runners.csv: RUNNERS (M/F): 292/77 (79.1%/20.9%) TOTAL: 369 
data/2019_entrants.csv: RUNNERS (M/F): 4689/1173 (80.0%/20.0%) TOTAL: 5862 
data/2019_entrants.csv: TICKETS (M/F): 16680/3439 (82.9%/17.1%) TOTAL: 20119 
data/2019_runners.csv: RUNNERS (M/F): 282/87 (76.4%/23.6%) TOTAL: 369 
data/2020_entrants.csv: RUNNERS (M/F): 5288/1376 (79.4%/20.6%) TOTAL: 6664 
data/2020_entrants.csv: TICKETS (M/F): 23098/4774 (82.9%/17.1%) TOTAL: 27872 
data/2020_runners.csv: RUNNERS (M/F): 275/63 (81.4%/18.6%) TOTAL: 338 
```
