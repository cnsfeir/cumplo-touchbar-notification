<div align="center">
  <img src="https://user-images.githubusercontent.com/58790635/175819449-e2442b67-d759-4959-916e-33390fd2f5e1.png" width="650"/>
</div>

<p align="center">
    <em>
      A <b>smart</b> touch-bar notification badge for "promising" Cumplo investment opportunities.
    </em>
</p>
<br>

____

## Context

[**Cumplo**](https://www.cumplo.com/) is a **chilean crowdlending company** and [certified B Corp](https://www.bcorporation.net/en-us/find-a-b-corp/company/cumplo-chile-sa), operating in Mexico, Peru and Chile, which **connects loan applicant companies with a network of investors through its online platform**. Cumplo's aim is to deliver a transparent and excellence service with **fair rate**. Its network consists of about 50,000 registered users on the website, 3,000 investors and 1,000 SMEs.

## The Problem

**⌛ Good investment opportunities are financed in a matter of minutes by big bidders.** <br>
**🚨 No real-time notification system for new investment opportunities.**

## Solution

I started using [BetterTouchTool](https://folivora.ai/) (BTT) for customizing my touch-bar and make it somehow useful. Then I found [GoldenChaos](https://goldenchaos.net/goldenchaos-btt.html) (a general purpose touch-bar UI build on top of BTT) and **it was a game changer.** One of its cool features, are notification badges for different apps. Diving into BTT configuration, I found out that creating your own badge wasn't that hard. **You can connect them to an apple script or shell script that's going to be executed periodically, updating its value**.

<div align="center">
  <img src="https://user-images.githubusercontent.com/58790635/175826321-acb8b6ca-4b01-4765-8682-b6c0bf74856b.png"/>
</div>

Once you can execute code, the sky is the limit. So I built **a scraper that searches Cumplo website for "promising" investment opportunities (based on your preferences) and displays in the badge how many did it find**. Also, you can press the badge and it'll open Cumplo's webpage so you can invest as soon as you see the notification.
 
 <div align="center">
  <img src="https://user-images.githubusercontent.com/58790635/175827375-eda33994-7489-41bc-8fc1-eab01ebcdd30.png" width="400"/>
</div>



