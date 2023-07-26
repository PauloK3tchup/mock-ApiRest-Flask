import secrets
from typing import Any, List, Dict

from flask import Flask, Response, request, jsonify

app = Flask(__name__)

recomendados: List[Dict[str, Any]] = [
    {
      "id": 1,
      "nome": "Bicicleta",
      "preco": 10000.00,
      "capa": "https://m.media-amazon.com/images/S/aplus-media-library-service-media/e34cebad-ca71-4de2-a4d1-b74d5e7168cf.__CR0,0,970,600_PT0_SX970_V1___.png",
      "descricao": "Bicicleta de 2 rodas muito poggers",
    },
    {
      "id": 2,
      "nome": "Among Action Figure",
      "preco": 95.50,
      "capa": "https://ae01.alicdn.com/kf/H7a083e0513714932a2578cca8a4aac75x.jpg?width=1920&height=1920&hash=3840",
      "descricao": "Figura de ação do Among Us muito poggers",
    },
    {
      "id": 3,
      "nome": "DVD Morbius HD",
      "preco": 10.50,
      "capa": "https://pbs.twimg.com/media/FFyT_6GVgAAGgrG?format=jpg&name=900x900",
      "descricao": "DVD do filme do Morbius muito poggers",
    },
    {
      "id": 4,
      "nome": "Banana (0.5kg)",
      "preco": 5.75,
      "capa": "https://img.freepik.com/vetores-gratis/bando-de-banana-amarela-madura-de-vetor-isolado-no-fundo-branco_1284-45456.jpg?w=360",
      "descricao": "Banana muito poggers (potássio(K))",
    },
    {
      "id": 5,
      "nome": "Armas de fogo",
      "preco": 50,
      "capa": "https://www.clubedetiroitajai.com.br/wp-content/uploads/2022/05/voce-sabe-qual-e-a-origem-das-armas-de-fogo-acesse-e-descubra-tudo-sobre.jpg",
      "descricao": "Armas de fogo muito poggers (pew pew)",
    },
    {
      "id": 6,
      "nome": "Videotutorial Sun Tzu",
      "preco": 5000000,
      "capa": "https://upload.wikimedia.org/wikipedia/commons/c/cf/%E5%90%B4%E5%8F%B8%E9%A9%AC%E5%AD%99%E6%AD%A6.jpg",
      "descricao": "Videotutorial do Sun Tzu desenho animado foda muito poggers",
    },
    {
      "id": 7,
      "nome": "Casca de banana",
      "preco": 2.75,
      "capa": "https://vitat.com.br/wp-content/uploads/2022/04/casca-de-banana-1.jpg",
      "descricao": "Casca de banana muito poggers (não tem potássio(K))",
    },
    {
      "id": 8,
      "nome": "Florianópolis",
      "preco": 7.50,
      "capa": "https://magazine.zarpo.com.br/wp-content/uploads/2023/01/capa-o-que-fazer-florianopolis.jpg",
      "descricao": "Florianópolis muito poggers (tem praia)",
    },
    {
      "id": 9,
      "nome": "1 Unidade de Amendoim",
      "preco": 0.50,
      "capa": "https://thumbs.dreamstime.com/b/um-amendoim-isolado-85881501.jpg",
      "descricao": "Amendoim muito poggers (não tem potássio(K))",
    },
    {
      "id": 10,
      "nome": "Super Luigi para o Xbox One",
      "preco": 0.50,
      "capa": "https://steamuserimages-a.akamaihd.net/ugc/1467563393551129446/5D6824881D455B66A71853918555FD343B6C21B0/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true",
      "descricao": "Super Luigi muito poggers (não tem potássio(K))",
    },
]

produtos: List[Dict[str, Any]] = [
    {
      "id": 1,
      "nome": "Fone de ouvido vegano",
      "preco": 20.00,
      "capa": "https://i.imgur.com/m6NBhBm.jpg",
      "descricao": "Fone de ouvido vegano muito poggers (feito de vegas)",
    },
    {
      "id": 2,
      "nome": "Recorte do Obama",
      "preco": 35.60,
      "capa": "https://m.media-amazon.com/images/I/51oxbTodnfL.jpg",
      "descricao": "Recorte do Obama muito poggers (não tem potássio(K))",
    },
    {
      "id": 3,
      "nome": "Super Mario para o PS4",
      "preco": 55.50,
      "capa": "https://i1.sndcdn.com/artworks-Zhp4Hc1szbkYin1Z-CkHDCA-t500x500.jpg",
      "descricao": "Super Mario muito poggers (potássio(K))",
    },
    {
      "id": 4,
      "nome": "DVD Sharknado 5 8K",
      "preco": 50.00,
      "capa": "https://m.media-amazon.com/images/M/MV5BMjQ3Mzk5NzAwNV5BMl5BanBnXkFtZTgwNDkwOTc3MjI@._V1_FMjpg_UX1000_.jpg",
      "descricao":
        "DVD Sharknado 5 8K full hd dublado legendado hd muito poggers (não tem potássio(K))",
    },
    {
      "id": 5,
      "nome": "Peppino",
      "preco": 3.25,
      "capa": "https://d332juqdd9b8hn.cloudfront.net/wp-content/uploads/2023/01/PIZZA-TOWER-SCREENSHOT.jpg",
      "descricao":
        "Peppino pizza tower torre pizza pepino italia muito poggers (potássio(K))",
    },
    {
      "id": 6,
      "nome": "Fusca",
      "preco": 120.99,
      "capa": "https://motortudo.com/wp-content/uploads/2019/07/cropped-Fusca-1500-1973-Motor-Tudo-0.jpg",
      "descricao": "Fusca",
    },
    {
      "id": 7,
      "nome": "Avião",
      "preco": 10.99,
      "capa": "https://cdn.panrotas.com.br/portal-panrotas-statics/media-files-cache/334042/e66c929a0d582bcde0c05fcc44d3742014aviaodeafrotamaismagicadomundo/77,0,2412,1440/1206,720,0.28/0/default.jpg",
      "descricao": "Avião com 2 asas que voa ,e decoração foda dms mlk top",
    },
    {
      "id": 8,
      "nome": "Gol Quadrado",
      "preco": 4,
      "capa": "https://quatrorodas.abril.com.br/wp-content/uploads/2018/02/chr8486-dng.jpg?quality=70&strip=info",
      "descricao": "Gol Quadrado direto do minecraft bedrock edition 1.17.10",
    },
    {
      "id": 9,
      "nome": "Guilherme Tamanhinho",
      "preco": 10.99,
      "capa": "https://static.wikia.nocookie.net/cnfanon/images/8/82/Dexter.jpg/revision/latest/scale-to-width-down/445?cb=20130406175710",
      "descricao": "Guilherme Tamanhinho (IFC araquari)",
    },
    {
      "id": 10,
      "nome": "Ácido sulfúrico",
      "preco": 25.75,
      "capa": "https://fontagua.com.br/wp-content/webp-express/webp-images/uploads/2023/01/agua-cristalina-1160x773.jpg.webp",
      "descricao": "Ácido sulfúrico muito poggers (não tem potássio(K))",
    },
    {
      "id": 11,
      "nome": "Saul Goodman",
      "preco": 45.65,
      "capa": "data:image/jpeg;base64,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",
      "descricao": "BUOOOMMMMM BOROROROROOMMMMM TCHOTCHOROROMMMMMM",
    },
    {
      "id": 12,
      "nome": "AAAA",
      "preco": 44.44,
      "capa": "https://pbs.twimg.com/media/FMRQx-5XEAM5Wb7.jpg",
      "descricao":
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    },
]

@app.route("/auth", methods=["POST"])
def auth() -> Response:
    """
    Perform authentication
    """
    data: Any = request.get_json()
    if (
        {"username", "password"}.issubset(data)
        and data["username"] == "bob"
        and data["password"] == "bob"
    ):
        access_token: str = secrets.token_urlsafe()
        refresh_token: str = secrets.token_urlsafe()
        print(access_token)
        return jsonify(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "status": "success",
            }
        )
    return jsonify({"status": "login failed"}), 401


@app.route("/produtos", methods=["GET"])
def getProdutos() -> Response:

    return jsonify(produtos)

@app.route("/recomendados", methods=["GET"])
def getRecomendados() -> Response:

    return jsonify(recomendados)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=19003)
