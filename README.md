# The code for thewallsof.com


This was a small website built for me and some friends in 2019. The purpose was to create a small website where anyone can post their frustrations, joys, wisdom, and maybe secrets. Anyone can scroll through, share laughs, and maybe learn something interesting! 

The website implements responsive design and is optimized for all screen sizes and is anonymous. Anyone can post, upvote, or downvote on any page.

Although it is a very small website that mostly keeps only public data and no sensitive data, I did try to utilize some good security measures at the time and to have a safe experience, and a prevent anything malicious that could possibly arise while in production. As Einstein said, "Smart people fix problems, geniuses prevent them." I generally take security very seriously with all applications I build, and this is no exception. A small security flaw can be costly and be a headache for some time.

The wall of spam is the first page that appears because soon after launching I found that there were many posts being uploaded that were spam and bad marketers trying to spread awareness about their products by posting on the first page of my website. I decided to keep them all in one neat place and give them their own dedicated wall where they could spam as much as they wanted! Some marketers were posting inappropriate comments that were not as tasteful, so I decided to put a filter for the most common words and discard those posts.

The code does repeat in some places, which if I have any time, I will try to make cleaner and more efficient! There are also smaller parts like database that could be written better with the use of UUID instead of how it is currently written. Also, I put static files inside of templates folder, which I no longer do, and always put it in the base directory and collect static in a parent folder or in another s3 bucket if needed. In this project I updated the server manually through ssh but going forward I am looking to use GitHub actions or Jenkins for continuous deployment.

Some of the files include regular Django files, python, Django template HTML, JavaScript, CSS, images, gifs, audio, Adobe Illustrated files, SVG files, mockups, and a photoshop file that I was working on. In hindsight I should have probably used SASS/SCSS to keep the CSS cleaner and more organized, and compile, minify, and uglify with something like gulp, grunt, or webpack, and if I ever have free time, I will go through it and improve it.

Some time ago I dockerized the whole application so it could work platform independently and easier to deploy. I used a postgres database inside of a container on the same server as the application code to reduce server cost and keep everything simpler. Better practice typically is to set up postgres on its own server with an environment variable for all the secrets and firewall that only accepts the server ip for better security.

Recently docker has not been working on my computer and I have not tested docker recently, but I believe from the last time that I tested it on my computer and on aws ec2 instance, everything should be working
