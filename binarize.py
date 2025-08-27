from PIL import Image

def binarizar_imagem(caminho_imagem, limiar=128):
    try:
        img = Image.open(caminho_imagem).convert('RGB')
        largura, altura = img.size
        imagem_cinza = Image.new('L', (largura, altura))
        imagem_binarizada = Image.new('1', (largura, altura))

        #Conversao manual para tons de cinza e binarizacao
        for x in range(largura):
            for y in range(altura):
                r, g, b = img.getpixel((x, y))
                
                #Tons de cinza - Metodo de luminosidade
                valor_cinza = int(0.299 * r + 0.587 * g + 0.114 * b)
                imagem_cinza.putpixel((x, y), valor_cinza)
                
                #Binarizacao
                if valor_cinza < limiar:
                    imagem_binarizada.putpixel((x, y), 0)
                else:
                    imagem_binarizada.putpixel((x, y), 255)

        imagem_cinza.save('imagem_em_tons_de_cinza.png')
        imagem_binarizada.save('imagem_binarizada.png')
        print(f"Imagem convertida para tons de cinza em imagem_em_tons_de_cinza.png")
        print(f"Imagem binarizada em imagem_binarizada.png")

    except FileNotFoundError:
        print(f"Erro: Arquivo de imagem não encontrado em {caminho_imagem}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    try:
        with open('path.txt', 'r') as f:
            caminho_imagem = f.read().strip()
        binarizar_imagem(caminho_imagem)
    except FileNotFoundError:
        print("Caminho não encontrado.")
