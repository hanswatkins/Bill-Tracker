# Hans Watkins - Project 4

- I am going to create an app which will help couples split their spending based on their income making paying for bills, dinner dates, or shopping an easier and more equitable transaction.
- Users can upload their bills and the date they are due to help them remember their due dates and automatically tell them how much each of them should be paying
- One to many relationship: one user can have many bills/purchases.

## Home page/Main page
- has the main functionality of the app
- fields to input two people's income
- field to input the price of the bill
- two returns showing the amount each person will pay

## Bills/purchases have
- price
- name of bill/purchase
- due date of bill
- are displayed as a card
- styled with bulma

## User Stories
- As a user, I want to be able to easily split bills between my partner and I based on our inputted annual incomes.
- As a user, I want to be able to keep track of the bills I share with my partner
- As a user, I want to be able to access the splitting calculator quickly
- As a user, I want to be able to add new bills to my collection and look through them easily. 

## Models
### User
  - properties
    - name
    - income  
    - (mutiple) bills

### Bill
  - properties
    - user it belongs to
    - amount
    - due date



