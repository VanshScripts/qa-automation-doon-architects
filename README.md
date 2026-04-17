# QA Automation – Doon Architects Website

## Overview

This project focuses on testing a production-level architecture website (https://doonarchitects.com) built using Next.js.  
The goal was to validate real user workflows such as lead generation (contact form) and hiring (careers module), while ensuring reliability across UI and backend interactions.

The project combines UI automation and API validation to simulate real-world usage scenarios.

---

## Tech Stack

- Python  
- Selenium WebDriver  
- pytest  
- requests (API testing)  

---

## What Was Tested

### End-to-End User Flows

- Contact form submission (lead generation flow)
- Careers/job application workflow (including resume upload)
- Navigation across key pages (Home, Services, Projects, Contact, Careers)

---

### UI & Functional Testing

- Form validations (required fields, incorrect inputs)
- Dropdown interactions (project type, experience selection)
- Multi-step workflows (job role → apply → form submission)
- Cross-page navigation and component rendering
- Responsive UI behavior and interaction flows

---

### Negative Scenarios

- Submitting forms with missing required fields
- Invalid email input handling
- Ensuring submission is blocked when validation fails

---

### API Validation

- Tested contact form API using Python requests and Postman
- Verified response status and basic data flow between frontend and backend

---

## Automation Framework Design

The framework follows the Page Object Model (POM) approach:

- Each page (e.g., ContactPage, CareersPage) is implemented as a separate class  
- Locators and actions are encapsulated inside page files  
- Test files focus only on test logic and workflows  

This structure improves readability, reusability, and maintainability.

---

## Key Challenges Handled

- Dynamic UI rendering in a Next.js application  
- Handling elements inside modals (careers application form)  
- Click interception issues due to layered UI components  
- File upload automation using Selenium  
- Synchronization issues with dynamic content (explicit waits used instead of static delays)  

---

## Project Structure
pages/ → Page Object classes
tests/ → Test cases (UI + API)
data/ → Test files (e.g., resume upload)
utils/ → Helper functions

## How to Run

```bash
pip install -r requirements.txt
pytest
