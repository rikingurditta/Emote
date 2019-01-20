# Emote
A user-friendly tool to support the emotional development of youth with autism. Made at UofTHacks VI by Nive, Rikin, Sarina, Shannon.

## Inspiration

Making friends and maintaining relationships can be hard. This challenge is further complicated if you are a youth living with autism. Autism spectrum disorder (ASD) is characterized by difficulties with social skills, speech, and nonverbal communication. People with autism often struggle to identify emotion and react appropriately. Such struggles can make it difficult to form friends, even though, like all youth, youth with autism yearn for connection. The obstacle these youth face in identifying emotion was our inspiration for this project. By facilitating emotive identification through technology, we hope to be able to support the widespread emotional development and well-being of youth with autism.

## What it does

On regular intervals, Emote will capture an image of your screen and send it to the Microsoft Azure Cognitive Face API to analyze the expressions on any face present. The top three closest matches in emotion will be displayed on a screen, with the size of the emotion name corresponding to the likelihood of the match.

## How we built it

We used mss, a screenshot library, to grab an image of the user’s screen on regular intervals, we implemented the Azure Cognitive Services Face API (with the Python module cognitive_face) to get emotion data from what's on the user's screen, and we used Tkinter to create a custom accessible GUI for our application.

## Challenges we ran into

Our biggest challenge was a result of using tkinter to format our screens. Specifically, we had difficulties making our string variable update labels without reconstructing the screen. The solution was simple: we realized the variable needed to explicitly be defined globally.

## Accomplishments that we're proud of

Our biggest accomplishment was thinking of an ambitious product and developing it in 36 hours! Many of our team members had never created a product geared to a specific audience, so having to worry about the user interface and accessibility was new to us. Additionally, since our product is directed toward an audience with a disability that none of our group members have, we made sure to do thorough research in order to avoid misguided design errors. Overall, we are proud of the product that we developed and cannot wait to share it with youth with autism.

## What we learned

During project development, we had the opportunity to apply many theoretical skills that we learned in class to create a real project. We implemented an API, learned how to use the Python library Tkinter to create engaging graphics, and picked up tips and tricks from our team members. Moreover, we learned the importance of clear communication in group projects as well as how to plan and develop a presentable project under strict time constraints.

## What's next for Emote

Our next plan for Emote is to add a feature that uses the text-to-speech and natural language processing APIs to support sentiment analysis. It will assist autistic youth to interpret emotions from text messages, emails, and more.
