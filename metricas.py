def calcular_sensibilidade(vp, fn):
    if (vp + fn) == 0:
        return 0.0
    return vp / (vp + fn)

def calcular_especificidade(vn, fp):
    if (fp + vn) == 0:
        return 0.0
    return vn / (fp + vn)

def calcular_acuracia(vp, vn, fp, fn):
    n = vp + vn + fp + fn
    if n == 0:
        return 0.0
    return (vp + vn) / n

def calcular_precisao(vp, fp):
    if (vp + fp) == 0:
        return 0.0
    return vp / (vp + fp)

def calcular_f_score(vp, vn, fp, fn):  
    precisao = calcular_precisao(vp, fp)
    sensibilidade = calcular_sensibilidade(vp, fn)

    if (precisao + sensibilidade) == 0:
        return 0.0
    return 2 * (precisao * sensibilidade) / (precisao + sensibilidade)

if __name__ == "__main__":
    #Exemplo de valores para VP, VN, FP, FN (matriz de confusao arbitraria)
    verdadeiros_positivos = 80
    verdadeiros_negativos = 100
    falsos_positivos = 10
    falsos_negativos = 5

    print("->-> Metricas de Avaliacao de Classificacao <-<-")
    print(f"Valores de Entrada:")
    print(f"  Verdadeiros Positivos (VP): {verdadeiros_positivos}")
    print(f"  Verdadeiros Negativos (VN): {verdadeiros_negativos}")
    print(f"  Falsos Positivos (FP): {falsos_positivos}")
    print(f"  Falsos Negativos (FN): {falsos_negativos}")
    print("->->->->->->->->->->->->->->-><-<-<-<-<-<-<-<-<-<-<-<-<-")

    sensibilidade = calcular_sensibilidade(verdadeiros_positivos, falsos_negativos)
    especificidade = calcular_especificidade(verdadeiros_negativos, falsos_positivos)
    acuracia = calcular_acuracia(verdadeiros_positivos, verdadeiros_negativos, falsos_positivos, falsos_negativos)
    precisao = calcular_precisao(verdadeiros_positivos, falsos_positivos)
    f_score = calcular_f_score(verdadeiros_positivos, verdadeiros_negativos, falsos_positivos, falsos_negativos)

    print(f"Sensibilidade (Recall): {sensibilidade:.4f}")
    print(f"Especificidade: {especificidade:.4f}")
    print(f"Acuracia: {acuracia:.4f}")
    print(f"Precisao: {precisao:.4f}")
    print(f"F-score: {f_score:.4f}")
