
   CREATE TABLE customers_log (
  id SERIAL PRIMARY KEY,
  table_name VARCHAR(255) NOT NULL,
  action VARCHAR(255) NOT NULL,
  timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE OR REPLACE FUNCTION address_insert_trigger()
  RETURNS TRIGGER AS $$
  BEGIN
    INSERT INTO customers_log (table_name, action)
    VALUES ('address', 'insert');
    RETURN NEW;
  END;
$$ LANGUAGE plpgsql;





CREATE TRIGGER category_insert
  AFTER INSERT ON category
  FOR EACH ROW
  EXECUTE FUNCTION category_insert_trigger();

CREATE OR REPLACE FUNCTION dish_insert_trigger()
  RETURNS TRIGGER AS $$
  BEGIN
    INSERT INTO customers_log (table_name, action)
    VALUES ('dish', 'insert');
    RETURN NEW;
  END;
$$ LANGUAGE plpgsql;






CREATE TRIGGER address_insert
  AFTER INSERT ON address
  FOR EACH ROW
  EXECUTE FUNCTION address_insert_trigger();

CREATE OR REPLACE FUNCTION category_insert_trigger()
  RETURNS TRIGGER AS $$
  BEGIN
    INSERT INTO customers_log (table_name, action)
    VALUES ('category', 'insert');
    RETURN NEW;
  END;
$$ LANGUAGE plpgsql;

