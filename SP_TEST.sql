CREATE OR REPLACE FUNCTION test() RETURNS void
LANGUAGE plpgsql
AS $$
    DECLARE
        value1 text[];
        counter INTEGER := 0 ; 
        cur_seq CURSOR FOR SELECT sequence FROM consumption;
        quant_elem Integer;
    BEGIN
        SELECT count(*) into quant_elem from consumption;
            OPEN cur_seq;
            LOOP 
                EXIT WHEN counter > quant_elem; 
                counter := counter + 1 ; 
                FETCH cur_seq INTO value1;
                foreach x in array $1 loop
                    RAISE INFO 'information message %', now();
                END LOOP;
          MOVE cur_seq;
        END LOOP;
    END;
$$;

-- DECLARE
--       value1 integer;
--  BEGIN
--         SELECT count(*) into value1 from consumption;
--      RETURN value1;
--  END; 