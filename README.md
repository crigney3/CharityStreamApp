# CSH Minecraft Charity Stream Store

[minecraftstream.csh.rit.edu](minecraftstream.csh.rit.edu) is the official website for the annual Computer Science House Minecraft Charity Tournament. 

## The Event

CSH's Annual Charity Minecraft Tournament is a competition between any number of players who sign up to fight through a series of Minecraft minigames. The players represent organizations from all over the Rochester Institute of Technology's campus, such as CSH, Engineering House, House of General Sciences, and, as thanks for their contributions on this project, employees of Blackbaud.
***
#### First Annual Tournament (April 12th, 2019)

Our first tournament was hosted on April 12th of 2019, and was broadcast on the [official JustGiving Twitch channel](https://www.twitch.tv/justgiving). With 18 players entering the initial round, our competitors fought through:
* Hunger Games
* The Walls
* Bed Wars
* Race for the Wool
* Spleef
In the end, we had a triumphant winner and had raised $300 for the Mental Health Association of Rochester!
---
#### Second Annual Tournament (TBD, 2020)

Our second tournament is being planned, and will have new and improved features to update the flow of gameplay and make the best viewing/playing experience.

## The Website

#### The Purpose

[minecraftstream.csh.rit.edu](This website) was developed to add a unique twist to this tournament. I wanted to create something so that donations would automatically change the course of the game. I came up with the idea of having donations grant items to players in the tournament. I was able to create this through this site, and our first tournament resulted in some amazing swings caused by donations. 

#### How it works

The app uses Flask and Jinja to generate a website that acts as a store. Once a user has gotten the items they want, they select a player, and then go through the regular, secure process of donating through JustGiving. Then, an app I worked with JustGiving to create checks to see if the user had any items attached to their donation. If they do, and the amount is compatible with the items, it sends a series of commands to listeners I had on my minecraft server, which in turn run the commands.

##### Notes on the JustGiving App
The app I've mentioned in JustGiving's system is owned and created by JustGiving and the code is not FOSS. I helped by guiding functionality and consulting. This app still exists in their system, but you must have certain internal permissions to use/view it, as it is considered in Beta.
