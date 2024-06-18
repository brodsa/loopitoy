# Testing & Validation 
 
  - [Responsivness Testing](#responsivness-testing)
  - [Browser Compatibility Testing](#browser-compatibility-testing)
  - [User Stories Testing](#user-stories-testing)
  - [Features Testing (Manual Testing)](#feature-testing)
  - [Code Validation](#code-validation)
  - [Lighthouse Testing](#lighthouse)


## Responsiveness Testing
All pages were tested in terms of responsivness to ensure that the conent reacts on various screen size, ranging from 280px up to 1200px. To test the responsiveness the following devices were considered in addition to DevTools.
  - Dell Latitude (DevTool) 
  - iPhone 8 (iOS 16.5)
  - Samsung Galaxy A52




[Back to the content](#testing--validation)

## Browser Compatibility Testing
The website was tested on different browser (see the list below) to assure that features and responsiveness work accordingly.
- Safari
- Chrome
- Firefox
- Edge


## User Stories Testing
The testing was grouped according to the epics to which user story belongs.



[Back to the content](#testing--validation-report)

## Features Testing
The features testing was also conducted group-wise. The outcome and testing steps are described bellow in detail.



## Code Validation
The webpage was validated from several perspectives:
- the markup validity, see [HTML](#html).
- the css properties, see [CSS](#css).
- the web accessibility, see [Accessibility](#accessibility).
- the coding rules of the JavaScript source code, see [JavaScript](#javascript).
- the coding rules of Python source code, see [Python](#pep8).
- the more general quality of the webpage, see [Lighthouse](#lighthouse)


### HTML 
The [Nu Html Checker](https://validator.w3.org/nu/) web-based tool by W3 was used to validate the pages of the webpage. **The Checker did not reveal any errors.** The source code of pages requiring login was checked directly via text input. Other pages were tested via provided page URL. The detailed reports for each page are below:



### Javascript
The [JShint](https://jshint.com/) static tool was considered to check the code rules of the Javascript source code.

### CSS
The [jigsaw](https://jigsaw.w3.org/css-validator/) web-based tool by W3 was used to validate the CSS of the webpage. The core `base.css` file was directly uploaded on [the webpage](https://jigsaw.w3.org/css-validator/#validate_by_upload).


### PEP8
To validate the Python code in terms of PEP8, the [CI Python Linter](https://pep8ci.herokuapp.com/#) was used.

| Module | Python file               | Report | Results   |
|--------|---------------------------|--------|-----------|
|`findmereadme` | `urls.py`          | <img src="./docs/testing/python/python_findmereadme_urls.png" alt="findmereadme_urls" width="200"/> | no error |



### Accessibility
The [WAVE](https://wave.webaim.org/) web-based tool was considered for the evaluation of the web accessibility. For the pages required authentication chrome extension [WAVE Evaluation Tool](https://chromewebstore.google.com/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh) was used. In generally, the validation did not reveal any errors. Two alerts were noticed. A redundant link in navigation as there is a link to homepage attached to both logo and home. The home item and link was removed from the navigation menu. Second alert is related to the PDF link. To increase the accessibility an `arial-label` attribute is present. The detailed reports are below:

| Category | Page Report | Results |
|----------|-------------|---------|
| Homepage | [Home](https://wave.webaim.org/report#/https://findme-readme-10d0bfb3ba28.herokuapp.com/) | no errors


## Lighthouse
The Lighthouse in Chrome DevTools evaluates the webpage for performance, accessibility, best practices, and SEO. The pages with the main content were evaluated, meaning the pages with forms were not considered as they are produce mainly form The evaluation did not reveal any big issues. The detailed reports can be viewed at:

| Page            | Desktop | Mobile | 
|-------------------|--------|------------------|
| Home | <img src="./docs/testing/lighthouse/desktop_home.PNG" alt="desktop_home" width="200"/> | <img src="./docs/testing/lighthouse/mobile_home.PNG" alt="mobile_home" width="200"/> |

[Back to the content](#testing--validation-report)