![](https://github.com/alckasoc/Joblisting-Webscraper/blob/main/images/banner.png?raw=true)

[![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-F3f0f0?&logo=Jupyter&labelColor=F3f0f0)](https://jupyter.org/try)
[![Python](https://img.shields.io/badge/Python-3.8.3-21455f?logo=python&labelColor=21455f)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-3.141.0-F3f0f0?logo=selenium&labelColor=F3f0f0)](https://selenium-python.readthedocs.io/)
[![Gmail 1](https://img.shields.io/badge/Gmail-tuvincent0106%40gmail.com-F3f0f0?logo=gmail&labelColor=F3f0f0)](https://mail.google.com/mail/?view=cm&fs=1&to=tuvincent0106@gmail.com)
[![Gmail 2](https://img.shields.io/badge/Gmail-alckasoc%40gmail.com-F3f0f0?logo=gmail&labelColor=F3f0f0)](https://mail.google.com/mail/?view=cm&fs=1&to=tuvincent0106@gmail.com)
[![Linkedin](https://img.shields.io/badge/Linkedin-Vincent%20Tu-0A66C2?logo=linkedin&labelColor=0A66C2)](https://www.linkedin.com/in/vincent-tu-422b18208)
[![Discord](https://img.shields.io/badge/Discord-alckasoc%235261-7187da?logo=discord&labelColor=7288db&logoColor=white)](https://discordapp.com/users/251152357063131138/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg?labelColor=blue)](https://raw.githubusercontent.com/alckasoc/Joblisting-Webscraper/main/LICENSE)

This project allows for configuring joblisting filters and webscraping joblisting data from Glassdoor.com.

## Table of Contents:
- [Motivation](https://github.com/alckasoc/Joblisting-Webscraper/blob/main/README.md#motivation)
- [Technologies](https://github.com/alckasoc/Joblisting-Webscraper/blob/main/README.md#technologies)
- [Requirements for Use](https://github.com/alckasoc/Joblisting-Webscraper/blob/main/README.md#requirements-for-use)
- Tutorial
- UML Diagrams
- Difficulties:
    - elements.py
        - ConfigElements
    - webscraper.py
        - GlassdoorWebScraper
    - Other
- What I Learned
- Additional Notes
- References
- Author Info
- Future Notice
- Credits
- Thank you!

## Motivation

Inspired by Omer Sakarya's [glassdoor-webscraper-selenium](https://github.com/arapfaik/scraping-glassdoor-selenium) project and aiming to create a data science project from end to end, I took the opportunity to explore the webscraping world and create a project. I found webscraping joblistings from Glassdoor.com to be valuable for a wealth of applications: quickly generating real-life applicable data, the generated data can be wrangled with and explored through exploratory data analysis (EDA). Additionally, it could have the potential of helping future employers and job seekers discover demographics previously hidden (I hope).

## Technologies

re

&nbsp;&nbsp;&nbsp;&nbsp;I used RegEx for parsing and searching strings. This was helpful for reading in different filter options and scraping data.

time

&nbsp;&nbsp;&nbsp;&nbsp;Time was for a time.sleep() delay —since internet speed can affect how quickly a page loads and Glassdoor.com has a slightly slow page load up. Successive calls to functions can also be skipped over if the page does not load fast enough.

selenium

&nbsp;&nbsp;&nbsp;&nbsp;I used selenium for this project because it, unlike beautifulsoup4, allows for JavaScript which proved especially helpful in one of the large difficulties of this project.

## Requirements for Use

- I used Google Chrome Version 90.0.4430.212 and its corresponding Chromedriver for this project (you can find your Chromedriver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). To check Chrome version, navigate to a Google browser and click the upper right three dots > Settings > Help > About Google Chrome.
- Python ≥ 3.8.3.
- Selenium ≥ 3.141.0.

## Tutorial

Refer to the demo.ipynb for a demonstration of the project. Also, don't forget to call help(GlassdoorWebScraper) to get a breakdown of all the possible functions and attributes of my project! With these 2 components, I believe you will be able to use it.

## UML Diagrams

I created my UML diagrams in EdrawMax. Attached is a folder called diagrams. This folder holds 3 separate .eddx files that are diagrams: structure, filter pipeline, and the filters themselves. I've also attached .png images corresponding to these .eddx files for easier view (note: these images are watermarked). These diagrams can help you better understand my project as they have for generalizing it for me.

## Difficulties

### elements.py/ConfigElements
- The salary filter is not a dropdown *list*, instead, it is composed of 2 sliders with a histogram displayed on top accompanied by a salary range header in the top left corner of the dropdown (refer to Figure 1-1). Creativity led me to utilize the arrow keys to move these sliders while monitoring the change in the salary range header such that the salary range could be edited by the user correctly.
- I noticed the salary filter, by chance upon page load up, would include or not include the checkbox for including data with no salaries. This issue was solved with a try and except block so that the code would not produce an error in the case where there is no checkbox.
- In the case where it does not display this checkbox, the histograms were always out of alignment and did not form a rounded bell curve otherwise it formed a smooth histogram bell curve (refer to Figure 1-1 & 1-2). This issue posed a few interesting features that were later explored and compensated for in code.

<br/><br/>
![](https://github.com/alckasoc/Joblisting-Webscraper/blob/main/images/salary1.PNG?raw=true)
Figure 1-1. Smooth salary histogram bell curve with a checkbox.
<br/><br/>
![](https://github.com/alckasoc/Joblisting-Webscraper/blob/main/images/salary2.PNG?raw=true)
Figure 1-2. Rough salary histogram without a checkbox.
<br/><br/>

- In both cases where the checkbox is present and absent, moving the left slider immediately to the right would send it to the absolute farthest right and the same goes for moving the right slider immediately to the left (actually, in some cases this would happen and in some other cases it wouldn't). Refer to Figure 1-3. I solved this by moving these sliders before any computation was executed on them (move the left slider left first before moving right and the right slider right first before moving left). P.S. This also solved another issue where the salary range in the header doesn't match the actual salary range the histogram displays. Refer to figure 1-3.5.

<br/><br/>
![](https://github.com/alckasoc/Joblisting-Webscraper/blob/main/images/salary3.PNG?raw=true)
Figure 1-3. Slider movement.
<br/><br/>

- In another issue, the bell curve shown in Figure 1-1 could be reset (the default is 18k to 404k and this default salary range would vary slightly every now and then when the page is loaded —granted it is not the curve shown in Figure 1-2) In contrast, the rough salary histogram in Figure 1-2 could not be reset (reset as in moving the sliders back to the original positions, which means moving the left slider to the far left and the right slider to the far right). Refer to Figure 1-4 & 1-5. I solved this issue by simply forcing a clear_filters() when initializing Figure 1-2 and by resetting the salary slider for Figure 1-1. Alternatively, I could've  simply clear_filters() however this would erase all filters, and I wanted extra functionality for editing the salary filter in the case where it can be edited separately.

<br/><br/>
![](https://github.com/alckasoc/Joblisting-Webscraper/blob/main/images/salary4.PNG?raw=true)
Figure 1-4. Resetting the salary ranges. Notice how I can reset this by simply dragging the left and right sliders to the far left and right, respectively. 
<br/><br/>
![](https://github.com/alckasoc/Joblisting-Webscraper/blob/main/images/salary5.PNG?raw=true)
Figure 1-5. Resetting the salary ranges. Notice how I set a salary range and this new salary range becomes the endpoints.
<br/><br/>

- The "More" dropdown randomly omits, by chance on page load up, the "All City" filter and a few other filters like "All Seniority Labels". This difficulty was solved with a try and except block that would constantly update the self.filters() attribute to keep the most up-to-date filters and filter options.

<br/><br/>
![](https://github.com/alckasoc/Joblisting-Webscraper/blob/main/images/salary6.PNG?raw=true)
Figure 1-6. Notice all the "More" dropdowns.
<br/><br/>
![](https://github.com/alckasoc/Joblisting-Webscraper/blob/main/images/salary7.PNG?raw=true)
Figure 1-7. Notice how this dropdown is missing "All Job Functions" and "All Seniority Labels".
<br/><br/>

- Another difficulty was trying to extract the maximum amount of information from the dropdowns (e.g. the numbers located next to the filter options in the dropdown lists). Some dropdowns such as "Miles" (or referred to as radii in the HTML) did not have a count next to the filter option while filters like "Job Type" did. This step required a bit of regex and experimenting until I finally created the get_and_parse_filters() function. This implementation along with many other try and accept blocks and the similarities/differences of the filters all made for a difficult act of properly creating streamlined functions to easily maintain and update filters (this took several revisions).
- init_filter() was a function that took a great deal of time and thinking to create. In fact, I simply copied and pasted reusable code the first go around because the filters (dropdown list-like filters) were *extremely* similar, but had small variations (and I also did this because I was lazy). After copying and pasting reusable code to edit all the filters, I had to find a functional way to aggregate them into 1 unique and reusable/flexible function and that was init_filter()! P.S. change_filter_to() also presented a similar problem though I was a little better equipped with tackling this problem.
- reset_salary_base_fn() was initially not needed (or so I thought then). However, once I was part way through writing the init_change_filter() function, I realized the need for a salary reset (alternatively, I could reset the salary by just using clear_filters() however this would clear all filters and sometimes it might not work in the case where there are no filters chosen). Thus, it demanded the implementation of a custom salary reset. reset_salary_base_fn() required a bit of creative thinking as a somewhat farfetched solution I had was to move the sliders until the salary header didn't change (originally, I was trying to think of a more elaborative solution that would be more elegant).
- More on categorization, I had to deal with how I would categorize different filters. For instance, the entire filter initialization and change pipeline, the filters are divided into multiple functions. get_and_parse_filters() is used only for dropdown list filters. Sortby is initialized and changed separately as it is not a part of the DKFilters tag. The salary filter/dropdown required its own initialization function and change function. Join functions had to be separated in case some slight variation might occur in the actual text of the filters. init_filter() was wrapped with the init_filters() function for ease of use and conveniency. These were all stateful filters as they all were dynamic and changed along with the other filters. Static or stateless filters included the "Company Rating", "Easy Apply Only", "Work From Home Only", and the "Mile" dropdown (however, I lumped this filter with the stateful filters as it was more convenient and fitting).

### webscraper.py
- Clearing the location search bar required a custom implementation of a delete instead of a simple clear() in selenium.
- Writing the webscraping function was certainly a difficulty as the input was a number specifying the number of jobs the user wants to scrape from the website. In contrast to the function input, the actual webscraping was done in nested loops that would loop through all the joblistings on a page before moving onto the next page. This complicated structure proved difficult at first, however, with a bit of testing, I was able to implement a few appropriate breaks that would allow for this scraping function to work.
- The init_change_filter() function posed a lot of difficulty, especially for initializing and changing the salary filter. Before writing this function, changing salary was pretty static: you initialize once, change and if it does not work or there seems to be a bug, then you simply clear filters and retry again or call get() again and try it on a new page. Writing this function made this process dynamic: now you could initialize and change the salary filter without clearing filters and initialize whenever you want (there might be a few problems lingering) and change salary whenever you want. I solved this unnoticeable issue with a myriad of functions: reset_salary_slider, reset_salary_base_fn, and regex_parse_salary. These then had to be integrated into existing codebases and delayed appropriately according to the speed of the page load up and refresh speed.
### Other
- Designing the entire project was, in itself, a difficulty as I had to partition the code into multiple files and organize them in an object-oriented way.
- Learning how to write docstrings, comment, use git (my first time), use poetry and packaging conventions, and structure a project also demanded a great amount of time!
- Deciding on what to include and not include in a function posed a significant difficulty especially since a great deal of the functions implemented are reused. For example, an initial implementation used a recursive-like structure such that the programmer could access any of the tags leading to a grandchild tag or child tag. This would be useful if in any case parent or child tags would be traversed, but it was never generally used and thus discarded.
- As the number of functions grew, naming became a general issue as the abundance of variables demanded conciseness and also a lot of *concise* explainability (ease of understanding for me).
- Categorizing the filters and writing reusable code for them also posed a large difficulty. There are a total of 10 dropdown-like filters, 1 of the 10 is the salary dropdown which doesn't have a dropdown list but rather 2 sliders. This is just one example of how these filters are similar yet dissimilar.
- Depending on internet speed, the code would or would not work. I had to implement a few waits whether that be the WebDriverElement's wait or a simple time.sleep() to compensate for both internet speed and the slow page load up speed.

## What I Learned

Here's a curated list of topics I learned:

- Selenium (fundamentals)
- Python Packaging (basics)
- Git & Github
- Poetry
- Python Programming Conventions (PEP8 & PEP257)
- A Few Software Design Principles
- Autoformatters
- Documentation formatting (brief overview)
- UML (class diagrams)

Wow, where do I begin! This project definitely encouraged me to learn a lot. Before even starting, I had to learn webscraping (either with BeautifulSoup4 or Selenium). Moreover, I learned a bit about Python packaging with PyPI and all the documents to go along with that (e.g. setup.py, MANIFEST.in, README.md, requirements.txt or pyproject.toml, setup.cfg (still not entirely sure what this one is), src, test, and docs folders, images folder, the .gitignore file, and much more). Furthermore, I learned the fundamentals of git and github and poetry (a Python dependency manager and Python package tool). I read a bit on PEP8 (Python conventions) and PEP257 (docstring conventions). One topic of interest that really stood out was design principles! I'm currently in my last year of high school, and in all the time I've spent in programming classes, I've never considered the importance of principles like D.R.Y. or K.I.S.S. until now (curiously, I also looked a little bit into software design documents and how to code review)! Additionally, I learned about autoformatters like black or yapf or autopep8 and other related tools like flake8. In fact, this README actually took me forever as this was my first time ever learning this! In my project's journey, I've encountered countless design choices (my project is far from perfect, I believe its structure now is still *really* hard to decipher). I also briefly looked at different documentation formats: Google's format, NumPy format, and the Sphinx documentation tool. And lastly, I learned just the basics of the Unified Modeling Language (UML) for creating class diagrams and just general-purpose box diagrams to better capture the infrastructure of my project!

## Additional Notes
- update_keyword_and_URL may be called any time. However, if called after a web browser is opened, the user must close and call get() again to open up a web browser with the updated keyword and URL.
- set_implicitly_wait() will set the *global* implicit wait for the driver instantiated in get(). This function is called by default in get() and can be configured separately or through get().
- After a lot of testing, it seems that the init_change_filter() is the one function that can perform all the filter configurations properly. However, it may still contain some problems. If you run into issues with this function, please defer to lower level functions like init_filters(filter) followed by a change_*_to().
- scrape_jobs() was tested dozens of times, however there may still be some uncovered test cases. For example, if there is no page button at the bottom, then there might be an error. In this case, avoid over-applying too many filter options (over-specificity would narrow down joblistings to only a few) and ensure that the list of joblistings always exceeds 1 page (this also makes sense for data collection-wise).
- Since the GlassdoorWebScraper class inherits from the element classes, it has access to the class variables and public methods of those element classes. This allowed me to quickly configure and test out specific aspects of my project without having to code small experiments (which I still did nonetheless). Check out the diagrams folder for a UML class diagram breakdown of my project.
- If you have any issues, feel free to reach out to me any way possible!

## References

- Tech With Tim's amazing [webscraping tutorial](https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ) with Selenium was a strong starting point for me in webscraping (and it also briefly introduced me to unittesting).

- I learned a bit more on the Selenium documentation (I found 2 documentation sites, first is for Python and the second is more generalized for multiple languages): [Selenium with Python](https://selenium-python.readthedocs.io/) and [The Selenium Browser Automation Project](https://www.selenium.dev/documentation/en/).

- [Corey Schafer's Tutorial](https://www.youtube.com/watch?v=C-gEQdGVXbk) on better Python programming definitely aided in writing more organized code.

- [Jasmine Finer's Blog](https://realpython.com/python-pep8/#:~:text=PEP%208%2C%20sometimes%20spelled%20PEP8%20or%20PEP-8%2C%20is,improve%20the%20readability%20and%20consistency%20of%20Python%20code) on writing beautiful Python quickly summarized the necessary knowledge I needed to start writing *better* looking code.

- [Tech With Tim's Software Design Principles](https://www.youtube.com/watch?v=XQzEo1qag4A) video and [TechLead's Software Design Principles](https://www.youtube.com/watch?v=RQOI6DEpfpk) video both helped in reminding me the fundamental pillars of programming (even though I didn't perfectly adhere to them).

- The following resources helped me in understanding the Python packaging convention and structure (these aren't all of them, they are just the main ones):
    - [Jerry Zhao's requirements.txt blog](https://www.dev2qa.com/how-to-install-python-packages-using-requirements-text-file/#:~:text=Use%20PIP%20To%20Install%20Python%20Packages%20From%20Requirements.txt,new%20virtual%20Python%20environment%20use%20Python%20virtualenv%20module)
    - [an IONOS Digitalguide on READMEs](https://www.ionos.com/digitalguide/websites/web-development/readme-file/#:~:text=1%20For%20end%20users%2C%20a%20readme%20file%20answers,of%20a%20system%2C%20software%20or%20an%20open-source%20project)
    - [Kenneth Reitz's and Real Python's Hitchhiker's Guide to Python Packaging](https://docs.python-guide.org/writing/structure/)
    - [codebasics's .gitignore tutorial](https://www.youtube.com/watch?v=ErJyWO8TGoM&ab_channel=codebasics)
    - [RetroTK2's .gitignore tutorial](https://www.youtube.com/watch?v=_vejzukmn4s&ab_channel=RetroTK2)
    - [Packt Video's tutorial on Python Distribution](https://www.youtube.com/watch?v=j8q428a_7Is&ab_channel=PacktVideo)
    - [An \_\_init\_\_.py Introduction](https://careerkarma.com/blog/what-is-init-py/)
    - [A Django Lesson on Python's setuptools](https://www.youtube.com/watch?v=wCGsLqHOT2I&ab_channel=DjangoLessons)
    - [Installing Packages With pip and requirements.txt]()
    - [How to Write a Great README](https://x-team.com/blog/how-to-write-a-great-readme/)
    - [PyGotham 2019 - An Introduction to Poetry](https://www.youtube.com/watch?v=QX_Nhu1zhlg)
    - [Official Poetry Documentation](https://python-poetry.org/docs/)
    - [Poetry Tutorial by JCharisTech & J-Secur1ty](https://www.youtube.com/watch?v=m9mtNecfWDY&t=196s&ab_channel=JCharisTech%26J-Secur1ty)
    - [Choose a License](https://choosealicense.com/)
    - [Black autoformatter by R3ap3rPy](https://www.youtube.com/watch?v=ia19n_yK4Qs&ab_channel=R3ap3rPy)
    - [How to Do Code Reviews by Michael Lynch](https://mtlynch.io/human-code-reviews-1/)
    - [Intro to SWE Design Documents](https://blog.simpleokr.com/what-is-a-design-document-software-engineering-best-practice/)
    - [GeeksforGeeks Docstring Tutorial](https://www.geeksforgeeks.org/python-docstrings/)

- [UML Class Diagrams Tutorial by LucidCharts](https://www.youtube.com/watch?v=UI6lqHOVHic) and [FreeCodeCamp's UML Diagram Tutorial](https://www.youtube.com/watch?v=WnMQ8HlmeXc&t=1147s) helped me learn about standard conventions in creating modeling diagrams for software engineering.

## Author Info

Contact me:

Gmail: tuvincent0106@gmail.com (preferably) or alckasoc@gmail.com
Linkedin (I have not configured my Linkedin profile yet!): [Vincent Tu](https://www.linkedin.com/in/vincent-tu-422b18208/)
Discord: [alckasoc#5261](https://discordapp.com/users/251152357063131138/)

## Future Notice

As of now, this project works. However, as joblistings are constantly updated, and consequently Glassdoor.com's joblistings and jobpage will consistently update (also general website updates), there may be a time where this project may not work as intended. I never expected this project to reach this size. With more documentation, docstrings, comments, and functions, I found the project's line of code size growing rapidly. Downloading this project is definitely a hassle as it is not a PyPI package. However, my choice to not make it a PyPI package is because I do not plan on maintaining this project with the oncoming future updates to Glassdoor.com. However, regardless of where this project stands, I can say that it has been a priceless journey. I've learned a wealth of material and topics not to mention the joy I've experienced in seeing my huge block of code run without errors. 

## Credits

This project was made with inspiration from:
https://github.com/arapfaik/scraping-glassdoor-selenium

## Thank you!

It has certainly been a grueling rollercoaster of coding and debugging, but seeing my clunky code run while learning topics I've previously never heard of before is unmistakably a hallmark of this project and any project! Hills and valleys are inevitable and I definitely learned that climbing out of the valleys is what makes the journey so enjoyable. Thank you for viewing my project.
