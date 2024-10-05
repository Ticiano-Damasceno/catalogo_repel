import sqlalchemy as sqla
import os
from dotenv import load_dotenv

load_dotenv()
#criando a tabela
#cursor.execute("""
#    create table tbl_pessoal(
#        id integer primary key autoincrement,
#        nome text,
#        idade integer
#    )
#""")

class db():
    def __init__(self) -> None:
        conexao_db = os.getenv("URL_CONEXAO")
        self.__engine = sqla.create_engine(conexao_db, echo = True)
        self.__conn = self.__engine.connect()

    def inserir(self, descricao:str, referencia:str, aplicacao:str, codigo_fornecedor:str, valor_venda:float, observacao:str):
        self.__conn.execute(sqla.sql.text(""" 
            INSERT INTO tbl_produto 
            (
                descricao,
                referencia,
                aplicacao,
                codigo_fornecedor,
                valor_venda,
                observacao
            )
            VALUES(
                :descricao,
                :referencia,
                :aplicacao,
                :codigo_fornecedor,
                :valor_venda,
                :observacao
            )
        """), {
            "descricao": descricao,
            "referencia": referencia,
            "aplicacao": aplicacao,
            "codigo_fornecedor": codigo_fornecedor,
            "valor_venda": valor_venda,
            "observacao": observacao
        })
        self.__conn.commit()

    def consulta_unico(self, id:int):
        result = self.__conn.execute(sqla.sql.text("""
            SELECT * FROM tbl_produto WHERE id = :id
        """),{"id": id}).fetchall()
        return [e for e in result]

    def consulta_geral(self):
        result = self.__conn.execute(sqla.sql.text("""
            SELECT * FROM tbl_produto 
        """)).fetchall()
        if result == []:
            return []
        else:
            return [e for e in result]

    def alterar(self, id:int, descricao:str, referencia:str, aplicacao:str, codigo_fornecedor:str, valor_venda:float, observacao:str):
        query = sqla.sql.text("""
            UPDATE tbl_produto 
            SET
                descricao = :descricao,
                referencia = :referencia,
                aplicacao = :aplicacao,
                codigo_fornecedor = :codigo_fornecedor,
                valor_venda = :valor_venda,
                observacao = :observacao
            WHERE
                id = :id
        """)
        self.__conn.execute(query, {
            "id": id,
            "descricao": descricao,
            "referencia": referencia,
            "aplicacao": aplicacao,
            "codigo_fornecedor": codigo_fornecedor,
            "valor_venda": valor_venda,
            "observacao": observacao
        })
        self.__conn.commit()

    def excluir(self, id:int):
        query = sqla.sql.text(""" 
            DELETE FROM tbl_produto
            WHERE id = :id
        """)
        self.__conn.execute(query, {'id': id})
        self.__conn.commit()

#listando os índices de uma tupla => ()
#print([list(enumerate(e)) for e in cursor.execute("select * from tbl_pessoal")])

#exemplo de dicionário
#e = cursor.execute("select * from tbl_pessoal").fetchall()
#print(dict({'id':e[0][0], 'nome': e[0][1], 'idade': e[0][2]}))

#print(db.consulta_geral()) 
#print(db.consulta_unico(2))