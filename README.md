# Restaurant Booking System

## 1. Project Overview

### 1.1 Project Objective

The **Restaurant Booking System** (also known as *Our Restaurant*) is a full-stack Django web application that allows users to view the restaurant menu, book a table, manage their reservations, and contact the restaurant. The project was built to simplify table reservations while maintaining a clean and responsive interface for users, and an efficient backend for admins.

The application also includes admin-facing functionality via the Django admin panel, where restaurant staff can manage tables, reservations, and menu items. The goal was to build a user-friendly but scalable solution suitable for small-to-medium restaurants.

![Home Page responsive](static\images\screenshots\responsive.png)

### 1.2 Target Audience

- **New visitors** who want to explore the restaurant menu, check the ambiance, and find contact information or directions.
- **Returning customers** looking to log in and manage their bookings.
- **Restaurant staff or admin users** responsible for managing daily reservations and menu updates through a secure backend.

### 1.3 User Stories

| **User Type** | **User Story** | **Acceptance Criteria** |
|--------------|----------------|--------------------------|
| Customer | I want to book a table for a specific date/time, so that I can dine at the restaurant. | The booking form must support date, time, and number of guests. A confirmation should be displayed and saved to the database. |
| Customer | I don’t want my slot to be taken once I’ve booked it, to avoid confusion or overbooking. | The system checks table availability before confirming. If no availability, a message prompts the user to choose another time. |
| Customer | I want to cancel a reservation so I can change plans. | A cancellation confirmation appears. The slot becomes available again. Booking is removed from the user’s list. |
| Customer | I want to see the restaurant menu before booking. | Menu is categorized and publicly viewable. Admins can update items anytime. |
| Admin | I want to manage table occupancies efficiently. | Tables are defined by number and size. The system auto-assigns tables based on party size. Admins can edit via the panel. |
| Admin | I want to view all upcoming bookings to plan service. | Bookings are sortable by date/time and searchable. Admin can edit or delete as needed. |

![GitHub User Stories](static\images\screenshots\userstories.png)


**Live Site**: https://restaurant-booking-system-001-81d0f1b38ae2.herokuapp.com/  
**Repository**: https://github.com/GeorgeBarh/restaurant-booking-system-project

---

## Table of Contents

1. [Project Overview](#1-project-overview)  
   1.1 [Project Objective](#11-project-objective)  
   1.2 [Target Audience](#12-target-audience)  
   1.3 [User Stories](#13-user-stories)  

2. [Features](#2-features)  
   2.1 [Core Features](#21-core-features)  
   2.2 [Additional Features](#22-additional-features)  

3. [Design](#3-design)  
   3.1 [UX/UI Strategy](#31-uxui-strategy)  
   3.2 [Wireframes](#32-wireframes)  
   3.3 [Color Scheme & Typography](#33-color-scheme--typography)  

4. [Agile Methodology](#4-agile-methodology)  
   4.1 [Planning Approach](#41-planning-approach)  
   4.2 [MoSCoW Prioritization](#42-moscow-prioritization)  
   4.3 [Sprint & Task Board](#43-sprint--task-board)  

5. [Technologies Used](#5-technologies-used)  

6. [Testing](#6-testing)  
   6.1 [Manual Testing](#61-manual-testing)  
   6.2 [Automated Testing](#62-automated-testing)  
   6.3 [Validators & Lighthouse](#63-validators--lighthouse)  
   6.4 [Bugs & Fixes](#64-bugs--fixes)  

7. [Deployment](#7-deployment)  
   7.1 [Deployment to Heroku](#71-deployment-to-heroku)  
   7.2 [Environment Variables](#73-environment-variables)  

8. [Database Schema](#8-database-schema)  

9. [Responsive Design](#9-responsive-design)  

10. [Future Enhancements](#10-future-enhancements)  

11. [Credits](#11-credits)  
   11.1 [Content & Code](#111-content--code)  
   11.2 [Media & Assets](#112-media--assets)  

12. [Acknowledgements](#12-acknowledgements)  

---

## 2. Features

This project has gone through multiple iterations and refinements to make sure both the customer and the restaurant staff have the tools they need. While the interface stays clean and friendly, there’s a good amount of logic happening behind the scenes to prevent booking conflicts, keep data secure, and provide clear user feedback.

### 2.1 Core Features

#### Navigation & Layout

- Every page uses a shared responsive navigation bar that works well on desktops and mobile devices.
- The nav includes links to key pages: Home, Menu, Book a Table, Contact, and (when logged in) My Bookings.
- The navbar collapses into a mobile menu on smaller devices, which helps usability.
- A universal footer includes contact info, social icons, opening hours, and stays consistent throughout.

 ![Nav-bar](static/images/screenshots/nav-bar.png)



#### Menu Display

- Menu items are managed in the database and displayed to users grouped by categories (e.g. Starters, Mains, Vegan, etc.).
- The page supports category filtering using links that apply GET parameters, without full page reload.
- Pagination is built-in so the menu remains clean even with many dishes — 6 per page.
- Only available items are shown to users — the admin can toggle visibility through the admin panel.

 ![Menu page ]( static/images/screenshots/menu.png  )

#### Booking System

- The booking form includes smart inputs: calendar for date, dropdown for time, and guest count selector.
- Optional “notes” field allows customers to leave custom requests (e.g. “table near the window”).
- The system checks if there’s an available table that fits the group size and chosen time — if not, it tells the user politely to try another slot.
- If all is valid, the booking is saved and a success message appears right away.

 ![ Book a table page ]( static\images\screenshots\booking.png )

#### Manage Bookings (CRUD)

- Logged-in users can access a "My Bookings" page showing their upcoming and past reservations.
- Past bookings are displayed but marked with a muted label so it’s clear they can’t be changed anymore.
- Each future booking includes buttons to:
  - Edit the booking (pre-filled form)
  - Cancel the booking (with a confirmation modal)
- The cancel button triggers a JavaScript modal to make sure the action isn’t taken accidentally.

 ![ My Bookings without a booking ]( static\images\screenshots\my-bookings.png  )
 ![ My Bookings with a booking ]( static\images\screenshots\mybookings2.png)

 ![  Edit Booking ]( static\images\screenshots\edit.png )

![ Cancel Confirmation ](static\images\screenshots\confirm-cancel.png)

 ![ Cancelled Booking  ]( static/images/screenshots/cancelled.png )


#### Contact Form

- A simple front-end form collects name, email, and message.
- Form is protected with CSRF tokens and styled using Django Crispy Forms.
- Success or error messages appear after submitting, letting the user know exactly what happened.
- A Google Maps iframe shows the location of the restaurant right next to the contact info.

 ![  Contact page up ]( static\images\screenshots\contact1.png )
 ![ Contact page down  ]( static\images\screenshots\contact2.png )

#### Authentication

- Registration, login, logout, and password reset are all handled using Django AllAuth.
- When logged in, users see a welcome message and additional navigation options.
- Only authenticated users can access booking creation, editing, or cancellation.
- Friendly prompts remind unauthenticated visitors to log in when they try to do something protected.

 ![ Register  ]( static\images\screenshots\register.png )
 ![  Login ]( static\images\screenshots\log-in.png )
 ![  Logout ]( static/images/screenshots/log-out.png )

#### Admin Features

- The Django admin panel gives full control over:
  - Menu items (add, edit, delete)
  - Tables (configure number and seats per table)
  - Bookings (view, search, delete if needed)
- Admins can also view user messages submitted through the contact form.
- This makes it suitable for restaurants that don’t have a custom dashboard yet, but still want control.

 ![  Admin page ]( static/images/screenshots/admin.png )

### 2.2 Additional Features

Even though these aren’t required for the MVP, they were added to improve polish and user experience.

- Booking confirmations and form feedback are delivered via Bootstrap alert messages (they dismiss automatically).
- Canceling a booking opens a Bootstrap modal asking the user to confirm, preventing mistakes.
- The menu and booking cards use a semi-transparent “glass” effect to blend nicely with background images.
- The nav highlights the current page so the user doesn’t get lost.
- Forms use both front-end validation (e.g. required fields, input types) and server-side validation.
- A custom favicon appears in the browser tab for branding.
- Fully responsive design thanks to Bootstrap’s grid — pages tested on mobile, tablet, and widescreen layouts.

We tried to strike a balance between functionality and simplicity. The booking system was the biggest challenge to make dynamic but predictable, and it took some tweaking to avoid bugs when multiple users book at once. Menu filtering and feedback messages were added later once the core flow worked well.

## 3. Design

The visual design of the Restaurant Booking System was just as important as the logic behind it. A clean and welcoming interface helps build trust, especially when users are providing personal info like booking details or login credentials.

While it’s a fairly simple site, a lot of decisions went into the layout, color scheme, spacing, and responsiveness. Our goal was to keep it intuitive — nothing too flashy, just functional and modern.

### 3.1 UX/UI Strategy

We wanted users to immediately understand how to use the website, even if they only visited once. So we prioritized:

- **Clarity over complexity**: Every page uses headings, icons, or short text blocks so that users don’t get overwhelmed or confused.
- **Minimal input steps**: Whether booking a table or sending a message, the forms are short, with just the fields that are really necessary.
- **Feedback on every action**: After submitting forms, users see clear success or error messages so they know what happened.
- **Consistency**: All buttons, cards, and headings follow a uniform style across pages.
- **Trust indicators**: Features like password validation, confirmation prompts, and authentication gates make users feel secure.

Some smaller layout decisions were adjusted after testing in different screen sizes. For example, form cards were centered with some padding to prevent them from stretching too wide on desktop.

### 3.2 Wireframes

Wireframes were sketched during the planning stage to decide general page layouts. These helped figure out things like:

- Where to place buttons like “Book a Table” on the home page
- How the booking list would look on different devices
- How to position the contact form and the Google map side-by-side

The wireframes were basic and not pixel-perfect, but they gave enough structure to move forward confidently.

Wireframes included:

- Home Page layout (hero section, CTA)

 ![  Home Page ](static\images\screenshots\home.png  )

- Booking form (card layout, mobile-friendly)

 ![  Booking Form ]( static\images\screenshots\booking.png )

- My Bookings page (table list with action buttons)

 ![ My Bookings  ]( static\images\screenshots\mybookings2.png )

- Contact page (form beside map)

 ![  Contact form ]( static\images\screenshots\contact1.png )

They were sketched by hand first and then adjusted as development went on — some spacing and behavior changed once the real data came in.

### 3.3 Color Scheme & Typography

We chose a color palette that gives off a premium, cozy restaurant vibe — not too bright, not too dull. The main colors were:

- **Dark brown / deep gray overlays** for backgrounds (like menus and bookings)
- **White and semi-transparent glass cards** to help text stand out
- **Primary buttons** use Bootstrap’s `btn-primary` style (blue by default), but we overrode with custom coloring in some places like cancel buttons (red)

Text is kept large enough to read easily, especially on mobile.

For typography:

- **Lato** font from Google Fonts was used for its modern, soft look.
- Headings are bold and sized up, while paragraphs are lighter.
- All text was left-aligned on cards, except titles which were centered on mobile.

We also made sure all text had high contrast ratios and ran Lighthouse to double-check accessibility scores (100%).

---

Overall, the design was guided by the idea that less is more — the user should focus on the menu or booking, not on navigating around.

## 4. Agile Methodology

This project was developed using Agile principles and tracked using a GitHub Project board in Kanban style. From the beginning, we tried to stay organized by writing out our user stories and converting them into actionable tasks.

The main goal was to plan a Minimum Viable Product (MVP) first and then build from there — that way we could focus on functionality early on without getting too distracted by extras.

### 4.1 Planning Approach

Before starting to code, we created a GitHub project board and began outlining:

- User stories (for customers and admins)
- Tasks for each story
- Milestones for major steps (like completing the booking form logic or connecting templates)

Each task card usually included a checklist and a label (like *bug*, *frontend*, or *backend*), so it was easier to keep things separate. We moved cards through stages like **To Do**, **In Progress**, **Review**, and **Done**.

 ![ User Stories  ](  static\images\screenshots\userstories.png)

Even though it was a solo project, working this way helped stay focused and not forget small details — for example, we caught some issues with date validations just because they were part of the checklist.

We used Git branches to separate work on different parts of the app (like `feature/booking-form` or `fix/menu-pagination`), and then merged into main after testing.

### 4.2 MoSCoW Prioritization

We used the **MoSCoW** technique to decide which features were essential and which ones could wait if time ran out. Here's a summary:

#### Must Have
- Booking form with conflict checks
- Menu display with categories
- User login/logout and authentication
- My Bookings (Edit & Cancel)
- Contact form with validation
- Admin control via Django panel

#### Should Have
- JS modal for cancel confirmation
- Menu pagination
- Table capacity logic

#### Could Have
- Background images and styling polish
- Toast-style feedback messages
- Prefilled edit form with previous booking data

#### Won’t Have (this time)
- Review system for past bookings
- Blog or newsletter
- Table map or visual seating plan

These priorities helped us avoid getting stuck on visual stuff too early. We focused first on making sure bookings couldn’t conflict and that everything was saved correctly in the database.

### 4.3 Sprint & Task Board

The GitHub Project board tracked everything. We had around 20–25 cards in total, including user stories, enhancements, and bugs.

A few example cards:

- *"Set up Booking model and table logic"* — included subtasks for guests, time checks, and foreign keys.
- *"Fix 'edit booking' not showing correct initial values"* — found during testing and fixed by passing instance to form.
- *"Style Contact page similar to booking form"* — to maintain UI consistency.

Most cards went through the full flow from **To Do** → **In Progress** → **Done**, although a few minor bugs were fixed right away without cards due to time (but still noted in commits).

We added checklists for tasks like testing or adding success messages, which helped not forget important things like user feedback or view permissions.

---

This workflow helped build the app steadily without forgetting anything major, and it also showed progress clearly along the way.


## 5. Technologies Used

This project combines multiple tools and technologies — some were used during development, others are part of the production environment. We chose tried-and-tested tools to ensure performance, scalability, and smooth deployment.

### Core Stack

- **Python 3.12** – Used as the backend programming language.
- **Django 4.2** – Full-stack framework that handles routing, models, admin, views, and templates.
- **SQLite3** – Used as the local development database.
- **PostgreSQL** – Used in production for a more scalable, secure database.

### Frontend

- **HTML5** – Structure of the pages.
- **CSS3** – Styling (both custom and framework-based).
- **Bootstrap 5** – Provided a solid, mobile-first grid system and components like buttons, alerts, and modals.
- **JavaScript** – Added interactivity to the booking cancellation modal and general client-side behavior.

### Django Packages

- **Django AllAuth** – Handles registration, login, logout, password reset, and more.
- **Crispy Forms (Bootstrap 5)** – Made form layout easy and consistent with Bootstrap styles.
- **Gunicorn** – Production-ready WSGI HTTP server for Django, used by Heroku.
- **dj-database-url** – Parses the `DATABASE_URL` env variable for Heroku’s PostgreSQL database.
- **whitenoise** – Serves static files efficiently in production.

### Tools & Hosting

- **Git** – Version control throughout the project.
- **GitHub** – Code hosting and project board for agile planning.
- **Gitpod** – Cloud IDE used during development.
- **Heroku** – Deployed the live app with PostgreSQL add-on and environment variables.
- **Cloudinary** – Although configured, it was not used in the final version (media upload not needed).
- **Chrome DevTools** – Used for responsive testing and Lighthouse reports.
- **Am I Responsive?** – Tool used for screenshots in README.

### Validators & Testing

- **W3C HTML Validator** – Ensured no structural markup issues.
- **W3C CSS Validator** – Confirmed stylesheets were clean.
- **Lighthouse** – Tested performance, accessibility, and best practices.
- **Django TestCase** – Used for writing unit tests for views and forms.

---

We kept the stack relatively lean and chose Django for its batteries-included approach. It gave us a lot of useful features like user auth and admin control without needing to build everything from scratch.


## 6. Testing

Testing was carried out through a mix of manual testing, built-in Django unit tests, and third-party validators like Lighthouse and W3C tools. We tested each view, form, and feature based on user stories and edge cases (like booking a past date or accessing another user's data). Bugs were also recorded and resolved along the way.

### 6.1 Manual Testing

We manually tested all major features using different browsers and devices. The main focus was on the booking flow, authentication, and navigation.

#### Key test cases:

| Feature             | Test Description                                         | Status |
|---------------------|----------------------------------------------------------|--------|
| Menu page           | Menu loads with categories and pagination                | Pass   |
| Booking form        | Form validates inputs (date, time, guests)               | Pass   |
| Table allocation    | Prevents double-booking of same time slot                | Pass   |
| Contact form        | Sends message with success or error feedback             | Pass   |
| My Bookings page    | Lists upcoming and past bookings                         | Pass   |
| Edit Booking        | Form is pre-filled and updates data correctly            | Pass   |
| Cancel Booking      | Modal confirms cancel, booking is removed                | Pass   |
| Auth protection     | Guests can’t book/edit/cancel without logging in         | Pass   |
| Navbar links        | All navigation links work correctly (desktop/mobile)     | Pass   |
| Admin access        | Admins can add/edit menu items and bookings              | Pass   |

Responsiveness was also tested in:

- Chrome, Firefox, and Safari
- Mobile (iPhone, Android) using Chrome DevTools
- Resizing browser window manually

### 6.2 Automated Testing

We created two Django test files for unit testing:

#### `reservations/test_forms.py`

- Tests valid and invalid form submissions
- Checks required fields are enforced
- Ensures past-dated bookings are rejected

#### `reservations/test_views.py`

- Tests each view’s response status (200 OK, 302 redirects)
- Ensures unauthorized access is blocked
- Verifies booking CRUD operations from a logged-in user
- Confirms messages show for success/cancellation
- Protects user data (can't view/edit others' bookings)

To run the tests:

```bash
python manage.py test reservations.test_forms
python manage.py test reservations.test_views
```

Around 20 tests were written, covering all main logic. A few edge cases (like editing to the same date/time) were added late in the project after bug hunting.

 ![ Testing  ]( static\images\screenshots\test.png )

### 6.3 Validators & Lighthouse

#### HTML

All pages passed the W3C HTML Validator, aside from a few ignored warnings (like using `target="_blank"` without `rel="noopener"` in the map link, which was deemed safe here).

#### CSS

CSS validated with the Jigsaw CSS Validator — no major errors, only one warning for browser-specific prefix.

#### Lighthouse

Lighthouse audits were performed using Chrome DevTools in mobile view.

| Category       | Score |
|----------------|-------|
| Performance    | 59    |
| Accessibility  | 95    |
| Best Practices | 100   |
| SEO            | 90    |

The **performance score** was affected during the audit, with a warning that Chrome extensions may have influenced the result. This was confirmed by re-running the audit in incognito mode, where the score improved slightly.

The lower performance was mainly due to image loading and render-blocking CSS/JS on first paint. Since the site uses high-resolution background images and Bootstrap, this was expected to a degree. We plan to improve this by compressing assets and enabling lazy-loading where possible.

Despite that, the **accessibility**, **SEO**, and **best practices** scores remained very high, which indicates the project is well-built and user-friendly.

 ![  Lighthouse audit ](static\images\screenshots\lighthouse.png  )



### 6.4 Bugs & Fixes

A few bugs were encountered during development and testing. Below is a detailed list of what was found and how it was resolved:

#### General Development Bugs

| Issue                                               | Fix Applied                                           |
|-----------------------------------------------------|--------------------------------------------------------|
| Cancel modal not showing on My Bookings             | JS selector was incorrect; fixed by updating `id`     |
| Booking in the past was still possible              | Added custom form validation using `clean_date()`     |
| Edit form didn’t show previous values               | Fixed by passing `instance=booking` to form           |
| Multiple `{% block extras %}` tags in base template | Removed duplicates — caused rendering conflicts       |
| Booking list misaligned on mobile                   | Adjusted Bootstrap column classes                     |
| Booking by unauthenticated user caused 500 error    | Added `@login_required` decorator on view functions   |

#### Debugging During Testing Phase

| Issue                                      | Fix & Explanation                                                                 |
|-------------------------------------------|------------------------------------------------------------------------------------|
| **Duplicate Flash Messages**              | Confirmation messages showed up twice (in both `base.html` and `my_bookings.html`). Removed the duplicate block from `my_bookings.html`. |
| **Contact Form Not Saving to Admin**      | Forgot to register the `Contact` model in `admin.py`. Added it, and submissions became visible. |
| **Google Maps iframe Broken**             | Manually typed iframe code caused a `Google Maps Platform rejected your request` error. Replaced it with the correct embed code from Google Maps. |



**Double Messaging Error**  
*Issue:*  
![Double Message Error](static/images/screenshots/double-message.png)  
*Fix:*  
![Double Message Fix](static/images/screenshots/double-message-fix.png)

---

**Contact Form Missing in Admin Panel**  
*Issue:*  
![No Contact Form in Admin](static/images/screenshots/no-contact-form-in-admin.png)  
*Fix:*  
![Contact Model](static/images/screenshots/contact-model.png)  
![Contact Forms.py](static/images/screenshots/contact-forms.py.png)  
![Contact Admin Registration](static/images/screenshots/contact-admin.png)

---

**Google Maps Error**  
*Issue:*  
![Google Maps Error](static/images/screenshots/gmaps-error.png)  
*Fix:*  
![Google Maps Fixed](static/images/screenshots/gmaps-fix.png)

Testing was a big focus in the second half of the project. After adding core features, we did another round of testing with fresh eyes — caught a few things we had overlooked like permission checks and past bookings logic.

## 7. Deployment

The project was developed using Gitpod and version-controlled with Git. It was then pushed to GitHub and deployed to Heroku using a connected repository and necessary configuration variables. Below are the deployment details for both live and local setups.

### 7.1 Deployment to Heroku

The live site is hosted on [Heroku](https://restaurant-booking-system-001-81d0f1b38ae2.herokuapp.com/). These were the main steps followed to deploy the application:

1. **Created a new Heroku app**
   - Set the region and app name
   - Chose GitHub deployment method

2. **Configured environment variables**
   - `DATABASE_URL`: PostgreSQL database provided by Heroku
   - `SECRET_KEY`: Django secret key (generated manually)
   - `DISABLE_COLLECTSTATIC`: set to `1` to avoid static build errors during first push
   - `CLOUDINARY_URL`: optional, not actively used in this project
   - `ALLOWED_HOSTS`: included Heroku app domain

3. **Added necessary files**
   - `Procfile`: tells Heroku how to run the app using Gunicorn
   - `requirements.txt`: includes all dependencies
   - `runtime.txt`: specifies the Python version
   - `.gitignore`: excludes sensitive and local dev files from version control

4. **Connected GitHub repository to Heroku**
   - Enabled automatic deploys from the main branch
   - Manually deployed the branch for first-time setup

5. **Ran migrations and created superuser**
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

6. **Verified app was live** using the generated Heroku URL.

---

### 7.2 Environment Variables

These environment variables are critical for deployment and security:

| Variable Name       | Description                             |
|---------------------|-----------------------------------------|
| `SECRET_KEY`        | Django secret key for encryption        |
| `DEBUG`             | False in production, True for local dev |
| `DATABASE_URL`      | PostgreSQL in Heroku, SQLite locally    |
| `ALLOWED_HOSTS`     | App domain and localhost                |
| `CLOUDINARY_URL`    | Optional, used only if media is enabled |
| `DISABLE_COLLECTSTATIC` | Prevents collectstatic during initial deploy |

---

## 8. Database Schema

The application uses Django’s ORM to manage data models and their relationships. In development, it runs on **SQLite3**; in production (Heroku), it connects to a **PostgreSQL** database.

The database includes three primary models:

---

### 1. User

The default Django `User` model is used for authentication (via Django AllAuth). It stores:

- Username
- Email
- Password (hashed)
- Date joined, last login, etc.

Every booking is linked to a specific user, ensuring secure ownership and visibility.

---

### 2. Table

Represents a physical table in the restaurant.

| Field     | Type     | Description                      |
|-----------|----------|----------------------------------|
| `number`  | Integer  | Unique table number              |
| `seats`   | Integer  | Number of seats at the table     |

Admin users can create/edit/remove tables through the Django admin panel. This allows flexible configuration as the restaurant grows or changes layout.

---

### 3. Booking

This is the core model of the system — it stores reservation details submitted by users.

| Field     | Type      | Description                                       |
|-----------|-----------|---------------------------------------------------|
| `user`    | FK to User| The customer who made the booking                 |
| `table`   | FK to Table| The assigned table                               |
| `name`    | String    | Name provided on the reservation form            |
| `email`   | Email     | Contact email                                     |
| `phone`   | String    | Phone number                                      |
| `guests`  | Integer   | Number of guests attending                        |
| `date`    | Date      | Booking date                                      |
| `time`    | Time      | Booking time                                      |
| `notes`   | Text      | Optional notes (e.g., “Window seat, please”)      |
| `created_on` | DateTime | Timestamp when the booking was created          |

**Constraints and Validation:**

- A table cannot be double-booked for the same time slot.
- Date/time inputs are validated to prevent past bookings.
- User-specific filtering is used to show only their own bookings.

---

All models were registered in `admin.py`, and can be managed through the Django admin interface, which is ideal for internal restaurant use.

## 9. Responsive Design

The site was designed with a mobile-first approach using Bootstrap 5 and tested across various screen sizes and devices. The goal was to ensure users could easily navigate and interact with the booking system whether they’re using a phone, tablet, or desktop.

### Techniques Used

- **Bootstrap Grid System**  
  Used throughout to organize content into rows and columns that collapse and stack on smaller screens.

- **Media Queries**  
  Applied minimal custom CSS where needed to adjust paddings, background images, and text visibility based on screen width.

- **Flexbox & Utility Classes**  
  Used for layout alignment (e.g., centering the "My Bookings" buttons and the navbar links).

- **Responsive Navigation Bar**  
  The navbar collapses into a hamburger menu on small screens and expands on larger ones. The active page is highlighted.

- **Glassmorphic Form Cards**  
  On contact and booking pages, cards use a translucent background with white text for readability over images. These cards stay centered and readable across devices.

- **Google Maps Embed**  
  The embedded iframe in the contact page was sized responsively using Bootstrap's column system. It collapses nicely under the contact info on small screens.

---

### Pages Optimized for Responsiveness

| Page              | Responsive Notes                                               |
|------------------|----------------------------------------------------------------|
| Home              | Hero section text resizes properly; button always visible     |
| Menu              | Grid of menu items adjusts column layout across breakpoints   |
| Book Table        | Form fits narrow screens without horizontal scrolling         |
| My Bookings       | Table layout scrolls horizontally on mobile; buttons stack     |
| Contact           | Map and contact info stack vertically on small screens        |
| Authentication    | Login/Signup pages styled via AllAuth templates and Bootstrap |

### Tools Used for Testing

- **Chrome DevTools** – Simulated mobile views (iPhone, Galaxy, iPad, etc.)
- **Real Devices** – Tested on actual mobile (Android) and tablet (Samsung) browsers
- **Am I Responsive?** – Used to generate responsive screenshots for README

---

## 10. Future Enhancements

While the current version of the Restaurant Booking System delivers a fully functional and tested booking flow, there are a few features and ideas that we’d like to explore or implement in the future. These enhancements could improve both the user experience and backend management.

---

### 1. Review Your Booking (Post-Visit Feedback)

- **Idea**: After a completed booking (past date), allow users to submit a short review or comment.
- **Why**: Helps admins gather feedback and improve services.
- **Status**: Model and admin setup partially scaffolded; not yet exposed in frontend.

---

### 2. Email Confirmations

- **Idea**: Send automatic emails for booking confirmation, edits, and cancellations.
- **Why**: Gives users extra reassurance and documentation.
- **How**: Can use Django’s built-in email backend with SendGrid or Mailgun.
- **Status**: Not yet started (was out of scope).

---

### 3. Admin Dashboard UI

- **Idea**: Create a custom admin dashboard with stats like:
  - Bookings by date
  - Table usage heatmaps
  - Peak hours
- **Why**: Makes it easier for restaurant staff to make decisions.
- **Status**: Not implemented (currently using Django admin only).

---

### 4. Booking Search & Filters

- **Idea**: Allow users to search their bookings by date, email, or guest name.
- **Why**: Improves user control, especially for frequent visitors.
- **Status**: Planned as optional UX upgrade.

---

### 5. Multi-language Support

- **Idea**: Add localization for templates using Django’s `gettext`.
- **Why**: Helps support non-English-speaking users (especially tourists).
- **Status**: Not started.

---

### 6. Booking Limits per User

- **Idea**: Set a daily or weekly booking limit per user.
- **Why**: Prevents abuse or excessive bookings from one account.
- **Status**: Could be added via signals or custom validation.

---

### 7. Image Uploads for Menu Items

- **Idea**: Admins can upload images for each dish (hosted via Cloudinary).
- **Why**: Makes the menu page more visually appealing.
- **Status**: Cloudinary config was started but removed to keep MVP simple.

---

These enhancements were either considered during development but postponed to stay focused on the core functionality, or they emerged from reflection and usability testing after launch. If this app were to be maintained long-term, these would be the next priority features.

## 11. Credits

---

### 11.1 Content & Code

- **Code Institute** – For the project structure guidance and walkthroughs.
- **Django Documentation** – [https://docs.djangoproject.com/](https://docs.djangoproject.com/)  
  The official Django docs were essential throughout the backend setup, especially for models, forms, and views.
- **Bootstrap Documentation** – [https://getbootstrap.com/docs/5.0](https://getbootstrap.com/docs/5.0)  
  Used extensively for layout, responsiveness, cards, forms, and modals.
- **W3Schools & MDN Web Docs** – Helped with general HTML/CSS/JS behaviors and syntax checks.
- **Stack Overflow** – For solving bugs, especially with modals and form validation issues.
- **ChatGPT** – Used  for debugging help, explaining error messages, and reviewing code structure for clarity.
- **GitHub Discussions** – Looked at solutions for Heroku deployment issues and Django signals.
- **Code Institute Mentors & Slack Community** – For constant support and quick feedback.

---

### 11.2 Media & Assets

- **Font Awesome** – [https://fontawesome.com](https://fontawesome.com)  
  Provided icons used in navbar and footer (social links, map pins, etc.)
- **Google Fonts** – Lato font used for clean typography
- **Pexels** – [https://pexels.com](https://pexels.com)  
  Provided free-use images for background and menu designs.
- **Responsively App** – Used to preview and test the site across multiple device sizes in parallel  
  [https://responsively.app/download](https://responsively.app/download) 
  Used to generate the responsiveness mockup for the README.
- **Google Maps** – Used iframe embed for the Contact page map view.
- **Favicon.io** – Generated the favicon used in the site tab.
- **Heroku Docs** – [https://devcenter.heroku.com/](https://devcenter.heroku.com/)  
  For managing config vars, deploys, and Dynos.

---


