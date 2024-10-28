CREATE OR REPLACE PROCEDURE AtualizaFerramenta(
	nSAP IN VARCHAR2,
	nTotal IN INT)
AS
BEGIN
    UPDATE Almoxarifado
    SET Total = nTotal
    WHERE SAP = nSAP;
		 DBMS_OUTPUT.PUT_LINE('Quantidade atualizada com sucesso.');
END;
/
