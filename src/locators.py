
from selenium.webdriver.common.by import By


class ConfigLocators:
    """ConfigLocators contains the locators for configuration i.e. filters.
    
    Locators are in uppercase because they are constants and are
    grouped by category. Categories are denoted by a comment and separated
    by two lines of whitespaces. A single line of whitespace denotes
    the subcategory within a category. 
    
    The categories are as follows:
    
        - Search bars.
        - Primary dropdown.
        - Main Filters.
        - "More" dropdown.
        - "More" filters.
        - "Most Relevant" filter.
        - Clear filters.
        
    Note: There are some redundant constant variables,
    however they are kept to provide better clarity.
    Previous long variable names have been changed
    to a shorter form:
    
        Examples:
        
            Before:
                FILTER_MINSALARY_INCLUDE_SALARY_CHECKBOX
            After:
                INCLUDE_SALARY_CHECKBOX
            
            Before:
                PRIMARY_DROPDOWN,
                PRIMARY_DROPDOWN_UL,
                PRIMARY_DROPDOWN_UL_LI
            After:
                PRIMARY_DROPDOWN,
                DROPDOWN_UL,
                UL_LI
          
    """
    
    # Search bars.
    KEYWORD_SEARCH = (By.ID, "sc.keyword")
    LOCATION_SEARCH = (By.ID, "sc.location")
    SEARCH_BUTTON = (By.CLASS_NAME, "SearchStyles__newSearchButton")
    
    
    # Primary dropdown (the dropdown currently open).
    PRIMARY_DROPDOWN = (By.ID, "PrimaryDropdown")
    DROPDOWN_UL = (By.CLASS_NAME, "css-wpidup")
    UL_LI = (By.TAG_NAME, "li")
    
    
    # Main filters (all filters except "More" filters and "Most Relevant").
    FILTER_JOBTYPE = (By.ID, "filter_jobType")
    FILTER_FROMAGE = (By.ID, "filter_fromAge")
    
    FILTER_MINSALARY = (By.ID, "filter_minSalary")
    INCLUDE_SALARY_CHECKBOX = (By.CLASS_NAME, "gd-ui-checkbox")
    CHECKBOX_LABEL = (By.TAG_NAME, "label")
    APPLY_BUTTON = (By.CLASS_NAME, "applybutton")
    HISTOGRAM = (By.CLASS_NAME, "histogramContainer")
    HISTOGRAM_DIVS = (By.TAG_NAME, "div")
    LEFT_SLIDER = (By.XPATH, "//div[@class='leftHandle']")
    HIST_LABEL = (By.ID, "salary-range-hist-label")
    HIST_LABEL_HEADER = (By.TAG_NAME, "h4")
    RIGHT_SLIDER = (By.XPATH, "//div[@class='rightHandle']")
    
    FILTER_RADIUS = (By.ID, "filter_radius")
    
    
    # The "More" dropdown.
    DKFILTERS = (By.ID, "DKFilters")
    FILTER_MORE = (By.CLASS_NAME, "ewzpq9a0")
    
    
    # Filters under the "More" dropdown.
    FILTER_CITYID = (By.ID, "filter_cityId")
    FILTER_INDUSTRYID = (By.ID, "filter_industryId")
    # EAO: Early Apply Only; WFHO: Work From Home Only
    FILTER_EAOWFHO = (By.CLASS_NAME, "justified")
    EAOWFHO_LABEL = (By.TAG_NAME, "label")
    
    FILTER_COMPANYRATING = (By.CLASS_NAME, "noHover")
    COMPANYRATING_STARS = (By.CLASS_NAME, "e1wcngjj1")
    STARS_DIVS = (By.TAG_NAME, "div")
    
    FILTER_JOBFUNCTIONS = (By.ID, "filter_sgocId")
    FILTER_SENIORITYLABELS = (By.ID, "filter_seniorityType")
    FILTER_COMPANIES = (By.ID, "filter_companyId")
    FILTER_COMPANYSIZES = (By.ID, "filter_employerSizes")
    
    
    # "Most Relevant" filter (a part of the mainCol but not DKFilters).
    MAIN_COL = (By.ID, "MainCol")
    BODY = (By.CLASS_NAME, "main")
    FILTER_MOSTRELEVANT = (By.CLASS_NAME, "css-150lexj")
    MOSTRELEVANT_DROPDOWN = (By.CLASS_NAME, "e1gtdke61")
    MOSTRELEVANT_DROPDOWN_UL = (By.TAG_NAME, "ul")
    UL_LI = (By.TAG_NAME, "li")
    
    
    # The Clear filters button.
    CLEAR_FILTERS = (By.CLASS_NAME, "clearFilters")
    CLEAR_FILTERS_SPAN = (By.TAG_NAME, "span")
    

class WebScrapingLocators:
    """WebScrapingLocators contains the locators for webscraping data.
    
    Refer to ConfigLocators for notation in this class.
    
    The categories are as follows:
    
        - Pop-up close button.
        - Joblistings list.
        - Page navigator.
        - Job Description column.
        - Try again button.
        - Job Info I.
        - Job Info II.
        - Job Info III.
        - Job Info IV.
        - Total page numbers.
    
    Note: The features for the dataset that will be returned
    from webscraping is split into 4 groups of features:
    job info 1, 2, 3, and 4. 
    
    """
    
    # Button to close pop-up.
    POPUP_CLOSE_BTN = (By.CLASS_NAME, "modal_closeIcon")
    
    
    # The joblistings list.
    MAIN_COL = (By.ID, "MainCol")
    JOBLISTING_CONTAINER = (By.TAG_NAME, "ul")
    JOBLISTINGS = (By.TAG_NAME, "li")
    
    
    # Page navigators at the bottom of the page.
    FOOTER_PAGE_NAV = (By.ID, "FooterPageNav")
    PAGES_CONTAINER = (By.XPATH, "//div[@class='middle']")
    PAGE_NAVS = (By.TAG_NAME, "li")
    
    
    # Job description column. 
    JD_COL = (By.ID, "JDCol")
    
    # Try again button for when a joblisting fails to show.
    TRY_AGAIN_DIV = (By.CLASS_NAME, "erj00if0")
    TRY_AGAIN_BTN = (By.TAG_NAME, "button")
    
    # Job Info I (company, rating, headquarters, salary est).
    HEADER = (By.CLASS_NAME, "e14vl8nk0")
    HEADER_JOB_INFO = (By.CLASS_NAME, "e1tk4kwz6")
    JOB_INFO_1 = (By.TAG_NAME, "div")
    
    # Job Info II (ratings, job type).
    JOB_INFO_2_CONTAINER = (By.CLASS_NAME, "epgue5a3")  # 2 classes correspond to this.
    JOB_INFO_2 = (By.TAG_NAME, "div")
    
    
    # Job Info III (size, founded date, type, industry, sector, revenue).
    EMP_BASIC_INFO = (By.ID, "EmpBasicInfo")
    COMP_OVERVIEW_CONTAINER = (By.CLASS_NAME, "flex-wrap")
    
    
    # Job Info IV (job description).
    JOB_DESC_CONTAINER = (By.ID, "JobDescriptionContainer")
    JOB_INFO_4 = (By.CLASS_NAME, "jobDescriptionContent")
    
    
    # Total page numbers.
    MAIN_COL = (By.ID, "MainCol")
    FOOTER = (By.CLASS_NAME, "tbl")
    PAGE_COUNT = (By.CLASS_NAME, "middle")
    
