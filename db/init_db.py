import db_service

create_test_table = """
CREATE TABLE if not exists base_user (
	last_login timestamptz ,
	is_superuser bool  ,
	username varchar(150)  ,
	first_name varchar(150)  ,
	last_name varchar(150)  ,
	email varchar(254)  ,
	is_staff bool  ,
	is_active bool  ,
	date_joined timestamptz ,
	id int8 ,
	seed_code int4 ,
	telegram_username varchar(64) ,
	telegram_language_code varchar(16) ,
	timezone interval ,
	current_utrl varchar(64) ,
	current_utrl_code_dttm timestamptz ,
	current_utrl_context_db varchar(4096) ,
	current_utrl_form_db varchar(4096) ,
	CONSTRAINT base_user_pkey PRIMARY KEY (id),
	CONSTRAINT base_user_username_key UNIQUE (username)
);
CREATE INDEX base_user_username_59bfc15c_like ON public.base_user USING btree (username varchar_pattern_ops);
"""

db_service.execute(create_test_table)