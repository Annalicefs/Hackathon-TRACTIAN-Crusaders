CREATE OR REPLACE PROCEDURE CadastroFerramenta(
    nSAP IN VARCHAR2,
    nCategoria IN VARCHAR2,
    nEquipamento IN VARCHAR2,
    nTotal IN INT
) IS
    v_count INT;
BEGIN

    SELECT COUNT(*) INTO v_count 
    FROM Almoxarifado 
    WHERE SAP = nSAP;

    IF v_count > 0 THEN
        DBMS_OUTPUT.PUT_LINE('Erro: Já existe um equipamento com estes dados cadastrado.');
        RETURN;
    END IF;

    INSERT INTO Almoxarifado(SAP, Categoria, Equipamento, Total)
    VALUES (nSAP, nCategoria, nEquipamento, nTotal);
    
    DBMS_OUTPUT.PUT_LINE('Equipamento cadastrado com sucesso.');
END;
/
