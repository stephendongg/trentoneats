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
    restaurant_id integer NOT NULL,
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
-- Name: restaurants_restaurant_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.restaurants_restaurant_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: restaurants_restaurant_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.restaurants_restaurant_id_seq OWNED BY public.restaurants.restaurant_id;


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
-- Name: usertype; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.usertype (
    user_id integer NOT NULL,
    customer_id character varying(20),
    restaurant_id character varying(20),
    admin boolean,
    restaurant boolean,
    customer boolean
);


--
-- Name: usertype_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.usertype_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: usertype_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.usertype_user_id_seq OWNED BY public.usertype.user_id;


--
-- Name: restaurants restaurant_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.restaurants ALTER COLUMN restaurant_id SET DEFAULT nextval('public.restaurants_restaurant_id_seq'::regclass);


--
-- Name: usertype user_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usertype ALTER COLUMN user_id SET DEFAULT nextval('public.usertype_user_id_seq'::regclass);


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
1	1911 Smokehouse BBQ	11 W Front St, Trenton, NJ 08608	Monday\t11AM - 3:30PM,\n        Tuesday\t11AM - 3:30PM,\n        Wednesday 11AM - 10:30PM,\n        Thursday 11AM - 10:30PM,\n        Friday 11AM - 10:30PM,\n        Saturday 1 - 10:30PM,\n        Sunday 1 - 10:30PM	f	http://places.singleplatform.com/1911-smoke-house-barbeque/menu?ref=google	https://1911bbq.com	BBQ	12	5
2	Bamboo Grill Jamaican Restaurant	1005 Chambers St, Trenton, NJ 08611	Monday\t10AM - 7PM,\n        Tuesday\t10AM - 7PM,\n        Wednesday 10AM - 7PM,\n        Thursday 10AM - 7PM,\n        Friday 10AM - 8PM,\n        Saturday 10AM - 8PM,\n        Sunday Closed	t	None	None	Jamaican, Grill	1	3.2
3	Ila Mae's Restaurant	313 Market St, Trenton, NJ 08611	Monday\tClosed,\n        Tuesday\t9AM - 8PM,\n        Wednesday 9AM - 8PM,\n        Thursday 9AM - 8PM,\n        Friday 9AM - 8PM,\n        Saturday 9AM - 8PM,\n        Sunday Closed	f	http://places.singleplatform.com/ila-maes-restaurant/menu?ref=google	None	Soul	10	4.3
4	Blue Danube Restaurant	538 Adeline St, Trenton, NJ 08611	Monday\tClosed\n        Tuesday\t11:30AM - 2:15PM, 5 - 7:30PM,\n        Wednesday 11:30AM - 2:15PM, 5 - 7:30PM,\n        Thursday 11:30AM - 2:15PM, 5 - 7:30PM,\n        Friday 11:30AM - 2:15PM, 5 - 8PM,\n        Saturday 3 - 8PM,\n        Sunday 3 - 7:30PM	t	http://www.bluedanuberestaurant.net/menu.php	http://www.bluedanuberestaurant.net/about.php	Eastern European	273	4.6
5	The Big Easy of Trenton Restaurant	111 S Warren St, Trenton, NJ 08608	Monday\t12 - 7PM,\n        Tuesday\t12 - 7PM,\n        Wednesday 12 - 7PM,\n        Thursday 12 - 7PM,\n        Friday 12 - 7PM,\n        Saturday 9AM - 5PM,\n        Sunday Closed	f	None	None	Dine-in	260	4.5
6	Don Julio's Bar and Grill	900 Liberty St, Trenton, NJ 08611	Monday\t11AM - 2AM,\n        Tuesday\t11AM - 2AM,\n        Wednesday 11AM - 2AM,\n        Thursday 11AM - 2AM,\n        Friday 11AM - 2AM,\n        Saturday 11AM - 2AM,\n        Sunday 12PM - 2AM	t	None	None	Bar & Grill	190	4.3
7	The Hummingbird Restaurant	29 S Warren St, Trenton, NJ 08608	Monday\t10AM - 7PM,\n        Tuesday\t10AM - 7PM,\n        Wednesday 10AM - 7PM,\n        Thursday 10AM - 7PM,\n        Friday 10AM - 6PM,\n        Saturday 10AM - 6PM,\n        Sunday Closed	f	None	None	Jamaican	282	4.2
8	Sabor Latino	293 Ashmore Ave, Trenton, NJ 08611	Tuesday 10AM - 12AM,\n        Wednesday Closed,\n        Thursday 10AM - 12AM,\n        Friday 10AM - 2AM,\n        Saturday 10AM - 2AM,\n        Sunday 10AM - 12AM,\n        Monday 10AM - 12AM	t	None	None	Dominican	80	4.1
9	Trentini's	635 S Clinton Ave, Trenton, NJ 08611	Tuesday 10AM - 10PM,\n        Wednesday 10AM - 10PM,\n        Thursday 10AM - 10PM,\n        Friday 10AM - 10PM,\n        Saturday 10AM - 10PM,\n        Sunday 10AM - 10PM,\n        Monday 10AM - 10PM	f	https://trentinismenu.com/menu.html	https://trentinismenu.com/index.html	Italian	420	4.1
10	Mama D Soul Food 2	312 S Broad St, Trenton, NJ 08609	Tuesday Closed,\n        Wednesday 12 - 7PM,\n        Thursday 12 - 7PM,\n        Friday 12 - 7PM,\n        Saturday 9AM - 7PM,\n        Sunday 1 - 7PM,\n        Monday Closed	t	None	None	Soul	112	3.9
11	Cooper's Riverview	50 Riverview Plaza, Trenton, NJ 08611	Tuesday 12PM - 2AM,\n        Wednesday 12PM - 2AM,\n        Thursday 12PM - 2AM,\n        Friday 12PM - 2AM,\n        Saturday 12PM - 2AM,\n        Sunday 11:30AM - 11PM,\n        Monday Closed	f	coopersnj.com	None	English	455	4
12	Mi Ranchito Pizza and Tacos	911 Chambers St, Trenton, NJ 08611	Tuesday 10AM - 10PM,\n        Wednesday Closed,\n        Thursday 10AM - 10PM,\n        Friday 10AM - 10PM,\n        Saturday 10AM - 10PM,\n        Sunday 10AM - 10PM,\n        Monday 10AM - 10PM	t	None	None	Tacos	61	4.7
13	El Potrillo	541 Roebling Ave, Trenton, NJ 08611	Tuesday Closed,\n        Wednesday 10AM - 10PM,\n        Thursday 10AM - 10PM,\n        Friday 10AM - 10PM,\n        Saturday 10AM - 10PM,\n        Sunday 10AM - 10PM,\n        Monday 10AM - 10PM	f	http://places.singleplatform.com/el-potrillo-mexican-restaurant-7/menu?ref=google	None	Mexican	213	3.9
14	Chencha y Chole	865 S Broad St, Trenton, NJ 08611	11AM - 10PM everyday	t	None	None	Mexican	319	4.2
15	Casablanca Restaurant	140 Washington St, Trenton, NJ 08611	Monday\t11AM - 2AM,\n        Tuesday\t11AM - 2AM,\n        Wednesday 11AM - 2AM,\n        Thursday 11AM - 2AM,\n        Friday 11AM - 2AM,\n        Saturday 11AM - 2AM,\n        Sunday 11AM - 2AM	f	None	None	Spanish	372	4.1
16	c			t				0	0
17	c			t				0	0
18	c			t				0	0
19	c			t				0	0
20	c			t				0	0
21	c			t				0	0
22	b			t				0	0
23				t				0	0
24	a			t				0	0
25	a			t				0	0
26	c			t				0	0
27	c			t				0	0
28	c			t				0	0
29	c			t				0	0
30	c			t				0	0
31	c			t				0	0
32	c			t				0	0
33	c			t				0	0
34	c			t				0	0
35	c			t				0	0
36	c			t				0	0
37	c			t				0	0
38	c			t				0	0
39	c			t				0	0
40	c			t				0	0
41	c			t				0	0
42	c			t				0	0
43	c			t				0	0
44	c			t				0	0
45	c			t				0	0
46	c			t				0	0
47	c			t				0	0
48	c			t				0	0
49	c			t				0	0
50	c			t				0	0
51	c			t				0	0
52	c			t				0	0
53	c			t				0	0
54	c			t				0	0
55	c			t				0	0
56	c			t				0	0
57	c			t				0	0
58	c			t				0	0
59	c			t				0	0
60	c			t				0	0
61	c			t				0	0
62	c			t				0	0
63	c			t				0	0
64	c			t				0	0
65	c			t				0	0
66	c			t				0	0
67	c			t				0	0
68	c			t				0	0
69	c			t				0	0
70	c			t				0	0
71	c			t				0	0
72	c			t				0	0
73	c			t				0	0
74	c			t				0	0
75	c			t				0	0
76	c			t				0	0
77	c			t				0	0
78	c			t				0	0
79	c			t				0	0
80	c			t				0	0
81	c			t				0	0
82	c			t				0	0
83	c			t				0	0
84	c			t				0	0
85	c			t				0	0
86	c			t				0	0
87	c			t				0	0
88	c			t				0	0
89	c			t				0	0
90	c			t				0	0
91	c			t				0	0
92	c			t				0	0
93	c			t				0	0
94	c			t				0	0
95	c			t				0	0
96	c			t				0	0
97	c			t				0	0
98	c			t				0	0
99	c			t				0	0
100	c			t				0	0
101	c			t				0	0
102	c			t				0	0
103	c			t				0	0
104	c			t				0	0
105	c			t				0	0
106	c			t				0	0
107	c			t				0	0
108	c			t				0	0
109	c			t				0	0
110	c			t				0	0
111	c			t				0	0
112	c			t				0	0
113	c			t				0	0
114	c			t				0	0
115	c			t				0	0
116	c			t				0	0
117	c			t				0	0
118	c			t				0	0
119	c			t				0	0
120	c			t				0	0
121	c			t				0	0
122	c			t				0	0
123	c			t				0	0
124	c			t				0	0
125	c			t				0	0
126	c			t				0	0
127	c			t				0	0
128	c			t				0	0
129	c			t				0	0
130	c			t				0	0
131	c			t				0	0
132	c			t				0	0
133	c			t				0	0
134	c			t				0	0
135	c			t				0	0
136	c			t				0	0
137	c			t				0	0
138	c			t				0	0
139	c			t				0	0
140	c			t				0	0
141	c			t				0	0
142	c			t				0	0
143	c			t				0	0
144	c			t				0	0
145	c			t				0	0
146	c			t				0	0
147	c			t				0	0
148	c			t				0	0
149	c			t				0	0
150	c			t				0	0
151	c			t				0	0
152	c			t				0	0
153	c			t				0	0
154	c			t				0	0
155	c			t				0	0
156	c			t				0	0
157	c			t				0	0
158	c			t				0	0
159	c			t				0	0
160	c			t				0	0
161	c			t				0	0
162	c			t				0	0
163	c			t				0	0
164	c			t				0	0
165	c			t				0	0
166	c			t				0	0
167	c			t				0	0
168	c			t				0	0
169	c			t				0	0
170	c			t				0	0
171	c			t				0	0
172	c			t				0	0
173	c			t				0	0
174	c			t				0	0
175	c			t				0	0
176	c			t				0	0
177	c			t				0	0
178	c			t				0	0
179	c			t				0	0
180	c			t				0	0
181	c			t				0	0
182	c			t				0	0
183	c			t				0	0
184	c			t				0	0
185	c			t				0	0
186	c			t				0	0
187	c			t				0	0
188	c			t				0	0
189	c			t				0	0
190	c			t				0	0
191	c			t				0	0
192	c			t				0	0
193	c			t				0	0
194	c			t				0	0
195	c			t				0	0
196	c			t				0	0
197	c			t				0	0
198	c			t				0	0
199	c			t				0	0
200	c			t				0	0
201	c			t				0	0
202	c			t				0	0
203	c			t				0	0
204	c			t				0	0
205	c			t				0	0
206	c			t				0	0
207	c			t				0	0
208	c			t				0	0
209	c			t				0	0
210	c			t				0	0
211	c			t				0	0
212	c			t				0	0
213	c			t				0	0
214	c			t				0	0
215	c			t				0	0
216	c			t				0	0
217	c			t				0	0
218	c			t				0	0
219	c			t				0	0
220	c			t				0	0
221	c			t				0	0
222	c			t				0	0
223	c			t				0	0
224	c			t				0	0
225	c			t				0	0
226	c			t				0	0
227	c			t				0	0
228	c			t				0	0
229	c			t				0	0
230	c			t				0	0
231	c			t				0	0
232	c			t				0	0
233	c			t				0	0
234	c			t				0	0
235	c			t				0	0
236	c			t				0	0
237	c			t				0	0
238	c			t				0	0
239	c			t				0	0
240	c			t				0	0
241	c			t				0	0
242	c			t				0	0
243	c			t				0	0
244	c			t				0	0
245	c			t				0	0
246	c			t				0	0
247	c			t				0	0
248	c			t				0	0
249	c			t				0	0
250	c			t				0	0
251	c			t				0	0
252	c			t				0	0
253	c			t				0	0
254	c			t				0	0
255	c			t				0	0
256	c			t				0	0
257	c			t				0	0
258	c			t				0	0
259	c			t				0	0
260	c			t				0	0
261	c			t				0	0
262	c			t				0	0
263	c			t				0	0
264	c			t				0	0
265	c			t				0	0
266	c			t				0	0
267	c			t				0	0
268	c			t				0	0
269	c			t				0	0
270	c			t				0	0
271	c			t				0	0
272	c			t				0	0
273	c			t				0	0
274	c			t				0	0
275	c			t				0	0
276	c			t				0	0
277	c			t				0	0
278	c			t				0	0
279	c			t				0	0
280	c			t				0	0
281	c			t				0	0
282	c			t				0	0
283	c			t				0	0
284	c			t				0	0
285	c			t				0	0
286	c			t				0	0
287	c			t				0	0
288	c			t				0	0
289	c			t				0	0
290	c			t				0	0
291	c			t				0	0
292	c			t				0	0
293	c			t				0	0
294	c			t				0	0
295	c			t				0	0
296	c			t				0	0
297	c			t				0	0
298	c			t				0	0
299	c			t				0	0
300	c			t				0	0
301	c			t				0	0
302	c			t				0	0
303	c			t				0	0
304	c			t				0	0
305	c			t				0	0
306	c			t				0	0
307	c			t				0	0
308	c			t				0	0
309	c			t				0	0
310	c			t				0	0
311	c			t				0	0
312	c			t				0	0
313	c			t				0	0
314	c			t				0	0
315	c			t				0	0
316	c			t				0	0
317	c			t				0	0
318	c			t				0	0
319	c			t				0	0
320	c			t				0	0
321	c			t				0	0
322	c			t				0	0
323	c			t				0	0
324	c			t				0	0
325	c			t				0	0
326	c			t				0	0
327	c			t				0	0
328	c			t				0	0
329	c			t				0	0
330	c			t				0	0
331	c			t				0	0
332	c			t				0	0
333	c			t				0	0
334	c			t				0	0
335	c			t				0	0
336	c			t				0	0
337	c			t				0	0
338	c			t				0	0
339	c			t				0	0
340	c			t				0	0
341	c			t				0	0
342	c			t				0	0
343	c			t				0	0
344	c			t				0	0
345	c			t				0	0
346	c			t				0	0
347	c			t				0	0
348	c			t				0	0
349	c			t				0	0
350	c			t				0	0
351	c			t				0	0
352	c			t				0	0
353	c			t				0	0
354	c			t				0	0
355	c			t				0	0
356	c			t				0	0
357	c			t				0	0
358	c			t				0	0
359	c			t				0	0
360	c			t				0	0
361	c			t				0	0
362	c			t				0	0
363	c			t				0	0
364	c			t				0	0
365	c			t				0	0
366	c			t				0	0
367	c			t				0	0
368	c			t				0	0
369	c			t				0	0
370	c			t				0	0
371	c			t				0	0
372	c			t				0	0
373	c			t				0	0
374	c			t				0	0
375	c			t				0	0
376	c			t				0	0
377	c			t				0	0
378	c			t				0	0
379	c			t				0	0
380	c			t				0	0
381	c			t				0	0
382	c			t				0	0
383	c			t				0	0
384	c			t				0	0
385	c			t				0	0
386	c			t				0	0
387	c			t				0	0
388	c			t				0	0
389	c			t				0	0
390	c			t				0	0
391	c			t				0	0
392	c			t				0	0
393	c			t				0	0
394	c			t				0	0
395	c			t				0	0
396	c			t				0	0
397	c			t				0	0
398	c			t				0	0
399	c			t				0	0
400	c			t				0	0
401	c			t				0	0
402	c			t				0	0
403	c			t				0	0
404	c			t				0	0
405	c			t				0	0
406	c			t				0	0
407	c			t				0	0
408	c			t				0	0
409	c			t				0	0
410	c			t				0	0
411	c			t				0	0
412	c			t				0	0
413	c			t				0	0
414	c			t				0	0
415	c			t				0	0
416	c			t				0	0
417	c			t				0	0
418	c			t				0	0
419	c			t				0	0
420	c			t				0	0
421	c			t				0	0
422	c			t				0	0
423	c			t				0	0
424	c			t				0	0
425	c			t				0	0
426	c			t				0	0
427	c			t				0	0
428	c			t				0	0
429	c			t				0	0
430	c			t				0	0
431	c			t				0	0
432	c			t				0	0
433	c			t				0	0
434	c			t				0	0
435	c			t				0	0
436	c			t				0	0
437	c			t				0	0
438	c			t				0	0
439	c			t				0	0
440	c			t				0	0
441	c			t				0	0
442	c			t				0	0
443	c			t				0	0
444	c			t				0	0
445	c			t				0	0
446	c			t				0	0
447	c			t				0	0
448	c			t				0	0
449	c			t				0	0
450	c			t				0	0
451	c			t				0	0
452	c			t				0	0
453	c			t				0	0
454	c			t				0	0
455	c			t				0	0
456	c			t				0	0
457	c			t				0	0
458	c			t				0	0
459	c			t				0	0
460	c			t				0	0
461	c			t				0	0
462	c			t				0	0
463	c			t				0	0
464	c			t				0	0
465	c			t				0	0
466	c			t				0	0
467	c			t				0	0
468	c			t				0	0
469	c			t				0	0
470	c			t				0	0
471	c			t				0	0
472	c			t				0	0
473	c			t				0	0
474	c			t				0	0
475	c			t				0	0
476	c			t				0	0
477	c			t				0	0
478	c			t				0	0
479	c			t				0	0
480	c			t				0	0
481	c			t				0	0
482	c			t				0	0
483	c			t				0	0
484	c			t				0	0
485	c			t				0	0
486	c			t				0	0
487	c			t				0	0
488	c			t				0	0
489	c			t				0	0
490	c			t				0	0
491	c			t				0	0
492	c			t				0	0
493	c			t				0	0
494	c			t				0	0
495	c			t				0	0
496	c			t				0	0
497	c			t				0	0
498	c			t				0	0
499	c			t				0	0
500	c			t				0	0
501	c			t				0	0
502	c			t				0	0
503	c			t				0	0
504	c			t				0	0
505	c			t				0	0
506	c			t				0	0
507	c			t				0	0
508	c			t				0	0
509	c			t				0	0
510	c			t				0	0
511	c			t				0	0
512	c			t				0	0
513	c			t				0	0
514	c			t				0	0
515	c			t				0	0
516	c			t				0	0
517	c			t				0	0
518	c			t				0	0
519	c			t				0	0
520	c			t				0	0
521	c			t				0	0
522	c			t				0	0
523	c			t				0	0
524	c			t				0	0
525	c			t				0	0
526	c			t				0	0
527	c			t				0	0
528	c			t				0	0
529	c			t				0	0
530	c			t				0	0
531	c			t				0	0
532	c			t				0	0
533	c			t				0	0
534	c			t				0	0
535	c			t				0	0
536	c			t				0	0
537	c			t				0	0
538	c			t				0	0
539	c			t				0	0
540	c			t				0	0
541	c			t				0	0
542	c			t				0	0
543	c			t				0	0
544	c			t				0	0
545	c			t				0	0
546	c			t				0	0
547	c			t				0	0
548	c			t				0	0
549	c			t				0	0
550	c			t				0	0
551	c			t				0	0
552	c			t				0	0
553	c			t				0	0
554	c			t				0	0
555	c			t				0	0
556	c			t				0	0
557	c			t				0	0
558	c			t				0	0
559	c			t				0	0
560	c			t				0	0
561	c			t				0	0
562	c			t				0	0
563	c			t				0	0
564	c			t				0	0
565	c			t				0	0
566	c			t				0	0
567	c			t				0	0
568	c			t				0	0
569	c			t				0	0
570	c			t				0	0
571	c			t				0	0
572	c			t				0	0
573	c			t				0	0
574	c			t				0	0
575	c			t				0	0
576	c			t				0	0
577	c			t				0	0
578	c			t				0	0
579	c			t				0	0
580	c			t				0	0
581	c			t				0	0
582	c			t				0	0
583	c			t				0	0
584	c			t				0	0
585	c			t				0	0
586	c			t				0	0
587	c			t				0	0
588	c			t				0	0
589	c			t				0	0
590	c			t				0	0
591	c			t				0	0
592	c			t				0	0
593	c			t				0	0
594	c			t				0	0
595	c			t				0	0
596	c			t				0	0
597	c			t				0	0
598	c			t				0	0
599	c			t				0	0
600	c			t				0	0
601	c			t				0	0
602	c			t				0	0
603	c			t				0	0
604	c			t				0	0
605	c			t				0	0
606	c			t				0	0
607	c			t				0	0
608	c			t				0	0
609	c			t				0	0
610	c			t				0	0
611	c			t				0	0
612	c			t				0	0
613	c			t				0	0
614	c			t				0	0
615	c			t				0	0
616	c			t				0	0
617	c			t				0	0
618	c			t				0	0
619	c			t				0	0
620	c			t				0	0
621	c			t				0	0
622	c			t				0	0
623	c			t				0	0
624	c			t				0	0
625	c			t				0	0
626	c			t				0	0
627	c			t				0	0
628	c			t				0	0
629	c			t				0	0
630	c			t				0	0
631	c			t				0	0
632	c			t				0	0
633	c			t				0	0
634	c			t				0	0
635	c			t				0	0
636	c			t				0	0
637	c			t				0	0
638	c			t				0	0
639	c			t				0	0
640	c			t				0	0
641	c			t				0	0
642	c			t				0	0
643	c			t				0	0
644	c			t				0	0
645	c			t				0	0
646	c			t				0	0
647	c			t				0	0
648	c			t				0	0
649	c			t				0	0
650	c			t				0	0
651	c			t				0	0
652	c			t				0	0
653	c			t				0	0
654	c			t				0	0
655	c			t				0	0
656	c			t				0	0
657	c			t				0	0
658	c			t				0	0
659	c			t				0	0
660	c			t				0	0
661	c			t				0	0
662	c			t				0	0
663	c			t				0	0
664	c			t				0	0
665	c			t				0	0
666	c			t				0	0
667	c			t				0	0
668	c			t				0	0
669	c			t				0	0
670	c			t				0	0
671	c			t				0	0
672	c			t				0	0
673	c			t				0	0
674	c			t				0	0
675	c			t				0	0
676	c			t				0	0
677	c			t				0	0
678	c			t				0	0
679	c			t				0	0
680	c			t				0	0
681	c			t				0	0
682	c			t				0	0
683	c			t				0	0
684	c			t				0	0
685	c			t				0	0
686	c			t				0	0
687	c			t				0	0
688	c			t				0	0
689	c			t				0	0
690	c			t				0	0
691	c			t				0	0
692	c			t				0	0
693	c			t				0	0
694	c			t				0	0
695	c			t				0	0
696	c			t				0	0
697	c			t				0	0
698	c			t				0	0
699	c			t				0	0
700	c			t				0	0
701	c			t				0	0
702	c			t				0	0
703	c			t				0	0
704	c			t				0	0
705	c			t				0	0
706	c			t				0	0
707	c			t				0	0
708	c			t				0	0
709	c			t				0	0
710	c			t				0	0
711	c			t				0	0
712	c			t				0	0
713	c			t				0	0
714	c			t				0	0
715	c			t				0	0
716	c			t				0	0
717	c			t				0	0
718	c			t				0	0
719	c			t				0	0
720	c			t				0	0
721	c			t				0	0
722	c			t				0	0
723	c			t				0	0
724	c			t				0	0
725	c			t				0	0
726	c			t				0	0
727	c			t				0	0
728	c			t				0	0
729	c			t				0	0
730	c			t				0	0
731	c			t				0	0
732	c			t				0	0
733	c			t				0	0
734	c			t				0	0
735	c			t				0	0
736	c			t				0	0
737	c			t				0	0
738	c			t				0	0
739	c			t				0	0
740	c			t				0	0
741	c			t				0	0
742	c			t				0	0
743	c			t				0	0
744	c			t				0	0
745	c			t				0	0
746	c			t				0	0
747	c			t				0	0
748	c			t				0	0
749	c			t				0	0
750	c			t				0	0
751	c			t				0	0
752	c			t				0	0
753	c			t				0	0
754	c			t				0	0
755	c			t				0	0
756	c			t				0	0
757	c			t				0	0
758	c			t				0	0
759	c			t				0	0
760	c			t				0	0
761	c			t				0	0
762	c			t				0	0
763	c			t				0	0
764	c			t				0	0
765	c			t				0	0
766	c			t				0	0
767	c			t				0	0
768	c			t				0	0
769	c			t				0	0
770	c			t				0	0
771	c			t				0	0
772	c			t				0	0
773	c			t				0	0
774	c			t				0	0
775	c			t				0	0
776	c			t				0	0
777	c			t				0	0
778	c			t				0	0
779	c			t				0	0
780	c			t				0	0
781	c			t				0	0
782	c			t				0	0
783	c			t				0	0
784	c			t				0	0
785	c			t				0	0
786	c			t				0	0
787	c			t				0	0
788	c			t				0	0
789	c			t				0	0
790	c			t				0	0
791	c			t				0	0
792	c			t				0	0
793	c			t				0	0
794	c			t				0	0
795	c			t				0	0
796	c			t				0	0
797	c			t				0	0
798	c			t				0	0
799	c			t				0	0
800	c			t				0	0
801	c			t				0	0
802	c			t				0	0
803	c			t				0	0
804	c			t				0	0
805	c			t				0	0
806	c			t				0	0
807	c			t				0	0
808	c			t				0	0
809	c			t				0	0
810	c			t				0	0
811	c			t				0	0
812	c			t				0	0
813	c			t				0	0
814	c			t				0	0
815	c			t				0	0
816	c			t				0	0
817	c			t				0	0
818	c			t				0	0
819	c			t				0	0
820	c			t				0	0
821	c			t				0	0
822	c			t				0	0
823	c			t				0	0
824	c			t				0	0
825	c			t				0	0
826	c			t				0	0
827	c			t				0	0
828	c			t				0	0
829	c			t				0	0
830	c			t				0	0
831	c			t				0	0
832	c			t				0	0
833	c			t				0	0
834	c			t				0	0
835	c			t				0	0
836	c			t				0	0
837	c			t				0	0
838	c			t				0	0
839	c			t				0	0
840	c			t				0	0
841	c			t				0	0
842	c			t				0	0
843	c			t				0	0
844	c			t				0	0
845	c			t				0	0
846	c			t				0	0
847	c			t				0	0
848	c			t				0	0
849	c			t				0	0
850	c			t				0	0
851	c			t				0	0
852	c			t				0	0
853	c			t				0	0
854	c			t				0	0
855	c			t				0	0
856	c			t				0	0
857	c			t				0	0
858	c			t				0	0
859	c			t				0	0
860	c			t				0	0
861	c			t				0	0
862	c			t				0	0
863	c			t				0	0
864	c			t				0	0
865	c			t				0	0
866	c			t				0	0
867	c			t				0	0
868	c			t				0	0
869	c			t				0	0
870	c			t				0	0
871	c			t				0	0
872	c			t				0	0
873	c			t				0	0
874	c			t				0	0
875	c			t				0	0
876	c			t				0	0
877	c			t				0	0
878	c			t				0	0
879	c			t				0	0
880	c			t				0	0
881	c			t				0	0
882	c			t				0	0
883	c			t				0	0
884	c			t				0	0
885	c			t				0	0
886	c			t				0	0
887	c			t				0	0
888	c			t				0	0
889	c			t				0	0
890	c			t				0	0
891	c			t				0	0
892	c			t				0	0
893	c			t				0	0
894	c			t				0	0
895	c			t				0	0
896	c			t				0	0
897	c			t				0	0
898	c			t				0	0
899	c			t				0	0
900	c			t				0	0
901	c			t				0	0
902	c			t				0	0
903	c			t				0	0
904	c			t				0	0
905	c			t				0	0
906	c			t				0	0
907	c			t				0	0
908	c			t				0	0
909	c			t				0	0
910	c			t				0	0
911	c			t				0	0
912	c			t				0	0
913	c			t				0	0
914	c			t				0	0
915	c			t				0	0
916	c			t				0	0
917	c			t				0	0
918	c			t				0	0
919	c			t				0	0
920	c			t				0	0
921	c			t				0	0
922	c			t				0	0
923	c			t				0	0
924	c			t				0	0
925	c			t				0	0
926	c			t				0	0
927	c			t				0	0
928	c			t				0	0
929	c			t				0	0
930	c			t				0	0
931	c			t				0	0
932	c			t				0	0
933	c			t				0	0
934	c			t				0	0
935	c			t				0	0
936	c			t				0	0
937	c			t				0	0
938	c			t				0	0
939	c			t				0	0
940	c			t				0	0
941	c			t				0	0
942	c			t				0	0
943	c			t				0	0
944	c			t				0	0
945	c			t				0	0
946	c			t				0	0
947	c			t				0	0
948	c			t				0	0
949	c			t				0	0
950	c			t				0	0
951	c			t				0	0
952	c			t				0	0
953	c			t				0	0
954	c			t				0	0
955	c			t				0	0
956	c			t				0	0
957	c			t				0	0
958	c			t				0	0
959	c			t				0	0
960	c			t				0	0
961	c			t				0	0
962	c			t				0	0
963	c			t				0	0
964	c			t				0	0
965	c			t				0	0
966	c			t				0	0
967	c			t				0	0
968	c			t				0	0
969	c			t				0	0
970	c			t				0	0
971	c			t				0	0
972	c			t				0	0
973	c			t				0	0
974	c			t				0	0
975	c			t				0	0
976	c			t				0	0
977	c			t				0	0
978	c			t				0	0
979	c			t				0	0
980	c			t				0	0
981	c			t				0	0
982	c			t				0	0
983	c			t				0	0
984	c			t				0	0
985	c			t				0	0
986	c			t				0	0
987	c			t				0	0
988	c			t				0	0
989	c			t				0	0
990	c			t				0	0
991	c			t				0	0
992	c			t				0	0
993	c			t				0	0
994	c			t				0	0
995	c			t				0	0
996	c			t				0	0
997	a			t				0	0
998	a			t				0	0
999	a			t				0	0
1000	a			t				0	0
1001	a			t				0	0
1002	a			t				0	0
1003	a			t				0	0
1004	a			t				0	0
1005	a			t				0	0
1006	a			t				0	0
1007	a			t				0	0
1008	a			t				0	0
1009	a			t				0	0
1010	a			t				0	0
1011	a			t				0	0
1012	a			t				0	0
1013	a			t				0	0
1014	a			t				0	0
1015	a			t				0	0
1016	a			t				0	0
1017	a			t				0	0
1018	a			t				0	0
1019	a			t				0	0
1020	a			t				0	0
1021	a			t				0	0
1022	a			t				0	0
1023	a			t				0	0
1024	a			t				0	0
1025	a			t				0	0
1026	a			t				0	0
1027	a			t				0	0
1028	a			t				0	0
1029	a			t				0	0
1030	a			t				0	0
1031	a			t				0	0
1032	a			t				0	0
1033	a			t				0	0
1034	a			t				0	0
1035	a			t				0	0
1036	a			t				0	0
1037	a			t				0	0
1038	a			t				0	0
1039	a			t				0	0
1040	a			t				0	0
1041	a			t				0	0
1042	a			t				0	0
1043	a			t				0	0
1044	a			t				0	0
1045	a			t				0	0
1046	a			t				0	0
1047	a			t				0	0
1048	a			t				0	0
1049	a			t				0	0
1050	a			t				0	0
1051	a			t				0	0
1052	a			t				0	0
1053	a			t				0	0
1054	a			t				0	0
1055	a			t				0	0
1056	a			t				0	0
1057	a			t				0	0
1058	a			t				0	0
1059	a			t				0	0
1060	a			t				0	0
1061	a			t				0	0
1062	a			t				0	0
1063	a			t				0	0
1064	a			t				0	0
1065	a			t				0	0
1066	a			t				0	0
1067	a			t				0	0
1068	a			t				0	0
1069	a			t				0	0
1070	a			t				0	0
1071	a			t				0	0
1072	a			t				0	0
1073	a			t				0	0
1074	a			t				0	0
1075	a			t				0	0
1076	a			t				0	0
1077	a			t				0	0
1078	a			t				0	0
1079	a			t				0	0
1080	a			t				0	0
1081	a			t				0	0
1082	a			t				0	0
1083	a			t				0	0
1084	a			t				0	0
1085	a			t				0	0
1086	a			t				0	0
1087	a			t				0	0
1088	a			t				0	0
1089	a			t				0	0
1090	a			t				0	0
1091	a			t				0	0
1092	a			t				0	0
1093	a			t				0	0
1094	a			t				0	0
1095	a			t				0	0
1096	a			t				0	0
1097	a			t				0	0
1098	a			t				0	0
1099	a			t				0	0
1100	a			t				0	0
1101	a			t				0	0
1102	a			t				0	0
1103	a			t				0	0
1104	a			t				0	0
1105	a			t				0	0
1106	a			t				0	0
1107	a			t				0	0
1108	a			t				0	0
1109	a			t				0	0
1110	a			t				0	0
1111	a			t				0	0
1112	a			t				0	0
1113	a			t				0	0
1114	a			t				0	0
1115	a			t				0	0
1116	a			t				0	0
1117	a			t				0	0
1118	a			t				0	0
1119	a			t				0	0
1120	a			t				0	0
1121	a			t				0	0
1122	a			t				0	0
1123	a			t				0	0
1124	a			t				0	0
1125	a			t				0	0
1126	a			t				0	0
1127	a			t				0	0
1128	a			t				0	0
1129	a			t				0	0
1130	a			t				0	0
1131	a			t				0	0
1132	a			t				0	0
1133	a			t				0	0
1134	a			t				0	0
1135	a			t				0	0
1136	a			t				0	0
1137	a			t				0	0
1138	a			t				0	0
1139	a			t				0	0
1140	a			t				0	0
1141	a			t				0	0
1142	a			t				0	0
1143	a			t				0	0
1144	a			t				0	0
1145	a			t				0	0
1146	a			t				0	0
1147	a			t				0	0
1148	a			t				0	0
1149	a			t				0	0
1150	a			t				0	0
1151	a			t				0	0
1152	a			t				0	0
1153	a			t				0	0
1154	a			t				0	0
1155	a			t				0	0
1156	a			t				0	0
1157	a			t				0	0
1158	a			t				0	0
1159	a			t				0	0
1160	a			t				0	0
1161	a			t				0	0
1162	a			t				0	0
1163	a			t				0	0
1164	a			t				0	0
1165	a			t				0	0
1166	a			t				0	0
1167	a			t				0	0
1168	a			t				0	0
1169	a			t				0	0
1170	a			t				0	0
1171	a			t				0	0
1172	a			t				0	0
1173	a			t				0	0
1174	a			t				0	0
1175	a			t				0	0
1176	a			t				0	0
1177	a			t				0	0
1178	a			t				0	0
1179	a			t				0	0
1180	a			t				0	0
1181	a			t				0	0
1182	a			t				0	0
1183	a			t				0	0
1184	a			t				0	0
1185	a			t				0	0
1186	a			t				0	0
1187	a			t				0	0
1188	a			t				0	0
1189	a			t				0	0
1190	a			t				0	0
1191	a			t				0	0
1192	a			t				0	0
1193	a			t				0	0
1194	a			t				0	0
1195	a			t				0	0
1196	a			t				0	0
1197	a			t				0	0
1198	a			t				0	0
1199	a			t				0	0
1200	a			t				0	0
1201	a			t				0	0
1202	a			t				0	0
1203	a			t				0	0
1204	a			t				0	0
1205	a			t				0	0
1206	a			t				0	0
1207	a			t				0	0
1208	a			t				0	0
1209	a			t				0	0
1210	a			t				0	0
1211	a			t				0	0
1212	a			t				0	0
1213	a			t				0	0
1214	a			t				0	0
1215	a			t				0	0
1216	a			t				0	0
1217	a			t				0	0
1218	a			t				0	0
1219	a			t				0	0
1220	a			t				0	0
1221	a			t				0	0
1222	a			t				0	0
1223	a			t				0	0
1224	a			t				0	0
1225	a			t				0	0
1226	a			t				0	0
1227	a			t				0	0
1228	a			t				0	0
1229	a			t				0	0
1230	a			t				0	0
1231	a			t				0	0
1232	a			t				0	0
1233	a			t				0	0
1234	a			t				0	0
1235	a			t				0	0
1236	a			t				0	0
1237	a			t				0	0
1238	a			t				0	0
1239	a			t				0	0
1240	a			t				0	0
1241	a			t				0	0
1242	a			t				0	0
1243	a			t				0	0
1244	a			t				0	0
1245	a			t				0	0
1246	a			t				0	0
1247	a			t				0	0
1248	a			t				0	0
1249	a			t				0	0
1250	a			t				0	0
1251	a			t				0	0
1252	a			t				0	0
1253	a			t				0	0
1254	a			t				0	0
1255	a			t				0	0
1256	a			t				0	0
1257	a			t				0	0
1258	a			t				0	0
1259	a			t				0	0
1260	a			t				0	0
1261	a			t				0	0
1262	a			t				0	0
1263	a			t				0	0
1264	a			t				0	0
1265	a			t				0	0
1266	a			t				0	0
1267	a			t				0	0
1268	a			t				0	0
1269	a			t				0	0
1270	a			t				0	0
1271	a			t				0	0
1272	a			t				0	0
1273	a			t				0	0
1274	a			t				0	0
1275	a			t				0	0
1276	a			t				0	0
1277	a			t				0	0
1278	a			t				0	0
1279	a			t				0	0
1280	a			t				0	0
1281	a			t				0	0
1282	a			t				0	0
1283	a			t				0	0
1284	a			t				0	0
1285	a			t				0	0
1286	a			t				0	0
1287	a			t				0	0
1288	a			t				0	0
1289	a			t				0	0
1290	a			t				0	0
1291	a			t				0	0
1292	a			t				0	0
1293	a			t				0	0
1294	a			t				0	0
1295	a			t				0	0
1296	a			t				0	0
1297	a			t				0	0
1298	a			t				0	0
1299	a			t				0	0
1300	a			t				0	0
1301	a			t				0	0
1302	a			t				0	0
1303	a			t				0	0
1304	a			t				0	0
1305	a			t				0	0
1306	a			t				0	0
1307	a			t				0	0
1308	a			t				0	0
1309	a			t				0	0
1310	a			t				0	0
1311	a			t				0	0
1312	a			t				0	0
1313	a			t				0	0
1314	a			t				0	0
1315	a			t				0	0
1316	a			t				0	0
1317	a			t				0	0
1318	a			t				0	0
1319	a			t				0	0
1320	a			t				0	0
1321	a			t				0	0
1322	a			t				0	0
1323	a			t				0	0
1324	a			t				0	0
1325	a			t				0	0
1326	a			t				0	0
1327	a			t				0	0
1328	a			t				0	0
1329	a			t				0	0
1330	a			t				0	0
1331	a			t				0	0
1332	a			t				0	0
1333	a			t				0	0
1334	a			t				0	0
1335	a			t				0	0
1336	a			t				0	0
1337	a			t				0	0
1338	a			t				0	0
1339	a			t				0	0
1340	a			t				0	0
1341	a			t				0	0
1342	a			t				0	0
1343	a			t				0	0
1344	a			t				0	0
1345	a			t				0	0
1346	a			t				0	0
1347	a			t				0	0
1348	a			t				0	0
1349	a			t				0	0
1350	a			t				0	0
1351	a			t				0	0
1352	a			t				0	0
1353	a			t				0	0
1354	a			t				0	0
1355	a			t				0	0
1356	a			t				0	0
1357	a			t				0	0
1358	a			t				0	0
1359	a			t				0	0
1360	a			t				0	0
1361	a			t				0	0
1362	a			t				0	0
1363	a			t				0	0
1364	a			t				0	0
1365	a			t				0	0
1366	a			t				0	0
1367	a			t				0	0
1368	a			t				0	0
1369	a			t				0	0
1370	a			t				0	0
1371	a			t				0	0
1372	a			t				0	0
1373	a			t				0	0
1374	a			t				0	0
1375	a			t				0	0
1376	a			t				0	0
1377	a			t				0	0
1378	a			t				0	0
1379	a			t				0	0
1380	a			t				0	0
1381	a			t				0	0
1382	a			t				0	0
1383	a			t				0	0
1384	a			t				0	0
1385	a			t				0	0
1386	a			t				0	0
1387	a			t				0	0
1388	a			t				0	0
1389	a			t				0	0
1390	a			t				0	0
1391	a			t				0	0
1392	a			t				0	0
1393	a			t				0	0
1394	a			t				0	0
1395	a			t				0	0
1396	a			t				0	0
1397	a			t				0	0
1398	a			t				0	0
1399	a			t				0	0
1400	a			t				0	0
1401	a			t				0	0
1402	a			t				0	0
1403	a			t				0	0
1404	a			t				0	0
1405	a			t				0	0
1406	a			t				0	0
1407	a			t				0	0
1408	a			t				0	0
1409	a			t				0	0
1410	a			t				0	0
1411	a			t				0	0
1412	a			t				0	0
1413	a			t				0	0
1414	a			t				0	0
1415	a			t				0	0
1416	a			t				0	0
1417	a			t				0	0
1418	a			t				0	0
1419	a			t				0	0
1420	a			t				0	0
1421	a			t				0	0
1422	a			t				0	0
1423	a			t				0	0
1424	a			t				0	0
1425	a			t				0	0
1426	a			t				0	0
1427	a			t				0	0
1428	a			t				0	0
1429	a			t				0	0
1430	a			t				0	0
1431	a			t				0	0
1432	a			t				0	0
1433	a			t				0	0
1434	a			t				0	0
1435	a			t				0	0
1436	a			t				0	0
1437	a			t				0	0
1438	a			t				0	0
1439	a			t				0	0
1440	a			t				0	0
1441	a			t				0	0
1442	a			t				0	0
1443	a			t				0	0
1444	a			t				0	0
1445	a			t				0	0
1446	a			t				0	0
1447	a			t				0	0
1448	a			t				0	0
1449	a			t				0	0
1450	a			t				0	0
1451	a			t				0	0
1452	a			t				0	0
1453	a			t				0	0
1454	a			t				0	0
1455	a			t				0	0
1456	a			t				0	0
1457	a			t				0	0
1458	a			t				0	0
1459	a			t				0	0
1460	a			t				0	0
1461	a			t				0	0
1462	a			t				0	0
1463	a			t				0	0
1464	a			t				0	0
1465	a			t				0	0
1466	a			t				0	0
1467	a			t				0	0
1468	a			t				0	0
1469	a			t				0	0
1470	a			t				0	0
1471	a			t				0	0
1472	a			t				0	0
1473	a			t				0	0
1474	a			t				0	0
1475	a			t				0	0
1476	a			t				0	0
1477	a			t				0	0
1478	a			t				0	0
1479	a			t				0	0
1480	a			t				0	0
1481	a			t				0	0
1482	a			t				0	0
1483	a			t				0	0
1484	a			t				0	0
1485	a			t				0	0
1486	a			t				0	0
1487	a			t				0	0
1488	a			t				0	0
1489	a			t				0	0
1490	a			t				0	0
1491	a			t				0	0
1492	a			t				0	0
1493	a			t				0	0
1494	a			t				0	0
1495	a			t				0	0
1496	a			t				0	0
1497	a			t				0	0
1498	a			t				0	0
1499	a			t				0	0
1500	a			t				0	0
1501	a			t				0	0
1502	a			t				0	0
1503	a			t				0	0
1504	a			t				0	0
1505	a			t				0	0
1506	a			t				0	0
1507	a			t				0	0
1508	a			t				0	0
1509	a			t				0	0
1510	a			t				0	0
1511	a			t				0	0
1512	a			t				0	0
1513	a			t				0	0
1514	a			t				0	0
1515	a			t				0	0
1516	a			t				0	0
1517	a			t				0	0
1518	a			t				0	0
1519	a			t				0	0
1520	a			t				0	0
1521	a			t				0	0
1522	a			t				0	0
1523	a			t				0	0
1524	a			t				0	0
1525	a			t				0	0
1526	a			t				0	0
1527	a			t				0	0
1528	a			t				0	0
1529	a			t				0	0
1530	a			t				0	0
1531	a			t				0	0
1532	a			t				0	0
1533	a			t				0	0
1534	a			t				0	0
1535	a			t				0	0
1536	a			t				0	0
1537	a			t				0	0
1538	a			t				0	0
1539	a			t				0	0
1540	a			t				0	0
1541	a			t				0	0
1542	a			t				0	0
1543	a			t				0	0
1544	a			t				0	0
1545	a			t				0	0
1546	a			t				0	0
1547	a			t				0	0
1548	a			t				0	0
1549	a			t				0	0
1550	a			t				0	0
1551	a			t				0	0
1552	a			t				0	0
1553	a			t				0	0
1554	a			t				0	0
1555	a			t				0	0
1556	a			t				0	0
1557	a			t				0	0
1558	a			t				0	0
1559	a			t				0	0
1560	a			t				0	0
1561	a			t				0	0
1562	a			t				0	0
1563	a			t				0	0
1564	a			t				0	0
1565	a			t				0	0
1566	a			t				0	0
1567	a			t				0	0
1568	a			t				0	0
1569	a			t				0	0
1570	a			t				0	0
1571	a			t				0	0
1572	a			t				0	0
1573	a			t				0	0
1574	a			t				0	0
1575	a			t				0	0
1576	a			t				0	0
1577	a			t				0	0
1578	a			t				0	0
1579	a			t				0	0
1580	a			t				0	0
1581	a			t				0	0
1582	a			t				0	0
1583	a			t				0	0
1584	a			t				0	0
1585	a			t				0	0
1586	a			t				0	0
1587	a			t				0	0
1588	a			t				0	0
1589	a			t				0	0
1590	a			t				0	0
1591	a			t				0	0
1592	a			t				0	0
1593	a			t				0	0
1594	a			t				0	0
1595	a			t				0	0
1596	a			t				0	0
1597	a			t				0	0
1598	a			t				0	0
1599	a			t				0	0
1600	a			t				0	0
1601	a			t				0	0
1602	a			t				0	0
1603	a			t				0	0
1604	a			t				0	0
1605	a			t				0	0
1606	a			t				0	0
1607	a			t				0	0
1608	a			t				0	0
1609	a			t				0	0
1610	a			t				0	0
1611	a			t				0	0
1612	a			t				0	0
1613	a			t				0	0
1614	a			t				0	0
1615	a			t				0	0
1616	a			t				0	0
1617	a			t				0	0
1618	a			t				0	0
1619	a			t				0	0
1620	a			t				0	0
1621	a			t				0	0
1622	a			t				0	0
1623	a			t				0	0
1624	a			t				0	0
1625	a			t				0	0
1626	a			t				0	0
1627	a			t				0	0
1628	a			t				0	0
1629	a			t				0	0
1630	a			t				0	0
1631	a			t				0	0
1632	a			t				0	0
1633	a			t				0	0
1634	a			t				0	0
1635	a			t				0	0
1636	a			t				0	0
1637	a			t				0	0
1638	a			t				0	0
1639	a			t				0	0
1640	a			t				0	0
1641	a			t				0	0
1642	a			t				0	0
1643	a			t				0	0
1644	a			t				0	0
1645	a			t				0	0
1646	a			t				0	0
1647	a			t				0	0
1648	a			t				0	0
1649	a			t				0	0
1650	a			t				0	0
1651	a			t				0	0
1652	a			t				0	0
1653	a			t				0	0
1654	a			t				0	0
1655	a			t				0	0
1656	a			t				0	0
1657	a			t				0	0
1658	a			t				0	0
1659	a			t				0	0
1660	a			t				0	0
1661	a			t				0	0
1662	a			t				0	0
1663	a			t				0	0
1664	a			t				0	0
1665	a			t				0	0
1666	a			t				0	0
1667	a			t				0	0
1668	a			t				0	0
1669	a			t				0	0
1670	a			t				0	0
1671	a			t				0	0
1672	a			t				0	0
1673	a			t				0	0
1674	a			t				0	0
1675	a			t				0	0
1676	a			t				0	0
1677	a			t				0	0
1678	a			t				0	0
1679	a			t				0	0
1680	a			t				0	0
1681	a			t				0	0
1682	a			t				0	0
1683	a			t				0	0
1684	a			t				0	0
1685	a			t				0	0
1686	a			t				0	0
1687	a			t				0	0
1688	a			t				0	0
1689	a			t				0	0
1690	a			t				0	0
1691	a			t				0	0
1692	a			t				0	0
1693	a			t				0	0
1694	a			t				0	0
1695	a			t				0	0
1696	a			t				0	0
1697	a			t				0	0
1698	a			t				0	0
1699	a			t				0	0
1700	a			t				0	0
1701	a			t				0	0
1702	a			t				0	0
1703	a			t				0	0
1704	a			t				0	0
1705	a			t				0	0
1706	a			t				0	0
1707	a			t				0	0
1708	a			t				0	0
1709	a			t				0	0
1710	a			t				0	0
1711	a			t				0	0
1712	a			t				0	0
1713	a			t				0	0
1714	a			t				0	0
1715	a			t				0	0
1716	a			t				0	0
1717	a			t				0	0
1718	a			t				0	0
1719	a			t				0	0
1720	a			t				0	0
1721	a			t				0	0
1722	a			t				0	0
1723	a			t				0	0
1724	a			t				0	0
1725	a			t				0	0
1726	a			t				0	0
1727	a			t				0	0
1728	a			t				0	0
1729	a			t				0	0
1730	a			t				0	0
1731	a			t				0	0
1732	a			t				0	0
1733	a			t				0	0
1734	a			t				0	0
1735	a			t				0	0
1736	a			t				0	0
1737	a			t				0	0
1738	a			t				0	0
1739	a			t				0	0
1740	a			t				0	0
1741	a			t				0	0
1742	a			t				0	0
1743	a			t				0	0
1744	a			t				0	0
1745	a			t				0	0
1746	a			t				0	0
1747	a			t				0	0
1748	a			t				0	0
1749	a			t				0	0
1750	a			t				0	0
1751	a			t				0	0
1752	a			t				0	0
1753	a			t				0	0
1754	a			t				0	0
1755	a			t				0	0
1756	a			t				0	0
1757	a			t				0	0
1758	a			t				0	0
1759	a			t				0	0
1760	a			t				0	0
1761	a			t				0	0
1762	a			t				0	0
1763	a			t				0	0
1764	a			t				0	0
1765	a			t				0	0
1766	a			t				0	0
1767	a			t				0	0
1768	a			t				0	0
1769	a			t				0	0
1770	a			t				0	0
1771	a			t				0	0
1772	a			t				0	0
1773	a			t				0	0
1774	a			t				0	0
1775	a			t				0	0
1776	a			t				0	0
1777	a			t				0	0
1778	a			t				0	0
1779	a			t				0	0
1780	a			t				0	0
1781	a			t				0	0
1782	a			t				0	0
1783	a			t				0	0
1784	a			t				0	0
1785	a			t				0	0
1786	a			t				0	0
1787	a			t				0	0
1788	a			t				0	0
1789	a			t				0	0
1790	a			t				0	0
1791	a			t				0	0
1792	a			t				0	0
1793	a			t				0	0
1794	a			t				0	0
1795	a			t				0	0
1796	a			t				0	0
1797	a			t				0	0
1798	a			t				0	0
1799	a			t				0	0
1800	a			t				0	0
1801	a			t				0	0
1802	a			t				0	0
1803	a			t				0	0
1804	a			t				0	0
1805	a			t				0	0
1806	a			t				0	0
1807	a			t				0	0
1808	a			t				0	0
1809	a			t				0	0
1810	a			t				0	0
1811	a			t				0	0
1812	a			t				0	0
1813	a			t				0	0
1814	a			t				0	0
1815	a			t				0	0
1816	a			t				0	0
1817	a			t				0	0
1818	a			t				0	0
1819	a			t				0	0
1820	a			t				0	0
1821	a			t				0	0
1822	a			t				0	0
1823	a			t				0	0
1824	a			t				0	0
1825	a			t				0	0
1826	a			t				0	0
1827	a			t				0	0
1828	a			t				0	0
1829	a			t				0	0
1830	a			t				0	0
1831	a			t				0	0
1832	a			t				0	0
1833	a			t				0	0
1834	a			t				0	0
1835	a			t				0	0
1836	a			t				0	0
1837	a			t				0	0
1838	a			t				0	0
1839	a			t				0	0
1840	a			t				0	0
1841	a			t				0	0
1842	a			t				0	0
1843	a			t				0	0
1844	a			t				0	0
1845	a			t				0	0
1846	a			t				0	0
1847	a			t				0	0
1848	a			t				0	0
1849	a			t				0	0
1850	a			t				0	0
1851	a			t				0	0
1852	a			t				0	0
1853	a			t				0	0
1854	a			t				0	0
1855	a			t				0	0
1856	a			t				0	0
1857	a			t				0	0
1858	a			t				0	0
1859	a			t				0	0
1860	a			t				0	0
1861	a			t				0	0
1862	a			t				0	0
1863	a			t				0	0
1864	a			t				0	0
1865	a			t				0	0
1866	a			t				0	0
1867	a			t				0	0
1868	a			t				0	0
1869	a			t				0	0
1870	a			t				0	0
1871	a			t				0	0
1872	a			t				0	0
1873	a			t				0	0
1874	a			t				0	0
1875	a			t				0	0
1876	a			t				0	0
1877	a			t				0	0
1878	a			t				0	0
1879	a			t				0	0
1880	a			t				0	0
1881	a			t				0	0
1882	a			t				0	0
1883	a			t				0	0
1884	a			t				0	0
1885	a			t				0	0
1886	a			t				0	0
1887	a			t				0	0
1888	a			t				0	0
1889	a			t				0	0
1890	a			t				0	0
1891	a			t				0	0
1892	a			t				0	0
1893	a			t				0	0
1894	a			t				0	0
1895	a			t				0	0
1896	a			t				0	0
1897	a			t				0	0
1898	a			t				0	0
1899	a			t				0	0
1900	a			t				0	0
1901	a			t				0	0
1902	a			t				0	0
1903	a			t				0	0
1904	a			t				0	0
1905	a			t				0	0
1906	a			t				0	0
1907	a			t				0	0
1908	a			t				0	0
1909	a			t				0	0
1910	a			t				0	0
1911	a			t				0	0
1912	a			t				0	0
1913	a			t				0	0
1914	a			t				0	0
1915	a			t				0	0
1916	a			t				0	0
1917	a			t				0	0
1918	a			t				0	0
1919	a			t				0	0
1920	a			t				0	0
1921	a			t				0	0
1922	a			t				0	0
1923	a			t				0	0
1924	a			t				0	0
1925	a			t				0	0
1926	a			t				0	0
1927	a			t				0	0
1928	a			t				0	0
1929	a			t				0	0
1930	a			t				0	0
1931	a			t				0	0
1932	a			t				0	0
1933	a			t				0	0
1934	a			t				0	0
1935	a			t				0	0
1936	a			t				0	0
1937	a			t				0	0
1938	a			t				0	0
1939	a			t				0	0
1940	a			t				0	0
1941	a			t				0	0
1942	a			t				0	0
1943	a			t				0	0
1944	a			t				0	0
1945	a			t				0	0
1946	a			t				0	0
1947	a			t				0	0
1948	a			t				0	0
1949	a			t				0	0
1950	a			t				0	0
1951	a			t				0	0
1952	a			t				0	0
1953	a			t				0	0
1954	a			t				0	0
1955	a			t				0	0
1956	a			t				0	0
1957	a			t				0	0
1958	a			t				0	0
1959	a			t				0	0
1960	a			t				0	0
1961	a			t				0	0
1962	a			t				0	0
1963	a			t				0	0
1964	a			t				0	0
1965	a			t				0	0
1966	a			t				0	0
1967	a			t				0	0
1968	test			t				0	0
1969	taco			t				0	0
1970				t				0	0
1971				t				0	0
1972	bur			t				0	0
1973	bur			t				0	0
1974	bur			t				0	0
1975	c			t				0	0
1976	c			t				0	0
\.


--
-- Data for Name: reviews; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.reviews (review_id, customer_id, restaurant_id, date, text, price, taste, authenticity, coolness, overall) FROM stdin;
\.


--
-- Data for Name: usertype; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.usertype (user_id, customer_id, restaurant_id, admin, restaurant, customer) FROM stdin;
\.


--
-- Name: restaurants_restaurant_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.restaurants_restaurant_id_seq', 1976, true);


--
-- Name: usertype_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.usertype_user_id_seq', 1, false);


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
-- Name: usertype usertype_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usertype
    ADD CONSTRAINT usertype_pkey PRIMARY KEY (user_id);


--
-- Name: reviews reviews_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(customer_id);


--
-- Name: usertype usertype_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usertype
    ADD CONSTRAINT usertype_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(customer_id);


--
-- PostgreSQL database dump complete
--

