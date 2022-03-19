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
-- Name: categories; Type: TABLE; Schema: public; Owner: rmd
--

CREATE TABLE public.categories (
    restaurant_id character varying(20) NOT NULL,
    fast_food boolean,
    fine_dining boolean,
    casual_dining boolean,
    inexpensive boolean,
    moderate_price boolean,
    pricey boolean,
    priciest boolean,
    american boolean,
    french boolean,
    indian boolean
);


ALTER TABLE public.categories OWNER TO rmd;

--
-- Name: customers; Type: TABLE; Schema: public; Owner: rmd
--

CREATE TABLE public.customers (
    customer_id character varying(20) NOT NULL,
    name character varying(255),
    review_count integer NOT NULL,
    avg_rating double precision NOT NULL,
    account_type character varying(255) NOT NULL,
    reported_count integer
);


ALTER TABLE public.customers OWNER TO rmd;

--
-- Name: restaurants; Type: TABLE; Schema: public; Owner: rmd
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


ALTER TABLE public.restaurants OWNER TO rmd;

--
-- Name: reviews; Type: TABLE; Schema: public; Owner: rmd
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


ALTER TABLE public.reviews OWNER TO rmd;

--
-- Name: usertype; Type: TABLE; Schema: public; Owner: rmd
--

CREATE TABLE public.usertype (
    user_id character varying(20) NOT NULL,
    customer_id character varying(20),
    restaurant_id character varying(20),
    admin boolean,
    restaurant boolean,
    customer boolean
);


ALTER TABLE public.usertype OWNER TO rmd;

--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: rmd
--

COPY public.categories (restaurant_id, fast_food, fine_dining, casual_dining, inexpensive, moderate_price, pricey, priciest, american, french, indian) FROM stdin;
\.


--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: rmd
--

COPY public.customers (customer_id, name, review_count, avg_rating, account_type, reported_count) FROM stdin;
\.


--
-- Data for Name: restaurants; Type: TABLE DATA; Schema: public; Owner: rmd
--

COPY public.restaurants (restaurant_id, name, address, hours, open_closed, menu, media, tags, review_count, stars) FROM stdin;
1	Playa Bowls	24 Trenton Avenue, Trenton, NJ	9am-5pm everyday	t	Playa Bowlsabowls.com/trenton	playabowlos.com/media	Acai, Fruit	15	4.2
\.


--
-- Data for Name: reviews; Type: TABLE DATA; Schema: public; Owner: rmd
--

COPY public.reviews (review_id, customer_id, restaurant_id, date, text, price, taste, authenticity, coolness, overall) FROM stdin;
\.


--
-- Data for Name: usertype; Type: TABLE DATA; Schema: public; Owner: rmd
--

COPY public.usertype (user_id, customer_id, restaurant_id, admin, restaurant, customer) FROM stdin;
\.


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: rmd
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (restaurant_id);


--
-- Name: customers customers_pkey; Type: CONSTRAINT; Schema: public; Owner: rmd
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (customer_id);


--
-- Name: restaurants restaurants_pkey; Type: CONSTRAINT; Schema: public; Owner: rmd
--

ALTER TABLE ONLY public.restaurants
    ADD CONSTRAINT restaurants_pkey PRIMARY KEY (restaurant_id);


--
-- Name: reviews reviews_pkey; Type: CONSTRAINT; Schema: public; Owner: rmd
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_pkey PRIMARY KEY (review_id);


--
-- Name: usertype usertype_pkey; Type: CONSTRAINT; Schema: public; Owner: rmd
--

ALTER TABLE ONLY public.usertype
    ADD CONSTRAINT usertype_pkey PRIMARY KEY (user_id);


--
-- Name: categories categories_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rmd
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES public.restaurants(restaurant_id);


--
-- Name: reviews reviews_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rmd
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(customer_id);


--
-- Name: reviews reviews_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rmd
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES public.restaurants(restaurant_id);


--
-- Name: usertype usertype_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rmd
--

ALTER TABLE ONLY public.usertype
    ADD CONSTRAINT usertype_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(customer_id);


--
-- Name: usertype usertype_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rmd
--

ALTER TABLE ONLY public.usertype
    ADD CONSTRAINT usertype_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES public.restaurants(restaurant_id);


--
-- PostgreSQL database dump complete
--

