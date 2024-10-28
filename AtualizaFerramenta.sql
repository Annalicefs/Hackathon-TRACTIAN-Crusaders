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

/*
function atualizaFerramenta(nSAP, nTotal) {
    // Atualiza o total da ferramenta no Almoxarifado
    const resultado = db.Almoxarifado.updateOne(
        { "SAP": nSAP }, // Filtro para encontrar o documento
        { $set: { "Total": nTotal } } // Atualiza o campo Total
    );

    // Verifica se a atualização foi bem-sucedida
    if (resultado.modifiedCount > 0) {
        print('Quantidade atualizada com sucesso.');
    } else {
        print('Erro: Nenhum equipamento encontrado com o SAP fornecido.');
    }
}

// Exemplo de uso da função
atualizaFerramenta("A12345", 15);
*/
