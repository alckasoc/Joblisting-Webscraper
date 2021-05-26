
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from elements import ConfigElements, WebScrapingElements


class GlassdoorWebScraper(ConfigElements, WebScrapingElements):
    """ A GlassdoorWebScraper obj will be able to configure filters and webscrape.

    Ensure that your chromedriver corresponds correctly to your current
    Google chrome version here: 

    https://sites.google.com/a/chromium.org/chromedriver/downloads
    
    
    
    Here is the same URL with keyword="data scientist":
    
    https://www.glassdoor.com/Job/jobs.htm?sc.keyword="data scientist"
    &locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&
    fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=
    -1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=
    -1&employerSizes=0&applicationType=0&remoteWorkType=0
    
    
    
    Design:
        
        - locators.py and elements.py are split into 2 components: 
          filter configuration and webscraping.
        - The GlassdoorWebScraper class uses the low level functions
          of elements.py to create higher level functions.
        - GlassdoorWebScraper also inherits from elements.py to give 
          access to the lower level functions.
    
    
    
    Table of Contents:
    
    - Basic Utility Functions
        - update keyword and URL
        - set implicit wait
        - get
        - close
    - Filter Configuration Functions
        - clear filters
        - init filters
        - init change filters
        - include no salary data
        - change *
            > keyword
            > location
            > jobtype
            > postdate
            > salary
            > city
            > industry
            > job function
            > seniority label
            > company
            > company size
            > Easy Apply Only/Work From Home Only
            > rating
            > sortby
    - Webscrape Function

    
    
    Functions:
    
    update_keyword_and_URL(keyword)
        Updates the keyword and URL simultaneously.
        
    set_implicitly_wait(implicitly_wait_time)
        Set the global implicit wait time.
        
    get(implicitly_wait_time=5, set_implicitly_wait=True)
        Creates a webdriver, maximizes window, sets the implicit wait time
        (which defaults to 5) if set_implicitly_wait is true, then
        finally opens the URL.
        
    close()
        Closes the current tab. This function is a wrapper just for 
        convenience.
    
    change_keyword_to(keyword)
        Enter keyword into the keyword search bar and return.
        
    change_location_to(location)
        Enter location into the location search bar and return.
        
    init_filters(_filter=None)
        Initialize all filters if _filter is None else initialize _filter.
        
    reset_salary_slider(is_both=True, is_left=True)
        Reset salary slider. is_both decides if both sliders should be reset
        and is_left decides if the left or the right one should be reset 
        (in the case that is_both is False).
        
     init_change_filters(filter_type)
         Initialize a filter, then print out possible filter options,
         then change the filter to specified input. 
        
    change_jobtype_to(jobtype)
        Change to a specified jobtype filter option.
        
    change_postdate_to(postdate)
        Change to a specified postdate filter option.
        
    include_no_salary_data(include)
        The boolean include dictates whether or not the checkbox is checked. 
    
    change_salary_to(begin_salary, end_salary)
        The salary range is in the form [a, b]. a is the begin_salary and is a string
        (e.g. "125K" where the K represents thousands). b is the end_salary and
        is also a string. include_no_salary_data defaults to True meaning
        it will by default include data with no salary.
        
    change_radius_to(radius)
        Change to a specified radius filter option.
        
    change_cityid_to(cityid)
        Change to a specified cityid filter option.
        
    change_industry_to(industry)
        Change to a specified industry filter option.
        
    change_jobfunction_to(job_function)
        Change to a specified job function filter option.
        
    change_senioritylabel_to(seniority_label)
        Change to a specified seniority label filter option.
        
    change_company_to(company)
        Change to a specified company filter option.
        
    change_companysize_to(company_size)
        Change to a specified company size filter option.
        
    easy_apply_work_home(is_eao, will_apply)
        If is_eao is true, then select the Easy Apply Only label button else
        select the Work From Home Only label button. Then, if will_apply is true,
        then apply. 
        
    change_rating_to(rating)
        Change the rating.
        
    clear_filters()
        Clears all filters.
        
    sort_by(sort_type)
        Changes the "Most Relevant" dropdown (sortby) filter to a specified filter option.
        
    scrape_jobs(n_jobs)
        Webscrape jobs. n_jobs determines the size of the dataset.
        
        
    This project was created with inspiration from:
    
    https://github.com/arapfaik/scraping-glassdoor-selenium
    
    """     
     
    def __init__(self, keyword, PATH="C:\Program Files (x86)\chromedriver.exe"):
        """The following attributes can be accessed and changed but it is advised not to do so directly.
        
            All attributes of a GlassdoorWebScraper obj include:
        
            self.PATH: 
                The path to your chromedriver.exe.
            
            
            self.keyword: 
                The keyword initialized by the user.
            
            
            self.URL_part_1: 
                The first part of the Glassdoor URL. 
            
            
            self.URL_part_2: 
                The second part of the Glassdoor URL.
        
        
            self.URL:
                The concatenation of self.URL_part_1, self.keyword, and self.URL_part_2 
                in that exact order.
                
                
            self.driver:
                The Selenium webdriver. Only created when the user creates a GlassdoorWebScraper obj and
                calls the get() method.
                
                
            self.filters:
                A dictionary of dictionaries and lists. It contains all the configurable filters 
                of the current opened webpage. Only created when the init_configs() method is called.
                
                
            self.get_join_filters:
                A dictionary of dictionaries. The outer dict has keys for each filter. These keys correspond
                to dictionary values that hold: name, get fn, join fn, is_salary, and is_more. Name is the name
                of the filter. Get fn is the get locator function for that filter. Join fn is the function used to
                regex simplify and concatenate the preprocessed filter options corresponding to a filter. is_salary 
                checks if the filter is the salary filter. is_more checks if the filter is under the more dropdown.
                
        """
        self.PATH = PATH
        self.keyword = keyword
        
        self.URL_part_1 = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword='
        self.URL_part_2 = '&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType= \
                             all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId= \
                             -1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId= \
                             -1&employerSizes=0&applicationType=0&remoteWorkType=0'
        self.URL = self.URL_part_1 + self.keyword + self.URL_part_2

        self.filters = {}
        
        # Excludes company rating, easy apply only, work from home only, and the
        # most relevant (sortby) filters. 
        self.get_join_filters = {
            "jobtypes": {
                "get": self.get_filters_jobtypes,
                "join": self.join_filters_jobtypes,
                "is_salary": False,
                "is_more": False,
                "change": self.change_jobtype_to
            },
            "postdates": {
                "get": self.get_filters_postdates,
                "join": self.join_filters_postdates, 
                "is_salary": False,
                "is_more": False,
                "change": self.change_postdate_to
            },
            "salaries": {
                "get": self.get_filters_minsalaries,
                "join": None,
                "is_salary": True,
                "is_more": False,
                "change": self.change_salary_to
            },
            "radii": {
                "get": self.get_filters_radii,
                "join": self.join_filters_radii,
                "is_salary": False,
                "is_more": False,
                "change": self.change_radius_to
            },
            "cityids": {
                "get": self.get_filters_cityids,
                "join": self.join_filters_cityids,
                "is_salary": False,
                "is_more": True,
                "change": self.change_cityid_to
            },
            "industries": {
                "get": self.get_filters_industries,
                "join": self.join_filters_industries,
                "is_salary": False,
                "is_more": True,
                "change": self.change_industry_to
            },
            "job_functions": {
                "get": self.get_filters_jobfunctions,
                "join": self.join_filters_jobfunctions,
                "is_salary": False,
                "is_more": True,
                "change": self.change_jobfunction_to
            },
            "seniority_labels": {
                "get": self.get_filters_senioritylabels,
                "join": self.join_filters_senioritylabels,
                "is_salary": False,
                "is_more": True,
                "change": self.change_senioritylabel_to
            },
            "companies": {
                "get": self.get_filters_companies,
                "join": self.join_filters_companies,
                "is_salary": False,
                "is_more": True,
                "change": self.change_company_to
            },
            "company_sizes": {
                "get": self.get_filters_companysizes,
                "join": self.join_filters_companysizes,
                "is_salary": False,
                "is_more": True,
                "change": self.change_companysize_to
            },
        }
        
        
        
    # ==================================================
    # Basic Utility Functions.
    # ==================================================
    
    
    
    def update_keyword_and_URL(self, keyword):
        self.keyword = keyword
        self.URL = self.URL_part_1 + self.keyword + self.URL_part_2
    
    
    # Sets the implicit wait time.
    # Note: Implicit wait time is set for life of the Webdriver obj once declared;
    # this means the get() function must be called again before setting a new 
    # implicit wait time.
    def set_implicitly_wait(self, implicitly_wait_time):
        self.driver.implicitly_wait(implicitly_wait_time)
    
    
    def get(self, implicitly_wait_time=5, set_implicitly_wait=True): 
        self.driver = webdriver.Chrome(self.PATH)
        if set_implicitly_wait: self.set_implicitly_wait(implicitly_wait_time)
        self.driver.maximize_window()
        self.driver.get(self.URL)
    
    
    def close(self):
        self.driver.close()
    
    
    
    # ==================================================
    # Filter Configuration Functions.
    # ==================================================
    
    
    
    def clear_filters(self):
        try:
            clear_filter_button = self.get_clear_filter_span()
            clear_filter_button.click()
        except Exception as e:
            print(e)
    
    
    # Initialize all filter configurations and allows for initializing specific filters.
    # Note: filters change when other filters are updated.
    # Note: Make sure to glance the self.filters attribute and call init_filters() on 
    # the filter that will be next changed.
    def init_filters(self, _filter=None):
        if not _filter:
            for filters, attribs in self.get_join_filters.items():
                self.init_filter(name=filters, 
                                 get_filters_=attribs["get"], 
                                 join_filters_=attribs["join"],
                                 is_salary=attribs["is_salary"],
                                 is_more=attribs["is_more"])
            
            self.init_sortby()
            
            self.click_more_dropdown(n_clicks=2)
        elif _filter:
            if _filter == "sortbys":
                self.init_sortby()
            else:
                attribs = self.get_join_filters[_filter]
                self.init_filter(name=_filter,
                                 get_filters_=attribs["get"],
                                 join_filters_=attribs["join"],
                                 is_salary=attribs["is_salary"],
                                 is_more=attribs["is_more"])
        
        
    def reset_salary_slider(self, is_both=True, is_left=True):
        slider_info = {
            "left_slider": {
                "slider": self.get_left_slider,
                "idx": 0,
                "key_fn": Keys.ARROW_LEFT
            },
            "right_slider": {
                "slider": self.get_right_slider,
                "idx": 1,
                "key_fn": Keys.ARROW_RIGHT
            }
        }
        
        salary_filter = self.get_join_filters["salaries"]["get"]()
        salary_filter.click()
        
        if not is_both:
            if is_left:
                left_slider_info = slider_info["left_slider"]

                slider = left_slider_info["slider"]()
                idx = left_slider_info["idx"]
                key_fn = left_slider_info["key_fn"]
            elif not is_left:
                right_slider_info = slider_info["right_slider"]

                slider = right_slider_info["slider"]()
                idx = right_slider_info["idx"]
                key_fn = right_slider_info["key_fn"]
                
            self.reset_salary_base_fn(slider, idx, key_fn)
        elif is_both:
            for _, values in slider_info.items():
                slider = values["slider"]()
                idx = values["idx"]
                key_fn = values["key_fn"]
                self.reset_salary_base_fn(slider, idx, key_fn, is_both=True)
            applybutton = self.get_filters_minsalaries_applybutton()
            applybutton.click()
        
        
        
        
    
    # A streamlined wrapper function to chain together common methods:
    # initialize a filter, print the viable filter options,
    # and change to the specified filter option(s).
    # Note: If you use this function to change "salaries",
    # then it will reset all filters and then initialize the salary filter.
    # This design choice was because there are certain
    # page loadups that have a weird looking salary histogram.
    # Note: Default to init_filters("salaries") and change_salary_to()
    # if the histogram is chaotic (this function doesn't work well with the
    # weird features of the chaotic histogram).
    def init_change_filter(self, filter_type):
        if filter_type != "salaries":
            self.init_filters(filter_type)
            print(f"Your options for filter {filter_type} are :")
            print("----------------------------")
            print(f"{filter_type}: ", self.filters[filter_type])
            _filter = input("Enter a filter option: ")
            self.get_join_filters[filter_type]["change"](_filter)
        elif filter_type == "salaries":
            try:
                # Check if there is a preexisting config dict.
                _ = self.filters["salaries"]["left_slider"]
                # Since Glassdoor.com's salary filter changes
                # randomly upon page load-up, this try block checks
                # what setup the salary filter is and 
                # acts accordingly.
                try:
                    # Try to get the checkbox.
                    salary_filter = self.get_filters_minsalaries()
                    salary_filter.click()
                    no_salary_label = self.get_filters_minsalaries_checkbox_label()
                    salary_filter.click()
                    
                    clear_filter = False
                except:
                    clear_filter = True
                if clear_filter:
                    salary_filter = self.get_filters_minsalaries()
                    salary_filter.click()
                    self.clear_filters()
                    
                    
                time.sleep(1)
                self.init_filters(filter_type)
            except Exception as e:
                print(e)
                print("ENTER EXCEPTION")
                self.init_filters(filter_type)
                time.sleep(1)
            print(f"Your options for filter {filter_type} are :")
            print("----------------------------")
            print("left_slider: ", self.filters[filter_type]["left_slider"])
            print("")
            print("right_slider: ", self.filters[filter_type]["right_slider"])
            begin_salary = input("Enter a lower bound salary from the left slider list: ")
            end_salary = input("Enter an upper bound salary from the left slider list: ")
            
            # The include no salary data feature is deleted from this function
            # because it seems to not work well together. So the user must call
            # include_no_salary_data() separately.
            self.get_join_filters[filter_type]["change"](begin_salary, 
                                                         end_salary)
            
    
    def include_no_salary_data(self, include):
        try:
            salary_filter = self.get_filters_minsalaries()
            salary_filter.click()

            no_salary_label = self.get_filters_minsalaries_checkbox_label()
            checkbox = self.get_filters_minsalaries_checkbox()
            is_checked = checkbox.get_attribute("aria-checked")
            if is_checked == "true":
                is_checked = True
            else:
                is_checked = False
            if is_checked:
                if include: pass
                elif not include: no_salary_label.click()
            elif not is_checked:
                if include: no_salary_label.click()
                elif not include: pass
            applybutton = self.get_filters_minsalaries_applybutton()
            applybutton.click()
        except Exception as e:
            print(e)
    
    
    # Change keyword (occupation).
    def change_keyword_to(self, keyword):
        keyword_search = self.get_keyword_search()
        self.clear_and_search(keyword_search, keyword)
        
    
    def change_location_to(self, location):
        location_search = self.get_location_search()
        
        # Clears the input field for the location search bar.
        # Note: Selenium's clear() function does not work here
        # so a custom delete was implemented.
        initial_location = location_search.get_attribute("value")
        for _ in range(len(initial_location)):
            location_search.send_keys(Keys.BACKSPACE)
            
        # Enters user's inputted location and presses the search icon.
        # Note: clear_and_search() was not used because clear() does 
        # not work.
        location_search.send_keys(location)
        search_button = self.get_search_button()
        search_button.click()
        
        
    def change_jobtype_to(self, jobtype):
        jobtype_attribs = self.get_join_filters["jobtypes"]
        self.change_filter_to(name="jobtypes", 
                              choice=jobtype,
                              is_more=jobtype_attribs["is_more"])
    
    
    def change_postdate_to(self, postdate):
        postdate_attribs = self.get_join_filters["postdates"]
        self.change_filter_to(name="postdates", 
                              choice=postdate,
                              is_more=postdate_attribs["is_more"])
            
    
    # Note: Glassdoor.com has a weird inconsistency with how the
    # salary filter is initialized and used (the salary ranges themselves
    # change as well depending on clicking the apply, or moving the sliders
    # left or right when they are already at the edges!).
    # Note: change_salary_to() works fine for the bell curve
    # histogram, but might take a few clear_filters() and init_filters("salaries")
    # to work somewhat consistently for the chaotic histogram.
    def change_salary_to(self, begin_salary, end_salary):
        
        
        salary_filter = self.get_filters_minsalaries()
        salary_filter.click()
            
        # For some reason, the salary range header is bugged.
        # These statements here is to ensure that the lower endpoint
        # of the salary range is actually correctly displayed.
        left_slider = self.get_left_slider()
        left_slider.click()
        left_slider.send_keys(Keys.ARROW_LEFT)
        left_slider.send_keys(Keys.ARROW_RIGHT)
        right_slider = self.get_right_slider()
        right_slider.send_keys(Keys.ARROW_RIGHT)
        right_slider.send_keys(Keys.ARROW_LEFT)
        
        # Regex parse the current salary range.
        a_bin = self.get_histogram_labels_header()
        a_bin = a_bin.text.replace("$", "").split("-")
        
        # The next 4 blocks of code dictate how far the current left and right 
        # sliders are from the desired begin_salary (left slider) and 
        # end_salary (right slider).
        left_slider_salaries = self.filters["salaries"]["left_slider"]
        right_slider_salaries = self.filters["salaries"]["right_slider"]
        
        begin_salary = begin_salary.upper()
        end_salary = end_salary.upper()
        
        begin_salary_idx = left_slider_salaries.index(begin_salary)
        end_salary_idx = right_slider_salaries.index(end_salary)
        
        current_begin_salary, current_end_salary = a_bin[0], a_bin[1]
        current_begin_salary_idx = left_slider_salaries.index(current_begin_salary)
        current_end_salary_idx = right_slider_salaries.index(current_end_salary)
        
        begin_salary_difference = abs(begin_salary_idx - current_begin_salary_idx)
        end_salary_difference = abs(end_salary_idx - current_end_salary_idx)
        
        # Click and move left slider.
        left_slider = self.get_left_slider()                                                        
        left_slider.click()
                    
        self.move_slider(left_slider, 
                         begin_salary_idx, 
                         current_begin_salary_idx,
                         begin_salary_difference)
        
        # Click and move right slider.
        right_slider = self.get_right_slider()
        right_slider.click()
        
        self.move_slider(right_slider,
                         end_salary_idx,
                         current_end_salary_idx,
                         end_salary_difference)
        
        # Finally, apply the changes.
        applybutton = self.get_filters_minsalaries_applybutton()
        applybutton.click()
        
        
    def change_radius_to(self, radius):
        radius_attribs = self.get_join_filters["radii"]
        self.change_filter_to(name="radii", 
                              choice=radius,
                              is_more=radius_attribs["is_more"])
    
    
    def change_cityid_to(self, cityid):
        cityid_attribs = self.get_join_filters["cityids"]
        self.change_filter_to(name="cityids", 
                              choice=cityid,
                              is_more=cityid_attribs["is_more"])
        
        
    def change_industry_to(self, industry):
        industry_attribs = self.get_join_filters["industries"]
        self.change_filter_to(name="industries", 
                              choice=industry,
                              is_more=industry_attribs["is_more"])
        
        
    def change_jobfunction_to(self, job_function):
        jobfunction_attribs = self.get_join_filters["job_functions"]
        self.change_filter_to(name="job_functions", 
                              choice=job_function,
                              is_more=jobfunction_attribs["is_more"])
        
        
    def change_senioritylabel_to(self, seniority_label):
        senioritylabel_attribs = self.get_join_filters["seniority_labels"]
        self.change_filter_to(name="seniority_labels", 
                              choice=seniority_label,
                              is_more=senioritylabel_attribs["is_more"])
        
        
    def change_company_to(self, company):
        company_attribs = self.get_join_filters["companies"]
        self.change_filter_to(name="companies", 
                              choice=company,
                              is_more=company_attribs["is_more"])
        
        
    def change_companysize_to(self, company_size):
        companysize_attribs = self.get_join_filters["company_sizes"]
        self.change_filter_to(name="company_sizes", 
                              choice=company_size,
                              is_more=companysize_attribs["is_more"])
        
        
    def easy_apply_work_home(self, is_eao, will_apply):
        self.click_more_dropdown()
        
        apply = self.get_filters_eaowfho(is_eao)
        btn = self.get_filters_eaowfho_label(is_eao, eaowfho=apply)
        if "applied" in apply.get_attribute("class"):
            if will_apply:
                pass
            elif not will_apply:
                btn.click()
        elif "applied" not in apply.get_attribute("class"):
            if will_apply:
                btn.click()
            elif not will_apply:
                pass
        
        self.click_more_dropdown()
        
        
    def change_rating_to(self, rating):  # Rating goes from 1-4.
        self.click_more_dropdown()
        
        ratings = self.get_filters_companyratings_stars_divs()
        
        ratings[rating - 1].click()
        
        self.click_more_dropdown()
        
        
    # The sort by dropdown seems to be a little bugged.
    # It changes the order of the job listings which implies that it works
    # yet the checkmark for the dropdown (there is a checkmark next to the user's selected dropdown
    # choice) stays on "Most Relevant" regardless of what option ("Most Relevant" or "Most Recent")
    # the user chooses. Additionally, it is unsure whether or not the actual dropdown button
    # should change when one selects "Most Relevant" or "Most Recent". That could possibly
    # be bugged too.
    # Note: since this "filter" isn't a part of the DKFilters tag, it will not follow
    # the general pipeline for DKFilters for flexibility.
    def sort_by(self, sort_type):
        sortby_filter = self.get_filters_sortby()
        sortby_filter.click()
        
        dropdown_ul_li = self.get_main_body_sortby_dropdown_ul_li()  
        ul_li_element = dropdown_ul_li[self.get_filters_by_type("sortbys").index(sort_type)]
        ul_li_element.click()
    
    
    
    # ==================================================
    # Webscraping Function.
    # ==================================================
    
    
    
    def scrape_jobs(self, n_jobs):
        # Gets the total number of pages.
        total_pages = int(self.get_page_count().text.split()[-1])
        page_counter = 1
        jobs = []
        
        while len(jobs) < n_jobs and page_counter <= total_pages:
            time.sleep(2)
            
            joblistings = self.get_joblistings()

            for joblisting in joblistings:
                if len(jobs) == n_jobs:
                    break
                
                joblisting.click()

                time.sleep(2)

                # Check if there is a pop-up.
                try:
                    close_popup_btn = self.close_popup()
                    close_popup_btn.click()
                except:
                    pass

                time.sleep(2)

                jobinfo = {}

                # Job Info I.
                jobinfo1 = self.get_jobinfo1()

                try:
                    company = jobinfo1[0].text
                except:
                    company = -1
                try:
                    job_title = jobinfo1[1].text
                except:
                    job_title = -1
                try:
                    headquarters = jobinfo1[2].text
                except:
                    headquarters = -1
                try:
                    salary_estimate = jobinfo1[3].text
                except:
                    salary_estimate = -1

                jobinfo1_features = {
                    "company": company,
                    "job title": job_title,
                    "headquarters": headquarters,
                    "salary estimate": salary_estimate
                }

                # Job Info II.
                jobinfo2 = self.get_jobinfo2()

                try:
                    job_type = jobinfo2[0].text
                except:
                    job_type = -1

                jobinfo2_features = {
                    "job type": job_type
                }

                # Job Info III.
                try:
                    jobinfo3 = self.get_jobinfo3()
                except:
                    pass

                jobinfo3_features = {
                    "size": -1,
                    "founded": -1,
                    "type": -1,
                    "industry": -1,
                    "sector": -1,
                    "revenue": -1
                }

                try:
                    # The text is a string, split by "\n", it will 
                    # be a list with every value an attribute and every other
                    # value corresponding to a value.
                    jobinfo3_features_updated = {}
                    features_list = jobinfo3.text.lower().split("\n")
                    for i in range(0, len(features_list)-1, 2):
                        jobinfo3_features_updated[features_list[i]] = features_list[i + 1]
                except:
                    pass

                jobinfo3_features.update(jobinfo3_features_updated)

                # Job Info IV.
                jobinfo4_features = {"job description": self.get_jobinfo4().text}

                for jobinfo_features in [jobinfo1_features, 
                                jobinfo2_features, 
                                jobinfo3_features, 
                                jobinfo4_features]:
                    jobinfo.update(jobinfo_features)

                jobs.append(jobinfo)
            
            if len(jobs) == n_jobs:
                break
            
            # Clicks the right arrow in the page navigator footer.
            try:
                page_nav_right_arrow = self.get_page_nav()[6]
                page_nav_right_arrow.click()
            except:
                pass
            
            page_counter += 1
            
        return pd.DataFrame(jobs)
    
