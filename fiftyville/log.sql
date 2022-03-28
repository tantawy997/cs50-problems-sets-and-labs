-- Keep a log of any SQL queries you execute as you solve the mystery.

-- to search for the thefts that happend that day and street
select id from crime_scene_reports where month = 7 and day = 28 and street = "Humphrey Street";

/*295 | 2021 | 7 | 28 | Humphrey Street |  Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. 


Interviews were conducted
today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.*/

-- to get a sense of the thefts that happend in that day and we know that the theft happend bhind the bakery store and we have the id 459 might be helpful
select id from bakery_security_logs where hour = 10 and minute = 15 and  (select id from crime_scene_reports where month = 7 and day = 28 and street = "Humphrey Street");

-- to get a sense of the people table
 select * from people;

-- lets have so info from the interviews table
select transcript from interviews where month = 7 and day = 28;
/* 161 | Ruth | 2021 | 7 | 28 | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.

162 | Eugene | 2021 | 7 | 28 | I don't know the thief's name, but it was someone I recognized. Earlier this morning,
before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

163 | Raymond | 2021 | 7 | 28 | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call,
I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.

193 | Emma | 2021 | 7 | 28 | I'm the bakery owner, and someone came in, suspiciously whispering into a phone for about half an hour. They never bought anything.
*/


select transcript, id, name  from interviews where month = 7 and day = 28;


-- selecting only the transstion that is witidrawn and in the month 7 and day 28
select * from atm_transactions where transaction_type = "withdraw" and month = 7 and day = 28 and  atm_location = "Humphrey Lane";

-- we know that the theft made a call for a minute tops in the bakery
select *, max(duration) as max from phone_calls where month = 7 and day = 28 and duration < 60;



select * from flights where day = 29;

select origin_airport_id, destination_airport_id , airports.id from flights join airports on flights.id = airports.id;

-- I concluded that the first flight (earlist flight at the date 29) is the flight number 18 which was from fifltyvile airport to Logan International Airport which arrived at Boston

select * from airports;

-- to get the accomplice name which is dorris by the phone number

select * from people where phone_number = "(066) 555-9701";

select * from phone_calls where day = 28 and month = 7 and duration < 60;
-- id | caller | receiver | year | month | day | duration
 -- 221 | (130) 555-0289 | (996) 555-8899 | 2021 | 7 | 28 | 51
--224 | (499) 555-9472 | (892) 555-8872 | 2021 | 7 | 28 | 36
-- 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7 | 28 | 45
-- 251 | (499) 555-9472 | (717) 555-1342 | 2021 | 7 | 28 | 50
--254 | (286) 555-6063 | (676) 555-6554 | 2021 | 7 | 28 | 43
--255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7 | 28 | 49
--261 | (031) 555-6622 | (910) 555-3251 | 2021 | 7 | 28 | 38
--279 | (826) 555-1652 | (066) 555-9701 | 2021 | 7 | 28 | 55
--281 | (338) 555-6650 | (704) 555-2131 | 2021 | 7 | 28 | 54


--id | caller | receiver | year | month | day | duration
--233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7 | 28 | 45
--254 | (286) 555-6063 | (676) 555-6554 | 2021 | 7 | 28 | 43
--255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7 | 28 | 49
--279 | (826) 555-1652 | (066) 555-9701 | 2021 | 7 | 28 | 55
--281 | (338) 555-6650 | (704) 555-2131 | 2021 | 7 | 28 | 54
--395 | (367) 555-5533 | (455) 555-5315 | 2021 | 7 | 30 | 31

select * from bakery_security_logs where id in (select id from phone_calls where day = 28 and month = 7 and duration < 60);
--id | year | month | day | hour | minute | activity | license_plate
--221 | 2021 | 7 | 28 | 8 | 2 | exit | 1M92998
--224 | 2021 | 7 | 28 | 8 | 7 | exit | 7Z8B130
--233 | 2021 | 7 | 28 | 8 | 25 | entrance | L68E5I0
--251 | 2021 | 7 | 28 | 8 | 57 | exit | 8LLB02B
--254 | 2021 | 7 | 28 | 9 | 14 | entrance | 4328GD8
--255 | 2021 | 7 | 28 | 9 | 15 | entrance | 5P2BI95
--261 | 2021 | 7 | 28 | 10 | 18 | exit | 94KL13X
--279 | 2021 | 7 | 28 | 13 | 42 | entrance | NAW9653
--281 | 2021 | 7 | 28 | 15 | 6 | exit | RS7I6A0

select * from atm_transactions where id in (select id from crime_scene_reports where day = 28 and month = 7 and street = "Humphrey street")

--id | account_number | year | month | day | atm_location | transaction_type | amount
-- 295 | 74812642 | 2021 | 7 | 28 | Blumberg Boulevard | withdraw | 60

select * from bakery_security_logs where id in (select id from crime_scene_reports where month = 7 and day = 28 and street = "Humphrey Street");
-- 295 | 2021 | 7 | 29 | 8 | 22 | entrance | IH61GO8



--main goal
-- id | name | phone_number | passport_number | license_plate
--686048 | Bruce | (367) 555-5533 | 5773159633 | 94KL13X
/*
id | caller | receiver | year | month | day | duration
251 | (499) 555-9472 | (717) 555-1342 | 2021 | 7 | 28 | 50
*/

-- from the next query the earlist flight is
--id | origin_airport_id | destination_airport_id | year | month | day | hour | minute
--36 | 8 | 4 | 2021 | 7 | 29 | 8 | 20
select * from flights where day = 29 and month = 7 and origin_airport_id = 8;

/*select * from bakery_security_logs where license_plate in (select license_plate  from people where id in
(select person_id from bank_accounts where account_number in (select account_number from atm_transactions where month = 7 and day = 28 and transaction_type = "withdraw" and atm_location = "Leggett Street")));

-- qeery that mght be useful
*/
select * from phone_calls where duration < 60 and day = 28 and caller in (select phone_number from people where id in (select person_id from bank_accounts where account_number in  (select account_number from atm_transactions where month = 7 and day = 28 and transaction_type = "withdraw" and atm_location = "Leggett Street"))));

select * from flights  where day = 29 and month = 7 and origin_airport_id = 8 and destination_airport_id = 4;

select  from atm_transactions where day = 28 and month = 7 and transaction_type = "withdraw" and atm_location = "Leggett Street" and account_number  in (select account_number from bank_accounts where person_id in (select id from people where passport_number in (select passport_number from passengers where flight_id in (select id  from flights  where day = 29 and month = 7 and origin_airport_id = 8 and destination_airport_id = 4))));

-- important
--account_number
--28296815
--76054385
--49610011
--28500762


select * from bakery_security_logs where day = 28 and  month = 7 and  license_plate in  (select license_plate from people where passport_number in (select passport_number from passengers where flight_id in (select id  from flights  where day = 29 and month = 7 and origin_airport_id = 8 and destination_airport_id = 4)));

--254 | 2021 | 7 | 28 | 9 | 14 | entrance | 4328GD8
--257 | 2021 | 7 | 28 | 9 | 28 | entrance | G412CB7

--flights id important < 36 >

select * from bakery_(select license_plate from people where id in (select person_id from bank_accounts where account_number in  (select account_number from atm_transactions where month = 7 and day = 28 and transaction_type = "withdraw" and atm_location = "Leggett Street")))



