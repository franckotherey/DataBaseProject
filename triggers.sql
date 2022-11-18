
CREATE OR REPLACE FUNCTION calcular_monto_total_pedido()
RETURNS TRIGGER AS $$
DECLARE
BEGIN
    UPDATE pedido SET monto_total = (
        SELECT SUM(subtotal)
        FROM contieneP
        WHERE NEW.pedidocodigo = pedido.codigo
    );
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER monto_total_pedido
AFTER INSERT ON contieneP
FOR EACH ROW EXECUTE PROCEDURE calcular_monto_total_pedido();  