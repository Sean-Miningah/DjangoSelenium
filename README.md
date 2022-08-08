# Django with Selenium 
## Table of Contents
1. [Introduction](#introduction)
2. [Some paragraph](#subparagraph1)
   1. [Sub paragraph](#subparagraph1)
3. [What are we doing with all these tests?](#paragraph2)
4. [Saving User Input](#chapter5)
5. [Improving Functional Tests](#chapter6)

### This is the introduction <a name="introduction"></a>
Some introduction text, formatted in heading 2 style

### Some paragraph <a name="paragraph1"></a>
The first paragraph text

#### Sub paragraph <a name="subparagraph1"></a>
This is a sub-paragraph, formatted in heading 3 style

### What are we doing with all these tests? <a name="paragraph2"></a>
Instead of manually  creating an HttpRequest object and calling the view function directly, we call 
```python

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
```
The function allows us to check what template was used to render a response 
##### The Test Driven Development Process
The overall process is 
* Write a test
* Run the test.Does it pass? 
* If pass does it need refactoring
* If no respectively and yes write minimal code 

### Saving User Input: Testing the Database <a name="chapter5"></a>

When a functional test fails with an unexpected failure, there are several things we can do to debug it: 
* Add print statements, to show, for example, what the current page text is. 
* Improve the error message to show more info about the current state
* Manually visit the site yourself
* Use __time.sleep__ to pause the test during execution
##### Status Codes
__302 Found__ indicates that the resource requested has been temporarily moved to the URL given by the __location__ 
header. A browser redirects to this page. 
##### Useful __TDD__ Concepts
* __Regression__
When new code breaks some aspect of the application which used to work.
* __Unexpected failure__
When a test fails in a way we weren't expecting. This either means that we've made a mistake in our tests,or that the
tests have helped us find a regression, and we need to fix something in our code. 
* __Red/Green/Refactor__
Another way of describing the __TDD__ process. Write a test and see if fail(Red), write some code to get it to pass
(Green), then Refactor to improve the implementation.
* __Triangulation__
Adding a test case with a new specific example for something existing code, to jusfity generalising the implementation
(which may be a "cheat" until that point)
* __Three strikes and refactor__
A rule of thumb for when to remove duplication form code. When two pieces of code look very similar, it often pays to
wait until you see a third use case, so that you are more sure about what part of the code really is the common, re-usable part
* __The scratchpad to-do list__
A place to write down things that occur to us as we're coding, so that we can finish up what we're doing and come back to them later

### Improving Functional Tests <a name="chapter6"></a>
To run the functional test
```python
python manage.py test functional_tests
```
To run the unit test
```python
python manage.py test lists
```