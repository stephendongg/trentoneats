--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.categories (
    category character varying(20) NOT NULL,
    restaurant_id character varying(20)
);


--
-- Name: customers; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.customers (
    customer_id character varying(20) NOT NULL,
    name character varying(255),
    review_count integer NOT NULL,
    avg_rating double precision NOT NULL,
    account_type character varying(255) NOT NULL,
    reported_count integer
);


--
-- Name: restaurants; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.restaurants (
    restaurant_id character varying(20) NOT NULL,
    name character varying(255) NOT NULL,
    address character varying(255) NOT NULL,
    hours character varying(255) NOT NULL,
    open_closed boolean,
    menu character varying(255),
    media character varying(255),
    tags character varying(255),
    review_count integer,
    stars double precision NOT NULL
);


--
-- Name: reviews; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reviews (
    review_id integer NOT NULL,
    customer_id character varying(20),
    restaurant_id character varying(20),
    date timestamp without time zone NOT NULL,
    text text NOT NULL,
    price integer,
    taste integer,
    authenticity integer,
    coolness integer,
    overall integer
);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.categories (category, restaurant_id) FROM stdin;
\.


--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.customers (customer_id, name, review_count, avg_rating, account_type, reported_count) FROM stdin;
\.


--
-- Data for Name: restaurants; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.restaurants (restaurant_id, name, address, hours, open_closed, menu, media, tags, review_count, stars) FROM stdin;
1	Playa Bowls	24 Trenton Avenue, Trenton, NJ	9am-5pm everyday	t	Playa Bowlsabowls.com/trenton	playabowlos.com/media	Acai, Fruit	15	4.2
2	1911 Smokehouse BBQ	11 W Front St, Trenton, NJ 08608	Monday\t11AM - 3:30PM,\n        Tuesday\t11AM - 3:30PM,\n        Wednesday 11AM - 10:30PM,\n        Thursday 11AM - 10:30PM,\n        Friday 11AM - 10:30PM,\n        Saturday 1 - 10:30PM,\n        Sunday 1 - 10:30PM	f	http://places.singleplatform.com/1911-smoke-house-barbeque/menu?ref=google	https://1911bbq.com	BBQ	12	5
3	Bamboo Grill Jamaican Restaurant	1005 Chambers St, Trenton, NJ 08611	Monday\t10AM - 7PM,\n        Tuesday\t10AM - 7PM,\n        Wednesday 10AM - 7PM,\n        Thursday 10AM - 7PM,\n        Friday 10AM - 8PM,\n        Saturday 10AM - 8PM,\n        Sunday Closed	t	None	None	Jamaican, Grill	1	3.2
4	'Ila Mae's Restaurant'	313 Market St, Trenton, NJ 08611	Monday\tClosed,\n        Tuesday\t9AM - 8PM,\n        Wednesday 9AM - 8PM,\n        Thursday 9AM - 8PM,\n        Friday 9AM - 8PM,\n        Saturday 9AM - 8PM,\n        Sunday Closed	f	http://places.singleplatform.com/ila-maes-restaurant/menu?ref=google	None	Soul	10	4.3
5	Blue Danube Restaurant	538 Adeline St, Trenton, NJ 08611	Monday\tClosed\n        Tuesday\t11:30AM - 2:15PM, 5 - 7:30PM,\n        Wednesday 11:30AM - 2:15PM, 5 - 7:30PM,\n        Thursday 11:30AM - 2:15PM, 5 - 7:30PM,\n        Friday 11:30AM - 2:15PM, 5 - 8PM,\n        Saturday 3 - 8PM,\n        Sunday 3 - 7:30PM	t	http://www.bluedanuberestaurant.net/menu.php	http://www.bluedanuberestaurant.net/about.php	Eastern European	273	4.6
6	The Big Easy of Trenton Restaurant	111 S Warren St, Trenton, NJ 08608	Monday\t12 - 7PM,\n        Tuesday\t12 - 7PM,\n        Wednesday 12 - 7PM,\n        Thursday 12 - 7PM,\n        Friday 12 - 7PM,\n        Saturday 9AM - 5PM,\n        Sunday Closed	f	None	None	Dine-in	260	4.5
7	'Don Julio's Bar and Grill'	900 Liberty St, Trenton, NJ 08611	Monday\t11AM - 2AM,\n        Tuesday\t11AM - 2AM,\n        Wednesday 11AM - 2AM,\n        Thursday 11AM - 2AM,\n        Friday 11AM - 2AM,\n        Saturday 11AM - 2AM,\n        Sunday 12PM - 2AM	t	None	None	Bar & Grill	190	4.3
8	The Hummingbird Restaurant	29 S Warren St, Trenton, NJ 08608	Monday\t10AM - 7PM,\n        Tuesday\t10AM - 7PM,\n        Wednesday 10AM - 7PM,\n        Thursday 10AM - 7PM,\n        Friday 10AM - 6PM,\n        Saturday 10AM - 6PM,\n        Sunday Closed	f	None	None	Jamaican	282	4.2
9	Sabor Latino	293 Ashmore Ave, Trenton, NJ 08611	Tuesday 10AM - 12AM,\n        Wednesday Closed,\n        Thursday 10AM - 12AM,\n        Friday 10AM - 2AM,\n        Saturday 10AM - 2AM,\n        Sunday 10AM - 12AM,\n        Monday 10AM - 12AM	t	None	None	Dominican	80	4.1
10	'Trentini's'	635 S Clinton Ave, Trenton, NJ 08611	Tuesday 10AM - 10PM,\n        Wednesday 10AM - 10PM,\n        Thursday 10AM - 10PM,\n        Friday 10AM - 10PM,\n        Saturday 10AM - 10PM,\n        Sunday 10AM - 10PM,\n        Monday 10AM - 10PM	f	https://trentinismenu.com/menu.html	https://trentinismenu.com/index.html	Italian	420	4.1
11	Mama D Soul Food 2	312 S Broad St, Trenton, NJ 08609	Tuesday Closed,\n        Wednesday 12 - 7PM,\n        Thursday 12 - 7PM,\n        Friday 12 - 7PM,\n        Saturday 9AM - 7PM,\n        Sunday 1 - 7PM,\n        Monday Closed	t	None	None	Soul	112	3.9
12	'Cooper's Riverview'	50 Riverview Plaza, Trenton, NJ 08611	Tuesday 12PM - 2AM,\n        Wednesday 12PM - 2AM,\n        Thursday 12PM - 2AM,\n        Friday 12PM - 2AM,\n        Saturday 12PM - 2AM,\n        Sunday 11:30AM - 11PM,\n        Monday Closed	f	coopersnj.com	None	English	455	4
13	Mi Ranchito Pizza and Tacos	911 Chambers St, Trenton, NJ 08611	Tuesday 10AM - 10PM,\n        Wednesday Closed,\n        Thursday 10AM - 10PM,\n        Friday 10AM - 10PM,\n        Saturday 10AM - 10PM,\n        Sunday 10AM - 10PM,\n        Monday 10AM - 10PM	t	None	None	Tacos	61	4.7
14	El Potrillo	541 Roebling Ave, Trenton, NJ 08611	Tuesday Closed,\n        Wednesday 10AM - 10PM,\n        Thursday 10AM - 10PM,\n        Friday 10AM - 10PM,\n        Saturday 10AM - 10PM,\n        Sunday 10AM - 10PM,\n        Monday 10AM - 10PM	f	http://places.singleplatform.com/el-potrillo-mexican-restaurant-7/menu?ref=google	None	Mexican	213	3.9
15	Chencha y Chole	865 S Broad St, Trenton, NJ 08611	11AM - 10PM everyday	t	None	None	Mexican	319	4.2
16	Casablanca Restaurant	140 Washington St, Trenton, NJ 08611	Monday\t11AM - 2AM,\n        Tuesday\t11AM - 2AM,\n        Wednesday 11AM - 2AM,\n        Thursday 11AM - 2AM,\n        Friday 11AM - 2AM,\n        Saturday 11AM - 2AM,\n        Sunday 11AM - 2AM	f	None	None	Spanish	372	4.1
\.


--
-- Data for Name: reviews; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.reviews (review_id, customer_id, restaurant_id, date, text, price, taste, authenticity, coolness, overall) FROM stdin;
\.


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (category);


--
-- Name: customers customers_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (customer_id);


--
-- Name: restaurants restaurants_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.restaurants
    ADD CONSTRAINT restaurants_pkey PRIMARY KEY (restaurant_id);


--
-- Name: reviews reviews_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_pkey PRIMARY KEY (review_id);


--
-- Name: categories categories_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES public.restaurants(restaurant_id);


--
-- Name: reviews reviews_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(customer_id);


--
-- Name: reviews reviews_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES public.restaurants(restaurant_id);


--
-- PostgreSQL database dump complete
--

