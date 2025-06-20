--postgreSQL queries--
CREATE TABLE dim_customers(
    "Customer ID" text COLLATE pg_catalog."default" NOT NULL,
    "Customer Name" text COLLATE pg_catalog."default",
    "Email" text COLLATE pg_catalog."default",
    "Phone Number" text COLLATE pg_catalog."default",
    "Address Line 1" text COLLATE pg_catalog."default",
    "City" text COLLATE pg_catalog."default",
    "Country" text COLLATE pg_catalog."default",
    "Postcode" text COLLATE pg_catalog."default",
    "Loyalty Card" text COLLATE pg_catalog."default",
    "PhoneNumberValid" boolean,
    CONSTRAINT "Customers_pkey" PRIMARY KEY ("Customer ID")
)

CREATE TABLE dim_products (
    "Product ID" text COLLATE pg_catalog."default" NOT NULL,
    "Coffee Type" text COLLATE pg_catalog."default" NOT NULL,
    "Roast Type" "char" NOT NULL,
    "Size" real NOT NULL,
    "Unit Price" real NOT NULL,
    "Price per 100g" real NOT NULL,
    "Profit" real NOT NULL,
    CONSTRAINT "Products_pkey" PRIMARY KEY ("Product ID")
)

CREATE TABLE dim_time (
    "Order Date" date NOT NULL,
    "Day" text COLLATE pg_catalog."default" NOT NULL,
    "Month" text COLLATE pg_catalog."default" NOT NULL,
    "Year" integer NOT NULL,
    CONSTRAINT "Time_pkey" PRIMARY KEY ("Order Date")
)

CREATE TABLE fact_orders (
    "Order ID" text COLLATE pg_catalog."default" NOT NULL,
    "Order Date" date NOT NULL,
    "Customer ID" text COLLATE pg_catalog."default" NOT NULL,
    "Product ID" text COLLATE pg_catalog."default" NOT NULL,
    "Quantity" integer NOT NULL,
    CONSTRAINT "Orders_pkey" PRIMARY KEY ("Order ID", "Customer ID", "Product ID", "Quantity"),
    CONSTRAINT customer_id_fk FOREIGN KEY ("Customer ID") REFERENCES public.dim_customers ("Customer ID") MATCH SIMPLE,
    CONSTRAINT order_date_fk FOREIGN KEY ("Order Date") REFERENCES public.dim_time ("Order Date") MATCH SIMPLE,
    CONSTRAINT product_id_fk FOREIGN KEY ("Product ID") REFERENCES public.dim_products ("Product ID") MATCH SIMPLE
)

