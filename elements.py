
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import ConfigLocators as CL
from locators import WebScrapingLocators as WSL


# CL = ConfigLocators
# WSL = WebScrapingLocators


class ConfigElements:
    """ConfigElements is a class for getting all the elements related to 
    configuring the filters. 
    
    Syntax for Table of Contents:
    
    The easiest way to demonstrate this is through an example.
    
        Example:
        
            - Category

                - get element * 
                    > _
                    > obj1
                    > obj2
        
        The above example is equivalent to:
        
            - Category
            
                - get element
                - get element -> obj1
                - get element -> obj2
            
    Additionally, arrows are used to denote that a certain webdriver
    element is being found from the preceding webdriver element.
    
    
    Table of Contents:
    
    - Get Elements
    
        - WebDriverWait base function
        
        - Search-Related
        
            - get *
                > keyword search
                > location search
                > search button

        - Filter-Related
        
            - get primary dropdown *
                > _
                > ul
                > ul -> all li
                
            - get filter *
                > jobtype
                > fromage/postdate
                > radius
                
            - Filter Minsalary (salary range)
            
                - get filter minsalary *
                    > include no salary data
                    > apply button
                    
                - get primary dropdown *
                    > salary range histogram container -> all bins
                    > left slider
                    > right slider
                    
                - get histogram labels -> header
                
            - More Filter
                - get dkfilters *
                    > _
                    > more
                    > clear filter -> span
                
                - get filter *
                    > cityid
                    > industry
                    > eaowfho (Easy Apply Only, Work From Home Only)
                    > eaowfho -> label
                    > company rating -> stars -> all divs
                    > job functions
                    > seniority labels
                    > companies
                    > company sizes
                                
            - get main col *
                > _
                > sortby filter
                
            - get body *
                > _
                > sortby dropdown
                > sortby dropdown -> ul
                > sortby dropdown -> ul -> all li
            
            
    - Reusable Filter-Related Functions
        - clear search and return keyword
        - get GlassdoorWebScraper obj filters by filter type 
        - getting and parsing filters 
        
        - Join Filters Functions
            - join filters *
                > jobtype
                > fromage/postdate
                > radius
                > cityid
                > industry
                > job function
                > seniority label
                > company
                > company size
                > sortby
            
        - initialize salary bins
        - move slider function
        - click more dropdown n_clicks times
        - initialize a filter
        - change filter to function
        - initialize sortby filter
        - regex parse salary
        - reset salary base function
    
    """
    
    # Tunable parameter.
    seconds_before_timeout = 10
    
    
    
    # ==================================================
    # Get Element(s)
    # ==================================================
    
    
    
    def wait_until_element(self, locator, seconds_before_timeout=seconds_before_timeout):
        return WebDriverWait(self.driver, seconds_before_timeout).until(
                   EC.presence_of_element_located(locator)
               )
    
    
    
    # ===============================
    # Search-Related
    # ===============================
    
    
    
    def get_keyword_search(self):
        return self.wait_until_element(CL.KEYWORD_SEARCH)
    
    
    def get_location_search(self):
        return self.wait_until_element(CL.LOCATION_SEARCH)
    
    
    def get_search_button(self):
        return self.wait_until_element(CL.SEARCH_BUTTON)
    
    
    
    # _______________________________
    
    
    # ===============================
    # Filter-Related
    # ===============================
    
    
    
    def get_primary_dropdown(self):
        return self.wait_until_element(CL.PRIMARY_DROPDOWN)
    
    
    # Gets the primary dropdown -> ul.
    def get_dropdown_ul(self):
        primary_dropdown = self.get_primary_dropdown()
        return primary_dropdown.find_element(*CL.DROPDOWN_UL)
    
    
    # Gets the primary dropdown -> ul -> all li.
    def get_ul_all_li(self):
        dropdown_ul = self.get_dropdown_ul()
        return dropdown_ul.find_elements(*CL.UL_LI)
    

    def get_filters_jobtypes(self):
        return self.wait_until_element(CL.FILTER_JOBTYPE)
    
    
    def get_filters_postdates(self):
        return self.wait_until_element(CL.FILTER_FROMAGE)
    
    
    def get_filters_radii(self):
        return self.wait_until_element(CL.FILTER_RADIUS)
    
    
    
    # ==================
    # Filter Minsalary
    # ==================
    
    
    
    def get_filters_minsalaries(self):
        return self.wait_until_element(CL.FILTER_MINSALARY)
    
    
    # Gets the minsalary -> checkbox.
    def get_filters_minsalaries_checkbox(self):
        primary_dropdown = self.get_primary_dropdown()
        return primary_dropdown.find_element(*CL.INCLUDE_SALARY_CHECKBOX)
    
    
    # Gets the minsalary -> checkbox -> include no salary data label.
    def get_filters_minsalaries_checkbox_label(self):
        minsalaries_checkbox = self.get_filters_minsalaries_checkbox()
        return minsalaries_checkbox.find_element(*CL.CHECKBOX_LABEL)
        
    
    
    # Gets the minsalary -> apply button.
    def get_filters_minsalaries_applybutton(self):
        primary_dropdown = self.get_primary_dropdown()
        return primary_dropdown.find_element(*CL.APPLY_BUTTON)
    
    
    # Gets the minsalary -> histogram container -> all divs.
    def get_primary_dropdown_histogram_container_all_div(self):
        primary_dropdown = self.get_primary_dropdown()
        primary_dropdown_histogram = primary_dropdown.find_element(*CL.HISTOGRAM)
        return primary_dropdown_histogram.find_elements(*CL.HISTOGRAM_DIVS)
    
    
    # Gets the minsalary -> left slider.
    def get_left_slider(self):
        primary_dropdown = self.get_primary_dropdown()
        return primary_dropdown.find_element(*CL.LEFT_SLIDER)
    
    
    # Gets the minsalary -> right slider.
    def get_right_slider(self):
        primary_dropdown = self.get_primary_dropdown()
        return primary_dropdown.find_element(*CL.RIGHT_SLIDER)
        
    
    # Gets histogram labels header.
    def get_histogram_labels_header(self):
        histogram_labels = self.wait_until_element(CL.HIST_LABEL)
        return histogram_labels.find_element(*CL.HIST_LABEL_HEADER)
        
        
        
    # __________________
    
    
    
    # ==================
    # More Filter
    # ==================
    
    
    
    def get_entire_filter(self):
        return self.wait_until_element(CL.DKFILTERS)
    
    
    def get_more_dropdown(self):
        DKFilters = self.get_entire_filter()
        return DKFilters.find_element(*CL.FILTER_MORE)
    
    
    # Gets DKFilters -> clear filter -> span.
    def get_clear_filter_span(self):
        DKFilters = self.get_entire_filter()
        clear_filter = DKFilters.find_element(*CL.CLEAR_FILTERS)
        return clear_filter.find_element(*CL.CLEAR_FILTERS_SPAN)
    
    
    def get_filters_cityids(self):
        return self.wait_until_element(CL.FILTER_CITYID)
    
    
    def get_filters_industries(self):
        return self.wait_until_element(CL.FILTER_INDUSTRYID)
    
    
    def get_filters_eaowfho(self, is_eao):
        eaowfho = self.driver.find_elements(*CL.FILTER_EAOWFHO)
        if is_eao:
            return eaowfho[0]
        return eaowfho[1]
    
    
    # Gets the EAO or WFHO filter's -> label.
    def get_filters_eaowfho_label(self, is_eao, eaowfho=None):
        if not eaowfho:
            eaowfho = self.get_filters_eaowfho(is_eao)
        return eaowfho.find_element(*CL.EAOWFHO_LABEL)
    
    
    # Gets the company rating filter -> stars -> all divs. 
    def get_filters_companyratings_stars_divs(self):
        companyratings = self.wait_until_element(CL.FILTER_COMPANYRATING)
        companyratings_stars = companyratings.find_element(*CL.COMPANYRATING_STARS)
        return companyratings_stars.find_elements(*CL.STARS_DIVS)


    def get_filters_jobfunctions(self):
        return self.wait_until_element(CL.FILTER_JOBFUNCTIONS)
    
    
    def get_filters_senioritylabels(self):
        return self.wait_until_element(CL.FILTER_SENIORITYLABELS)
    
    
    def get_filters_companies(self):
        return self.wait_until_element(CL.FILTER_COMPANIES)
    
    
    def get_filters_companysizes(self):
        return self.wait_until_element(CL.FILTER_COMPANYSIZES)
    

    
    # __________________

    
    
    def get_main_col(self):
        return self.wait_until_element(CL.MAIN_COL)
    
    
    # Gets the main col -> sortby filter.
    def get_filters_sortby(self):
        main_col = self.get_main_col()
        return main_col.find_element(*CL.FILTER_MOSTRELEVANT)
    
    
    def get_main_body(self):
        return self.wait_until_element(CL.BODY)
    
    
    # Gets the main body -> sortby dropdown.
    def get_main_body_sortby_dropdown(self):
        main_body = self.get_main_body()
        return main_body.find_element(*CL.MOSTRELEVANT_DROPDOWN)
    
    
    # Gets the main body -> sortby dropdown -> ul.
    def get_main_body_sortby_dropdown_ul(self):
        sortby_dropdown = self.get_main_body_sortby_dropdown()
        return sortby_dropdown.find_element(*CL.MOSTRELEVANT_DROPDOWN_UL)
    
    
    # Gets the main body -> sortby dropdown -> ul -> all li.
    def get_main_body_sortby_dropdown_ul_li(self):
        sortby_dropdown_ul = self.get_main_body_sortby_dropdown_ul()
        return sortby_dropdown_ul.find_elements(*CL.UL_LI)
    
    
    
    # _______________________________
    
    
    
    # __________________________________________________
    
    
    
    # ==================================================
    # Reusable Filter-Related Functions
    # ==================================================
    
    
    
    # Clear a search bar and return a keyword.
    def clear_and_search(self, search, keyword):
        search.clear()
        search.send_keys(keyword)
        search.send_keys(Keys.RETURN)    
    
    
    # Accesses the self.filters dictionary by key "filter_type"
    # and returns a list of keys (if the corresponding value to "filter_type"
    # is a dict), else it returns a list.
    def get_filters_by_type(self, filter_type):
        filters_by_type = self.filters[filter_type]
        if isinstance(filters_by_type, dict):
            return list(filters_by_type.keys())
        return filters_by_type
    
    
    # Note: get_and_parse_filters applies only to filters in the 
    # self.get_join_filters attribute.
    def get_and_parse_filters(self, filter_type_list, join_filters):
        """Gets filter text and parses it; then, it calls a join_filters function.
        
        Parameters
        ----------
        filter_type_list : str
            A string that contains all the possible filter options for a given filter
            in an unparsed manner. A filter option is defined as: jobtype/full_time where
            "full_time" is a filter option of the filter "jobtype". 
        join_filters : fn
            A function for a filter that will perform the concatenation
            of strings at the end of this get_and_parse_filters() method. This function
            varies depending on what special characters exist in the unparsed string
            "filter_type_list" and also on whether or not the filter options for a 
            filter will have counts.
            
        Returns
        -------
        type
            Returns a dict or a list.
        describe : dict or list
            If the filter options for a filter
            contains counts a dict is returned (where the parsed 
            filter options are keys and the values are the counts) 
            else it will return a list of the parsed filter options.
        
        Examples
        --------
        input : "Full-time (4722)\nPart-time (482)"
        output : {"full_time": 4722, "part_time": 482}
        
        input : "5 Miles\n10 Miles"
        output : ["5_miles", "10_miles"]

        """
        # Checks if there is at least one occurrence of the format:
        # a-zA-Z0-9 (0-9).
        # This search returns an re obj if it finds a match.
        check_for_count = re.search(r"\w+ \((\d+)\)", filter_type_list)
        
        # If there is no match for the aforementioned format,
        # then simply call the join_filters() function on the 
        # filter_type_list.
        if not check_for_count:
            return join_filters(filter_type_list)
        
        # At this point, there exists an re,
        # and group(1) is checked to see
        # if there is a count in the string "filter_type_list".
        elif check_for_count.group(1):
            filters, filters_counts = [], []
            
            for idx, filter_ in enumerate(filter_type_list.split("\n")):
                filter_split = filter_.split()
                
                # If 0.
                if not idx:
                    
                    # Since filter options come in a specified order,
                    # the first filter option is always the default
                    # and contains no count. Here, it is simply appended
                    # to list "filters". 
                    filters.append(filter_split)
                    
                # Idx != 0.
                else:
                    
                    # Append just the text portion.
                    filters.append(filter_split[:-1])
                    
                    # Strips parentheses from the number and appends
                    # to the list "filters_counts".
                    filters_counts.append(int(re.sub("[()]", "", filter_split[-1]).strip()))
                    
            # Since the default filter option is always the total,
            # the sum of all filter option counts are summed 
            # and inserted at index 0.
            filters_counts.insert(0, sum(filters_counts))
            return join_filters(filters, filters_counts)
    
    
    
    # ===============================
    # Join Filters Functions
    # ===============================
    
    
    
    def join_filters_jobtypes(self, jobtypes, jobtypes_counts):
        for idx, jobtype in enumerate(jobtypes):
            jobtypes[idx] = re.sub("-", "_", "_".join(jobtype).lower())
        return dict(zip(jobtypes, jobtypes_counts))
    
    
    def join_filters_postdates(self, postdates, postdates_counts):
        for idx, postdate in enumerate(postdates):
            postdates[idx] = "_".join(postdate).lower()
        return dict(zip(postdates, postdates_counts))
    
    
    def join_filters_radii(self, radius):
        return radius.lower().replace(" ", "_").split("\n")
    
    
    def join_filters_cityids(self, cityids, cityids_counts):
        for idx, cityid in enumerate(cityids):
            cityids[idx] = "_".join(cityid).lower().replace(",", "")
        return dict(zip(cityids, cityids_counts))
    
    
    def join_filters_industries(self, industries, industries_counts):
        for idx, industry in enumerate(industries):
            industries[idx] = "_".join(industry).lower()
        return dict(zip(industries, industries_counts))
    
    
    def join_filters_jobfunctions(self, jobfunctions, jobfunctions_counts):
        for idx, jobfunction in enumerate(jobfunctions):
            jobfunctions[idx] = "_".join(jobfunction).lower()
        return dict(zip(jobfunctions, jobfunctions_counts))
    
    
    def join_filters_senioritylabels(self, senioritylabels, senioritylabels_counts):
        for idx, senioritylabel in enumerate(senioritylabels):
            senioritylabels[idx] = "_".join(senioritylabel).lower()
        return dict(zip(senioritylabels, senioritylabels_counts))
    
    
    def join_filters_companies(self, companies, companies_counts):
        for idx, company in enumerate(companies):
            companies[idx] = "_".join(company).lower()
        return dict(zip(companies, companies_counts))
    
    
    def join_filters_companysizes(self, companysizes, companysizes_counts):
        for idx, companysize in enumerate(companysizes):
            companysizes[idx] = ("_"
                                 .join(companysize)
                                 .lower()
                                 .replace("-", "_")
                                 .replace("+", ""))
        return dict(zip(companysizes, companysizes_counts))
    
    
    # Join filters function for sortby (not used in the regular filter pipeline).
    def join_filters_sortby(self, sortbys):
        return sortbys.lower().replace(" ", "_").split("\n")
    
    
    
    # _______________________________
    
    
    
    # Initializes the possible salary bins for filter minsalary.
    def initialize_salary_bins(self):
        # Glassdoor.com seems to have different salary ranges 
        # each time the job page is loaded in. To compensate,
        # the apply button under the salary filter is clicked
        # so that the correct salary ranges are displayed.
        salary_filter_applybutton = self.get_filters_minsalaries_applybutton()
        salary_filter_applybutton.click()
        
        print("BEFORE RESET")
        
        time.sleep(1)
        self.reset_salary_slider()
        time.sleep(1)
        
        print("AFTER RESET")
        
        salary_filter = self.get_filters_minsalaries()
        salary_filter.click()
        
#         left_slider = self.get_left_slider()
#         left_slider.click()
#         left_slider.click()
#         right_slider = self.get_right_slider()
#         right_slider.click()
#         right_slider.click()
        
        # Get all histogram bins into a list.
        histogram_bins = self.get_primary_dropdown_histogram_container_all_div()
        
        # Click the left slider first.
        left_slider = self.get_left_slider()
        left_slider.click()
        
        time.sleep(1)
        
        print("A")
        
        all_bins = []
        for idx, _ in enumerate(range(len(histogram_bins) - 1)):
            if not idx:
                
                # If 0, move the slider left first before
                # doing anything else because 
                # moving the left slider right immediately 
                # after clicking the left slider would move 
                # it to the far right.
                left_slider.send_keys(Keys.ARROW_LEFT)
                
            # Get the current salary range and regex parse it.
            a_bin = self.get_histogram_labels_header()
            a_bin = a_bin.text.replace("$", "").split("-")
            
            # Append the lower endpoint of the salary range.
            all_bins.append(a_bin[0])
            
            # Move once to the right to update the lower
            # endpoint of the salary range.
            left_slider.send_keys(Keys.ARROW_RIGHT)
            
        print("B")
            
        # Finally, add the endpointt of the last salary range
        # and close the filter and return all bins for 
        # the left and right slider bins.
        all_bins.append(a_bin[1])
        salary_filter.click()
        
        print("C")
        
        # If [a, b] is the largest possible salary range,
        # then the left slider can access values from
        # index(a) to index(b - 1) and the right slider
        # can access values from index(a + 1) to
        # index(b) inclusive of the endpoint.
        left_slider_bins = all_bins[:-1]
        right_slider_bins = all_bins[1:]
        return left_slider_bins, right_slider_bins
    
    
    # Moves left and right sliders for filter minsalary.
    def move_slider(self, slider, idx, current_idx, difference):
        if idx < current_idx:
            for _ in range(difference):
                slider.send_keys(Keys.ARROW_LEFT)
        elif idx > current_idx:
            for _ in range(difference):
                slider.send_keys(Keys.ARROW_RIGHT)
    
    
    # Because the more dropdown filters don't close properly, this small
    # function is aimed at simply closing that dropdown.
    # It also doubles as a more dropdown clicker, as it takes an
    # n_clicks argument.
    def click_more_dropdown(self, n_clicks=1):
        more_filter = self.get_more_dropdown()
        for _ in range(n_clicks):
            more_filter.click()
        
    
    # Note: init_filter works for only filters in the 
    # self.get_join_filters attribute.
    def init_filter(self, 
                    name, 
                    get_filters_, 
                    join_filters_=None,
                    is_salary=False,
                    is_more=False):
        """This function initializes a single filter. 
        
        Parameters
        ----------
        name : str
            Name of the filter.
        get_filters_ : fn
            The function that gets a certain filter.
        join_filters_ : fn, optional
            The join function for a certain filter. 
            This is optional as some filters don't use a join filters function
            like salary range.
        is_salary : bool
            True if the filter passed in is the salary range filter (it
            is a special filter that requires special initialization).
        is_more : bool
            True if the filter is under the "More" dropdown.
            
        Returns
        -------
        type
            NoneType
        describe
            This function simply initializes all filter options and doesn't
            return anything.
        """
        try:
            
            # First checks if it is_salary.
            if not is_salary:
                
                # If it is_more, then the more dropdown is clicked
                # and a JS script is called.
                if is_more:
                    self.click_more_dropdown()

                _filter = get_filters_()
                if not is_more:
                    _filter.click()
                elif is_more:
                    self.driver.execute_script("arguments[0].click();", _filter) 

                _dropdown_ul = self.get_dropdown_ul()
                self.filters[name] = self.get_and_parse_filters(_dropdown_ul.text,
                                                            join_filters_)
                
                # If is_more, then double click the more dropdown 
                # to ensure whatever dropdown might be left open
                # to be closed.
                if not is_more:
                    _filter.click()
                elif is_more:
                    self.click_more_dropdown(n_clicks=2)
                    
            # Special initialization for is_salary.
            elif is_salary:
                print("ENTER ELIF")
                self.filters[name] = {}
                salary_filter = get_filters_()
                salary_filter.click()
                print("CLICKED FILTER")
                left_slider_bins, right_slider_bins = self.initialize_salary_bins()
                self.filters[name]["left_slider"] = left_slider_bins
                self.filters[name]["right_slider"] = right_slider_bins
                print("INITIALIZED SALARY")
                
        # Glassdoor.com occassionally might exclude a filter or two 
        # from the "More" dropdown. This except block catches it and 
        # simply prints the exception.
        except Exception as e:
            print("init_filter is not working.")
            print(e)
        
    
    # Changes a filter option to.
    # Note: change_filter_to only applies to filters
    # in the self.get_join_filters attribute.
    def change_filter_to(self, name, choice, is_more=False):
        try:
            if is_more:
                self.click_more_dropdown()
            
            _filter = self.get_join_filters[name]["get"]
            if not is_more:
                _filter().click()
            elif is_more:
                self.driver.execute_script("arguments[0].click();", _filter()) 
                
            dropdown_ul_li = self.get_ul_all_li()
            ul_li_element = dropdown_ul_li[self.get_filters_by_type(name).index(choice)]
            ul_li_element.click()
            
            if is_more:
                self.click_more_dropdown(n_clicks=2)
        except Exception as e:
            print(e)
    
    
    # Initialize the "Most Relevant" dropdown "filter".
    # This one is under the main body of the page rather than the 
    # main group of filters and thus it is initialized separately
    # as it is not necessarily a filter.
    def init_sortby(self):
        sortby_filter = self.get_filters_sortby()
        sortby_filter.click()
        sortby_dropdown_ul = self.get_main_body_sortby_dropdown_ul()
        self.filters["sortbys"] = self.join_filters_sortby(sortby_dropdown_ul.text)
        self.click_more_dropdown(n_clicks=2)
    
    
    def regex_parse_salary(self, header):
                return header.text.replace("$", "").split("-")
        
        
    def reset_salary_base_fn(self, slider, idx, key_fn, is_both=False):
        # Given the salary dropdown is open.
        slider.click()
        a_bin = self.get_histogram_labels_header()
        a_bin = self.regex_parse_salary(a_bin)
        
        # Basically, keep a moving variable
        # one trails the other and the loop
        # breaks if the 2 variables are equal to each other 
        # meaning the end of the salary range has been hit by that
        # specific slider.
        before = a_bin[idx]
        slider.click()
        slider.send_keys(key_fn)
        current = self.regex_parse_salary(self.get_histogram_labels_header())[idx]
        while current != before:
            before = current
            slider.send_keys(key_fn)
            current = self.regex_parse_salary(self.get_histogram_labels_header())[idx]
        if not is_both:
            applybutton = self.get_filters_minsalaries_applybutton()
            applybutton.click()
    
    # __________________________________________________

    
    
class WebScrapingElements:
    """WebScrapingElements is a class for getting all the elements related to 
    webscraping the job listing data.
    
    Refer to ConfigElements for syntax in the table of contents.
    
    Table of Contents:
    
    - Wait Base Function
    
    - Pop-up
        
        - pop-up close button
        
    - Get Joblistings
    
        - get joblistings list
        - page navigator
        - get page count
        
    - Get Job Info
    
        - get jdcol
        - get job info *
            > 1
            > 2
            > 3
            > 4
    
    """
    
    seconds_before_timeout = 5
    
    def wait_until_element(self, locator, seconds_before_timeout=seconds_before_timeout):
        return WebDriverWait(self.driver, seconds_before_timeout).until(
                EC.presence_of_element_located(locator)
            )
    
    # ==================================================
    # Pop-up
    # ==================================================
    
    
    
    def close_popup(self):
        return self.wait_until_element(WSL.POPUP_CLOSE_BTN)
        
        
    # __________________________________________________
    
    
    
    # ==================================================
    # Get Joblistings
    # ==================================================
    
    
    
    def get_joblistings(self):
        main_col = self.wait_until_element(WSL.MAIN_COL)
        joblisting_container = main_col.find_element(*WSL.JOBLISTING_CONTAINER)
        return joblisting_container.find_elements(*WSL.JOBLISTINGS)
    
    
    def get_page_nav(self):
        footer_page_nav = self.wait_until_element(WSL.FOOTER_PAGE_NAV)
        pages_container = footer_page_nav.find_element(*WSL.PAGES_CONTAINER)
        return pages_container.find_elements(*WSL.PAGE_NAVS)

    
    def get_page_count(self):
        main_col = self.wait_until_element(WSL.MAIN_COL)
        footer = main_col.find_element(*WSL.FOOTER)
        return footer.find_element(*WSL.PAGE_COUNT)

    
    
    # __________________________________________________
    
    
    
    # ==================================================
    # Get Job Info
    # ==================================================
    
    
    
    def get_jdcol(self):
        return self.wait_until_element(WSL.JD_COL)
    
    
    def get_jobinfo1(self):
        jd_col = self.get_jdcol()
        header = jd_col.find_element(*WSL.HEADER)
        header_job_info = header.find_element(*WSL.HEADER_JOB_INFO)
        return header_job_info.find_elements(*WSL.JOB_INFO_1)
    
    
    def get_jobinfo2(self, is_insights=True):  # Get company insights or ratings.
        jd_col = self.get_jdcol()
        job_info_2_containers = jd_col.find_elements(*WSL.JOB_INFO_2_CONTAINER)
        if is_insights:
            return job_info_2_containers[1].find_elements(*WSL.JOB_INFO_2)
        return job_info_2_containers[0].find_elements(*WSL.JOB_INFO_2)
    
    
    def get_jobinfo3(self):
        emp_basic_info = self.wait_until_element(WSL.EMP_BASIC_INFO)
        return emp_basic_info.find_element(*WSL.COMP_OVERVIEW_CONTAINER)
    
    
    def get_jobinfo4(self):
        job_desc_container = self.wait_until_element(WSL.JOB_DESC_CONTAINER)
        return job_desc_container.find_element(*WSL.JOB_INFO_4)
    
    
        
    # __________________________________________________
    
