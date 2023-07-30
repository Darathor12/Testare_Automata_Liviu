# Selenium Library

Selenium is a free and open-source software testing framework that allows you to automate web browsers. 
It is designed to automate testing of web applications across different platforms and browsers. 
Selenium is built on top of WebDriver, which is a browser automation API. 
Selenium provides a variety of features for testing web applications, including:

1. **Synchronization** with the browser: Selenium can wait for elements to appear on the page, or for actions to complete.
2. **Locators**: Selenium provides a number of ways to identify elements on a web page, such as by id, name, or class.
3. **Actions**: Selenium can perform a variety of actions on elements, such as clicking on a link, entering text into a field, or submitting a form.
4. **Assertions**: Selenium can verify that the web page is in the expected state, such as checking that a particular element is displayed or that a particular text is present.

Selenium is a powerful tool that can be used to automate a wide range of web testing tasks. It is easy to use and can be integrated with a variety of other testing tools. Selenium is a valuable tool for any QA professional who wants to automate their web testing.


## What Selenium does:

Selenium is a web automation framework. It allows you to programmatically simulate user interactions with webpages. This means you can:

**1. Open web browsers:**

The first step is to launch the browser you want to automate. For example, to launch Chrome:

```text
from selenium import webdriver

driver = webdriver.Chrome()
```
This will launch a Chrome browser controlled by Selenium. Similarly, you can launch Firefox, Edge, Safari, etc.

**2. Navigate to websites**

Once you have a browser launched, you can navigate to web pages. For example:

```text
driver.get("https://google.com")
```

This will open Google's homepage in the Chrome browser. You can then navigate to other pages using:

```text
driver.get("https://facebook.com")
```

**3. Find HTML elements on pages (like text boxes, buttons, links, etc.)**

To interact with elements on the page, you first need to locate them. You can locate elements using:

```text
ID: driver.find_element_by_id("id")
Name: driver.find_element_by_name("name")
Class: driver.find_element_by_class_name("class")
Tag: driver.find_element_by_tag_name("tag")
XPath: driver.find_element_by_xpath("//xpath")
```
For example:

```text
search_box = driver.find_element_by_name("q")
```

**4. Interact with those elements (click, type text, submit forms, etc.)**

Once you have an element, you can interact with it using:

```text
.send_keys("text") to enter text
.click() to click
.clear() to clear text
```
For example:

```text
search_box.send_keys("Selenium Python")
search_box.submit()
```
This will search for "Selenium Python" on Google.

You can also locate and interact with buttons, links, dropdowns, radio buttons, checkboxes, etc.

**5. Wait for elements and pages to load**

Here's how you can wait for elements and pages to load in Selenium:

**Using `time.sleep()` - This is the simplest option:**
```text
time.sleep(5) # Waits for 5 seconds
```
But this is not ideal since the wait time is fixed. The page may load earlier or later.

**Using `WebDriverWait()` - This waits for a certain condition to be met:**

```text
wait = WebDriverWait(driver, 10)

element = wait.until(EC.presence_of_element_located((By.ID, "someid")))
```

Here we waited up to 10 seconds for an element with id `someid` to be present.

We can use other expected conditions too like:

  - `title_is` : Waits until the title of the page matches the expected title.
```text
wait = WebDriverWait(driver, 10)

wait.until(EC.title_is("Expected Title"))
```
This will wait up to 10 seconds for the page title to become "Expected Title".

  - `text_to_be_present_in_element`: Waits until the specified text is present in the specified element.
```text
element = wait.until(EC.text_to_be_present_in_element((By.ID, "someid"), "Some text"))
```
This will wait until the element with id "someid" contains the text "Some text".

  - `visibility_of_element_located`: Waits until the element is visible.
```text
element = wait.until(EC.visibility_of_element_located((By.ID, "someid")))
```
This will wait until the element with id "someid" is visible (shown on the page).

**6. Run tests in an automated fashion**

```text
To be continued...
```

In short, Selenium allows you to control a browser from your Python code. You can treat a browser like any other Python object.

## How it works:

Selenium uses a browser driver to communicate with the browser. A browser driver is basically software that translates commands from Selenium into browser actions. Selenium supports these drivers:

- ChromeDriver (for Chrome browser)
- GeckoDriver (for Firefox)
- EdgeDriver (for Edge browser)
- IEDriverServer (for Internet Explorer)
- SafariDriver (for Safari)

When you import Selenium and initialize a driver, Selenium starts controlling that browser, then when you execute Selenium commands, the browser driver translates those into actual browser actions.

## Common uses of Selenium:

**Web testing**: You can automate test cases that validate different parts of a website. Selenium makes it easy to repeatedly run the same tests.

**Web scraping**: Web scraping is the process of automatically extracting data from websites. It involves parsing HTML, extracting relevant data, and saving it for later use. Using Selenium, you can scrape data from dynamic websites.

**Automating repetitive web tasks**: Log into web apps, fill out forms, click through workflows, etc. Useful for demo, testing and maintenance tasks.


**Here is a simple Selenium Python test that automates login:**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Install ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://example.com/login")

# Find username field     
username = driver.find_element(By.ID, "username")

# Enter username      
username.send_keys("myusername")

# Find password field
password = driver.find_element(By.ID, "password")

# Enter password
password.send_keys("mypassword")  

# Find login button   
login_button = driver.find_element(By.ID, "login-btn")

# Click login button
login_button.click()

# Check if login successful    
if "Welcome" in driver.title:
    print("Login successful!")
else:
    print("Login failed!")

driver.quit()
```

**This test does the following:**

- Installs ChromeDriver version 
- Launches Chrome browser
- Navigates to login page
- Finds username and password fields by ID
- Enters username and password
- Finds login button by ID
- Clicks login button
- Checks if login was successful by looking for "Welcome" in the title
- Quits the browser

**The main steps are:**

- Launch browser
- Navigate to page
- Find elements
- Interact with elements
- Assert result
- Quit browser