# Bill Tracker

## Technologies Used

- HTML
- CSS
- jQuery
- Bulma
- Django
- Python
- Heroku

## Approach Taken

My plan was to create a bill-splitting app to help equitably split the price of purchases and bills based on two people's incomes, ideally intended for a couple to use. The users would input their income, their partner's income, and the price of the bill and it would calculate how much each user owes towards the balance. Users would also be able to sign in and save bills to their profile to view them later as well as add and delete bills as they see fit. This is my first attempt at a full-stack application with Django and while I didn't reach all of my goals with this project, I was able to learn a ton about Django's endless capabilities and built-in functionality.

## Setbacks

As I wrap up this project, I realize I made a decision early in the planning stage that sent me down a difficult path. I wanted to create a One-To-Many relationship between a "Bill Owner" and "Bills", however, I should've used Django's built in User instead my "Bill Owner". I spent most of my time struggling with passing around a bill_owner_id while Django had everything I needed within the built-in User. If I had realized that earlier, I likely would've met my goals like user authentication, CRUD, and automatic bill sharing.

## Features

- Create a bill
- Name a bill
- Set a bill amount
- View all bills
- Assign an owner of a bill

## Future Goals

- Restructure the Bill/BillOwner relationship by replacing BillOwner with Django's User and rebuild the app from that framework.
- Create a homepage
- Add CRUD capabilities
- User Auth
- Bill due dates

## Wireframes

Home Page
<img src='/planning/wireframes/Home Page.png' width=600>

Bills Page
<img src='/planning/wireframes/Bills Page.png' width=600>

Create Page
<img src='/planning/wireframes/Create a new bill.png' width=600>

Bills Card Closeup
<img src='/planning/wireframes/Bills Card Closeup.png' width=600>
